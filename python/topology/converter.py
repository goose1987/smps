

# base class for non isolated converters
class converter:
    def __init__(self,vimax,vimin,vomax,vomin,pomax,fsw):
        self.vimax=vimax # max input
        self.vimin = vimin # min input
        self.vomax = vomax # max output
        self.vomin = vomin # min output
        self.pomax = pomax # max output power (W)
        self.fsw = fsw # switching frequency (Hz)
        self.nsw = 2 # number of switches
        self.Rdrv = 4 # R fet driver (ohm)
