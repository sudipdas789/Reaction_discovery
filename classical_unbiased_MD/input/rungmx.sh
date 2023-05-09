gmx_mpi grompp -f em.mdp -c amylase_GMX.gro -p amylase_GMX.top -o em.tpr -v
gmx_mpi grompp -f equil_nvt.mdp -c em.gro -p amylase_GMX.top -n index.ndx  -o nvt_eqm.tpr -v
gmx_mpi grompp -f equil_npt.mdp -c nvt_eqm.gro -p amylase_GMX.top -n index.ndx  -o npt_eqm1.tpr -v
gmx_mpi grompp -f equil_npt.mdp -c npt_eqm1.gro -p amylase_GMX_noSOL.top -n index.ndx -o npt_eqm2.tpr -v
gmx_mpi grompp -f equil_npt3.mdp -c npt_eqm2.gro -p amylase_GMX.top -n index.ndx  -o npt_eqm3.tpr -v
nohup mpirun -np 1 gmx_mpi mdrun -deffnm npt_eqm3 -gpu_id 0 -pin on -pinoffset 1 -ntomp 1 &
