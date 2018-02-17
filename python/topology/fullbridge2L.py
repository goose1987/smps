from fullbridge import fullbridge
# center tap transformer with 4 windings
# synchronous
import math


class fullbridge2L(fullbridge):
    name='fullbridge w/current doubler'
    # return voltage on secondary switches
    def vsec(self,vin):
        # current doubler output configuration
        return vin/self.nps
    def __init__(self,reqs):
        fullbridge.__init__(self,reqs)
