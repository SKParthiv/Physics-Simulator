import sys
from simulation.engine import SimulationEngine
from simulation.renderer import Renderer

def main():
    # Initialize the simulation engine
    engine = SimulationEngine()
    
    # Initialize the renderer
    renderer = Renderer(engine)

    # Main loop
    while True:
        # Update the simulation state
        engine.update()
        
        # Render the current state
        renderer.render()

        # Check for exit conditions (e.g., user input)
        if engine.should_exit():
            break

if __name__ == "__main__":
    main()