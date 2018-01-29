classdef buck < n_iso_dcdc
  properties
    nleave=1; % number of interleaved
  end
  methods
    function y=D(obj,vin,vout)
      y=vout./vin;
    end
    % mosfet loss
    % synchronous half bridge
    function P=fetloss(obj,vin,vout,pout,Qmain,Qsync)
      Qm_ig=Qmain.Vdrv./obj.Rdrv; % gate drive current (A)
      toff=Qmain.Qg./Qm_ig; % turn on time (s)
      ton=Qmain.Qg./Qm_ig; % turn off time (s)
      iout = (pout./vout)./obj.nleave; % output current (A)
      D = vout./vin; % duty cycle
      %% main switch
      Qm_conduction = obj.I2R(iout,Qmain.rds).*(D); % conduction loss of main fet (W)
      Qm_sw_off = (1./2).*vin.*iout.*toff.*obj.fsw; % switching loss turning off (W)
      % switching + Qoss + Qrr
      Qm_sw_on = vin.*iout.*ton.*obj.fsw./2+Qmain.Qoss.*vin.*obj.fsw./2+Qsync.Qrr.*vin.*obj.fsw; % switching loss turning on
      Qm_sw = Qm_sw_off + Qm_sw_on; % total switching loss of main switch

      %% sync switch
      Qs_conduction = obj.I2R(iout,Qsync.rds).*(1-D); % conduction loss of sync fet (W)
      Qs_dt = iout.*Qsync.Vsd.*obj.tdt.*obj.fsw.*2; % dead time loss
      Qs_sw = Qsync.Qrr.*vin.*obj.fsw+0.5.*Qsync.Qoss.*vin.*obj.fsw; % switching loss (W)
      P=[Qm_conduction Qm_sw Qs_conduction Qs_sw];
    end
    % inductor loss
    function P = Lloss(obj,vin,vout,pout,inductor)
      iL=(pout./vout)./nleave; % inductor current
      P_conduction = obj.I2R(iL,inductor.esr); % conduction loss inductor
      P = P_conduction;
    end
    % filter transfer function
    function H = hfs(obj,s,RL,L,C,RC,R)
      H=(1+C.*RC.*s)./(1+RL./R+(L./R+RC.*C+RL.*C+RL.*RC.*C./R).*s+((R+RC)./R).*L.*C.*s.*s); %LC filter function
    end

    function ma = aramp(obj,L,V)
      m=-V./L; % inductor slope
      ma=0.5.*m; % calculated compensation ramp
    end
    % AC transfer function
    function y=tfs(obj,fmin,fmax)
    end
    function obj=buck(vimax,vimin,vomax,vomin,pomax,fsw)
      obj=obj@n_iso_dcdc(vimax,vimin,vomax,vomin,pomax,fsw);

      % buck only steps down
      if vimin<=vomax
        error('minimum input < maximum output')
      end
      % check for minimum on time issue
      obj.Dmin=vomin/vimax; % minimum duty cycle
      if obj.Dmin<0.1
        disp('low duty cycle, consider using a topology with a transformer')
      end

      obj.Dmax=vomax/vimin; % maximmum duty cycle
      obj.V_Qmain=vimax; % max voltage stress on main switch
      obj.V_Qsync=vimax; % max voltage stress on synchronous switch
      obj.I_Qmain=obj.Dmax.*(pomax./vomin); % max current rms through main fet
      obj.I_Qsync=(1-obj.Dmin).*(pomax./vomin); % max current rms through sync fet
      obj.Rdrv = 4; % R fet driver (ohm)


    end
  end
end
