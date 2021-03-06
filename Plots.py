import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize = (9,7))

# Files to read the data from
dataAB1 = np.loadtxt('NS_data_eosABPR1.txt', unpack=True)
dataAB2 = np.loadtxt('NS_data_eosABPR2.txt', unpack=True)
dataAB3 = np.loadtxt('NS_data_eosABPR3.txt', unpack=True)
dataAP = np.loadtxt('NS_data_eosAPR.txt', unpack=True)
dataB1 = np.loadtxt('NS_data_eosBBB1.txt', unpack=True)
dataB2 = np.loadtxt('NS_data_eosBBB2.txt', unpack=True)
dataHL1 = np.loadtxt('NS_data_eosHLPS1.txt', unpack=True)
dataHL2 = np.loadtxt('NS_data_eosHLPS2.txt', unpack=True)
dataHL3 = np.loadtxt('NS_data_eosHLPS3.txt', unpack=True)
dataL = np.loadtxt('NS_data_eosL.txt', unpack=True)

# Some constants
G = 6.67e-8
c = 2.99792458e10
Msun = 1

# Extracting columns from the data files
# EOS ABPR1
ec_AB1 = dataAB1[0,:]*10**15   # central energy density
M_AB1 = dataAB1[1,:]           # Total mass
M0_AB1 = dataAB1[2,:]          # Baryonic mass
Mstat_AB1 = dataAB1[3,:]       # Mass when the NS is not rotating 
Mmax_AB1 = dataAB1[4,:]        # Maximum mass for a given EOS
R_AB1 = dataAB1[5,:]           # Radius 
Rratio_AB1 = dataAB1[6,:]      # Ratio rp/re
Rstat_AB1 = dataAB1[7,:]       # Radius when the NS is not rotating
omega_AB1 = dataAB1[8,:]       # Angular velocity (rad/sec)
komega_AB1 = dataAB1[9,:]      # Kepler limit
J_AB1 = dataAB1[10,:]          # Angular momentum
T_AB1 = dataAB1[11,:]          # Rotational kinetic energy
W_AB1 = dataAB1[12,:]          # Gravitational binding energy
Rmax_AB1 = dataAB1[13,:]       # Maximum radius of the non rotating star
Qmax_AB1 = dataAB1[14,:]       # MaxMass / MaxRadius of the non rotating star

# EOS ABPR2
ec_AB2 = dataAB2[0,:]*10**15   # central energy density
M_AB2 = dataAB2[1,:]           # Total mass
M0_AB2 = dataAB2[2,:]          # Baryonic mass
Mstat_AB2 = dataAB2[3,:]       # Mass when the NS is not rotating 
Mmax_AB2 = dataAB2[4,:]        # MAximum mass for a given EOS
R_AB2 = dataAB2[5,:]           # Radius 
Rratio_AB2 = dataAB2[6,:]      # Ratio rp/re
Rstat_AB2 = dataAB2[7,:]       # Radius when the NS is not rotating
omega_AB2 = dataAB2[8,:]       # Angular velocity (rad/sec)
komega_AB2 = dataAB2[9,:]      # Kepler limit
J_AB2 = dataAB2[10,:]          # Angular momentum
T_AB2 = dataAB2[11,:]          # Rotational kinetic energy
W_AB2 = dataAB2[12,:]          # Gravitational binding energy
Rmax_AB2 = dataAB2[13,:]       # Maximum radius of the non rotating star
Qmax_AB2 = dataAB2[14,:]       # MaxMass / MaxRadius of the non rotating star

# EOS ABPR3
ec_AB3 = dataAB3[0,:]*10**15   # central energy density
M_AB3 = dataAB3[1,:]           # Total mass
M0_AB3 = dataAB3[2,:]          # Baryonic mass
Mstat_AB3 = dataAB3[3,:]       # Mass when the NS is not rotating 
Mmax_AB3 = dataAB3[4,:]        # MAximum mass for a given EOS
R_AB3 = dataAB3[5,:]           # Radius 
Rratio_AB3 = dataAB3[6,:]      # Ratio rp/re
Rstat_AB3 = dataAB3[7,:]       # Radius when the NS is not rotating
omega_AB3 = dataAB3[8,:]       # Angular velocity (rad/sec)
komega_AB3 = dataAB3[9,:]      # Kepler limit
J_AB3 = dataAB3[10,:]          # Angular momentum
T_AB3 = dataAB3[11,:]          # Rotational kinetic energy
W_AB3 = dataAB3[12,:]          # Gravitational binding energy
Rmax_AB3 = dataAB3[13,:]       # Maximum radius of the non rotating star
Qmax_AB3 = dataAB3[14,:]       # MaxMass / MaxRadius of the non rotating star

# EOS APR
ec_AP = dataAP[0,:]*10**15   # central energy density
M_AP = dataAP[1,:]           # Total mass
M0_AP = dataAP[2,:]          # Baryonic mass
Mstat_AP = dataAP[3,:]       # Mass when the NS is not rotating 
Mmax_AP = dataAP[4,:]        # MAximum mass for a given EOS
R_AP = dataAP[5,:]           # Radius 
Rratio_AP = dataAP[6,:]      # Ratio rp/re
Rstat_AP = dataAP[7,:]       # Radius when the NS is not rotating
omega_AP = dataAP[8,:]       # Angular velocity (rad/sec)
komega_AP = dataAP[9,:]      # Kepler limit
J_AP = dataAP[10,:]          # Angular momentum
T_AP = dataAP[11,:]          # Rotational kinetic energy
W_AP = dataAP[12,:]          # Gravitational binding energy
Rmax_AP = dataAP[13,:]       # Maximum radius of the non rotating star
Qmax_AP = dataAP[14,:]       # MaxMass / MaxRadius of the non rotating star

