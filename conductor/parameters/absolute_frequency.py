from conductor.parameter import ConductorParameter

class AbsoluteFrequency(ConductorParameter):
    priority = 4 #Must be higer than clock_aom.hr_frequency and clock_fiber_aom.hr_demod_frequency
    autostart = True
    def initialize(self,config):
	self.connect_to_labrad()
	comb_m = 1716882.
	f_rep = 250.0044673155e6
	f_ceo = 35e6
	self.value = comb_m*f_rep+2*f_ceo

    def update(self):
        request = {'si_demod': {}}
        mjm_comb_demod = self.server._get_parameter_values(request, all=False)['si_demod']
        fSr = 429228004229873.
        f_vco = 155.504e6/2.0

        SL_FNC_table_AOM = 30.0e6
        SL_FNC_comb = 95.524640e6 + 2*SL_FNC_table_AOM
        f_fnc = 2.0*(float(self.value) -fSr + SL_FNC_comb/2.0 - mjm_comb_demod)
        f_steer = f_fnc/2.0 - f_vco
        request = {
                'clock_aom.hr_frequency': float(f_steer),
                'clock_fiber_aom.hr_demod_frequency': float(f_fnc/2.0),
                }
        self.server._set_parameter_values(request)
        

Parameter = AbsoluteFrequency
