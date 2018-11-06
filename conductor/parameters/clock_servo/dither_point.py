from conductor.parameter import ConductorParameter

class Ditherer(object):
    def __init__(self, **kw):
        self.side = None
        for key, value in kw.items():
            setattr(self, key, value)
 
    @property
    def output(self):
        if self.side == 'left':
            return -self.modulation_depth 
        elif self.side == 'right':
            return self.modulation_depth 


class DitherPoint(ConductorParameter):
    """ 
    example_config = {
        'locks': {
            '+9/2': {
                'modulation_depth': 1,
                'control_parameters': ['clock_aom'],
                },
            '-9/2': {
                'modulation_depth': 1,
                'control_parameters': ['clock_aom'],
                },
            },
        }
    """
    priority = 8
    autostart = False
    locks = {}

    def initialize(self, config):
        print config
        super(DitherPoint, self).initialize(config)
        self.locks = config.get('locks')
        print "locks:"
        print self.locks
        if self.locks is not None:
            for name, settings in self.locks.items():
                setattr(self, name, Ditherer(**settings))

    def _get_lock(self, lock_name):
        print "get_lock for dither_point"
        print self.locks
        if lock_name not in self.locks:
            message = 'lock ({}) not defined in {}'.format(lock_name, self.name)
            raise Exception(message)
        else:
            return self.locks[lock_name]


    def update(self):
        print "updating dither_point"
        if self.value is not None:
            name, side = self.value
            lock = self._get_lock(name)
            print lock
            ditherer = Ditherer(**lock)
            ditherer.side = side
            request = {'clock_servo.dithers.{}'.format(name): ditherer.output}
            self.server._set_parameter_values(request)
            
            control_loop = self.server._get_parameter('clock_servo.control_loop')._get_lock(name)
            output = control_loop.output + ditherer.output
            control_loop.pmt_shot_number = self.server.experiment.get('shot_number')
            
            request = {parameter_name: output 
                       for parameter_name in dither.control_parameters}
            self.server._set_parameter_values(request)
        
        if self.previous_value is not None:
            request = {'clock_servo.feedback_point': self.previous_value}
            self.server._set_parameter_values(request)

Parameter=DitherPoint
