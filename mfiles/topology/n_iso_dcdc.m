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

  end

  methods
    function obj = n_iso_dcdc(vimax,vimin,vomax,vomin)
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

    end


  end

end
