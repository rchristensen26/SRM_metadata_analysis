"""
This code creates a new CSV file for all hits that meet the score threshold with the following
information for each hit:
hit_id, biosample_id, subject_id, ref_id

hit_id and biosample_id are in: closestRefInfo_allscore_threshold_df_02.csv
biosample_id and subject_id are in: bySubject_dataset.csv
hit_id and ref_id are in: compiled_dsrAB_scoreThreshold_noDups_gapPercentageInfo.csv

(note to self as i begin to write this: happy coding!)
"""

import pandas as pd
from ete3 import Tree

score_threshold_df = pd.read_csv("closestRefInfo_allScoreThresholdHits_02.csv")
subject_df = pd.read_csv("hgm_subject_df.csv", low_memory=False)
gap_perc_df = pd.read_csv("compiled_dsrAB_scoreThreshold_noDups_gapPercentageInfo.csv")
output_csv = "combined_IDs_forScoreThresholdHits_0609.csv"
tree_file = "RAxML_labelledTree_noBootstrap_rooted.newick"
# tree_file = "RAxML_originalLabelledTree_noBootstrap.newick" # reference tree
otu_matrix_file = "otu_subject_matrix_0609.csv"

# hit_id = score_threshold_df["hit_id"]
# sample_id = score_threshold_df["biosample_id"]
# subject_id_query = "sample_id == " + score_threshold_df["biosample_id"]
# print(hit_id)
# print(subject_id_query)
# for sample_id in score_threshold_df["biosample_id"]:
#     print(subject_df.loc[score_threshold_df["biosample_id"] in subject_df["sample_id"], "merged_subject_id"])
#
# for sample in score_threshold_df["biosample_id"]:
#     if sample in subject_df.sample_id.values:
#         print(subject_df.loc[subject_df.sample_id.str.contains(sample), "merged_subject_id"])
#
# for sample in score_threshold_df["biosample_id"]:
#     if not subject_df.loc[subject_df.sample_id.str.contains(sample), "merged_subject_id"].empty:
#         subject_id = subject_df.loc[subject_df.sample_id.str.contains(sample), "merged_subject_id"].item()
#         score_threshold_df["subject_id"] = subject_df.loc[subject_df.sample_id.str.contains(sample), "merged_subject_id"].item()
#     # else:
#     #     score_threshold_df["biosample_id" == sample]["subject_id"] = "NA"
#
# print(score_threshold_df["subject_id"])
# # subject_df.loc[subject_df.sample_id.str.contains(score_threshold_df["biosample_id"]), "merged_subject_id"].notnull.item()


