classdef EPC2010C < mosfet
  properties

  end

  methods
    function obj = EPC2010C()
      obj.rds = 25e-3; % on resistannce (Ohm)
      obj.vds = 200; % rated VDS
      obj.Qoss = 40e-9; % output charge (C)
      obj.Vsd = 2; % reverse conduction (V)
      obj.Vdrv = 5; % drive voltage (V)
      obj.Qg = 3.7e-9; % gate charge (C)
      obj.xdim = 3.6e-3; % x dimension (mm)
      obj.ydim = 1.6e-3; % y dimension (mm)
    end
  end

end
