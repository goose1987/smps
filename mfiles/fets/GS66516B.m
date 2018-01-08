classdef GS66516B < mosfet
  properties

  end

  methods
    function obj = GS66516B()
      obj.rds = 25e-3; % on resistannce (Ohm)
      obj.vds = 650; % rated VDS
      obj.Qoss = 113e-9; % output charge (C)
    end
  end

end