# EOS BBB1
ec_B1 = dataB1[0,:]*10**15   # central energy density
M_B1 = dataB1[1,:]           # Total mass
M0_B1 = dataB1[2,:]          # Baryonic mass
Mstat_B1 = dataB1[3,:]       # Mass when the NS is not rotating 
Mmax_B1 = dataB1[4,:]        # MAximum mass for a given EOS
R_B1 = dataB1[5,:]           # Radius 
Rratio_B1 = dataB1[6,:]      # Ratio rp/re
Rstat_B1 = dataB1[7,:]       # Radius when the NS is not rotating
omega_B1 = dataB1[8,:]       # Angular velocity (rad/sec)
komega_B1 = dataB1[9,:]      # Kepler limit
J_B1 = dataB1[10,:]          # Angular momentum
T_B1 = dataB1[11,:]          # Rotational kinetic energy
W_B1 = dataB1[12,:]          # Gravitational binding energy
Rmax_B1 = dataB1[13,:]       # Maximum radius of the non rotating star
Qmax_B1 = dataB1[14,:]       # MaxMass / MaxRadius of the non rotating star

# EOS BBB2
ec_B2 = dataB2[0,:]*10**15   # central energy density
M_B2 = dataB2[1,:]           # Total mass
M0_B2 = dataB2[2,:]          # Baryonic mass
Mstat_B2 = dataB2[3,:]       # Mass when the NS is not rotating 
Mmax_B2 = dataB2[4,:]        # MAximum mass for a given EOS
R_B2 = dataB2[5,:]           # Radius 
Rratio_B2 = dataB2[6,:]      # Ratio rp/re
Rstat_B2 = dataB2[7,:]       # Radius when the NS is not rotating
omega_B2 = dataB2[8,:]       # Angular velocity (rad/sec)
komega_B2 = dataB2[9,:]      # Kepler limit
J_B2 = dataB2[10,:]          # Angular momentum
T_B2 = dataB2[11,:]          # Rotational kinetic energy
W_B2 = dataB2[12,:]          # Gravitational binding energy
Rmax_B2 = dataB2[13,:]       # Maximum radius of the non rotating star
Qmax_B2 = dataB2[14,:]       # MaxMass / MaxRadius of the non rotating star

# EOS HLPS1
ec_HL1 = dataHL1[0,:]*10**15   # central energy density
M_HL1 = dataHL1[1,:]           # Total mass
M0_HL1 = dataHL1[2,:]          # Baryonic mass
Mstat_HL1 = dataHL1[3,:]       # Mass when the NS is not rotating 
Mmax_HL1 = dataHL1[4,:]        # MAximum mass for a given EOS
R_HL1 = dataHL1[5,:]           # Radius 
Rratio_HL1 = dataHL1[6,:]      # Ratio rp/re
Rstat_HL1 = dataHL1[7,:]       # Radius when the NS is not rotating
omega_HL1 = dataHL1[8,:]       # Angular velocity (rad/sec)
komega_HL1 = dataHL1[9,:]      # Kepler limit
J_HL1 = dataHL1[10,:]          # Angular momentum
T_HL1 = dataHL1[11,:]          # Rotational kinetic energy
W_HL1 = dataHL1[12,:]          # Gravitational binding energy
Rmax_HL1 = dataHL1[13,:]       # Maximum radius of the non rotating star
Qmax_HL1 = dataHL1[14,:]       # MaxMass / MaxRadius of the non rotating star

# EOS HLPS2
ec_HL2 = dataHL2[0,:]*10**15   # central energy density
M_HL2 = dataHL2[1,:]           # Total mass
M0_HL2 = dataHL2[2,:]          # Baryonic mass
Mstat_HL2 = dataHL2[3,:]       # Mass when the NS is not rotating 
Mmax_HL2 = dataHL2[4,:]        # MAximum mass for a given EOS
R_HL2 = dataHL2[5,:]           # Radius 
Rratio_HL2 = dataHL2[6,:]      # Ratio rp/re
Rstat_HL2 = dataHL2[7,:]       # Radius when the NS is not rotating
omega_HL2 = dataHL2[8,:]       # Angular velocity (rad/sec)
komega_HL2 = dataHL2[9,:]      # Kepler limit
J_HL2 = dataHL2[10,:]          # Angular momentum
T_HL2 = dataHL2[11,:]          # Rotational kinetic energy
W_HL2 = dataHL2[12,:]          # Gravitational binding energy
Rmax_HL2 = dataHL2[13,:]       # Maximum radius of the non rotating star
Qmax_HL2 = dataHL2[14,:]       # MaxMass / MaxRadius of the non rotating star

# EOS HLPS3
ec_HL3 = dataHL3[0,:]*10**15   # central energy density
M_HL3 = dataHL3[1,:]           # Total mass
M0_HL3 = dataHL3[2,:]          # Baryonic mass
Mstat_HL3 = dataHL3[3,:]       # Mass when the NS is not rotating 
Mmax_HL3 = dataHL3[4,:]        # MAximum mass for a given EOS
R_HL3 = dataHL3[5,:]           # Radius 
Rratio_HL3 = dataHL3[6,:]      # Ratio rp/re
Rstat_HL3 = dataHL3[7,:]       # Radius when the NS is not rotating
omega_HL3 = dataHL3[8,:]       # Angular velocity (rad/sec)
komega_HL3 = dataHL3[9,:]      # Kepler limit
J_HL3 = dataHL3[10,:]          # Angular momentum
T_HL3 = dataHL3[11,:]          # Rotational kinetic energy
W_HL3 = dataHL3[12,:]          # Gravitational binding energy
Rmax_HL3 = dataHL3[13,:]       # Maximum radius of the non rotating star
Qmax_HL3 = dataHL3[14,:]       # MaxMass / MaxRadius of the non rotating star

# EOS L
ec_L = dataL[0,:]*10**15   # central energy density
M_L = dataL[1,:]           # Total mass
M0_L = dataL[2,:]          # Baryonic mass
Mstat_L = dataL[3,:]       # Mass when the NS is not rotating 
Mmax_L = dataL[4,:]        # MAximum mass for a given EOS
R_L = dataL[5,:]           # Radius 
Rratio_L = dataL[6,:]      # Ratio rp/re
Rstat_L = dataL[7,:]       # Radius when the NS is not rotating
omega_L = dataL[8,:]       # Angular velocity (rad/sec)
komega_L = dataL[9,:]      # Kepler limit
J_L = dataL[10,:]          # Angular momentum
T_L = dataL[11,:]          # Rotational kinetic energy
W_L = dataL[12,:]          # Gravitational binding energy
Rmax_L = dataL[13,:]       # Maximum radius of the non rotating star
Qmax_L = dataL[14,:]       # MaxMass / MaxRadius of the non rotating star

