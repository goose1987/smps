from converter import converter
import math
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
    # return voltagexcurrent stress on semiconductor switches (W)
    def S2(self,vi,vo,pout):
        self.ops(vi,vo,pout)
        return self.V_Qp*self.Ippk,self.V_Qs*self.Iout # converter stress (W)
    # calculate stress based on rms current
    def S(self,vin,vout,pout):
        self.ops(vin,vout,pout)
        return self.V_Qp*self.Irms_Qp*self.nswp+self.V_Qs*(self.Irms_Qs1+self.Irms_Qs2)
    # utilization factor
    def U2(self,vi,vo,pout):
        Sp,Ss=self.S2(vi,vo,pout)
        return pout/Sp,pout/Ss
    def U(self,vin,vout,pout):
        return pout/self.S(vin,vout,pout)
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
    # calculate operating points for switches
    def ops(self,vin,vout,pout):
        D  = self.D(vin,vout)
        self.V_Qp = vin+vin*(D/(1-D)) # voltage stress on primary
        self.V_Qs = vin/self.nps  # voltage stress on secondary switches
        self.Iout=pout/vout # compute iout
        self.Irms_Qp = self.Iout*math.sqrt(D)/self.nps # current stress on primary switch
        self.Ippk = self.Iout/self.nps
        self.Irms_Qs1=self.Iout*math.sqrt(D) # current stress on secondary main switch
        self.Irms_Qs2=self.Iout*math.sqrt(1-D) # current stress on secondary sync switch
        return self.V_Qp,self.V_Qs,self.Iout,self.Irms_Qp,self.Ippk,self.Irms_Qs1,self.Irms_Qs2

    #I_Qsync  # current stress synchronous switch on secondary side
    def __init__(self,reqs):
        converter.__init__(self,reqs)
        center=0.45
        self.rangeD(center) # calculate turns ratio, min D, max D
        # for wide input and output requirement, not always possible to step back Dmin
         # while the minimum duty cycle is greater than 0.15(semi-arbitrary, most controller has minimum controllable ontime)
        #while self.Dmin>0.15:
        #    center=center-0.01 # step back center to minimize reset voltage stress on converter
        #    self.rangeD(center)

        self.Np=1.0 # primary turns default to 1 during init
