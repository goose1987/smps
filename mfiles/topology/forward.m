classdef forward < iso_dcdc
  % diode reset forward converter
  properties
    I_Qsync  % current stress synchronous switch on secondary side
  end
  methods
    function obj=forward(vimax,vimin,vomax,vomin,pomax)

      obj.Dmin = 0.15; % set minimum duty cycle
      obj.nps = vimax*obj.Dmin/vomin; % set turns ratio based on min duty cycle
      obj.Dmax = obj.nps*vomax/vimin; % max duty cycle
      % check for correctness
      checkDmax(obj.Dmax);
      %obj.V_Qs1 = vimax/obj.nps; % voltage stress on secondary switch
      %obj.V_Qs2 = vimax/obj.nps; % voltage stress on secondary switch
      obj.V_Qs = vimax/obj.nps; % voltage stress on secondary switches
      vix=vimin:vimax;
      obj.V_Qp = max(vix+vix.*(obj.nps.*vomax./vix./(1-obj.nps.*vomax./vix))); % max stress on primary switch
      obj.nsw = 3; % number of active switch not including diode on reset winding
      obj.nwinding = 3; % number of winding including reset winding
      obj.I_Qp = (pomax/vomin)*obj.Dmax/obj.nps; % current stress on primary switch
      obj.I_Qs = (pomax/vomin)*obj.Dmax; % current stress on secondary switch
      obj.I_Qsync=(pomax/vomin)*(1-obj.Dmax); % current stress on secondary synchronous switch
    end
  end
end
