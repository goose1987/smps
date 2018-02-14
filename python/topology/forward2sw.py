from forward import forward
import math

class forward2sw(forward):
    name='2swforward'
    def ops(self,vin,vout,pout):
        self.V_Qp = vin # max voltage stress on primary switches
        self.V_Qs = vin/self.nps
        D=self.D(vin,vout)
        self.Iout=pout/vout
        self.Irms_Qp = self.Iout*math.sqrt(D)/self.nps # current stress on primary switch
        self.Ippk = self.Iout/self.nps
        self.Irms_Qs1 = self.Iout*math.sqrt(D) # current rms on secondary main switch
        self.Irms_Qs2 = self.Iout*math.sqrt(1-D) # current rms on secondary synchronous switch

    def __init__(self,reqs):
        forward.__init__(self,reqs)
        self.nsw=4
        self.nswp = 2 # number of primary switch not including diode on reset
        self.nwinding = 2 # number of winding


        # for a 2 sw forward, maximum duty cycle is 50% to balance the transformer.
        # for practical implementation and dynamic range in transients, set Dmax to 0.45
        self.Dmax = 0.45
        self.nps = self.vimin*self.Dmax/self.vomax # turns ratio based on max duty cycle
        self.Ns=self.Np/self.nps
        self.Dmin = self.vomin*self.nps/self.vimax # min duty cycle
        self.checkD()
