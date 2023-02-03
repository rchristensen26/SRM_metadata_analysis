#!/bin/bash
#
#SBATCH --job-name=rerun_proj
#SBATCH --output=rerun_proj_%A_%a.out
#SBATCH --error=rerun_proj_%A_%a.err
#SBATCH --time=48:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem=100G

./retrieve_project_accession.bash < /home/users/reb26/SRM22/main/config/biosample_accessions_torerun.txt >> /home/users/reb26/SRM22/main/workflow/out/sample_projects_accessions_rerun.txt
