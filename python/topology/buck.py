import util
import numpy as np
from converter import converter
# synchronous buck converter

class buck(converter):
    '''
    # calculate loss of fets, assume synchronous operation
    # return [  conduction loss main sw,
                switching loss main sw,
                conduction loss synchronous sw,
                switching loss synchronous sw]
    '''
    name = 'buck'
    def fetloss(self,vin,vout,pout,Qp,Qsync):
        Qp_ig=Qp['Vdrv']/self.Rdrv # main fet drive current (A)
        toff = Qp['Qg']/Qp_ig # turn on time (s)
        ton = Qp['Qg']/Qp_ig # turn off time (s)
        Iout = (pout/vout) # output current (A)
        ######### main switch ############
        # main fet conduction loss (W)
        Qp_conduction = util.I2R(Iout,Qp['rds'])*self.D(vin,vout)
        # switching loss
        Qp_sw_on=vin*Iout*ton*self.fsw # switch transition
        Qp_Coss =0.5*Qp['Coss']*vin*vin*self.fsw # hard siwtching Coss loss
        Qp_sw = Qp_Coss+Qp_sw_on# combined switching loss

        ######### synchronous switch #######
        # conduction loss
        Qs_conduction = util.I2R(Iout,Qsync['rds'])*(1.0-self.D(vin,vout))
        # dead time loss
        #Qs_Qoss = Qsync['Qoss']*Qsync['Vsd']*self.fsw/2.0 # Qoss
        #Qs_Qrr = Qsync['Qrr']*Qsync['Vsd']*self.fsw # Qrr
        #Qs_sw = Qs_Qoss+Qs_Qrr # combine switching losses
        Qs_dt = Qsync['Vsd']*Iout*50e-9*self.fsw
        Qs_sw=Qsync['Vsd']*Iout*ton*self.fsw/2.0+Qs_dt
        # return loss contributions
        return Qp_conduction,Qp_sw,Qs_conduction,Qs_sw
    # calculate duty cycle at specific operating condition
    def D(self,vin,vout):
        return vout/vin
    # return the frequency of the double pole of the output LC filter in Hz
    def fLC(self,L,C):
        return 1.0/(np.sqrt(L*C)*2*np.pi)
    # return voltagexcurrent stress on semiconductor switches (W)
    def S2(self,vi,vo,pout):
        self.ops(vi,vo,pout)
        return self.V_Qp*self.Iout,self.V_Qs*self.Iout
        #return self.V_Qp*self.Iomax#*self.nsw # converter stress (W)
    # sum of stress calculated using rms current
    def S(self,vi,vo,pout):
        self.ops(vi,vo,pout)
        return self.V_Qp*self.Irms_Qp+self.V_Qs*self.Irms_Qs
    # utilization factor
    def U2(self,vi,vo,pout):
        Sp,Ss=self.S2(vi,vo,pout)
        return pout/Sp,pout/Ss
    def U(self,vin,vout,pout):
        return pout/self.S(vin,vout,pout)

    def ops(self,vin,vout,pout):
        self.V_Qp=vin # max voltage stress on main switch
        self.V_Qs=vin # max voltage stress on synchronous switch
        D=self.D(vin,vout)
        self.Iout=pout/vout
        self.Irms_Qp=np.sqrt(D)*(self.Iout) # max current rms through main fet
        self.Irms_Qs=np.sqrt(1.0-D)*(self.Iout) # max current rms through sync fet
    #I_Qsync  # current stress synchronous switch on secondary side
    def __init__(self,reqs):
        converter.__init__(self,reqs)
        # if max output is greater than min input clip max output to min input
        # buck steps down only
        if self.vomax>self.vimin:
            print 'warning : vomax > vimin; clipping vomax to vimin'
            self.vomax=self.vimin
        self.Dmin = self.vomin/self.vimax # calculate minimum duty cycle
        # if duty cycle is less than 10%, warn the user
        if self.Dmin<0.1:
            print 'warning : low duty cycle, consider using a topology with a transformer'
        self.Dmax=self.vomax/self.vimin # maximmum duty cycle
