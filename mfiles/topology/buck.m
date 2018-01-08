classdef buck < n_iso_dcdc
  properties
    nleave=1; % number of interleaved
  end
  methods
    function y=D(obj,vin,vout)
      y=vout./vin;
    end
    function obj=buck(vimax,vimin,vomax,vomin,pomax)
      obj=obj@n_iso_dcdc(vimax,vimin,vomax,vomin)

      % buck only steps down
      if vimin<=vomax
        error('minimum input < maximum output')
      end
      % check for minimum on time issue
      obj.Dmin=vomin/vimax; % minimum duty cycle
      if obj.Dmin<0.1
        disp('low duty cycle, consider using a topology with a transformer')
      end

      obj.Dmax=vomax/vimin; % maximmum duty cycle
      obj.V_Qmain=vimax; % max voltage stress on main switch
      obj.V_Qsync=vimax; % max voltage stress on synchronous switch
      obj.I_Qmain=obj.Dmax.*(pomax./vomin); % max current rms through main fet
      obj.I_Qsync=(1-obj.Dmin).*(pomax./vomin); % max current rms through sync fet

    end
  end
end
