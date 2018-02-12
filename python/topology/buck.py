import util
from converter import converter
# synchronous buck converter

class buck(converter):
    # calculate loss of fets, assume synchronous operation
    def fetloss(self,vin,vout,pout,Qp,Qsync):
        Qp_ig=Qp['Vdrv']/self.Rdrv # main fet drive current (A)
        toff = Qp['Qg']/Qp_ig # turn on time (s)
        ton = Qp['Qg']/Qp_ig # turn off time (s)
        Iout = (pout/vout) # output current (A)
        # main switch
        # main fet conduction loss (W)
        Qp_conduction = util.I2R(Iout,Qp['rds'])*self.D(vin,vout)
        # switching loss
        Qp_sw_on=vin*Iout*ton*self.fsw/2.0 # switch transition
        Qp_Qoss = Qp['Qoss']*vin*self.fsw/2.0 # Qoss
        Qp_Qrr = Qp['Qrr']*vin*self.fsw # Qrr
        Qp_sw_off=0.5*vin*Iout*toff*self.fsw # off
        Qp_sw = Qp_sw_on+Qp_Qoss+Qp_Qrr+Qp_sw_off # combined switching loss

        # synchronous switch
        # conduction loss
        Qs_conduction = util.I2R(Iout,Qsync['rds'])*(1.0-self.D(vin,vout))
        # dead time loss
        Qs_Qoss = Qsync['Qoss']*Qsync['Vsd']*self.fsw/2.0 # Qoss
        Qs_Qrr = Qsync['Qrr']*Qsync['Vsd']*self.fsw # Qrr
        Qs_sw = Qs_Qoss+Qs_Qrr # combine switching losses
        # return loss contributions
        return Qp_conduction,Qp_sw,Qs_conduction,Qs_sw
    # calculate duty cycle at specific operating condition
    def D(self,vin,vout):
        return vout/vin

    #I_Qsync  # current stress synchronous switch on secondary side
    def __init__(self,vimax,vimin,vomax,vomin,pomax,fsw):
        converter.__init__(self,vimax,vimin,vomax,vomin,pomax,fsw)
        # if max output is greater than min input clip max output to min input
        # buck steps down only
        if self.vomax>self.vimin:
            print 'warning : vomax > vimin; clipping vomax to vimin'
            self.vomax=vimin
        self.Dmin = vomin/vimax # calculate minimum duty cycle
        # if duty cycle is less than 10%, warn the user
        if self.Dmin<0.1:
            print 'low duty cycle, consider using a topology with a transformer'
        self.Dmax=self.vomax/self.vimin # maximmum duty cycle
        self.V_Qp=self.vimax # max voltage stress on main switch
        self.V_Qsync=self.vimax # max voltage stress on synchronous switch
        self.I_Qp=self.Dmax*(self.pomax/self.vomin) # max current rms through main fet
        self.I_Qsync=(1.0-self.Dmin)*(self.pomax/self.vomin) # max current rms through sync fet
