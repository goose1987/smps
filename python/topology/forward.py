from iso_dcdc import *
# diode reset forward converter
# tertiary winding

class forward(iso_dcdc):

    #I_Qsync  # current stress synchronous switch on secondary side
    def __init__(self,vimax,vimin,vomax,vomin,pomax):
        iso_dcdc.__init__(self,vimax,vimin,vomax,vomin,pomax)

        self.Dmin=0.15 # set minimum duty cycle
        self.nps = vimax*self.Dmin/vomin # set turns ratio based on min duty cycle
        self.Dmax = self.nps*vomax/vimin # max duty cycle
        self.V_Qp = vimax+vimax*(self.Dmax/(1-self.Dmax)) # voltage stress on primary
        self.V_Qs = vimax/self.nps  # voltage stress on secondary switches

        self.nsw = 3 # number of active swith not including diode on reset winding
        self.nwinding = 3 # number of winding including reset winding
        self.I_Qp = (pomax/vomin)*self.Dmax/self.nps # current stress on primary switch
        self.I_Qs = (pomax/vomin)*self.Dmax # current stress on secondry switch
        self.I_Qsync=(pomax/vomin)*(1-self.Dmax) # current stress on secondary synchronous switch
