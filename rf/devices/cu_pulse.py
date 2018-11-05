
import rf.devices.sg382.device
reload(rf.devices.sg382.device)
from rf.devices.sg382.device import SG382

class CUPulse(SG382):
    autostart = True
    vxi11_address='192.168.1.14'

    default_frequency = 2.0*135.374e6 #Default fiber noise demod freq
    frequency_range = (1e-6, 500e6)

Device = CUPulse


