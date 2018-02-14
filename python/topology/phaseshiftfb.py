from fullbridge import fullbridge

class phaseshiftfb(fullbridge):
    # calculate operating points for switches
    def ops(self):
        self.V_Qp = self.vimax # voltage stress on primary
        self.V_Qs = self.vimax/self.nps  # voltage stress on secondary switches
        self.Iomax=self.pomax/self.vomin
        self.Irms_Qp = self.Iomax*math.sqrt(self.Dmax/2.0)/self.nps # current stress on primary switch
        self.Ippk = self.Iomax/self.nps
        self.Irms_Qs=self.Iomax*math.sqrt(self.Dmax/2.0) # current stress on secondary synchronous switch
        return self.V_Qp,self.V_Qs,self.Iomax,self.Irms_Qp,self.Ippk,self.Irms_Qs

    def __init__(self,vimax,vimin,vomax,vomin,pomax,fsw):
        fullbridge.__init__(self,vimax,vimin,vomax,vomin,pomax,fsw)
        self.winding=2
