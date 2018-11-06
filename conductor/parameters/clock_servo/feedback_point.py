from conductor.parameter import ConductorParameter
from control_loops import PID, PIID

class FeedbackPoint(ConductorParameter):
    """ 
    example_config = {
        'locks': {
            '+9/2': {
                'type': 'PID',
                'prop_gain': 1,
                ...
                },
            '-9/2': {
                'type': 'PID',
                'prop_gain': 1,
                ...
                },
            },
        }
    """
    locks = {}
    priority = 9
    autostart = True

    def initialize(self, config):
        super(FeedbackPoint, self).initialize(config)
        self.connect_to_labrad()
        locks = config.get('locks')
        if locks is not None:
            for name, settings in locks.items():
                if settings['type'] == 'PID':
                    setattr(self, name, PID(**settings))
                if settings['type'] == 'PIID':
                    setattr(self, name, PIID(**settings))

    def _get_lock(self, lock_name):
        print "get lock for feedback point"
        if lock not in self.locks:
            message = 'lock ({}) not defined in {}'.format(lock, self.name)
            raise Exception(message)
        else:
            return self.locks[lock_name]

    def update(self):
        print "updating feedback_point"
        if self.value is not None:
            name, side = self.value
            control_loop = self._get_lock(name)
            request = {'blue_pmt': '{}.blue_pmt'.format(control_loop.pmt_shot_number)}
            response_json = self.cxn.pmt.retrive_records(json.dumps(request))
            response = json.loads(response_json)
            frac = response['frac_fit']
            tot = response['tot_fit']

            if tot > control_loop.tot_cutoff:
                control_loop.tick(side, frac)

            request = {'clock_servo.control_signals.{}'.format(name): control_loop.output}
            self.server._set_parameter_values(request)

Parameter = FeedbackPoint
