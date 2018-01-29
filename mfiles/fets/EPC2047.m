classdef EPC2047 < mosfet
  properties

  end

  methods
    function obj = EPC2047()
      obj.rds = 10e-3; % on resistannce (Ohm)
      obj.vds = 200; % rated VDS
      obj.Qoss = 60e-9; % output charge (C)
      obj.Vsd = 2; % reverse conduction (V)
      obj.Vdrv = 5; % drive voltage (V)
      obj.Qg = 8.2e-9; % gate charge (C)
      obj.xdim = 4.6e-3; % x dimension (mm)
      obj.ydim = 1.6e-3; % y dimension (mm)
    end
  end

end
