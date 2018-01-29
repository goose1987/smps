classdef iso_dcdc
  properties
    vimax     % max input voltage
    vimin     % min input voltage
    vomax     % max output voltage
    vomin     % min output voltage
    pomax     % max output power
    nps       % turns ratio
    nprim     % number of primary turns
    nsec      % number of secondary turns
    Dmin        % minimum duty cycle
    Dmax        % maximum duty cycle
    fsw         % switching frequency
    Lprim       % primary inductor
    Lprim_esr   % primary inductor ESR
    Cout        % output capacitor
    V_Qp        % max voltage on primary switches
    V_Qs        % max voltage on secondary switches
    I_Qp        % current stress on primary switches
    I_Qs        % current stress on seconary switches
    nsw         % number of switches
    nwinding    % number of windings
    nL          % number of inductor

  end
  methods
    function er=checkDmin(obj,D)
      if D<0.1
        error('minimum duty cycle <0.1. check input/output range. May not be achievable')
      end
    end
    function er=checkDmax(obj,D)
      if D>0.9
        error('max duty cycle > 0.9. check input/output range. may not be achievable')
      end
    end

  end

end
