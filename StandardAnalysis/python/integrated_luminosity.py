# All luminosities are in inverse picobarns

YEAR_ERAS = {
    "2015": "D",
    "2016": "BCDEFGH",
    "2017": "BCDEF",
    "2018": "ABCD",
    "2022": "CDEFG",
    "2023": "CD",
    "2024": "CDEFGHI",
}

# Base luminosities per dataset/year/era
# Keys are formatted as "{dataset}_{year}{era}"
_BASE_LUMIS = {
    # 2015 (rereco)
    "MET_2015D": 2672.144,
    "SingleElectron_2015D": 2669.639,
    "SingleMuon_2015D": 2669.752,
    "Tau_2015D": 2672.153,
    "ZeroBias_2015D": 0.0,

    # 2016 (PromptReco)
    # For 2016H, v2 and v3 have been pre-combined
    "MET_2016B": 5740.666,
    "MET_2016C": 2573.399,
    "MET_2016D": 4241.828,
    "MET_2016E": 3967.714,
    "MET_2016F": 3096.281,
    "MET_2016G": 7522.287,
    "MET_2016H": 8390.54 + 215.149,  # v2 + v3

    "SingleElectron_2016B": 5740.121,
    "SingleElectron_2016C": 2573.399,
    "SingleElectron_2016D": 4248.384,
    "SingleElectron_2016E": 4007.001,
    "SingleElectron_2016F": 3090.341,
    "SingleElectron_2016G": 7535.488,
    "SingleElectron_2016H": 8390.278 + 215.149,  # v2 + v3

    "SingleMuon_2016B": 5733.079,
    "SingleMuon_2016C": 2573.399,
    "SingleMuon_2016D": 4071.484,
    "SingleMuon_2016E": 4009.132,
    "SingleMuon_2016F": 3092.106,
    "SingleMuon_2016G": 7540.488,
    "SingleMuon_2016H": 8390.540 + 215.149,  # v2 + v3

    "Tau_2016B": 5737.738,
    "Tau_2016C": 2573.399,
    "Tau_2016D": 4248.384,
    "Tau_2016E": 4008.663,
    "Tau_2016F": 3099.583,
    "Tau_2016G": 7534.265,
    "Tau_2016H": 8635.591 + 221.442,  # v2 + v3

    "ZeroBias_2016B": 5733.453,
    "ZeroBias_2016C": 2573.399,
    "ZeroBias_2016D": 4248.383,
    "ZeroBias_2016E": 4009.130,
    "ZeroBias_2016F": 3079.608,
    "ZeroBias_2016G": 7488.562,
    "ZeroBias_2016H": 8390.540 + 215.149,  # v2 + v3

    # 2017 (from ntuple CRAB reports)
    # Note: 2017B had different triggers, see Triggers.py
    "MET_2017B": 4793.367,
    "MET_2017C": 9631.324,
    "MET_2017D": 4247.707,
    "MET_2017E": 9313.990,
    "MET_2017F": 13498.143,

    "SingleElectron_2017B": 4710.308,
    "SingleElectron_2017C": 9631.009,
    "SingleElectron_2017D": 4247.706,
    "SingleElectron_2017E": 9313.682,
    "SingleElectron_2017F": 13538.950,

    "SingleMuon_2017B": 4793.980,
    "SingleMuon_2017C": 9563.500,
    "SingleMuon_2017D": 4247.706,
    "SingleMuon_2017E": 9313.682,
    "SingleMuon_2017F": 13539.633,  # TODO: update from ntuple crab reports

    "Tau_2017B": 4793.980,
    "Tau_2017C": 9632.850,
    "Tau_2017D": 4247.707,
    "Tau_2017E": 9313.990,
    "Tau_2017F": 13534.185,

    # 2018 (from ntuple CRAB reports)
    "MET_2018A": 14024.176505487,
    "MET_2018B": 7060.764380203,
    "MET_2018C": 6894.782079681,
    "MET_2018D": 31742.980644688,

    "EGamma_2018A": 14012.067987968,
    "EGamma_2018B": 7060.617355256,
    "EGamma_2018C": 6688.523784,
    "EGamma_2018D": 30955.343627310,

    "SingleMuon_2018A": 13956.7120657598,
    "SingleMuon_2018B": 7060.622497490,
    "SingleMuon_2018C": 6894.770971269,
    "SingleMuon_2018D": 31585.906779588,

    "Tau_2018A": 14022.518202245,
    "Tau_2018B": 7015.791118,
    "Tau_2018C": 6873.907668,
    "Tau_2018D": 31742.631527,

    # 2022 (PromptReco)
    "MET_2022C": 5010.409016184,
    "MET_2022D": 2970.045129108,
    "MET_2022E": 5806.955207286,
    "MET_2022F": 17781.598893382,
    "MET_2022G": 3082.753035617,

    "Muon_2022C": 5010.409016184,
    "Muon_2022D": 2970.045129108,
    "Muon_2022E": 5806.955207286,
    "Muon_2022F": 17781.901464250,
    "Muon_2022G": 3082.753035617,

    "EGamma_2022C": 5010.409016,
    "EGamma_2022D": 2970.045129,
    "EGamma_2022E": 5806.955207,
    "EGamma_2022F": 17781.59889,
    "EGamma_2022G": 3082.753036,

    "Tau_2022C": 5010.409016115,
    "Tau_2022D": 2970.045129109,
    "Tau_2022E": 5806.955207273,
    "Tau_2022F": 17781.901464330,
    "Tau_2022G": 3082.753035626,

    # 2023 (PromptReco)
    # Multiple versions per era have been pre-combined
    "MET_2023C": 4351.994672 + 1272.559899 + 1604.898825 + 10854.987443,
    "MET_2023D": 7986.390339 + 1704.204266,

    "EGamma_2023C": 4351.994672 + 1272.559899 + 1604.898825 + 10854.987443,
    "EGamma_2023D": 7986.390339 + 1704.204266,

    "Muon_2023C": 4351.994672 + 1272.559899 + 1604.898825 + 10854.987443,
    "Muon_2023D": 7986.390339 + 1705.710797,

    "Tau_2023C": 4351.994672 + 1272.559899 + 1604.898825 + 10854.987443,
    "Tau_2023D": 7986.390339 + 1705.710797,

    # 2024
    "Muon_2024C": 6587.017170174,
    "Muon_2024D": 7932.086430022,
    "Muon_2024E": 11279.119389046,
    "Muon_2024F": 25411.488852840,
    "Muon_2024G": 36392.283866818,
    "Muon_2024H": 5284.113839244,
    "Muon_2024I": 11133.551308097,

    "EGamma_2024C": 6598.246038874,
    "EGamma_2024D": 7994.187834784,
    "EGamma_2024E": 11445.215789533,
    "EGamma_2024F": 28064.910914252,
    "EGamma_2024G": 38125.20690498,
    "EGamma_2024H": 5492.058299549,
    "EGamma_2024I": 11594.356453411,
}