# # i'm going to try iterating by hit id for now...
# dict_list = []
# for index, row in score_threshold_df.iterrows():
#     row_dict = {"hit_id": row["hit_id"], "sample_id": row["biosample_id"]}
#
#     # check if subject_id exists for this biosample_id
#     if not subject_df.loc[subject_df.sample_id.str.contains(row["biosample_id"]), "merged_subject_id"].empty:
#         row_dict["subject_id"] = subject_df.loc[subject_df.sample_id.str.contains(row["biosample_id"]), "merged_subject_id"].item()
#     else:
#         row_dict["subject_id"] = "NA"
#
#     # check gapPercentage hits for hit in order to find the leaf ID
#     # first condition: if hit_id in gapPercInfo contains hit_id
#     if not gap_perc_df.loc[gap_perc_df.id.str.contains(row["hit_id"]), "sample_name"].empty:
#         row_dict["ref_id"] = gap_perc_df.loc[gap_perc_df.id.str.contains(row["hit_id"]), "sample_name"].item()
#
#     # next condition: if hit_id in edups column. add ref_id directly? there should be only one occurrence of exact duplicates...
#     # im not actually sure if this worked lol but oh well. gotta check it later
#     elif not gap_perc_df.loc[gap_perc_df.edups.str.contains(row["hit_id"]), "sample_name"].empty:
#         row_dict["ref_id"] = gap_perc_df.loc[gap_perc_df.edups.str.contains(row["hit_id"]), "sample_name"].item()
#
#     # final condition: if hit_id in sdups column
#     # this is the trickiest one, as multiple rows will have the same sdup
#     # so first, we need to check that the leaf IDs for all rows with that sdup are the same. if not, don't assign a leaf ID
#     elif not gap_perc_df.loc[gap_perc_df.sdups.str.contains(row["hit_id"]), "sample_name"].empty:
#         if gap_perc_df.loc[gap_perc_df.sdups.str.contains(row["hit_id"]), "sample_name"].size == 1:
#             row_dict["ref_id"] = gap_perc_df.loc[gap_perc_df.sdups.str.contains(row["hit_id"]), "sample_name"].item()
#         else:
#             sdup_leaves_list = list(gap_perc_df.loc[gap_perc_df.sdups.str.contains(row["hit_id"]), "sample_name"].values)
#             leaf1 = sdup_leaves_list[0]
#             equal = True
#
#             for leaf in sdup_leaves_list:
#                 if leaf1 != leaf:
#                     equal = False
#                     row_dict["ref_id"] = "NA"
#                     break
#             if equal:
#                 row_dict["ref_id"] = leaf1
#     dict_list.append(row_dict)
#
# pd.DataFrame(dict_list).to_csv(output_csv)
#
# """
# time to mutate heheheh
# columns: subject IDs
# rows: leaf IDs
# """
#
# id_df = pd.read_csv(output_csv)
# subject_ids = subject_df.merged_subject_id.unique()  # effectively the sample columns
#
# # read in tree file and get the leaf names
# with open(tree_file, mode='r') as f:
#     tree = Tree(f.read())
# ref_ids = tree.get_leaf_names()  # effectively the OTU rows
#
# # make df with subject_id as column names and OTUs as row names; all cells = 0
# otu_mat = pd.DataFrame(columns=subject_ids, index=ref_ids, data=0)
#
# # iterate by subject_id from subject ID list
# for subject_id in subject_ids:
#     # if subject_id is in id_df, return list of leaf IDs associated with that subject_id
#     # if not id_df.loc[id_df.subject_id.str.contains(subject_id, na=False), "ref_id"].empty:
#     if not id_df.loc[id_df["subject_id"] == subject_id, "ref_id"].empty:
#         # extract list of all OTUs found in that subject
#         # subject_otus = list(id_df.loc[id_df.subject_id.str.contains(subject_id, na=False), "ref_id"].values)
#         subject_otus = list(id_df.loc[id_df["subject_id"] == subject_id, "ref_id"].values)
#         # iterate through list of OTUs and add cell value for OTU, subject_id
#         for otu in subject_otus:
#             # take away NA values
#             if str(otu) != "nan":
#                 ref_id = "QUERY___" + str(otu)
#                 # if ref_id in otu_mat.iterrows():
#                 otu_mat.at[ref_id, subject_id] = 1
#
# # write otu_mat to df
# pd.DataFrame(otu_mat).to_csv(otu_matrix_file)

"""
same thing as above (create otu table for otu by subject) except with ref leaves only
"""

id_df = pd.read_csv("combined_IDs_forScoreThresholdHits_closestRef_02.csv")
subject_ids = subject_df.merged_subject_id.unique()  # effectively the sample columns

# read in tree file and get the leaf names
with open(tree_file, mode='r') as f:
    tree = Tree(f.read())
ref_ids = tree.get_leaf_names()  # effectively the OTU rows

# make df with subject_id as column names and OTUs as row names; all cells = 0
otu_mat = pd.DataFrame(columns=subject_ids, index=ref_ids, data=0)

# iterate by subject_id from subject ID list
for subject_id in subject_ids:
    # if subject_id is in id_df, return list of leaf IDs associated with that subject_id
    # if not id_df.loc[id_df.subject_id.str.contains(subject_id, na=False), "ref_id"].empty:
    if not id_df.loc[id_df["subject_id"] == subject_id, "ref_id"].empty:
        # extract list of all OTUs found in that subject
        # subject_otus = list(id_df.loc[id_df.subject_id.str.contains(subject_id, na=False), "ref_id"].values)
        subject_otus = list(id_df.loc[id_df["subject_id"] == subject_id, "ref_id"].values)
        # iterate through list of OTUs and add cell value for OTU, subject_id
        for otu in subject_otus:
            # take away NA values
            if str(otu) != "nan":
                ref_id = str(otu)
                # if ref_id in otu_mat.iterrows():
                otu_mat.at[ref_id, subject_id] = 1

# write otu_mat to df
pd.DataFrame(otu_mat).to_csv("otu_subject_matrix_ref_0609.csv")