# Converting quantities to CGS
# EOS ABPR1
m_AB1 = M_AB1 * 1.9884e33   # Mass
r_AB1 = R_AB1 * 1.0e5       # Radius
rstat_AB1 = Rstat_AB1 * 1.0e5   # Radius of the non rotating NS
mstat_AB1 = Mstat_AB1 * 1.9884e33   # Mass of the non rotating NS
delta_AB1 = omega_AB1 * ((rstat_AB1**3)/(G*mstat_AB1))**(0.5)   # Normalized omega
m0_AB1 = M0_AB1 * 1.9884e33     # Baryonic mass
normJ_AB1 = (c*J_AB1)/(G*m0_AB1**2)     # Normalized angular momentum
# EOS ABPR2
m_AB2 = M_AB2 * 1.9884e33   # Mass
r_AB2 = R_AB2 * 1.0e5       # Radius
rstat_AB2 = Rstat_AB2 * 1.0e5   # Radius of the non rotating NS
mstat_AB2 = Mstat_AB2 * 1.9884e33   # Mass of the non rotating NS
delta_AB2 = omega_AB2 * ((rstat_AB2**3)/(G*mstat_AB2))**(0.5)   # Normalized omega
m0_AB2 = M0_AB2 * 1.9884e33     # Baryonic mass
normJ_AB2 = (c*J_AB2)/(G*m0_AB2**2)     # Normalized angular momentum
# EOS ABPR3
m_AB3 = M_AB3 * 1.9884e33   # Mass
r_AB3 = R_AB3 * 1.0e5       # Radius
rstat_AB3 = Rstat_AB3 * 1.0e5   # Radius of the non rotating NS
mstat_AB3 = Mstat_AB3 * 1.9884e33   # Mass of the non rotating NS
delta_AB3 = omega_AB3 * ((rstat_AB3**3)/(G*mstat_AB3))**(0.5)   # Normalized omega
m0_AB3 = M0_AB3 * 1.9884e33     # Baryonic mass
normJ_AB3 = (c*J_AB3)/(G*m0_AB3**2)     # Normalized angular momentum
# EOS APR
m_AP = M_AP * 1.9884e33   # Mass
r_AP = R_AP * 1.0e5       # Radius
rstat_AP = Rstat_AP * 1.0e5   # Radius of the non rotating NS
mstat_AP = Mstat_AP * 1.9884e33   # Mass of the non rotating NS
delta_AP = omega_AP * ((rstat_AP**3)/(G*mstat_AP))**(0.5)   # Normalized omega
m0_AP = M0_AP * 1.9884e33     # Baryonic mass
normJ_AP = (c*J_AP)/(G*m0_AP**2)     # Normalized angular momentum
# EOS BBB1
m_B1 = M_B1 * 1.9884e33   # Mass
r_B1 = R_B1 * 1.0e5       # Radius
rstat_B1 = Rstat_B1 * 1.0e5   # Radius of the non rotating NS
mstat_B1 = Mstat_B1 * 1.9884e33   # Mass of the non rotating NS
delta_B1 = omega_B1 * ((rstat_B1**3)/(G*mstat_B1))**(0.5)   # Normalized omega
m0_B1 = M0_B1 * 1.9884e33     # Baryonic mass
normJ_B1 = (c*J_B1)/(G*m0_B1**2)     # Normalized angular momentum
# EOS BBB2
m_B2 = M_B2 * 1.9884e33   # Mass
r_B2 = R_B2 * 1.0e5       # Radius
rstat_B2 = Rstat_B2 * 1.0e5   # Radius of the non rotating NS
mstat_B2 = Mstat_B2 * 1.9884e33   # Mass of the non rotating NS
delta_B2 = omega_B2 * ((rstat_B2**3)/(G*mstat_B2))**(0.5)   # Normalized omega
m0_B2 = M0_B2 * 1.9884e33     # Baryonic mass
normJ_B2 = (c*J_B2)/(G*m0_B2**2)     # Normalized angular momentum
# EOS HLPS1
m_HL1 = M_HL1 * 1.9884e33   # Mass
r_HL1 = R_HL1 * 1.0e5       # Radius
rstat_HL1 = Rstat_HL1 * 1.0e5   # Radius of the non rotating NS
mstat_HL1 = Mstat_HL1 * 1.9884e33   # Mass of the non rotating NS
delta_HL1 = omega_HL1 * ((rstat_HL1**3)/(G*mstat_HL1))**(0.5)   # Normalized omega
m0_HL1 = M0_HL1 * 1.9884e33     # Baryonic mass
normJ_HL1 = (c*J_HL1)/(G*m0_HL1**2)     # Normalized angular momentum
# EOS HLPS2
m_HL2 = M_HL2 * 1.9884e33   # Mass
r_HL2 = R_HL2 * 1.0e5       # Radius
rstat_HL2 = Rstat_HL2 * 1.0e5   # Radius of the non rotating NS
mstat_HL2 = Mstat_HL2 * 1.9884e33   # Mass of the non rotating NS
delta_HL2 = omega_HL2 * ((rstat_HL2**3)/(G*mstat_HL2))**(0.5)   # Normalized omega
m0_HL2 = M0_HL2 * 1.9884e33     # Baryonic mass
normJ_HL2 = (c*J_HL2)/(G*m0_HL2**2)     # Normalized angular momentum
# EOS HLPS3
m_HL3 = M_HL3 * 1.9884e33   # Mass
r_HL3 = R_HL3 * 1.0e5       # Radius
rstat_HL3 = Rstat_HL3 * 1.0e5   # Radius of the non rotating NS
mstat_HL3 = Mstat_HL3 * 1.9884e33   # Mass of the non rotating NS
delta_HL3 = omega_HL3 * ((rstat_HL3**3)/(G*mstat_HL3))**(0.5)   # Normalized omega
m0_HL3 = M0_HL3 * 1.9884e33     # Baryonic mass
normJ_HL3 = (c*J_HL3)/(G*m0_HL3**2)     # Normalized angular momentum
# EOS L
m_L = M_L * 1.9884e33   # Mass
r_L = R_L * 1.0e5       # Radius
rstat_L = Rstat_L * 1.0e5   # Radius of the non rotating NS
mstat_L = Mstat_L * 1.9884e33   # Mass of the non rotating NS
delta_L = omega_L * ((rstat_L**3)/(G*mstat_L))**(0.5)   # Normalized omega
m0_L = M0_L * 1.9884e33     # Baryonic mass
normJ_L = (c*J_L)/(G*m0_L**2)     # Normalized angular momentum

