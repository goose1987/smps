from forward import forward
# center tap transformer with 4 windings
# synchronous
import numpy as np

class fullbridge(forward):
    name='fullbridge'
    def vpri(self,vin):
        return vin
    def vsec(self,vin):
        return 2.0*vin/self.nps
    def iRmsPri(self,pout,vout,vin):
        return (pout/vout)/self.nps*np.sqrt(self.D(vin,vout)/2.0)

    def __init__(self,reqs):
        forward.__init__(self,reqs)
        self.nsw = 6 # total number of switches
        self.nswp= 4 # number of primary switches
