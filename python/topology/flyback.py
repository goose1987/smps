from converter import converter

class flyback(converter):
    name='flyback'
    def __init__(self,vimax,vimin,vomax,vomin,pomax,fsw):
        converter.__init__(self,vimax,vimin,vomax,vomin,pomax,fsw)
        self.nsw = 2
        self.nwinding = 2

        self.I_Qs = pomax/vomin # current stress on secondary side switch
        self.Dmin = 0.15; # minimum duty cycle
        self.nps = vimax/vomin*(self.Dmin/(1-self.Dmin)) # Np/Ns turns ratio
        self.V_Qp = vimax+vomax*self.nps # voltage stress on primary switch
        self.V_Qs = vomax+vimax/self.nps # voltage stress on secondary switch

        self.Np=1.0;
        self.Ns=1.0;
        #obj.I_Qs = pomax/vomin; % current stress on secondary side switches
        #obj.Dmin = 0.15;

        #obj.nps = vimax./vomin.*(obj.Dmin/(1-obj.Dmin));



        #obj.V_Qp = vimax+vomax.*obj.nps; % voltage stress on primary switch
        #obj.V_Qs = vomax+vimax./obj.nps; % voltage stress on secondary switch
