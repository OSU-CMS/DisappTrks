import re
import subprocess

DATA_PATHS = [
    ("verification/files/EGamma_2022CD.root", "electron"),
    ("verification/files/EGamma_2022EFG.root", "electron"),
    ("verification/files/EGamma_2023C.root", "electron"),
    ("verification/files/EGamma_2023D.root", "electron"),
    ("verification/files/Muon_2022CD.root", "muon"),
    ("verification/files/Muon_2022EFG.root", "muon"),
    ("verification/files/Muon_2023C.root", "muon"),
    ("verification/files/Muon_2023D.root", "muon")
]

TEMPLATE_PATHS = {
    "electron": "verification/templates/electron.py",
    "muon": "verification/templates/muon.py"
}

# "VALUE +- ERROR" -> (VALUE, ERROR)
SYM_PATTERN = re.compile(r"([\d.eE+-]+)\s+\+-\s+([\d.eE+-]+)")
# "VALUE - LOW + HIGH" -> (VALUE, LOW, HIGH)  (used when value is 0)
ASYM_PATTERN = re.compile(r"([\d.eE+-]+)\s+-\s+([\d.eE+-]+)\s+\+\s+([\d.eE+-]+)")


def parse_value(text):
    """Parse 'VALUE +- ERROR' or 'VALUE - LOW + HIGH' from text.

    Returns (value, error). For asymmetric errors, error = high side.
    """
    m = ASYM_PATTERN.search(text)
    if m:
        return float(m.group(1)), float(m.group(3))

    m = SYM_PATTERN.search(text)
    if m:
        return float(m.group(1)), float(m.group(2))

    raise ValueError(f"Could not parse value from: {text!r}")


def parse_old(s):
    """Parse one block of old-script output.

    Returns a dict with keys: N_ctrl, P_veto, P_met_cut, P_met_trigger,
    trigger_eff, N_est. Each value is a (value, error) tuple.
    """
    result = {}
    lines = s.split("\n")

    trigger_eff_count = 0
    for line in lines:
        if line.startswith("N_ctrl:"):
            # "N_ctrl: VALUE +- ERROR (... fb)"
            result["N_ctrl"] = parse_value(line.split("(")[0])

        elif "P (pass lepton veto) in tag-probe sample:" in line:
            after = line.split("P (pass lepton veto) in tag-probe sample:")[1]
            result["P_veto"] = parse_value(after)

        elif line.startswith("P (pass met cut):"):
            # "P (pass met cut): VALUE +- ERROR numerator ..."
            result["P_met_cut"] = parse_value(line.split("numerator")[0])

        elif line.startswith("P (pass met triggers):"):
            # "P (pass met triggers): VALUE +- ERROR numerator ..."
            result["P_met_trigger"] = parse_value(line.split("numerator")[0])

        elif line.startswith("Trigger Efficiency:"):
            trigger_eff_count += 1
            # First line is raw counts "A - B / C - D"
            # Second line is the actual efficiency "VALUE +- ERROR"
            if trigger_eff_count == 2:
                after = line.split("Trigger Efficiency:")[1]
                result["trigger_eff"] = parse_value(after)

        elif line.startswith("N_est:"):
            # "N_est: VALUE +- ERROR (... fb)"
            result["N_est"] = parse_value(line.split("(")[0])

    return result


# Map new script labels to the same keys used by parse_old
NEW_LABEL_MAP = {
    "N_ctrl":              "N_ctrl",
    "P(pass lepton veto)": "P_veto",
    "P(pass MET cut)":     "P_met_cut",
    "P(pass MET trigger)": "P_met_trigger",
    "Lepton trigger eff":  "trigger_eff",
    "N_est":               "N_est",
}

# "VALUE +/- ERROR" (new script uses +/- instead of +-)
NEW_VALUE_PATTERN = re.compile(r"([\d.eE+-]+)\s+\+/-\s+([\d.eE+-]+)")


def parse_new(s):
    """Parse one tabulate simple_outline table from the new script.

    Returns a dict with the same keys as parse_old.
    """
    result = {}
    for line in s.split("\n"):
        if "│" not in line:
            continue

        parts = [p.strip() for p in line.split("│")]
        # parts: ['', label, value_str, ''] from leading/trailing │
        if len(parts) < 4:
            continue

        label = parts[1]
        value_str = parts[2]

        if label not in NEW_LABEL_MAP:
            continue

        m = NEW_VALUE_PATTERN.search(value_str)
        if not m:
            continue

        result[NEW_LABEL_MAP[label]] = (float(m.group(1)), float(m.group(2)))

    return result


REL_TOL = 1e-4

def _approx_equal(a, b):
    if a == b:
        return True
    scale = max(abs(a), abs(b))
    if scale == 0:
        return True
    return abs(a - b) / scale < REL_TOL


for path, lepton_type in DATA_PATHS:
    year = path.split("_")[1][0:4]
    era = path.split("_")[1][4:].split(".")[0]

    with open(TEMPLATE_PATHS[lepton_type]) as f:
        contents = f.read()

    contents = contents.replace("__YEAR__", repr(year))
    contents = contents.replace("__ERA__", repr(era))
    contents = contents.replace("__PATH__", repr(path))

    old_path = f"verification/scripts/{lepton_type}_{year}{era}_old.py"
    with open(old_path, "w") as f:
        f.write(contents)

    old_result = subprocess.run(
        f"python3 {old_path}",
        shell=True,
        capture_output=True,
        text=True
    )

    old_split = old_result.stdout.split("\n\n\n")

    old_nlayers4 = parse_old(old_split[1])
    old_nlayers5 = parse_old(old_split[2])
    old_nlayers6 = parse_old(old_split[3])
    old_nlayers_combined = parse_old(old_split[0])

    new_result = subprocess.run(
        f"python3 lepton_background_estimate.py {path} --lepton-type {lepton_type} --year {year} --era {era}",
        shell=True,
        capture_output=True,
        text=True
    )

    new_split = new_result.stdout.split("\n\n")

    new_nlayers4 = parse_new(new_split[0])
    new_nlayers5 = parse_new(new_split[1])
    new_nlayers6 = parse_new(new_split[2])
    new_nlayers_combined = parse_new(new_split[3])

    # Compare
    comparisons = [
        (f"{lepton_type} {year}{era} - NLayers4",  old_nlayers4,  new_nlayers4),
        (f"{lepton_type} {year}{era} - NLayers5",  old_nlayers5,  new_nlayers5),
        (f"{lepton_type} {year}{era} - NLayers6+", old_nlayers6,  new_nlayers6),
        (f"{lepton_type} {year}{era} - Combined",  old_nlayers_combined, new_nlayers_combined),
    ]

    keys = ["N_ctrl", "P_veto", "P_met_cut", "P_met_trigger", "trigger_eff", "N_est"]

    for label, old, new in comparisons:
        mismatches = []
        for key in keys:
            if key not in old or key not in new:
                continue
            old_val, old_err = old[key]
            new_val, new_err = new[key]
            if not _approx_equal(old_val, new_val) or not _approx_equal(old_err, new_err):
                mismatches.append((key, old_val, old_err, new_val, new_err))

        if mismatches:
            print(f"\n{'=' * 60}")
            print(f"  {label}")
            print(f"{'=' * 60}")
            for key, old_val, old_err, new_val, new_err in mismatches:
                print(f"  {key}")
                print(f"    old: {old_val:>20.8g} +/- {old_err:.6g}")
                print(f"    new: {new_val:>20.8g} +/- {new_err:.6g}")
        else:
            print(f"  {label}: all values match")