# Prescaled trigger luminosities
# These triggers ran with prescales, so their effective luminosity differs from nominal
_PRESCALED_LUMIS = {
    "HLT_LooseIsoPFTau50_Trk30_eta2p1_v*": {
        "Tau_2015D": 225.172,
        "Tau_2016B": 712.32,
        "Tau_2016C": 81.448,
        "Tau_2016D": 135.498,
        "Tau_2016E": 116.127,
        "Tau_2016F": 66.043,
        "Tau_2016G": 114.311,
        "Tau_2016H": 116.278 + 3.092,  # v2 + v3
    },

    "HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*": {
        "Tau_2017B": 4094.150,
        "Tau_2017C": 498.846,
        "Tau_2017D": 311.834,
        "Tau_2017E": 391.608,
        "Tau_2017F": 465.854,
        "Tau_2018A": 73.802727380,
        "Tau_2018B": 36.925216,
        "Tau_2018C": 36.178461,
        "Tau_2018D": 167.066482,
    },

    "HLT_ZeroBias_v*": {
        "ZeroBias_2015D": 0.0,
        "ZeroBias_2016B": 0.012195551,
        "ZeroBias_2016C": 0.001267369,
        "ZeroBias_2016D": 0.001898671,
        "ZeroBias_2016E": 0.00301127,
        "ZeroBias_2016F": 0.001710604,
        "ZeroBias_2016G": 0.003144164,
        "ZeroBias_2016H": 0.005520328 + 0.000180316,  # v2 + v3
    },
}


