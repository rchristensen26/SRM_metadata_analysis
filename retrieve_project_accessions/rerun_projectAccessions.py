"""
This code checks which samples have retrieved project accessions and creates
a new file with sample accessions that do not yet have project accessions
(so i can rerun the code to retrieve project accessions for these)

side note: make multiple files so i can submit the jobs in batch
"""

BATCH_INDEX = 4
BATCH_SIZE = 8000
START_LINE = 32452 + (8000 * BATCH_INDEX)
END_LINE = START_LINE + BATCH_SIZE

full_sample_file = "biosample_accession_files/biosample_accessions.txt"
new_sample_file = "biosample_accession_files/biosample_accessions_" + str(START_LINE) + "-END" + ".txt"

# read in sample file as a list of samples
with open(full_sample_file) as f:
    samples = f.read().splitlines()

# make a subset list of samples by index
samples = '\n'.join(samples[START_LINE:])

# write subset sample list to new file
with open(new_sample_file, 'w') as f:
    f.write(samples)