# Menu
print('Choose the plot to generate (Choose only integer numbers)')
print('1. Sequences of Mass vs energy density')
print('2. Mass vs Radius')
print('3. Omega vs Mass')
print('4. (M-M*)/M* vs omega')
print('5. (M-M*)/M* vs normalized omega')
print('6. (M-M_0)/M_0 vs omega')
print('7. (M-M_0)/M_0 vs normalized omega')
print('8. M/Mmax vs normalized omega')
print('9. (R-R*)/R* vs omega')
print('10. (R-R*)/R* vs normalized omega')
print('11. Compactness vs omega')
print('12. Compactness vs normalized omega')
print('13. omega vs Normalized angular momentum')
print('14. omega vs T/W')
print('15. 3D plot of M/Mmax, normalized omega and compactness')
print('16. 3D plot of (R-R*)/R*, normalized omega and compactness')
print('17. 3D plot of (M-M*)/M*, normalized omega and compactness')
print('18. 3D plot of (M-M_0)/M_0, normalized omega and compactness')

method = input()


if method == 1:
    plt.scatter(ec_AB1, M_AB1, s=3, label = 'EOS ABPR1')
    plt.scatter(ec_AB2, M_AB2, s=3, label = 'EOS ABPR2')
    plt.scatter(ec_AB3, M_AB3, s=3, label = 'EOS ABPR3')
    plt.scatter(ec_AP, M_AP, s=3, label = 'EOS APR')
    plt.scatter(ec_B1, M_B1, s=3, label = 'EOS BBB1')
    plt.scatter(ec_B2, M_B2, s=3, label = 'EOS BBB2')
    plt.scatter(ec_HL1, M_HL1, s=3, label = 'EOS HLPS1')
    plt.scatter(ec_HL2, M_HL2, s=3, label = 'EOS HLPS2')
    plt.scatter(ec_HL3, M_HL3, s=3, label = 'EOS HLPS3')
    plt.scatter(ec_L, M_L, s=3, label = 'EOS L')
    plt.xlabel(r'$\varepsilon_c$ [g cm$^{-3}$]', fontsize='15')
    plt.ylabel(r'$M$ [M$_\odot$]', fontsize='15')
    plt.legend()
    plt.show()

elif method == 2:
    plt.scatter(R_AB1, M_AB1, s=3, label = 'EOS ABPR1')
    plt.scatter(R_AB2, M_AB2, s=3, label = 'EOS ABPR2')
    plt.scatter(R_AB3, M_AB3, s=3, label = 'EOS ABPR3')
    plt.scatter(R_AP, M_AP, s=3, label = 'EOS APR')
    plt.scatter(R_B1, M_B1, s=3, label = 'EOS BBB1')
    plt.scatter(R_B2, M_B2, s=3, label = 'EOS BBB2')
    plt.scatter(R_HL1, M_HL1, s=3, label = 'EOS HLPS1')
    plt.scatter(R_HL2, M_HL2, s=3, label = 'EOS HLPS2')
    plt.scatter(R_HL3, M_HL3, s=3, label = 'EOS HLPS3')
    plt.scatter(R_L, M_L, s=3, label = 'EOS L')
    plt.xlabel(r'$R$ [km]', fontsize='15')
    plt.ylabel(r'$M$ [M$_\odot$]', fontsize='15')
    plt.legend()
    plt.show()
    
elif method == 3:
    plt.scatter(M_AB1, omega_AB1, s=3, label = 'EOS ABPR1')
    plt.scatter(M_AB2, omega_AB2, s=3, label = 'EOS ABPR2')
    plt.scatter(M_AB3, omega_AB3, s=3, label = 'EOS ABPR3')
    plt.scatter(M_AP, omega_AP, s=3, label = 'EOS APR')
    plt.scatter(M_B1, omega_B1, s=3, label = 'EOS BBB1')
    plt.scatter(M_B2, omega_B2, s=3, label = 'EOS BBB2')
    plt.scatter(M_HL1, omega_HL1, s=3, label = 'EOS HLPS1')
    plt.scatter(M_HL2, omega_HL2, s=3, label = 'EOS HLPS2')
    plt.scatter(M_HL3, omega_HL3, s=3, label = 'EOS HLPS3')
    plt.scatter(M_L, omega_L, s=3, label = 'EOS L')
    plt.xlabel(r'$M$ [M$_\odot$]', fontsize='15')
    plt.ylabel(r'$\Omega$', fontsize='15')
    plt.legend()
    plt.show()
    
elif method == 4:
    plt.scatter(omega_AB1, (M_AB1-Mstat_AB1)/Mstat_AB1, s=3, label = 'EOS ABPR1')
    plt.scatter(omega_AB2, (M_AB2-Mstat_AB2)/Mstat_AB2, s=3, label = 'EOS ABPR2')
    plt.scatter(omega_AB3, (M_AB3-Mstat_AB3)/Mstat_AB3, s=3, label = 'EOS ABPR3')
    plt.scatter(omega_AP, (M_AP-Mstat_AP)/Mstat_AP, s=3, label = 'EOS APR')
    plt.scatter(omega_B1, (M_B1-Mstat_B1)/Mstat_B1, s=3, label = 'EOS BBB1')
    plt.scatter(omega_B2, (M_B2-Mstat_B2)/Mstat_B2, s=3, label = 'EOS BBB2')
    plt.scatter(omega_HL1, (M_HL1-Mstat_HL1)/Mstat_HL1, s=3, label = 'EOS HLPS1')
    plt.scatter(omega_HL2, (M_HL2-Mstat_HL2)/Mstat_HL2, s=3, label = 'EOS HLPS2')
    plt.scatter(omega_HL3, (M_HL3-Mstat_HL3)/Mstat_HL3, s=3, label = 'EOS HLPS3')
    plt.scatter(omega_L, (M_L-Mstat_L)/Mstat_L, s=3, label = 'EOS L')
    plt.xlabel(r'$\Omega$ [Hz]', fontsize='15')
    plt.ylabel(r'$(M-M_*)/M_*$', fontsize='15')
    plt.legend()
    plt.show()
    
