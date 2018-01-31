
% calculate closest 5%  Resistor values required to meet a ratio
% assume E24 values

function [R1 R2 err]=rdiv5(target)
  % standard e24 resistors
  E24=[1.0;1.1;1.2;1.3;1.5;1.6;1.8;2.0;2.2;2.4;2.7;3.0;3.3;3.6;3.9;4.3;4.7;5.1;5.6;6.2;6.8;7.5;8.2;9.1];
  % decade options
  Rpref=[1e0 1e1 1e2 1e3 1e4 1e5 1e6];
  % index the decade based on the log value of ratio for ratio >9.1/1
  idx=floor(log10(target))+1;

  % invert standard e24
  E24inv=1./E24;
  % compute possible ratio matrix
  rat=1+(E24.*Rpref(idx))*E24inv';

  % compute difference between target and ratio matrix
  ratdiff = abs(rat-target);
  % find the indexes of minimum difference
  [row,col]=find(ratdiff==min(ratdiff(:)));
  % return E24 resistor values and error as a percentage
  R1 = E24(row).*Rpref(idx);
  R2 = E24(col);
  err = ratdiff(row,col)./target;

end
