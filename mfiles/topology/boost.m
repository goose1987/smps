classdef boost < n_iso_dcdc
  properties
  end
  methods
    function y = D(obj,vin,vout)
      y=(vout-vin)/vout;
    end
    function obj=boost(vimax,vimin,vomax,vomin,pomax)
      obj=obj@n_iso_dcdc(vimax,vimin,vomax,vomin);

      % boost only steps up
      if vimax>=vomin
        error('maximum input > minimum output')
      end


      obj.Dmax=(vomax-vimin)/vomax; % max duty cycle
      obj.Dmin=(vomin-vimax)/vomin; % min duty cycle
      obj.V_Qmain=vomax; % voltage stress on main switch
      obj.V_Qsync=vomax; % voltage stress on synchronous switch
      obj.I_Qsync=(pomax/vomin); % current through synchronous switch
      obj.I_Qmain=obj.I_Qsync.*(1/(1-obj.Dmax)); % current through main switch

    end
  end
end
