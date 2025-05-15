def calculate_distance(point1, point2):
    """Calculate the Euclidean distance between two points."""
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

def normalize_vector(vector):
    """Normalize a 2D vector."""
    magnitude = (vector[0] ** 2 + vector[1] ** 2) ** 0.5
    if magnitude == 0:
        return (0, 0)
    return (vector[0] / magnitude, vector[1] / magnitude)

def clamp(value, min_value, max_value):
    """Clamp a value between a minimum and maximum."""
    return max(min_value, min(value, max_value))

# Constants
GRAVITY = 9.81  # Acceleration due to gravity (m/s^2)
TIME_STEP = 0.01  # Time step for simulation updates (seconds)