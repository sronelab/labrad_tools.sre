
import rf.devices.ag335xxx.device
reload(rf.devices.ag335xxx.device)
from rf.devices.ag335xxx.device import AG335xxx

class keysight33521a(AG335xxx):

    vxi11_address='192.168.1.17'
    source = 1
    state = 1

    amplitude = 17.0
    amplitude_range = (-30.0, 18.0)

    frequency = 4.0e6 #Default EOM modulation freq
    frequency_range = (1, 30e6)

Device = keysight33521a


