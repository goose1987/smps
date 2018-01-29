classdef fullbridge2L < iso_dcdc
  properties
    %V_Qp1
    %V_Qp2
    %V_Qs1
    %V_Qs2
    %I_Qp1
    %I_Qp2
    %I_Qs1
    %I_Qs2
  end
  methods
    function P=fetloss(obj,vin,vout,pout,Qp,Qs)
      Qp_ig=Qp.Vdrv./obj.Rdrv;
      toff = Qp.Qg./Qp_ig; % turn on time (s)
      ton = Qp.Qg./Qp_ig; % turn off time (s)
      iout=(pout./vout);
      ip = (iout)./obj.nps; % primary current
      D = vout./vin.*0.5.*obj.nps; % duty cycle

      %% primary switch
      Qp_conduction = Qp.rds.*(ip).^2.*(D).*4; % 4 primary switches

      % switching
      Qp_sw_off = 0.5.*vin.*ip.*toff.*obj.fsw;
      Qp_sw_on = 0.5.*vin.*ip.*ton.*obj.fsw+0.5.*Qp.Qoss.*vin.*obj.fsw+Qp.Qrr.*vin.*obj.fsw;
      Qp_sw = (Qp_sw_off+Qp_sw_on).*4; % 4 primary switches

      %% secondary switches
      Qs_conduction = Qs.rds.*(0.5.*iout).^2.*2; % 2 secondary switches

      % switching
      Qs_sw_off=0.5.*vin./obj.nps.*ip.*toff.*obj.fsw;
      Qs_sw = Qs_sw_off;

      P=[Qp_conduction Qp_sw Qs_conduction Qs_sw];

    end
    % inductor losses
    function P= Lloss(obj,vin,vout,pout,inductor)
      iL=0.5.*(pout./vout); % inductor current
      P_conduction = inductor.esr.*iL.*iL.*2; % 2 inductor 1/2 current
      P=P_conduction;

    end
    % Xformer losses
    function P = Xloss(obj,vin,vout,pout,Xformer)
      Pcore = 0; % core loss
      Pwinding_DC=0; % DC winding loss
      Pwinding_AC=0; % AC winding loss

    end
    function y = D(obj,vin,vout)
      y=0.5.*obj.nps.*vout./vin;
    end
    function obj=fullbridge2L(vimax,vimin,vomax,vomin,pomax)

      %obj.V_Qp1=2*vimax; % voltage stress on primary switch
      %obj.V_Qp2=2*vimax; % voltage stress on primary switch
      obj.V_Qp = vimax;
      % for push pull Dmax is limited at 50%, set at 0.4 for dynamic range
      Dmid = 0.2;
      vimid=0.5.*(vimax+vimin);
      vomid=0.5.*(vomax+vomin);

      obj.nps=2*Dmid*vimid/vomid; % turns ratio based on minimum duty cycle
      obj.Dmax=obj.D(vimin,vomax);
      obj.Dmin=obj.D(vimax,vomin); % maximum duty cycle
      obj.checkDmin(obj.Dmin); % check minimum duty cycle
      %obj.I_Qp1 = obj.Dmax*(pomax/vomin)/obj.nps; % current stress on primary switch
      %obj.I_Qp2 = obj.Dmax*(pomax/vomin)/obj.nps; % current stress on primary switch
      obj.I_Qp = obj.Dmax.*(pomax/vomin)/obj.nps; % current stress on primary switch
      obj.V_Qs = vimax./obj.nps; % voltage stress on secondary switches
      obj.nsw = 6; % number of active switches
      obj.nwinding = 2; % number of windings
      obj.nL = 2; % number of inductor

    end
  end
end
