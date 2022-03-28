## First assignment of the Molecular Dynamics course

# The task:

1) During how many integration steps is the Maxwell distribution established in the system? (1 point)

2) Get the dynamic memory time t_dm. (2 points)
To do this, you need to calculate the dependence of residuals <(r-r')^2>(t) and <(v-v')^2>(t) for two trajectories (r,v) and (r',v') with different integration steps, but at the same time. The brackets <...> mean averaging over the particles of the system. The moment when the dependence <(v-v')^2>(t) reaches a plateau corresponds to the time t_dm.

3) Equation of state
a) Plot the dependence of the pressure and compressibility of the system on the density at temperature T = 2.0. Compare with tabular data. (2 points)

b) Plot P_{kinetic}/(P_{kinetic} + P_{potential}) versus density. (1 point)

c) Check the formula for pressure correction in the presence of potential cutoff. To do this, you need to calculate the pressure without cutting, with cutting at different r_cut and find the difference. (2 points)

4) Estimation of the error of averaging
Using the block average method, evaluate the error in calculating the total energy (see Workshop 2). (2 points)

# Directory description

A detailed report and its .tex file are located in this directory(otchet.pdf and report/otchet.tex).
The first item of the task is completed in the maxwell/ catalog.
