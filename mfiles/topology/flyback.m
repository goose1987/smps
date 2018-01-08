classdef flyback < iso_dcdc
  properties

  end
  methods
    function obj=flyback(vimax,vimin,vomax,vomin,pomax)

      obj.I_Qs = pomax/vomin; % current stress on secondary side switches
      obj.Dmin = 0.15;

      obj.nps = vimax./vomin.*(obj.Dmin/(1-obj.Dmin));

      % obj.nps*vomin/vimax=D/(1-D)
      % nps*vo/vi*(1-D)=D
      % nps*vo/vi=D(1+nps*vo/vi)
      % nps*vo/vi/(1+nps*vo/vi)=D

      % vqp = vi+vi/nps*(D/(1-D))
      % vqp = vi+vi/nps*((nps*vo/vi/(1+nps*vo/vi))/(1-nps*vo/vi/(1+nps*vo/vi)))
      % vqp = vi+vi*(vo/vi/(1+nps*vo/vi)/(1-nps*vo/vi/(1+nps*vo/vi)))

      obj.V_Qp = vimax+vomax.*obj.nps; % voltage stress on primary switch
      obj.V_Qs = vomax+vimax./obj.nps; % voltage stress on secondary switch
      obj.nsw = 2;
      obj.nwinding = 2;


    end
  end
end
