import web
import os
from math import *

#path example for running the app in qpython
#os.chdir('/sdcard/qpython/projects/eeswebgl/')

from ees.ees import *

urls = (
	'/', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/')

class Index:
    def GET(self):
        return render.input_form()
    
    def POST(self):
        form = web.input()
        Vehicle1 = form.Vehicle1
        Vehicle2 = form.Vehicle2
        L1 = float(form.L1)
        L2 = float(form.L2)
        W1 = float(form.W1)
        W2 = float(form.W2)
        OF1 = float(form.OF1)
        OF2 = float(form.OF2)
        CGFA1 = float(form.CGFA1)
        CGFA2 = float(form.CGFA2)
        R1 = float(form.R1)
        R2 = float(form.R2)
        M1 = float(form.M1)
        M2 = float(form.M2)
        V1p = float(form.V1p)/3.6
        V2p = float(form.V2p)/3.6
        Ny1p = float(form.Ny1p)*3.141592654/180
        Ny2p = float(form.Ny2p)*3.141592654/180
        Fi1p = float(form.Fi1p)
        Fi2p = float(form.Fi2p) 
        MyR1 = float(form.MyR1)
        MyR2 = float(form.MyR2)
        Psi1 = float(form.Psi1)*3.141592654/180
        Psi2 = float(form.Psi2)*3.141592654/180
        Om1 = float(form.Om1)
        Om2 = float(form.Om2)
        Ny1 = float(form.Ny1)
        Ny2 = float(form.Ny2)
        EES1 = float(form.EES1)/3.6
        EES2 = float(form.EES2)/3.6
        ETD1 = float(form.ETD1)
        ETD2 = float(form.ETD2)
        SHA1 = float(form.SHA1)
        SHA2 = float(form.SHA2)
        Rho1 = float(form.Rho1)
        Rho2 = float(form.Rho2)
        s1 = float(form.s1)
        s2 = float(form.s2)
        
        x1 = 0.0
        y1 = 0.0
        CG1x=x1+(L1/2-OF1-CGFA1)*cos(Psi1)
        CG1y=y1+(L1/2-OF1-CGFA1)*sin(Psi1)
        Cx=CG1x+SHA1*cos(Rho1*3.141592654/180+Psi1)
        Cy=CG1y+SHA1*sin(Rho1*3.141592654/180+Psi1)
        CG2x=Cx+SHA2*cos(-3.141592654+Rho2*3.141592654/180+Psi2)
        CG2y=Cy+SHA2*sin(-3.141592654+Rho2*3.141592654/180+Psi2)
        
        if((EES1+EES2)!=0):
            J1, J2, Om1p, Om2p = SR1(M1,M2,R1,R2,L1,L2,MyR1,MyR2,Fi1p,Fi2p)
            V1 = SR2(M1,M2,R1,J1,J2,Om1p,Om2p,Om1,Om2,EES1,EES2,V1p,V2p,Ny1p,Ny2p)
            V2, Ny2, dV1, dV2, S1, S2, Gam1, Gam2 = SR5(M1,M2,V1p,V2p,Ny1p,Ny2p,Ny2,V1)
            I1, I2, I1p, I2p, Om1w, Om2w, e1w, e2w = SR6(Rho1,Rho2,Psi1,Psi2,SHA1,SHA2,S1,S2,Gam1,Gam2,Om1,Om2,J1,J2,M1,M2,V1,V2,V1p,V2p)
        else:
            if (Ny2 == 0 or Ny2 == 180):
                print("Angle Ny2 must be different than 0/180 deg!") #Input error
 
            if(Ny2==90 or Ny2==270):
                Ny2 = Ny2 * 3.141592654 / 180;
                #Impulse formula calculation for Ny2 equal to 90 or 270 deg
                J1, J2, Om1p, Om2p = SR1(M1,M2,R1,R2,L1,L2,MyR1,MyR2,Fi1p,Fi2p)
                V1, V2, Ny2, dV1, dV2, S1, S2, Gam1, Gam2 = SR4(M1,M2,V1p,V2p,Ny1p,Ny2p,Ny2)
                I1, I2, I1p, I2p, Om1w, Om2w, e1w, e2w = SR6(Rho1,Rho2,Psi1,Psi2,SHA1,SHA2,S1,S2,Gam1,Gam2,Om1,Om2,J1,J2,M1,M2,V1,V2,V1p,V2p)
                EES1, EES2 = SR7(M1,M2,V1,V2,J1,J2,Om1,Om2,V1p,V2p,Om1p,Om2p,ETD1,ETD2)
                
            if(Ny2!=90 and Ny2!=270):
                Ny2 = Ny2 * 3.141592654 / 180;
                #Impulse formula calculation for Ny2 different than 90 or 270 deg
                J1, J2, Om1p, Om2p = SR1(M1,M2,R1,R2,L1,L2,MyR1,MyR2,Fi1p,Fi2p)
                V1 = SR3(M1,M2,V1p,V2p,Ny1p,Ny2p,Ny2)
                V2, Ny2, dV1, dV2, S1, S2, Gam1, Gam2 = SR5(M1,M2,V1p,V2p,Ny1p,Ny2p,Ny2,V1)
                I1, I2, I1p, I2p, Om1w, Om2w, e1w, e2w = SR6(Rho1,Rho2,Psi1,Psi2,SHA1,SHA2,S1,S2,Gam1,Gam2,Om1,Om2,J1,J2,M1,M2,V1,V2,V1p,V2p)
                EES1, EES2 = SR7(M1,M2,V1,V2,J1,J2,Om1,Om2,V1p,V2p,Om1p,Om2p,ETD1,ETD2)
                
        class results(object):
            def __init__(self, name, description):
                self.name = name
                self.description = description
        
        output = results("EES",
        """     
        Vehicle 1: %s\tVehicle 2: %s
        
        
        VELOCITIES:
        
        V1 = %.2f km/h\t\tV2 = %.2f km/h
        dV1 = %.2f km/h\tdV2 = %.2f km/h
        EES1 = %.2f km/h\tEES2 = %.2f km/h
        
        MOMENTA:
        
        I1 = %.2f Ns\tI2 = %.2f Ns
        I1p = %.2f Ns\tI2p = %.2f Ns
        S1 = %.2f Ns\t\tS2 = %.2f Ns
        Gam1 = %.2f deg\tGam2 = %.2f deg
        
        CHECK CALCULATION:
        
        Om1p = %.2f rad/s\tOm2p = %.2f rad/s
        Om1w = %.2f rad/s\tOm2w = %.2f rad/s
        e1w = %.2f m\t\te2w = %.2f m
        J1 = %.2f kgm^2\tJ2 = %.2f kgm^2        
        \t\t\tNy2 = %.2f deg             
        """ % (Vehicle1, Vehicle2, V1*3.6, V2*3.6, dV1*3.6, dV2*3.6, EES1*3.6, EES2*3.6, I1, I2, I1p, I2p, S1, S2, Gam1*180/3.141592654, Gam2*180/3.141592654, Om1p, Om2p, Om1w, Om2w, e1w, e2w, J1, J2, Ny2*180/3.141592654))
        
        return render.results(output = output, L1 = L1, L2 = L2, W1 = W1, W2 = W2, OF1 = OF1, OF2 = OF2, CGFA1 = CGFA1, CGFA2 = CGFA2, R1 = R1, R2 = R2,
        	Psi1 = Psi1, Psi2 = Psi2, Rho1 = Rho1, Rho2 = Rho2, CG1x = CG1x, CG1y = CG1y, CG2x = CG2x, CG2y = CG2y, Cx = Cx, Cy = Cy, Fi1p = Fi1p, Fi2p = Fi2p,
        	Ny1p = Ny1p, Ny2p = Ny2p, s1 = s1, s2 = s2)
        
if __name__ == "__main__":
    app.run()
