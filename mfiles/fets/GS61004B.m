classdef GS61004B < mosfet
  properties

  end

  methods
    function obj = GS61004B()
      obj.rds = 15e-3; % on resistannce (Ohm)
      obj.vds = 100; % rated VDS
      obj.Qoss = 11.5e-9; % output charge (C)
    end
  end

end
