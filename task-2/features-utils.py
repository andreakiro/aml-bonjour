complex_features_suffixes = [
    "mean",
    "std",
    "min",
    "quantile-25",
    "quantile-50",
    "quantile-75",
    "max"
]

complex_features_list = [
    "rpeaks_amplitude",
    "qpeaks_amplitude",
    "speaks_amplitude",
    "rr_durations",
    "qrs_durations",
    "qrs_direction",
    "qr_ratio",
]

simple_features_list = [
    "snr",
    "pNN28"
]

def features_list():
    complex_features = []
    for item in complex_features_list:
        for suffix in complex_features_suffixes:
            complex_features.append('-'.join([item, suffix]))
    return complex_features + simple_features_list

def features_map():
    idx = 0
    features_map = {}
    for item in complex_features_list:
        for suffix in complex_features_suffixes:
            features_map['-'.join([item, suffix])] = idx
            idx += 1
    for item in simple_features_list:
        features_map[item] = idx
        idx += 1
    return features_map