elif method == 5:
    plt.scatter(delta_AB1, (M_AB1-Mstat_AB1)/Mstat_AB1, s=3, label = 'EOS ABPR1')
    plt.scatter(delta_AB2, (M_AB2-Mstat_AB2)/Mstat_AB2, s=3, label = 'EOS ABPR2')
    plt.scatter(delta_AB3, (M_AB3-Mstat_AB3)/Mstat_AB3, s=3, label = 'EOS ABPR3')
    plt.scatter(delta_AP, (M_AP-Mstat_AP)/Mstat_AP, s=3, label = 'EOS APR')
    plt.scatter(delta_B1, (M_B1-Mstat_B1)/Mstat_B1, s=3, label = 'EOS BBB1')
    plt.scatter(delta_B2, (M_B2-Mstat_B2)/Mstat_B2, s=3, label = 'EOS BBB2')
    plt.scatter(delta_HL1, (M_HL1-Mstat_HL1)/Mstat_HL1, s=3, label = 'EOS HLPS1')
    plt.scatter(delta_HL2, (M_HL2-Mstat_HL2)/Mstat_HL2, s=3, label = 'EOS HLPS2')
    plt.scatter(delta_HL3, (M_HL3-Mstat_HL3)/Mstat_HL3, s=3, label = 'EOS HLPS3')
    plt.scatter(delta_L, (M_L-Mstat_L)/Mstat_L, s=3, label = 'EOS L')
    plt.xlabel(r'$\Omega (R_*^3 / GM_*)^{1/2}$', fontsize='15')
    plt.ylabel(r'$(M-M_*)/M_*$', fontsize='15')
    plt.legend()
    plt.show()
    
elif method == 6:
    plt.scatter(omega_AB1, (M0_AB1-M_AB1)/M0_AB1, s=3, label = 'EOS ABPR1')
    plt.scatter(omega_AB2, (M0_AB2-M_AB2)/M0_AB2, s=3, label = 'EOS ABPR2')
    plt.scatter(omega_AB3, (M0_AB3-M_AB3)/M0_AB3, s=3, label = 'EOS ABPR3')
    plt.scatter(omega_AP, (M0_AP-M_AP)/M0_AP, s=3, label = 'EOS APR')
    plt.scatter(omega_B1, (M0_B1-M_B1)/M0_B1, s=3, label = 'EOS BBB1')
    plt.scatter(omega_B2, (M0_B2-M_B2)/M0_B2, s=3, label = 'EOS BBB2')
    plt.scatter(omega_HL1, (M0_HL1-M_HL1)/M0_HL1, s=3, label = 'EOS HLPS1')
    plt.scatter(omega_HL2, (M0_HL2-M_HL2)/M0_HL2, s=3, label = 'EOS HLPS2')
    plt.scatter(omega_HL3, (M0_HL3-M_HL3)/M0_HL3, s=3, label = 'EOS HLPS3')
    plt.scatter(omega_L, (M0_L-M_L)/M0_L, s=3, label = 'EOS L')
    plt.xlabel(r'$\Omega$ [Hz]', fontsize='15')
    plt.ylabel(r'$(M_0-M)/M_0$', fontsize='15')
    plt.legend()
    plt.show()
    
elif method == 7:
    plt.scatter(delta_AB1, (M0_AB1-M_AB1)/M0_AB1, s=3, label = 'EOS ABPR1')
    plt.scatter(delta_AB2, (M0_AB2-M_AB2)/M0_AB2, s=3, label = 'EOS ABPR2')
    plt.scatter(delta_AB3, (M0_AB3-M_AB3)/M0_AB3, s=3, label = 'EOS ABPR3')
    plt.scatter(delta_AP, (M0_AP-M_AP)/M0_AP, s=3, label = 'EOS APR')
    plt.scatter(delta_B1, (M0_B1-M_B1)/M0_B1, s=3, label = 'EOS BBB1')
    plt.scatter(delta_B2, (M0_B2-M_B2)/M0_B2, s=3, label = 'EOS BBB2')
    plt.scatter(delta_HL1, (M0_HL1-M_HL1)/M0_HL1, s=3, label = 'EOS HLPS1')
    plt.scatter(delta_HL2, (M0_HL2-M_HL2)/M0_HL2, s=3, label = 'EOS HLPS2')
    plt.scatter(delta_HL3, (M0_HL3-M_HL3)/M0_HL3, s=3, label = 'EOS HLPS3')
    plt.scatter(delta_L, (M0_L-M_L)/M0_L, s=3, label = 'EOS L')
    plt.xlabel(r'$\Omega (R_*^3 / GM_*)^{1/2}$', fontsize='15')
    plt.ylabel(r'$(M_0-M)/M_0$', fontsize='15')
    plt.legend()
    plt.show()
  
