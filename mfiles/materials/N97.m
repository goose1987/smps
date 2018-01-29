classdef N97 < ferrite
  properties


  end

  methods
    function obj = N97()
      obj=obj@ferrite();
      obj.vendor = 'TDK';
      obj.resistivity = 8;
      obj.density = 4850;
      obj.Bsat = 0.410;

    end


  end

end
