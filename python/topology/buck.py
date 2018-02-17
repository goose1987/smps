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
        Qp_conduction = util.I2R(self.iRmsPri(pout,vout,vin),Qp['rds'])
        # switching loss
        Qp_sw_on=vin*Iout*ton*self.fsw # switch transition
        Qp_Coss =0.5*Qp['Coss']*vin*vin*self.fsw # hard siwtching Coss loss
        Qp_sw = Qp_Coss+Qp_sw_on# combined switching loss

        ######### synchronous switch #######
        # conduction loss
        Qs_conduction = util.I2R(self.iRmsSec(pout,vout,vin),Qsync['rds'])
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
        V_Qp=self.vpri(vi)
        V_Qs=self.vsec(vi)
        Iout=pout/vo
        return V_Qp*Iout,V_Qs*Iout
        #return self.V_Qp*self.Iomax#*self.nsw # converter stress (W)
    # sum of stress calculated using rms current
    def S(self,vi,vo,pout):
        V_Qp=self.vpri(vi)
        V_Qs=self.vsec(vi)
        Irms_Qp=self.iRmsPri(pout,vo,vi)
        Irms_Qs=self.iRmsSec(pout,vo,vi)
        return V_Qp*Irms_Qp+V_Qs*Irms_Qs
    # utilization factor
    def U2(self,vi,vo):
        Sp,Ss=self.S2(vi,vo,self.pomax)
        return self.pomax/Sp,pout/Ss
    def U(self,vin,vout):
        return self.pomax/self.S(vin,vout,self.pomax)
    # max primary switch stand off voltage
    def vpri(self,vin):
        return vin
    # synchronous switch
    def vsec(self,vin):
        return vin
    def iRmsPri(self,pout,vout,vin):
        return (pout/vout)*np.sqrt(self.D(vin,vout))
    def iRmsSec(self,pout,vout,vin):
        return (pout/vout)*np.sqrt(1.0-self.D(vin,vout))

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
        self.V_Qp_max=self.vimax
        self.V_Qs_max=self.vimax
        self.I_Qp_max=self.pomax/self.vomin*np.sqrt(self.D(self.vimin,self.vomin))
        self.I_Qs_max=self.pomax/self.vomin*np.sqrt(1.0-self.D(self.vimax,self.vomin))