def _get_available_datasets(year, lumi_dict=None):
    """Get all datasets that have luminosity data for a given year.

    Args:
        year: Year string (e.g., "2017")
        lumi_dict: Dictionary to search in. Defaults to _BASE_LUMIS.

    Returns:
        Set of dataset names available for that year.
    """
    if lumi_dict is None:
        lumi_dict = _BASE_LUMIS

    datasets = set()
    for key in lumi_dict:
        if f"_{year}" in key:
            # Extract dataset name (everything before _{year})
            dataset = key.split(f"_{year}")[0]
            datasets.add(dataset)
    return datasets


def get_lumi(dataset, year, eras=None, trigger=None):
    """Get integrated luminosity for a dataset/year/era combination.

    Args:
        dataset: Primary dataset name (e.g., "MET", "EGamma", "Tau")
        year: Year string (e.g., "2017", "2018")
        eras: Era(s) to include. If None, uses all eras for that year.
              Can be a single letter ("B") or multiple ("BC", "BCD").
        trigger: HLT path for prescaled triggers. If specified, returns the
                 effective luminosity for that trigger instead of the nominal.

    Returns:
        Integrated luminosity in inverse picobarns.

    Raises:
        ValueError: If year is unknown, dataset is not available for the year,
                    or trigger is unknown.

    Examples:
        get_lumi("MET", "2017")                    # Full 2017
        get_lumi("MET", "2017", "BC")              # Just B + C
        get_lumi("MET", "2017", "B")               # Just B
        get_lumi("Tau", "2017", trigger="HLT_MediumChargedIsoPFTau50_Trk30_eta2p1_1pr_v*")
    """
    if year not in YEAR_ERAS:
        raise ValueError(f"Unknown year: {year}. Valid years: {list(YEAR_ERAS.keys())}")

    lumi_dict = _PRESCALED_LUMIS.get(trigger) if trigger else _BASE_LUMIS
    if trigger and lumi_dict is None:
        raise ValueError(f"Unknown trigger: {trigger}")

    # Validate dataset exists for this year
    available_datasets = _get_available_datasets(year, lumi_dict)
    if dataset not in available_datasets:
        raise ValueError(
            f"Dataset '{dataset}' is not available for {year}. "
            f"Available datasets: {sorted(available_datasets)}. "
            f"If you believe this is a valid dataset, add its luminosity values to the data."
        )

    if eras is None:
        eras = YEAR_ERAS[year]

    total = 0.0
    for era in eras:
        key = f"{dataset}_{year}{era}"
        if key in lumi_dict:
            total += lumi_dict[key]
        else:
            valid_eras = YEAR_ERAS[year]
            raise ValueError(
                f"No luminosity data for '{key}'. "
                f"Valid eras for {year}: {valid_eras}. "
                f"Check that era '{era}' exists for dataset '{dataset}' in {year}."
            )

    return total


class _DeprecatedLumiDict:
    """Placeholder that shows an error message when accessed."""

    def __getitem__(self, key):
        raise RuntimeError(
            f"The lumi dictionary is deprecated. "
            f"Use get_lumi(dataset, year, eras) instead.\n"
            f"Example: lumi[\"{key}\"] -> get_lumi(\"MET\", \"2017\", \"BC\")"
        )

    def __contains__(self, key):
        raise RuntimeError(
            f"The lumi dictionary is deprecated. "
            f"Use get_lumi(dataset, year, eras) instead."
        )


lumi = _DeprecatedLumiDict()
