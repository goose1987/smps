classdef N87 < ferrite
  properties


  end

  methods
    function obj = N87()
      obj=obj@ferrite();
      obj.vendor = 'TDK';
      obj.resistivity = 10;
      obj.density = 4850;
      obj.Bsat = 0.390;

    end


  end

end
