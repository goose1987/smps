from iso_dcdc import *
# push pull converter
# center tap transformer with 4 windings
# synchronous

class pushpull(iso_dcdc):
    def __init__(self,vimax,vimin,vomax,vomin,pomax):

        self.V_Qp = 2*vimax # max voltage stress on primary switches
        # for push pull Dmax is limited at 50%, set at 0.4 for dynamic range
        self.Dmax=0.4;
        self.nps=2*self.Dmax*vimin/vomax; # turns ratio based on minimum duty cycle
        self.Dmin=vomin/vimax*self.nps/2; # maximum duty cycle
        #checkDmin(obj.Dmin); % check minimum duty cycle
        self.I_Qp = self.Dmax*(pomax/vomin)/self.nps; # current stress on primary switch
        self.V_Qs = 2.*vimax/self.nps; # voltage stress on secondary switches
        self.nsw = 4
        self.nwinding = 4
