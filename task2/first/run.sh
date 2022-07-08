#!/bin/bash
#SBATCH --no-requeue
#SBATCH --job-name="md-code"
#SBATCH --get-user-env
#SBATCH --output=_slurm-out.txt
#SBATCH --error=_slurm-error.txt
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
##SBATCH --time=02:00:00
##SBATCH --mem=10000


#SBATCH --comment="md course 2022"

./a.out -N 1000 -ns 30001 -rho 0.005 -fs 100 -dt 0.02 > out.txt

