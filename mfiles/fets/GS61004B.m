classdef GS61004B < mosfet
  properties

  end

  methods
    function obj = GS61004B()
      obj.rds = 15e-3; % on resistannce (Ohm)
      obj.vds = 100; % rated VDS
      obj.Qoss = 11.5e-9; % output charge (C)
      obj.Vsd = 2; % reverse conduction (V)
      obj.Vdrv = 5; % drive voltage (V)
      obj.Qg = 6.2e-9; % gate charge (C)
    end
  end

end
