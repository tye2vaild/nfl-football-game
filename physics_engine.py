# Physics Engine for NFL Football Game Simulation

class PhysicsEngine:
    def __init__(self):
        self.gravity = -9.81  # Gravity constant (m/s^2)
        self.time_step = 0.016  # Time step for simulation (seconds)

    def update_position(self, position, velocity):
        """Updates the position based on current velocity and time step."""
        new_position = (position[0] + velocity[0] * self.time_step,
                        position[1] + velocity[1] * self.time_step)
        return new_position

    def apply_gravity(self, velocity):
        """Applies gravity to the vertical component of the velocity."""
        new_velocity = (velocity[0], velocity[1] + self.gravity * self.time_step)
        return new_velocity

    def simulate_step(self, position, velocity):
        """Simulates one step of movement in the physics engine."""
        velocity = self.apply_gravity(velocity)
        position = self.update_position(position, velocity)
        return position, velocity

# Example usage
if __name__ == '__main__':
    engine = PhysicsEngine()
    position = (0, 100)  # Starting position (x, y)
    velocity = (10, 0)   # Starting velocity (vx, vy)
    for _ in range(60):  # Simulate for 60 steps
        position, velocity = engine.simulate_step(position, velocity)
        print(f'New Position: {position}, New Velocity: {velocity}');