elif method == 8:
    plt.scatter(delta_AB1, M_AB1/Mmax_AB1, s=3, label = 'EOS ABPR1')
    plt.scatter(delta_AB2, M_AB2/Mmax_AB2, s=3, label = 'EOS ABPR2')
    plt.scatter(delta_AB3, M_AB3/Mmax_AB3, s=3, label = 'EOS ABPR3')
    plt.scatter(delta_AP, M_AP/Mmax_AP, s=3, label = 'EOS APR')
    plt.scatter(delta_B1, M_B1/Mmax_B1, s=3, label = 'EOS BBB1')
    plt.scatter(delta_B2, M_B2/Mmax_B2, s=3, label = 'EOS BBB2')
    plt.scatter(delta_HL1, M_HL1/Mmax_HL1, s=3, label = 'EOS HLPS1')
    plt.scatter(delta_HL2, M_HL2/Mmax_HL2, s=3, label = 'EOS HLPS2')
    plt.scatter(delta_HL3, M_HL3/Mmax_HL3, s=3, label = 'EOS HLPS3')
    plt.scatter(delta_L, M_L/Mmax_L, s=3, label = 'EOS L')
    plt.xlabel(r'$\Omega (R_*^3 / GM_*)^{1/2}$', fontsize='15')
    plt.ylabel(r'$M/M_{max}$', fontsize='15')
    plt.legend()
    plt.show()
    
elif method == 9:
    plt.scatter(omega_AB1, (R_AB1-Rstat_AB1)/Rstat_AB1, s=3, label = 'EOS ABPR1')
    plt.scatter(omega_AB2, (R_AB2-Rstat_AB2)/Rstat_AB2, s=3, label = 'EOS ABPR2')
    plt.scatter(omega_AB3, (R_AB3-Rstat_AB3)/Rstat_AB3, s=3, label = 'EOS ABPR3')
    plt.scatter(omega_AP, (R_AP-Rstat_AP)/Rstat_AP, s=3, label = 'EOS APR')
    plt.scatter(omega_B1, (R_B1-Rstat_B1)/Rstat_B1, s=3, label = 'EOS BBB1')
    plt.scatter(omega_B2, (R_B2-Rstat_B2)/Rstat_B2, s=3, label = 'EOS BBB2')
    plt.scatter(omega_HL1, (R_HL1-Rstat_HL1)/Rstat_HL1, s=3, label = 'EOS HLPS1')
    plt.scatter(omega_HL2, (R_HL2-Rstat_HL2)/Rstat_HL2, s=3, label = 'EOS HLPS2')
    plt.scatter(omega_HL3, (R_HL3-Rstat_HL3)/Rstat_HL3, s=3, label = 'EOS HLPS3')
    plt.scatter(omega_L, (R_L-Rstat_L)/Rstat_L, s=3, label = 'EOS L')
    plt.xlabel(r'$\Omega$ [Hz]', fontsize='15')
    plt.ylabel(r'$(R-R_*)/R_*$', fontsize='15')
    plt.legend()
    plt.show()

elif method == 10:
    plt.scatter(delta_AB1, (R_AB1-Rstat_AB1)/Rstat_AB1, s=3, label = 'EOS ABPR1')
    plt.scatter(delta_AB2, (R_AB2-Rstat_AB2)/Rstat_AB2, s=3, label = 'EOS ABPR2')
    plt.scatter(delta_AB3, (R_AB3-Rstat_AB3)/Rstat_AB3, s=3, label = 'EOS ABPR3')
    plt.scatter(delta_AP, (R_AP-Rstat_AP)/Rstat_AP, s=3, label = 'EOS APR')
    plt.scatter(delta_B1, (R_B1-Rstat_B1)/Rstat_B1, s=3, label = 'EOS BBB1')
    plt.scatter(delta_B2, (R_B2-Rstat_B2)/Rstat_B2, s=3, label = 'EOS BBB2')
    plt.scatter(delta_HL1, (R_HL1-Rstat_HL1)/Rstat_HL1, s=3, label = 'EOS HLPS1')
    plt.scatter(delta_HL2, (R_HL2-Rstat_HL2)/Rstat_HL2, s=3, label = 'EOS HLPS2')
    plt.scatter(delta_HL3, (R_HL3-Rstat_HL3)/Rstat_HL3, s=3, label = 'EOS HLPS3')
    plt.scatter(delta_L, (R_L-Rstat_L)/Rstat_L, s=3, label = 'EOS L')
    plt.xlabel(r'$\Omega (R_*^3 / GM_*)^{1/2}$', fontsize='15')
    plt.ylabel(r'$(R-R_*)/R_*$', fontsize='15')
    plt.legend()
    plt.show()
    
elif method == 11:
    plt.scatter(omega_AB1, (M_AB1/Msun)*(1.47/R_AB1), s=3, label = 'EOS ABPR1')
    plt.scatter(omega_AB2, (M_AB2/Msun)*(1.47/R_AB2), s=3, label = 'EOS ABPR2')
    plt.scatter(omega_AB3, (M_AB3/Msun)*(1.47/R_AB3), s=3, label = 'EOS ABPR3')
    plt.scatter(omega_AP, (M_AP/Msun)*(1.47/R_AP), s=3, label = 'EOS APR')
    plt.scatter(omega_B1, (M_B1/Msun)*(1.47/R_B1), s=3, label = 'EOS BBB1')
    plt.scatter(omega_B2, (M_B2/Msun)*(1.47/R_B2), s=3, label = 'EOS BBB2')
    plt.scatter(omega_HL1, (M_HL1/Msun)*(1.47/R_HL1), s=3, label = 'EOS HLPS1')
    plt.scatter(omega_HL2, (M_HL2/Msun)*(1.47/R_HL2), s=3, label = 'EOS HLPS2')
    plt.scatter(omega_HL3, (M_HL3/Msun)*(1.47/R_HL3), s=3, label = 'EOS HLPS3')
    plt.scatter(omega_L, (M_L/Msun)*(1.47/R_L), s=3, label = 'EOS L')
    plt.xlabel(r'$\Omega$ [Hz]', fontsize='15')
    plt.ylabel(r'$\zeta$', fontsize='15')
    plt.legend()
    plt.show()
    
