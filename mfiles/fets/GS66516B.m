classdef GS66516B < mosfet
  properties

  end

  methods
    function obj = GS66516B()
      obj.rds = 25e-3; % on resistannce (Ohm)
      obj.vds = 650; % rated VDS
      obj.Qoss = 113e-9; % output charge (C)
      obj.Vsd = 2; % reverse conduction (V)
      obj.Vdrv = 5; % drive voltage (V)
      obj.Qg = 6.2e-9; % gate charge (C)
    end
  end

end
