"""
Create table need for the background estimates.
You will need to pass in a txt file that contains the output of bkgdEstimate_2022.py

If using for something other than the tau backgrounds you will probably have to modify format_estimates() to match
the given search strings.

NOTE: This script is a work in progress! It will get you 90% of the way to a completed table but you should verify and
clean up the table as needed.
"""
from jinja2 import Environment, FileSystemLoader
import re
import re

def fmt_number(x: float) -> str:
    """Format a number for LaTeX: truncate to 2 decimals or use scientific notation."""
    if x == 0:
        return "0.0"
    return f"{x:.2f}" if abs(x) >= 0.01 else f"{x:.2e}"

def parse_background_estimates(text):
    region_pattern = re.compile(
        r"performing tau background estimate in search region\((?P<region>[^)]+)\)",
        re.MULTILINE,
    )

    block_pattern = re.compile(
        r"performing tau background estimate in search region\([^)]+\)\n(?P<block>.*?)(?=\nperforming tau background estimate|\Z)",
        re.DOTALL,
    )

    number_pattern = re.compile(r"[-+]?(?:\d*\.\d+|\d+)(?:[eE][-+]?\d+)?")

    results = []

    for region_match, block_match in zip(region_pattern.finditer(text), block_pattern.finditer(text)):
        region = region_match.group("region").strip()
        block = block_match.group("block")

        entries = {}
        for line in block.splitlines():
            line = line.strip()
            if not line or ":" not in line:
                continue

            key, val = line.split(":", 1)
            key = key.strip()

            nums = number_pattern.findall(val)
            nums = [float(n) for n in nums] if nums else None

            entries[key] = nums if nums and len(nums) > 1 else (nums[0] if nums else None)

        nlayer_match = re.search(r"NLayers\s*([0-9]+)", region)
        nlayer = int(nlayer_match.group(1)) if nlayer_match else None

        results.append({
            "region": region,
            "nlayer": nlayer,
            "entries": entries,
        })

    return results

def list_to_value_with_uncertainty(value: list[float]) -> str:
    """
    Convert [val, ±err] or [val, err_down, err_up] into a formatted LaTeX string.
    Uses fmt_number() for all floats.
    """
    if len(value) == 2:
        val, err = map(fmt_number, value)
        return rf"${val} \pm {err}$"
    elif len(value) == 3:
        val, err_down, err_up = map(fmt_number, value)
        return rf"${val}_{{-{err_down}}}^{{+{err_up}}}$"
    else:
        raise ValueError(f"Unexpected number of values: {value}")

def format_estimates(parsed_values: list[dict]):
    """
    Convert parsed tau background estimates into a nested structure:
    [
        {
            "Era": "2022 CD",
            "layers": [
                {... layer dict ...},
                {... layer dict ...},
                ...
            ]
        },
        ...
    ]
    """
    if not parsed_values:
        return []

    # All entries share the same era label
    era = parsed_values[0]['region'].split('--')[0].strip()
    # NOTE: This line prevents the code from being ran with multiple eras at the same time.
    tauScalingFactor = list_to_value_with_uncertainty(
        parsed_values[0]['entries']['Trigger scale factor'][-2:]
    )
    era_dict = {
        "Era": era,
        "layers": [],
    }

    for layer in parsed_values:
        data = layer['entries']

        estimate_dict = {
            "triggerEfficiency": list_to_value_with_uncertainty(
                data['External trigger efficiency']
            ),
            "layer": layer['nlayer'] if layer['nlayer'] else "Combined",
            "tauScalingFactor": tauScalingFactor,
            "NCtrl": list_to_value_with_uncertainty(data['N_ctrl'][:2]),
            "PVeto": list_to_value_with_uncertainty(
                data['P (pass lepton veto) in tag-probe sample']
            ),
            "POffline": list_to_value_with_uncertainty(data['P (pass met cut)'][:2]),
            "Ptrigger": list_to_value_with_uncertainty(
                data['P (pass met triggers)'][:2]
            ),
            "estimate": list_to_value_with_uncertainty(data['N_est'][:3]),
        }

        if not all(estimate_dict.values()):
            print("⚠️ Failed to parse values correctly for region:", layer["region"])
            print(data)
            raise ValueError("Missing or malformed entry in estimate_dict")

        era_dict["layers"].append(estimate_dict)

    return [era_dict]





if __name__ == "__main__":
    env = Environment(loader=FileSystemLoader('.'))
    template=env.get_template('tau_background_estimate_table_template.tex')

    with open("bkgdEstimate_2025_10_07_16h32m09s.log") as f:
        text = f.read()
    estimate = parse_background_estimates(text)
    formatted_estimate = format_estimates(estimate)
    rendered_tex = template.render(estimates=formatted_estimate)

    output_file_path = "tau_bkgd_estimate.tex"
    with open(output_file_path, "w") as f:
        f.write(rendered_tex)
