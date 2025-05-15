class SimulationEngine:
    def __init__(self):
        self.state = {}
        self.time_step = 0.01  # Default time step for simulation

    def initialize(self):
        """Initialize the simulation state."""
        self.state = {
            'objects': [],
            'time': 0.0
        }

    def update(self):
        """Update the simulation state."""
        self.state['time'] += self.time_step
        # Update object states here (e.g., position, velocity)

    def add_object(self, obj):
        """Add an object to the simulation."""
        self.state['objects'].append(obj)

    def get_state(self):
        """Return the current state of the simulation."""
        return self.state

    def reset(self):
        """Reset the simulation to its initial state."""
        self.initialize()