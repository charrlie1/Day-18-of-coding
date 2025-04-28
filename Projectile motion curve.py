import math
import matplotlib.pyplot as plt

class Projectile:
    """Abstract class for projectile motion."""
    def __init__(self, initial_velocity, launch_angle_degrees, time_step=0.1):
        self.v0 = initial_velocity
        self.angle_rad = math.radians(launch_angle_degrees)
        self.dt = time_step
        self.g = 9.81  # Acceleration due to gravity (m/s^2)
        self.time = [0.0]
        self.x = [0.0]
        self.y = [0.0]

    def calculate_trajectory(self):
        """Calculates the trajectory of the projectile."""
        t = 0.0
        x = 0.0
        y = 0.0
        vx = self.v0 * math.cos(self.angle_rad)
        vy = self.v0 * math.sin(self.angle_rad)

        while y >= 0:
            t += self.dt
            x += vx * self.dt
            vy -= self.g * self.dt
            y += vy * self.dt

            self.time.append(t)
            self.x.append(x)
            self.y.append(y)

    def plot_trajectory(self, style='-', label='Projectile'):
        """Plots the trajectory."""
        plt.plot(self.x, self.y, style, label=label)
        plt.xlabel("Horizontal Distance (m)")
        plt.ylabel("Vertical Distance (m)")
        plt.title("Projectile Motion")
        plt.legend()
        plt.grid(True)

class ProjectileWithDrag(Projectile):
    """Subclass for projectile motion with air resistance (drag)."""
    def __init__(self, initial_velocity, launch_angle_degrees, drag_coefficient, air_density=1.225, projectile_area=0.01, time_step=0.1):
        super().__init__(initial_velocity, launch_angle_degrees, time_step)
        self.cd = drag_coefficient
        self.rho = air_density
        self.area = projectile_area

    def calculate_trajectory(self):
        """Calculates the trajectory considering air resistance."""
        t = 0.0
        x = 0.0
        y = 0.0
        vx = self.v0 * math.cos(self.angle_rad)
        vy = self.v0 * math.sin(self.angle_rad)
        mass = 1.0  # Assume a mass for drag calculation

        while y >= 0:
            t += self.dt
            v = math.sqrt(vx**2 + vy**2)
            drag_force = 0.5 * self.rho * v**2 * self.cd * self.area
            drag_x = -drag_force * (vx / v) if v > 0 else 0
            drag_y = -drag_force * (vy / v) if v > 0 else 0

            ax = drag_x / mass
            ay = -self.g + drag_y / mass

            x += vx * self.dt + 0.5 * ax * self.dt**2
            y += vy * self.dt + 0.5 * ay * self.dt**2
            vx += ax * self.dt
            vy += ay * self.dt

            self.time.append(t)
            self.x.append(x)
            self.y.append(y)

# Example Usage and Plotting
if __name__ == "__main__":
    # Projectile without drag
    projectile1 = Projectile(initial_velocity=50, launch_angle_degrees=45)
    projectile1.calculate_trajectory()
    projectile1.plot_trajectory(label='No Drag')

    # Projectile with drag
    projectile2 = ProjectileWithDrag(initial_velocity=50, launch_angle_degrees=45, drag_coefficient=0.01)
    projectile2.calculate_trajectory()
    projectile2.plot_trajectory(style='--', label='With Drag')

    plt.show()