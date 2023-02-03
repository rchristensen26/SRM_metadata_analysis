#!/bin/bash
export PATH=${PATH}:${HOME}/edirect
while read line; do
  project=$(esearch -db biosample -query $line < /dev/null \
  | elink -target bioproject \
  | efetch \
  | grep "BioProject" \
  | head -1 \
  | sed "s/BioProject Accession: //")
  echo $line","$project
done
