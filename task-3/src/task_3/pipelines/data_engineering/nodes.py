


from typing import Dict, List, Tuple


def separate_data(data: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
    output = {
        "amateur": [],
        "expert": [],
    }

    for d in data:
        output[d["dataset"]].append(d)

    return output["amateur"], output["expert"]

