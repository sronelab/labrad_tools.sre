import json
import numpy as np
import os
import time

from twisted.internet.defer import inlineCallbacks

from conductor.parameter import ConductorParameter

class Recorder(ConductorParameter):
    autostart = True
    priority = 8
    data_filename = '{}.blue_pmt'
    pmt_name = 'blue_pmt'
    record_sequences = [
        'lattice_sb_linescan',
        'sf_red_some_bs',
        'lattice_pol_p_linescan',
        'lattice_pol_m_linescan',
        'lattice_pol_m_noClock',
        'sf_red_some_test',
        'lattice_mF_scan',
        'co_pulse_plus',
        'co_pulse_minus'
        ]

    def initialize(self, config):
        super(Recorder, self).initialize(config)
        self.connect_to_labrad()
        request = {self.pmt_name: {}}
        self.cxn.pmt.initialize_devices(json.dumps(request))

    @property
    def value(self):
        experiment_name = self.server.experiment.get('name')
        shot_number = self.server.experiment.get('shot_number')
        sequence = self.server.parameters.get('sequencer.sequence')
        previous_sequence = self.server.parameters.get('sequencer.previous_sequence')

        value = None
        if (experiment_name is not None) and (sequence is not None):
            point_filename = self.data_filename.format(shot_number)
            rel_point_path = os.path.join(experiment_name, point_filename)
            #Mod for Sr 1
            name_tuple = os.path.split(rel_point_path)
            file_name = name_tuple[1]
            path_tuple = os.path.split(name_tuple[0])
            rel_point_path = os.path.join(path_tuple[0], 'scans', path_tuple[1],file_name) 
            
            if sequence.loop:
#                print 'pre', sequence.previous_value
                if np.intersect1d(previous_sequence.value, self.record_sequences):
                    value = rel_point_path
            elif np.intersect1d(sequence.value, self.record_sequences):
#                print 'now', sequence.value
                value = rel_point_path
        elif sequence is not None:
            rel_point_path = "pmt_data"
            if sequence.loop:
#                print 'pre', sequence.previous_value
                if np.intersect1d(previous_sequence.value, self.record_sequences):
                    value = rel_point_path
            elif np.intersect1d(sequence.value, self.record_sequences):
#                print 'now', sequence.value
                value = rel_point_path
        return value
    
    @value.setter
    def value(self, x):
        pass
    
    def update(self):
        if self.value is not None:
            request = {self.pmt_name: self.value}
            print request
            self.cxn.pmt.record(json.dumps(request))

Parameter = Recorder
