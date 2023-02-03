"""
Time to make an otu_table with reference otus only (using the closest reference sequence by
branch length for each query otu).
"""

import pandas as pd
import ast

# first, i'm just gonna add the closest reference otu for each hit sequence in combined_IDs_forScoreThresholdHits.csv
# closest ref info can be found in closestRefInfo_allScoreThresholdHits_02.csv

df = pd.read_csv("combined_IDs_forScoreThresholdHits.csv", usecols=range(1, 5))
closestRef_df = pd.read_csv("closestRefInfo_allScoreThresholdHits_02.csv")

n = 0

# drop duplicate rows in both dfs
df = df.drop_duplicates()
closestRef_df = closestRef_df.drop_duplicates()
# multiple_ref_df = pd.DataFrame(columns=["hit_id", "ref_id"])

# for hit in df["hit_id"]:
#     # print(hit)
#     if not pd.isna(closestRef_df.loc[closestRef_df["hit_id"] == hit, "distance"].item()):
#         if len(ast.literal_eval(closestRef_df.loc[closestRef_df["hit_id"] == hit, "closest_ref"].item())) == 1:
#             df.loc[df["hit_id"] == hit, "ref_id"] = ast.literal_eval(closestRef_df.loc[closestRef_df["hit_id"] == hit, "closest_ref"].item())[0]
#         if len(ast.literal_eval(closestRef_df.loc[closestRef_df["hit_id"] == hit, "closest_ref"].item())) > 1:
#             multiple_ref_df = multiple_ref_df.append({"hit_id": hit,
#                                                       "ref_id": ast.literal_eval(closestRef_df.loc[closestRef_df["hit_id"] == hit, "closest_ref"].item())},
#                                                      ignore_index=True)

for hit in df["hit_id"]:
    # print(hit)
    if not pd.isna(closestRef_df.loc[closestRef_df["hit_id"] == hit, "distance"].item()):
        df.loc[df["hit_id"] == hit, "ref_id"] = ast.literal_eval(closestRef_df.loc[closestRef_df["hit_id"] == hit, "closest_ref"].item())[0]

pd.DataFrame(df).to_csv("combined_IDs_forScoreThresholdHits_closestRef_02.csv")
# pd.DataFrame(multiple_ref_df).to_csv("multiple_refs_df.csv")

# only one instance of multiple reference ids of equal distance to query sequence: DslPige3 and DslPige4
# just assign DslPige3 as the closest_ref / ref_id for these cases

