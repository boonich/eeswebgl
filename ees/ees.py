from math import *

def SR1(M1,M2,R1,R2,L1,L2,MyR1,MyR2,Fi1p,Fi2p):
    G = 9.81
    J1 = 0.1269 * M1 * R1 * L1
    J2 = 0.1269 * M2 * R2 * L2
    Om1p = sqrt(M1 * G * MyR1 * R1 * abs(Fi1p) * 3.141592654 / (J1 * 180))
    Om2p = sqrt(M2 * G * MyR2 * R2 * abs(Fi2p) * 3.141592654 / (J2 * 180))

    if(Fi1p >= 0):
        Om1p = Om1p
    else:
        Om1p = -Om1p
        
    if(Fi2p >= 0):
        Om2p = Om2p
    else:
        Om2p = -Om2p
    
    return J1, J2, Om1p, Om2p

def SR2(M1,M2,R1,J1,J2,Om1p,Om2p,Om1,Om2,EES1,EES2,V1p,V2p,Ny1p,Ny2p):
    A = (1 / M1 + 1 / M2) * (J1 * (Om1p*Om1p - Om1*Om1) + M1 * EES1*EES1 + J2 * (Om2p*Om2p - Om2*Om2) + M2 * EES2*EES2)
    B = A + (V1p*V1p + V2p*V2p) - (2 * V1p * V2p * cos(Ny1p - Ny2p))
    C = sqrt(B - (V2p * sin(Ny2p) + V1p * M1 * sin(Ny1p) / M2)*(V2p * sin(Ny2p) + V1p * M1 * sin(Ny1p) / M2))
    V1 = M2 / (M1 + M2) * (C + M1 * V1p * cos(Ny1p) / M2 + V2p * cos(Ny2p))
    
    return V1

def SR3(M1,M2,V1p,V2p,Ny1p,Ny2p,Ny2):
    V1 = M2 / M1 * (V2p * cos(Ny2p) - V2p * sin(Ny2p) / tan(Ny2)) + V1p * cos(Ny1p) - V1p * sin(Ny1p) / tan(Ny2)
    
    return V1

def SR4(M1,M2,V1p,V2p,Ny1p,Ny2p,Ny2):
    V1 = M2 * V2p * cos(Ny2p) / M1 + V1p * cos(Ny1p)
    V2 = M1 * V1p * cos(Ny1p) / M2 + V2p * sin(Ny2p)
    dV1x = V1p * cos(Ny1p) - V1
    dV1y = V1p * sin(Ny1p)
    dV1 = sqrt(dV1x*dV1x + dV1y*dV1y)
    dV2x = V2p * cos(Ny2p)
    dV2y = V2p * sin(Ny2p) - V2
    dV2 = sqrt(dV2x*dV2x + dV2y*dV2y)
    S1 = dV1 * M1
    S2 = S1
    Gam1 = atan(dV1y / dV1x)
    Gam2 = atan(dV2y / dV2x)
    
    if(dV1x < 0):
        Gam1 = Gam1 + 3.141592654
        
    if(dV2x < 0):
        Gam2 = Gam2 + 3.141592654
    
    return V1, V2, Ny2, dV1, dV2, S1, S2, Gam1, Gam2

def SR5(M1,M2,V1p,V2p,Ny1p,Ny2p,Ny2,V1):
    V2x = V2p * cos(Ny2p) + M1 * (V1p * cos(Ny1p) - V1) / M2
    V2y = V2p * sin(Ny2p) + M1 * V1p * sin(Ny1p) / M2
    V2 = sqrt(V2x*V2x + V2y*V2y)
    Ny2 = atan(V2y / V2x)
    
    if(V2x < 0):
        Ny2 = Ny2 + 3.141592654
        
    dV1x = V1p * cos(Ny1p) - V1
    dV1y = V1p * sin(Ny1p)
    dV1 = sqrt(dV1x*dV1x + dV1y*dV1y)
    dV2x = V2p * cos(Ny2p) - V2 * cos(Ny2)
    dV2y = V2p * sin(Ny2p) - V2 * sin(Ny2)
    dV2 = sqrt(dV2x*dV2x + dV2y*dV2y)
    S1 = dV1 * M1
    S2 = S1
    Gam1 = atan(dV1y / dV1x)
    Gam2 = atan(dV2y / dV2x)
    
    if(dV1x < 0):
        Gam1 = Gam1 + 3.141592654
        
    if(dV2x < 0):
        Gam2 = Gam2 + 3.141592654
    
    return V2, Ny2, dV1, dV2, S1, S2, Gam1, Gam2

def SR6(Rho1,Rho2,Psi1,Psi2,SHA1,SHA2,S1,S2,Gam1,Gam2,Om1,Om2,J1,J2,M1,M2,V1,V2,V1p,V2p):
    RA1 = Rho1 + Psi1
    RA1x = SHA1 * cos(RA1)
    RA1y = SHA1 * sin(RA1)
    S1x = S1 * cos(Gam1)
    S1y = S1 * sin(Gam1)
    K1 = RA1x * S1y - RA1y * S1x
    RA2 = Rho2 + Psi2
    RA2x = SHA2 * cos(RA2)
    RA2y = SHA2 * sin(RA2)
    S2x = S2 * cos(Gam2)
    S2y = S2 * sin(Gam2)
    K2 = RA2x * S2y - RA2y * S2x
    Om1w = Om1 + K1 / J1
    Om2w = Om2 + K2 / J2
    e1w = abs(J1 * Om1w / S1)
    e2w = abs(J2 * Om2w / S2)
    I1 = M1 * V1
    I1p = M1 * V1p
    I2 = M2 * V2
    I2p = M2 * V2p
    
    return I1, I2, I1p, I2p, Om1w, Om2w, e1w, e2w

def SR7(M1,M2,V1,V2,J1,J2,Om1,Om2,V1p,V2p,Om1p,Om2p,ETD1,ETD2):
    D = M1 * V1*V1 + M2 * V2*V2 + J1 * Om1*Om1 + J2 * Om2*Om2 - (M1 * V1p*V1p + M2 * V2p*V2p + J1 * Om1p*Om1p + J2 * Om2p*Om2p)
    if(ETD1+ETD2==0):
        EES2 = sqrt(D / (M2*M2 / M1 + M2))
        EES1 = EES2 * M2 / M1
       
    if(ETD1 != 0 and ETD2 != 0):
        EES2 = sqrt(D / (M2 * (ETD1 / ETD2 + 1)))
        EES1 = EES2 * sqrt(ETD1 * M2 / (ETD2 * M1))
    
    return EES1, EES2
