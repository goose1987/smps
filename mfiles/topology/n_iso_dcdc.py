class n_iso_dcdc:

    """
    properties
    vimax       % max input voltage
    vimin       % min input voltage
    vomax       % max output voltage
    vomin       % min output voltage
    pomax       % max output power
    V_Qmain     % VDS max of main switch (V)
    V_Qsync     % VDS max of synchronous switch (V)
    I_Qmain     % I max of main switch (A)
    I_Qsync     % I max of synchronous switch(A)
    Dmin        % minimum duty cycle
    Dmax        % maximum duty cycle
    fsw         % switching frequency
    Lprim       % primary inductor
    Lprim_esr   % primary inductor ESR
    Cout        % output capacitor

    end

    """
    def __init__(self,vimax,vimin,vomax,vomin,pomax):
        # check for valid inputs
        if vimax<vimin:
            return 0
        if vomax<vomin:
            return 0

        # assign properties
        self.vimax = vimax
        self.vimin = vimin
        self.vomax = vomax
        self.vomin = vomin

class buck(n_iso_dcdc):
    def __init__(self,vimax,vimin,vomax,vomin,pomax):
        n_iso_dcdc.__init__(self,vimax,vimin,vomax,vomin,pomax)

        # buck only steps down
        if vimin<=vomax:
            print "Vout max > Vin min"
            return 1
        self.Dmin=vomin/vimax # minimum duty cycle
        # check for low duty cycle/minimum on time
        if self.Dmin<0.1:
            print "low duty cycle, consider using a Xformer topology "

        self.Dmax = vomax/vimin # max duty cycle
        self.V_Qmain = vimax # max voltage stress on main switch
        self.V_Qsync = vimax # max voltage stress on sync switch
        self.I_Qmain = self.Dmax*(pomax/vomin) # max current rms through main switch
        self.I_Qsync = (1-self.Dmin)*(pomax/vomin) # max current rms through sync switch


class boost(n_iso_dcdc):
    def __init__(self,vimax,vimin,vomax,vomin,pomax):
        n_iso_dcdc.__init__(self,vimax,vimin,vomax,vomin,pomax)
        # boost only steps up
        if vimax>=vomin:
            print "Vin max > Vout min"
            return 1

        self.Dmax = (vomax-vimin)/vomax # max duty cycle
        self.Dmin = (vomin-vimax)/vomin # min duty cycle
        self.V_Qmain = vomax # voltage stress on main switch
        self.V_Qsync = vomax # voltage stress on sync switch
        self.I_Qsync = (pomax/vomin) # current through sync switch
        self.I_Qmain = self.I_Qsync*(1/(1-self.Dmax)) # current through main switch
        
class sepic(n_iso_dcdc):
    def __init__(self,vimax,vimin,vomax,vomin,pomax):
        n_iso_dcdc.__init__(self,vimax,vimin,vomax,vomin,pomax)

        self.Dmax = (vomax/(vimin+vomax)) # max duty cycle
        self.Dmin = (vomin/(vimax+vomin)) # min duty cycle
        self.V_Qmain=vimax+vomax # max voltage on main switch
        self.V_Qsync = vimax+vomax # max voltage stress on sync switch
        self.I_Qsync = (pomax/vomin) # max current stress on sync fet
        self.I_Qmain = (pomax/vomin)*(self.Dmax/(1-self.Dmax)) # max current stress on main switch
