classdef EPC2032 < mosfet
  properties

  end

  methods
    function obj = EPC2032()
      obj.rds = 4e-3; % on resistannce (Ohm)
      obj.vds = 100; % rated VDS
      obj.Qoss = 66e-9; % output charge (C)
    end
  end

end
