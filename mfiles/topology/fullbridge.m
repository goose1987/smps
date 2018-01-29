classdef fullbridge < iso_dcdc
  properties
    %V_Qp1
    %V_Qp2
    %V_Qs1
    %V_Qs2
    %I_Qp1
    %I_Qp2
    %I_Qs1
    %I_Qs2
  end
  methods

    function y = D(obj,vin,vout)
      y=2.*obj.nps.*vout./vin;
    end
    function obj=fullbridge(vimax,vimin,vomax,vomin,pomax)

      %obj.V_Qp1=2*vimax; % voltage stress on primary switch
      %obj.V_Qp2=2*vimax; % voltage stress on primary switch
      obj.V_Qp = vimax;
      % for push pull Dmax is limited at 50%, set at 0.4 for dynamic range
      obj.Dmax=0.4;
      obj.nps=2*obj.Dmax*vimin/vomax; % turns ratio based on minimum duty cycle
      obj.Dmin=vomin/vimax*obj.nps/2; % maximum duty cycle
      obj.checkDmin(obj.Dmin); % check minimum duty cycle
      %obj.I_Qp1 = obj.Dmax*(pomax/vomin)/obj.nps; % current stress on primary switch
      %obj.I_Qp2 = obj.Dmax*(pomax/vomin)/obj.nps; % current stress on primary switch
      obj.I_Qp = obj.Dmax.*(pomax/vomin)/obj.nps; % current stress on primary switch
      obj.V_Qs = 2.*vimax./obj.nps; % voltage stress on secondary switches
      obj.nsw = 6; % number of active switches
      obj.nwinding = 3; % number of windings

    end
  end
end
