#!/bin/bash
#
#SBATCH --job-name=age_proj
#SBATCH --output=age_proj_%A_%a.out
#SBATCH --error=age_proj_%A_%a.err
#SBATCH --time=48:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=64G

./retrieve_project_accession_agedata.bash
