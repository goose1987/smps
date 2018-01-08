class iso_dcdc:
    """
    vimax    # max input voltage
    vimin     # min input voltage
    vomax     # max output voltage
    vomin     # min output voltage
    pomax     # max output power
    nps       # turns ratio
    nprim     # number of primary turns
    nsec      # number of secondary turns
    Dmin        # minimum duty cycle
    Dmax        # maximum duty cycle
    fsw         # switching frequency
    Lprim       # primary inductor
    Lprim_esr   # primary inductor ESR
    Cout        # output capacitor
    V_Qp        # max voltage on primary switches
    V_Qs        # max voltage on secondary switches
    I_Qp        # current stress on primary switches
    I_Qs        # current stress on seconary switches
    nsw         # number of switches
    nwinding    # number of windings
    """
    def __init__(self,vimax,vimin,vomax,vomin,pomax):
        self.vimax=vimax
        self.vimin=vimin
        self.vomax=vomax
        self.vomin=vomin

    def checkDmin(D):
      return 0
    def checkDmax(D):
      return 0

class forward(iso_dcdc):
    # diode reset forward converter
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

class pushpull(iso_dcdc):
    def __init__(self,vimax,vimin,vomax,vomin,pomax):

        self.V_Qp = 2*vimax # max voltage stress on primary switches
        # for push pull Dmax is limited at 50%, set at 0.4 for dynamic range
        self.Dmax=0.4;
        self.nps=2*self.Dmax*vimin/vomax; # turns ratio based on minimum duty cycle
        self.Dmin=vomin/vimax*self.nps/2; # maximum duty cycle
        #checkDmin(obj.Dmin); % check minimum duty cycle
        self.I_Qp = self.Dmax*(pomax/vomin)/self.nps; # current stress on primary switch
        self.V_Qs = 2.0*vimax/self.nps; # voltage stress on secondary switches
        self.nsw = 4
        self.nwinding = 4

class flyback(iso_dcdc):
    def __init__(self,vimax,vimin,vomax,vomin,pomax):

        self.nsw = 2
        self.nwinding = 2

        self.I_Qs = pomax/vomin # current stress on secondary side switch
        self.Dmin = 0.15; # minimum duty cycle
        self.nps = vimax/vomin*(self.Dmin/(1-self.Dmin)) # Np/Ns turns ratio
        self.V_Qp = vimax+vomax*self.nps # voltage stress on primary switch
        self.V_Qs = vomax+vimax/self.nps # voltage stress on secondary switch

        #obj.I_Qs = pomax/vomin; % current stress on secondary side switches
        #obj.Dmin = 0.15;

        #obj.nps = vimax./vomin.*(obj.Dmin/(1-obj.Dmin));



        #obj.V_Qp = vimax+vomax.*obj.nps; % voltage stress on primary switch
        #obj.V_Qs = vomax+vimax./obj.nps; % voltage stress on secondary switch
