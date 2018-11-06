from conductor.parameter import ConductorParameter

import sys
sys.path.append('/home/srgang/Password/')
from srq_password import password as srqPassword

class SiDemod(ConductorParameter):
    priority = 1
    autostart = True
    def initialize(self,config):
        #Connect to stable lasers demod server on Sr2 network
        self.connect_to_labrad(host = 'yesr10.colorado.edu', password = srqPassword)

    def update(self):
        self.value = self.cxn.si_demod.get_frequency()
        

Parameter = SiDemod
