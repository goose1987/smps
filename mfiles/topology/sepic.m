classdef sepic < n_iso_dcdc
  properties
    Lsec % secondary inductor
    Lsec_esr % secondary inductor esr
    Cc % coupling capacitor

  end
  methods
    function y=D(obj,vin,vout)
      y=vout/(vin+vout);
    end
    
    function obj=sepic(vimax,vimin,vomax,vomin,pomax)
      obj=obj@n_iso_dcdc(vimax,vimin,vomax,vomin);

      obj.Dmax=(vomax/(vimin+vomax)); % maximum duty cycle
      obj.Dmin=(vomin/(vimax+vomin)); % minimum duty cycle

      obj.V_Qmain=vimax+vomax; % maximum voltage stress on main switch
      obj.V_Qsync=vimax+vomax; % maximum voltage stress on synchronous switch
      obj.I_Qsync=(pomax/vomin); % maximum current stress on synchronous switch
      obj.I_Qmain=(pomax/vomin)*(obj.Dmax/(1-obj.Dmax)); % maximum current stress on main switch

    end
  end
end
