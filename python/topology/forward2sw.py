from forward import forward
import numpy as np

class forward2sw(forward):
    name='2swforward'

    def vpri(self,vin):
        return vin

    def __init__(self,reqs):
        forward.__init__(self,reqs)

        self.nsw=4
        self.nswp = 2 # number of primary switch not including diode on reset
        self.nwinding = 2 # number of winding


        # for a 2 sw forward, maximum duty cycle is 50% to balance the transformer.
        # for practical implementation and dynamic range in transients, set Dmax to 0.45
        center = 0.2
        self.rangeD(center)
        #self.Dmax = 0.45
        #self.nps = self.vimin*self.Dmax/self.vomax # turns ratio based on max duty cycle
        self.Ns=self.Np/self.nps
        #self.Dmin = self.vomin*self.nps/self.vimax # min duty cycle
        #self.checkD()
