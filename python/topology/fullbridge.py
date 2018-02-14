from forward import forward
# center tap transformer with 4 windings
# synchronous
import math

class fullbridge(forward):
    name='fullbridge'
    # calculate operating points for switches
    def ops(self,vin,vout,pout):
        D = self.D(vin,vout)
        self.V_Qp = vin# voltage stress on primary
        self.V_Qs = 2.*vin/self.nps  # voltage stress on secondary switches
        self.Iout=pout/vout
        self.Irms_Qp = self.Iout*math.sqrt(D/2.0)/self.nps # current stress on primary switch
        self.Ippk = self.Iout/self.nps
        self.Irms_Qs1=self.Iout*math.sqrt(D/2.0) # current stress on secondary synchronous switch
        self.Irms_Qs2=self.Iout*math.sqrt(D/2.0) # current stress on secondary synchronous switch
        return self.V_Qp,self.V_Qs,self.Iout,self.Irms_Qp,self.Ippk,self.Irms_Qs1,self.Irms_Qs2

    def __init__(self,reqs):
        forward.__init__(self,reqs)
        self.nsw = 6 # total number of switches
        self.nswp= 4 # number of primary switches
