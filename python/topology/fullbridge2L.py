from fullbridge import fullbridge
# center tap transformer with 4 windings
# synchronous
import math


class fullbridge2L(fullbridge):
    name='fullbridge w/current doubler'
    # calculate operating points for switches
    def ops(self,vin,vout,pout):
        D = self.D(vin,vout)
        self.V_Qp = vin # voltage stress on primary
        self.V_Qs = vin/self.nps  # voltage stress on secondary switches
        self.Iout=pout/vout
        self.Irms_Qp = self.Iout*math.sqrt(D/2.0)/self.nps # current stress on primary switch
        self.Ippk = self.Iout/self.nps
        self.Irms_Qs1=self.Iout*math.sqrt(D/2.0) # current stress on secondary synchronous switch
        self.Irms_Qs2=self.Iout*math.sqrt(D/2.0)
        return self.V_Qp,self.V_Qs,self.Iout,self.Irms_Qp,self.Ippk,self.Irms_Qs1,self.Irms_Qs2

    def __init__(self,reqs):
        fullbridge.__init__(self,reqs)
