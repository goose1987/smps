from iso_dcdc import *

class forward2sw(iso_dcdc):

    def __init__(self,vimax,vimin,vomax,vomin,pomax):
        self.V_Qp = vimax # max voltage stress on primary switches
        # for a 2 sw forward, maximum duty cycle is 50% to balance the transformer.
        # for practical implementation and dynamic range in transients, set Dmax to 0.35
        self.Dmax = 0.35
        self.nps = vimax*self.Dmax/vomax # turns ratio based on max duty cycle
        self.Dmin = vomin*self.nps/vimax # min duty cycle

        self.nsw = 4 # number of active switch not including diode on reset
        self.nwinding = 2 # number of winding
        self.V_Qs = vimax/self.nps;
        self.I_Qs = (pomax/vomin)*self.Dmax;
        self.I_Qsync = (pomax/vomin)*(1-self.Dmin); # max current n secondary side synchronous
        self.I_Qp = self.Dmax*(pomax/vomin)/self.nps;
