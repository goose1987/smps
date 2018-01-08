classdef EPC2047 < mosfet
  properties

  end

  methods
    function obj = EPC2047()
      obj.rds = 10e-3; % on resistannce (Ohm)
      obj.vds = 200; % rated VDS
      obj.Qoss = 60e-9; % output charge (C)
    end
  end

end
