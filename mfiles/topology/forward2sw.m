classdef forward2sw < iso_dcdc
  properties
    I_Qsync  % current stress synchronous switch on secondary side

  end
  methods
    function y = D(obj,vin,vou)
      y=obj.nps.*vout./vin;        
    end

    function obj=forward2sw(vimax,vimin,vomax,vomin,pomax)

      obj.V_Qp = vimax;
      % for a 2 sw forward, maximum duty cycle is 50% to balance the transformer.
      % for practical implementation and dynamic range in transients, set Dmax to 0.35
      obj.Dmax=0.35;
      obj.nps = vimin*obj.Dmax/vomax; % turns ratio based on maximum duty cycle
      obj.Dmin= vomin*obj.nps/vimax; % minimum duty cycle
      % check for correctness
      %obj.checkDmin(obj.Dmin);
      obj.checkDmin(obj.Dmin)
      %{
      %obj.V_Qs1=vimax/obj.nps; % maximum voltage stress on secondary switch 1
      %obj.V_Qs2=vimax/obj.nps; % maximum voltage stress on secondary switch 2
      %obj.I_Qs1=(pomax/vomin)*obj.Dmax; % maximum current on secondary side sw 1
      %obj.I_Qs2=(pomax/vomin)*(1-obj.Dmin); % maximum current on secondary side sw 2
      %obj.I_Qp1=obj.Dmax*(pomax/vomin)/obj.nps; % max current on primary sw 1
      %obj.I_Qp2=obj.Dmax*(pomax/vomin)/obj.nps; % max current on primary sw 2
      %}

      obj.V_Qs = vimax/obj.nps;
      obj.I_Qs = (pomax/vomin).*obj.Dmax;
      obj.I_Qsync = (pomax/vomin)*(1-obj.Dmin); % max current n secondary side synchronous
      obj.I_Qp = obj.Dmax.*(pomax/vomin)/obj.nps;
      obj.nsw = 4; % number of active switches
      obj.nwinding = 2; % number of winding on transformer

    end

  end
end
