#!/bin/bash
sample_file="/home/users/reb26/SRM22/main/config/biosample_accession_withAgeData_noSubjectID.txt"
output_file="/home/users/reb26/SRM22/main/workflow/out/sample_projects_accessions_withAgeData_noSubjectID.txt"
export PATH=${PATH}:${HOME}/edirect
cat $sample_file | while read line; do
  project=$(esearch -db biosample -query $line < /dev/null \
  | elink -target bioproject \
  | efetch \
  | grep "BioProject" \
  | head -1 \
  | sed "s/BioProject Accession: //")
  echo $line","$project >> $output_file
done
