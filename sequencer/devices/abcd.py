from sequencer.devices.yesr_digital_board.device import YeSrDigitalBoard
from sequencer.devices.yesr_digital_board.channel import YeSrDigitalChannel

class BoardABCD(YeSrDigitalBoard):
    ok_servername = 'yeelmo_ok'
    ok_interface = '1541000D3S'

    conductor_servername = 'conductor'

    sequence_directory = "/home/srgang/J/sequences/{}/"
    autostart = True
    is_master = True

    channels = [
        YeSrDigitalChannel(loc=['A', 0], name='AH mult A2', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['A', 1], name='AH mult A1', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['A', 2], name='AH mult A0', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['A', 3], name='AH switch (on/off)', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['A', 4], name='PV2 (phase)', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['A', 5], name='DDS phase trig', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['A', 6], name='N.C. 1', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['A', 7], name='A/D card trig', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['A', 8], name='Change pol', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['A', 9], name='Clock ramp TTL', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['A', 10], name='AH ramp trig', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['A', 11], name='ZS/TC shutter', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['A', 12], name='Atom shutter', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['A', 13], name='MOT shutter SRS', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['A', 14], name='Servo input', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['A', 15], name='N.C. 2', mode='auto', manual_output=False, invert=False),
        
        YeSrDigitalChannel(loc=['B', 0], name='Repump shutter', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['B', 1], name='Laser A shutter', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['B', 2], name='Laser B shutter', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['B', 3], name='Probe shutter', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['B', 4], name='PMT shutter', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['B', 5], name='H2 retro pol shutter', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['B', 6], name='ZS AOM', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['B', 7], name='TC AOM', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['B', 8], name='Probe AOM', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['B', 9], name='Jacob DAC trig', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['B', 10], name='Shim coil H2', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['B', 11], name='Shim coil H2 bias', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['B', 12], name='Shim coil H1/V', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['B', 13], name='Window heater', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['B', 14], name='Frame grabber trig', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['B', 15], name='TEC trig', mode='auto', manual_output=False, invert=False),
        
        YeSrDigitalChannel(loc=['C', 0], name='689', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['C', 1], name='689 modulation', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['C', 2], name='Polarizing AOM', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['C', 3], name='Polarizing shutter', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['C', 4], name='Killing beam laser B', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['C', 5], name='Cooling RF switch', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['C', 6], name='Repump AOM', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['C', 7], name='Lattice Ramp Trig', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['C', 8], name='DAC Trigger', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['C', 9], name='Clock servo switch', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['C', 10], name='Picoscope trig', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['C', 11], name='Ag FSK trigger', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['C', 12], name='Enable clock servo', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['C', 13], name='Zeeman intensity', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['C', 14], name='Clock AOM', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['C', 15], name='FNC integrator', mode='auto', manual_output=False, invert=False),
        
        YeSrDigitalChannel(loc=['D', 0], name='N.C. 4', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['D', 1], name='N.C. 5', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['D', 2], name='N.C. 6', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['D', 3], name='N.C. 7', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['D', 4], name='N.C. 8', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['D', 5], name='N.C. 9', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['D', 6], name='N.C. 10', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['D', 7], name='N.C. 11', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['D', 8], name='N.C. 12', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['D', 9], name='N.C. 13', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['D', 10], name='N.C. 14', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['D', 11], name='N.C. 15', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['D', 12], name='N.C. 16', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['D', 13], name='N.C. 17', mode='auto', manual_output=False, invert=False),
        YeSrDigitalChannel(loc=['D', 14], name='N.C. 18', mode='auto', manual_output=True, invert=False),
        YeSrDigitalChannel(loc=['D', 15], name='Trigger', mode='auto', manual_output=False, invert=False),
        ]
        
Device = BoardABCD