elif method == 12:
    plt.scatter(delta_AB1, (M_AB1/Msun)*(1.47/R_AB1), s=3, label = 'EOS ABPR1')
    plt.scatter(delta_AB2, (M_AB2/Msun)*(1.47/R_AB2), s=3, label = 'EOS ABPR2')
    plt.scatter(delta_AB3, (M_AB3/Msun)*(1.47/R_AB3), s=3, label = 'EOS ABPR3')
    plt.scatter(delta_AP, (M_AP/Msun)*(1.47/R_AP), s=3, label = 'EOS APR')
    plt.scatter(delta_B1, (M_B1/Msun)*(1.47/R_B1), s=3, label = 'EOS BBB1')
    plt.scatter(delta_B2, (M_B2/Msun)*(1.47/R_B2), s=3, label = 'EOS BBB2')
    plt.scatter(delta_HL1, (M_HL1/Msun)*(1.47/R_HL1), s=3, label = 'EOS HLPS1')
    plt.scatter(delta_HL2, (M_HL2/Msun)*(1.47/R_HL2), s=3, label = 'EOS HLPS2')
    plt.scatter(delta_HL3, (M_HL3/Msun)*(1.47/R_HL3), s=3, label = 'EOS HLPS3')
    plt.scatter(delta_L, (M_L/Msun)*(1.47/R_L), s=3, label = 'EOS L')
    plt.xlabel(r'$\Omega (R_*^3 / GM_*)^{1/2}$', fontsize='15')
    plt.ylabel(r'$\zeta$', fontsize='15')
    plt.legend()
    plt.show()
    
elif method == 13:
    plt.scatter(normJ_AB1, omega_AB1, s=3, label = 'EOS ABPR1')
    plt.scatter(normJ_AB2, omega_AB2, s=3, label = 'EOS ABPR2')
    plt.scatter(normJ_AB3, omega_AB3, s=3, label = 'EOS ABPR3')
    plt.scatter(normJ_AP, omega_AP, s=3, label = 'EOS APR')
    plt.scatter(normJ_B1, omega_B1, s=3, label = 'EOS BBB1')
    plt.scatter(normJ_B2, omega_B2, s=3, label = 'EOS BBB2')
    plt.scatter(normJ_HL1, omega_HL1, s=3, label = 'EOS HLPS1')
    plt.scatter(normJ_HL2, omega_HL2, s=3, label = 'EOS HLPS2')
    plt.scatter(normJ_HL3, omega_HL3, s=3, label = 'EOS HLPS3')
    plt.scatter(normJ_L, omega_L, s=3, label = 'EOS L')
    plt.xlabel(r'$cJ/GM_0^2$', fontsize='15')
    plt.ylabel(r'$\Omega$ [Hz]', fontsize='15')
    plt.legend()
    plt.show()
    
elif method == 14:
    plt.scatter(T_AB1/W_AB1, omega_AB1, s=3, label = 'EOS ABPR1')
    plt.scatter(T_AB2/W_AB2, omega_AB2, s=3, label = 'EOS ABPR2')
    plt.scatter(T_AB3/W_AB3, omega_AB3, s=3, label = 'EOS ABPR3')
    plt.scatter(T_AP/W_AP, omega_AP, s=3, label = 'EOS APR')
    plt.scatter(T_B1/W_B1, omega_B1, s=3, label = 'EOS BBB1')
    plt.scatter(T_B2/W_B2, omega_B2, s=3, label = 'EOS BBB2')
    plt.scatter(T_HL1/W_HL1, omega_HL1, s=3, label = 'EOS HLPS1')
    plt.scatter(T_HL2/W_HL2, omega_HL2, s=3, label = 'EOS HLPS2')
    plt.scatter(T_HL3/W_HL3, omega_HL3, s=3, label = 'EOS HLPS3')
    plt.scatter(T_L/W_L, omega_L, s=3, label = 'EOS L')
    plt.xlabel(r'$T/W$', fontsize='15')
    plt.ylabel(r'$\Omega$ [Hz]', fontsize='15')
    plt.grid()
    plt.legend()
    plt.show()
    
elif method == 15:
    ax = fig.gca(projection='3d')
    ax.scatter(delta_AB1, G*mstat_AB1/(rstat_AB1*c**2), M_AB1/Mmax_AB1, label = 'EOS ABPR1')
    ax.scatter(delta_AB2, G*mstat_AB2/(rstat_AB2*c**2), M_AB2/Mmax_AB2, label = 'EOS ABPR2')
    ax.scatter(delta_AB3, G*mstat_AB3/(rstat_AB3*c**2), M_AB3/Mmax_AB3, label = 'EOS ABPR3')
    ax.scatter(delta_AP, G*mstat_AP/(rstat_AP*c**2), M_AP/Mmax_AP, label = 'EOS APR')
    ax.scatter(delta_B1, G*mstat_B1/(rstat_B1*c**2), M_B1/Mmax_B1, label = 'EOS BBB1')
    ax.scatter(delta_B2, G*mstat_B2/(rstat_B2*c**2), M_B2/Mmax_B2, label = 'EOS BBB2')
    ax.scatter(delta_HL1, G*mstat_HL1/(rstat_HL1*c**2), M_HL1/Mmax_HL1, label = 'EOS HLPS1')
    ax.scatter(delta_HL2, G*mstat_HL2/(rstat_HL2*c**2), M_HL2/Mmax_HL2, label = 'EOS HLPS2')
    ax.scatter(delta_HL3, G*mstat_HL3/(rstat_HL3*c**2), M_HL3/Mmax_HL3, label = 'EOS HLPS3')
    ax.scatter(delta_L, G*mstat_L/(rstat_L*c**2), M_L/Mmax_L, label = 'EOS L')
    ax.set_xlabel(r'$\Omega (R_*^3 / GM_*)^{1/2}$', fontsize='15')
    ax.set_ylabel(r'$GM_*/Rc^2$', fontsize='15')
    ax.set_zlabel(r'$M/M_{max}$', fontsize='15')
    plt.legend()
    plt.show()
    
