classdef EPC2010C < mosfet
  properties

  end

  methods
    function obj = EPC2010C()
      obj.rds = 25e-3; % on resistannce (Ohm)
      obj.vds = 200; % rated VDS
      obj.Qoss = 40e-9; % output charge (C)
    end
  end

end
