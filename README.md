# Physics Simulator

This is a Physics Simulator using Python.

## Project Overview

The Physics Simulator is designed to simulate physical systems using Python. It leverages various libraries to handle physics calculations, rendering, and simulation management.

## Features

- **Simulation Engine**: Manages the state of the simulation and updates physics calculations.
- **Renderer**: Visualizes the simulation using PyOpenGL and Matplotlib.
- **Utility Functions**: Provides helper functions for mathematical calculations and data formatting.

## Installation

To install the project dependencies, use Poetry. First, ensure you have Poetry installed, then run:

```bash
poetry install
```

## Usage

To run the Physics Simulator, execute the following command:

```bash
poetry run python src/main.py
```

## Testing

To run the tests for the simulation components, use:

```bash
poetry run pytest src/tests
```

## Libraries Used

- **Poetry**: Dependency management and packaging.
- **PyOpenGL**: For rendering graphics.
- **Matplotlib**: For plotting and visualizing data.
- **Simpy**: For discrete-event simulation.
- **SciPy**: For scientific computing.
- **NumPy**: For numerical operations.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.