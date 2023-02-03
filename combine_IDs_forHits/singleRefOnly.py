"""
This code takes the closestRefInfo_allScoreThresholdHits csv file and creates a new csv file
with only hits that have a single closest ref leaf.
"""

import pandas as pd
import ast

df = pd.read_csv("closestRefInfo_allScoreThresholdHits_02.csv")
output_file = "closestRefInfo_allScoreThresholdHits_singleRefOnly.csv"

for index, row in df.iterrows():
    closest_ref_list = ast.literal_eval(row["closest_ref"])
    if len(closest_ref_list) == 1:
        df.at[index, "single_ref"] = "True"
        df.at[index, "closest_single_ref"] = closest_ref_list[0]
    else:
        df.at[index, "single_ref"] = "False"
        df.at[index, "closest_single_ref"] = "NA"

pd.DataFrame(df).to_csv(output_file)
