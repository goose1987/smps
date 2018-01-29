classdef mosfet
  properties
    rds % on resistance
    vds % rated drain to source voltage
    Qg % total gate charge
    Qgd % gate to drain charge
    Qgs % gate to source charge
    Qrr = 0; % reverse recovery charge, assume GaN
    Vdrv = 5; % drive voltage (V)
    Vsd
    Qoss % output charge
    xdim % x dimension
    ydim % y dimension
    zdim % z dimension

  end
  methods

  end
end
