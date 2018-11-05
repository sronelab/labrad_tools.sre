import sequencer.devices.yesr_analog_board.device
reload(sequencer.devices.yesr_analog_board.device)
import sequencer.devices.yesr_analog_board.channel
reload(sequencer.devices.yesr_analog_board.channel)
from sequencer.devices.yesr_analog_board.device import YeSrAnalogBoard
from sequencer.devices.yesr_analog_board.channel import YeSrAnalogChannel

class BoardF(YeSrAnalogBoard):
    conductor_servername = 'conductor'
    ok_servername = 'yeelmo_ok'
    ok_interface = '1744000K23'
    sequence_directory = "/home/srgang/J/sequences/{}/"

    autostart = True
    is_master = True

    channels = [
        YeSrAnalogChannel(loc=0, name='H2 Bias 2', mode='auto', manual_output=0.0),
        YeSrAnalogChannel(loc=1, name='813 H1 Intensity', mode='auto', manual_output=0.0),
        YeSrAnalogChannel(loc=2, name='813 H2 Intensity', mode='auto', manual_output=0.0),
        YeSrAnalogChannel(loc=3, name='813 V Intensity', mode='auto', manual_output=0.0),
        YeSrAnalogChannel(loc=4, name='Clock Intensity', mode='auto', manual_output=0.0),
        YeSrAnalogChannel(loc=5, name='813H Mixer', mode='manual', manual_output=-2.0),
        YeSrAnalogChannel(loc=6, name='813V Mixer', mode='manual', manual_output=-2.0),
        YeSrAnalogChannel(loc=7, name='Spin Pol. Intensity', mode='auto', manual_output=0.0),
        ]


Device = BoardF
