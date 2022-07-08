#!/bin/bash
#SBATCH --no-requeue
#SBATCH --job-name="lammps"
#SBATCH --get-user-env
#SBATCH --partition=RT
#SBATCH --output=_slurm-out.txt
#SBATCH --error=_slurm-error.txt
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=4
##SBATCH --time=02:00:00
##SBATCH --mem=10000


#SBATCH --comment="md course 2022"
for t in 1 2 3 4; do
	mpirun -np 4 lmp_mpi -in ./input.in -v T 1.0 -v rho 0.8
done
