from converter import converter
import numpy as np
# diode reset forward converter
# tertiary winding

class forward(converter):
    # topology specific definitions
    nsw=3
    nswp=1
    nsws=2
    nwinding=3
    name='forward xwinding reset'
    def D(self,vin,vout):
        return (vout/vin)*(self.nps)
    # return voltagexcurrent peak stress per semiconductor switches (W)
    def S2(self,vi,vo,pout):
        V_Qp=self.vpri(vi)
        V_Qs=self.vsec(vi)
        Iout=(pout/vo)
        Ippk = (pout/vo)/self.nps
        return V_Qp*Ippk,V_Qs*Iout # converter stress (W)
    # calculate stress based on rms current
    def S(self,vin,vout,pout):
        V_Qp=self.vpri(vin)
        V_Qs=self.vsec(vin)
        Irms_Qp=self.iRmsPri(pout,vout,vin)
        Irms_Qs1=self.iRmsSec(pout,vout,vin)
        Irms_Qs2=self.iRmsSec(pout,vout,vin)
        return V_Qp*Irms_Qp*self.nswp+V_Qs*(Irms_Qs1+Irms_Qs2)
    # utilization factor
    def U2(self,vi,vo):
        Sp,Ss=self.S2(vi,vo,self.pomax)
        return self.pomax/Sp,pomax/Ss
    def U(self,vin,vout):
        return self.pomax/self.S(vin,vout,self.pomax)
    def checkD(self):
        if self.Dmin<0.1:
            print "warning: low min duty cycle"
        if self.Dmax>0.8:
            print "warning: high max duty cycle"
        return 0

    def rangeD(self,center):
        alpha=self.vomax/self.vimin
        beta =self.vomin/self.vimax
        self.Dmin = (beta/alpha*center*2.0)/(beta/alpha+1.0) # minimum duty cycle
        self.nps =self.vimax*self.Dmin/self.vomin # set turns ratio based on min duty cycle
        self.Dmax=  self.nps*self.vomax/self.vimin # max duty cycle
        self.checkD()
        return self.nps,self.Dmin,self.Dmax

    #I_Qsync  # current stress synchronous switch on secondary side
    # max primary switch stand off voltage
    def vpri(self,vin):
        return vin+vin*(self.Dmax/(1.0-self.Dmax))
    def vsec(self,vin):
        return vin/self.nps
    def iRmsPri(self,pout,vout,vin):
        return (pout/vout)/self.nps*np.sqrt(self.D(vin,vout))
    def iRmsSec(self,pout,vout,vin):
        return (pout/vout)*np.sqrt(1.0-self.D(self.vimax,self.vomin))

    def __init__(self,reqs):
        converter.__init__(self,reqs)
        center=0.4
        self.rangeD(center) # calculate turns ratio, min D, max D

        # for wide input and output requirement, not always possible to step back Dmin
         # while the minimum duty cycle is greater than 0.15(semi-arbitrary, most controller has minimum controllable ontime)
        #while self.Dmin>0.15:
        #    center=center-0.01 # step back center to minimize reset voltage stress on converter
        #    self.rangeD(center)
        self.V_Qp_max=self.vpri(self.vimax)
        self.V_Qs_max=self.vsec(self.vimax)
        self.I_Qp_max=self.iRmsPri(self.pomax,self.vomin,self.vimin)
        self.I_Qs_max=self.iRmsSec(self.pomax,self.vomin,self.vimax)

        self.Np=1.0 # primary turns default to 1 during init
