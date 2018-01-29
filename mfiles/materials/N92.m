classdef N92 < ferrite
  properties


  end

  methods
    function obj = N92()
      obj=obj@ferrite();
      obj.vendor = 'TDK';
      obj.resistivity = 8;
      obj.density = 4850;
      obj.Bsat = 0.440;

    end


  end

end
