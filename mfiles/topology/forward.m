classdef forward < iso_dcdc
  % diode reset forward converter
  properties
    I_Qsync  % current stress synchronous switch on secondary side
    npr % Np/Nr primary to reset winding turns ratio
  end
  methods
    function y=D(obj,vin,vout)
      y=obj.nps.*vout./vin;
    end
    function obj=forward(vimax,vimin,vomax,vomin,pomax)

      obj.Dmin = 0.15; % set minimum duty cycle
      obj.nps = vimax*obj.Dmin/vomin; % set turns ratio based on min duty cycle
      obj.Dmax = obj.nps*vomax/vimin; % max duty cycle
      % check for correctness
      obj.checkDmax(obj.Dmax);
      %obj.V_Qs1 = vimax/obj.nps; % voltage stress on secondary switch
      %obj.V_Qs2 = vimax/obj.nps; % voltage stress on secondary switch
      obj.V_Qs = vimax/obj.nps; % voltage stress on secondary switches
      % find maximum reset voltage required
      vix=vimin:vimax;
      vreset=max(vix.*(obj.D(vix,vomax)./(1-obj.D(vix,vomax))));
      obj.npr=vimin./vreset; % turns ratio for reset winding
      obj.V_Qp = vimax+vimax/obj.npr; % max voltage stress on primary switch
      %obj.V_Qp = vimax+vimax.*(obj.D(vimax,vomax)./(1-obj.D(vimax,vomax))); % max stress on primary switch
      %obj.npr = vimax./vreset;
      %obj.npr = vimax/(vimax.*(obj.D(vimax,vomax)./(1-obj.D(vimax,vomax))));
      obj.nsw = 3; % number of active switch not including diode on reset winding
      obj.nwinding = 3; % number of winding including reset winding
      obj.I_Qp = (pomax/vomin)*obj.Dmax/obj.nps; % current stress on primary switch
      obj.I_Qs = (pomax/vomin)*obj.Dmax; % current stress on secondary switch
      obj.I_Qsync=(pomax/vomin)*(1-obj.Dmax); % current stress on secondary synchronous switch
    end
  end
end
