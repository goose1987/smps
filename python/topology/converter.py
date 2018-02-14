# base class for non isolated converters
class converter:
    def __init__(self,reqs):
        self.vimax=reqs["vimax"] # max input
        self.vimin = reqs["vimin"] # min input
        self.vomax = reqs["vomax"] # max output
        self.vomin = reqs["vomin"] # min output
        self.pomax = reqs["pomax"] # max output power (W)
        self.fsw = reqs["fsw"] # switching frequency (Hz)
        self.nsw = 2 # number of switches
        self.Rdrv = 4 # R fet driver (ohm)