elif method == 16:
    ax = fig.gca(projection='3d')
    ax.scatter(delta_AB1, G*mstat_AB1/(rstat_AB1*c**2), (R_AB1-Rstat_AB1)/Rstat_AB1, label = 'EOS ABPR1')
    ax.scatter(delta_AB2, G*mstat_AB2/(rstat_AB2*c**2), (R_AB2-Rstat_AB2)/Rstat_AB2, label = 'EOS ABPR2')
    ax.scatter(delta_AB3, G*mstat_AB3/(rstat_AB3*c**2), (R_AB3-Rstat_AB3)/Rstat_AB3, label = 'EOS ABPR3')
    ax.scatter(delta_AP, G*mstat_AP/(rstat_AP*c**2), (R_AP-Rstat_AP)/Rstat_AP, label = 'EOS APR')
    ax.scatter(delta_B1, G*mstat_B1/(rstat_B1*c**2), (R_B1-Rstat_B1)/Rstat_B1, label = 'EOS BBB1')
    ax.scatter(delta_B2, G*mstat_B2/(rstat_B2*c**2), (R_B2-Rstat_B2)/Rstat_B2, label = 'EOS BBB2')
    ax.scatter(delta_HL1, G*mstat_HL1/(rstat_HL1*c**2), (R_HL1-Rstat_HL1)/Rstat_HL1, label = 'EOS HLPS1')
    ax.scatter(delta_HL2, G*mstat_HL2/(rstat_HL2*c**2), (R_HL2-Rstat_HL2)/Rstat_HL2, label = 'EOS HLPS2')
    ax.scatter(delta_HL3, G*mstat_HL3/(rstat_HL3*c**2), (R_HL3-Rstat_HL3)/Rstat_HL3, label = 'EOS HLPS3')
    ax.scatter(delta_L, G*mstat_L/(rstat_L*c**2), (R_L-Rstat_L)/Rstat_L, label = 'EOS L')
    ax.set_xlabel(r'$\Omega (R_*^3 / GM_*)^{1/2}$', fontsize='15')
    ax.set_ylabel(r'$GM_*/Rc^2$', fontsize='15')
    ax.set_zlabel(r'$(R-R_*)/R_*$', fontsize='15')
    plt.legend()
    plt.show()
    
elif method == 17:
    ax = fig.gca(projection='3d')
    ax.scatter(delta_AB1, G*mstat_AB1/(rstat_AB1*c**2),(M_AB1-Mstat_AB1)/Mstat_AB1, label = 'EOS ABPR1')
    ax.scatter(delta_AB2, G*mstat_AB2/(rstat_AB2*c**2),(M_AB2-Mstat_AB2)/Mstat_AB2, label = 'EOS ABPR2')
    ax.scatter(delta_AB3, G*mstat_AB3/(rstat_AB3*c**2),(M_AB3-Mstat_AB3)/Mstat_AB3, label = 'EOS ABPR3')
    ax.scatter(delta_AP, G*mstat_AP/(rstat_AP*c**2),(M_AP-Mstat_AP)/Mstat_AP, label = 'EOS APR')
    ax.scatter(delta_B1, G*mstat_B1/(rstat_B1*c**2),(M_B1-Mstat_B1)/Mstat_B1, label = 'EOS BBB1')
    ax.scatter(delta_B2, G*mstat_B2/(rstat_B2*c**2),(M_B2-Mstat_B2)/Mstat_B2, label = 'EOS BBB2')
    ax.scatter(delta_HL1, G*mstat_HL1/(rstat_HL1*c**2),(M_HL1-Mstat_HL1)/Mstat_HL1, label = 'EOS HLPS1')
    ax.scatter(delta_HL2, G*mstat_HL2/(rstat_HL2*c**2),(M_HL2-Mstat_HL2)/Mstat_HL2, label = 'EOS HLPS2')
    ax.scatter(delta_HL3, G*mstat_HL3/(rstat_HL3*c**2),(M_HL3-Mstat_HL3)/Mstat_HL3, label = 'EOS HLPS3')
    ax.scatter(delta_L, G*mstat_L/(rstat_L*c**2),(M_L-Mstat_L)/Mstat_L, label = 'EOS L')
    ax.set_xlabel(r'$\Omega (R_*^3 / GM_*)^{1/2}$', fontsize='15')
    ax.set_ylabel(r'$GM_*/Rc^2$', fontsize='15')
    ax.set_zlabel(r'$(M-M_*)/M_*$', fontsize='15')
    plt.legend()
    plt.show()
    
elif method == 18:
    ax = fig.gca(projection='3d')
    ax.scatter(delta_AB1, G*mstat_AB1/(rstat_AB1*c**2), (M0_AB1-M_AB1)/M0_AB1, label = 'EOS ABPR1')
    ax.scatter(delta_AB2, G*mstat_AB2/(rstat_AB2*c**2), (M0_AB2-M_AB2)/M0_AB2, label = 'EOS ABPR2')
    ax.scatter(delta_AB3, G*mstat_AB3/(rstat_AB3*c**2), (M0_AB3-M_AB3)/M0_AB3, label = 'EOS ABPR3')
    ax.scatter(delta_AP, G*mstat_AP/(rstat_AP*c**2), (M0_AP-M_AP)/M0_AP, label = 'EOS APR')
    ax.scatter(delta_B1, G*mstat_B1/(rstat_B1*c**2), (M0_B1-M_B1)/M0_B1, label = 'EOS BBB1')
    ax.scatter(delta_B2, G*mstat_B2/(rstat_B2*c**2), (M0_B2-M_B2)/M0_B2, label = 'EOS BBB2')
    ax.scatter(delta_HL1, G*mstat_HL1/(rstat_HL1*c**2), (M0_HL1-M_HL1)/M0_HL1, label = 'EOS HLPS1')
    ax.scatter(delta_HL2, G*mstat_HL2/(rstat_HL2*c**2), (M0_HL2-M_HL2)/M0_HL2, label = 'EOS HLPS2')
    ax.scatter(delta_HL3, G*mstat_HL3/(rstat_HL3*c**2), (M0_HL3-M_HL3)/M0_HL3, label = 'EOS HLPS3')
    ax.scatter(delta_L, G*mstat_L/(rstat_L*c**2), (M0_L-M_L)/M0_L, label = 'EOS L')
    ax.set_xlabel(r'$\Omega (R_*^3 / GM_*)^{1/2}$', fontsize='15')
    ax.set_ylabel(r'$GM_*/Rc^2$', fontsize='15')
    ax.set_zlabel(r'$(M_0-M)/M_0$', fontsize='15')
    plt.legend()
    plt.show()
    
else:
    print('Enter a number from 1 to 18')
