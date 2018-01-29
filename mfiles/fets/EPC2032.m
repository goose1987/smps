classdef EPC2032 < mosfet
  properties

  end

  methods
    function obj = EPC2032()
      obj.rds = 4e-3; % on resistannce (Ohm)
      obj.vds = 100; % rated VDS
      obj.Qoss = 66e-9; % output charge (C)
      obj.Vsd = 2; % reverse conduction (V)
      obj.Vdrv = 5; % drive voltage (V)
      obj.Qg = 12e-9; % gate charge (C)
      obj.xdim = 4.6e-3; % x dimension (mm)
      obj.ydim = 2.6e-3; % y dimension (mm)
    end
  end

end
