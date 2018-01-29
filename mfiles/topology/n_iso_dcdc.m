classdef n_iso_dcdc
  properties
    vimax       % max input voltage
    vimin       % min input voltage
    vomax       % max output voltage
    vomin       % min output voltage
    pomax       % max output power
    V_Qmain     % VDS max of main switch (V)
    V_Qsync     % VDS max of synchronous switch (V)
    I_Qmain     % I max of main switch (A)
    I_Qsync     % I max of synchronous switch(A)
    Dmin        % minimum duty cycle
    Dmax        % maximum duty cycle
    fsw         % switching frequency
    Lprim       % primary inductor
    Lprim_esr   % primary inductor ESR
    Cout        % output capacitor
    Rdrv   = 4;     % R fet driver
    tdt    = 0;     % dead time (s)

  end

  methods
    function PI2R = I2R(obj,current,resistance)
      PI2R = current.*current.*resistance;
    end
    function obj = n_iso_dcdc(vimax,vimin,vomax,vomin,pomax,fsw)
      % check for valid inputs
      if vimax<vimin
        error('minimum input is larger than maximum input')
      end
      if vomax<vomin
        error('minimum output is larger than maximum output')
      end

      % assign inputs
      obj.vimax=vimax;
      obj.vimin=vimin;
      obj.vomax=vomax;
      obj.vomin=vomin;
      obj.pomax=pomax;
      obj.fsw = fsw;

    end


  end

end
