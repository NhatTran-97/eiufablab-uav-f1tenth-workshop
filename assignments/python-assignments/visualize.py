import math
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML, display


class RobotAnimator:
    def __init__(self, robot):
        self.robot = robot
        self.frames = []
        self.path_x = []
        self.path_y = []

        self.fig, self.ax = plt.subplots(figsize=(8, 6))
        self.path_line = None
        self.robot_body = None
        self.arrow = None
        self.info_text = None
        self.ani = None

    def add_frame(self, x, y, yaw, state, battery):
        self.frames.append((x, y, yaw, state, battery))

    def animate_move_linear(self, start_x, start_y, end_x, end_y, yaw, state,
                            start_battery, end_battery, steps=20):
        for i in range(1, steps + 1):
            t = i / steps
            x = start_x + (end_x - start_x) * t
            y = start_y + (end_y - start_y) * t
            battery = start_battery + (end_battery - start_battery) * t
            self.add_frame(x, y, yaw, state, battery)

    def animate_rotate_motion(self, x, y, start_yaw, end_yaw, state,
                              start_battery, end_battery, steps=50):
        for i in range(1, steps + 1):
            t = i / steps
            yaw = start_yaw + (end_yaw - start_yaw) * t
            battery = start_battery + (end_battery - start_battery) * t
            self.add_frame(x, y, yaw, state, battery)

    def animate_scan_motion(self, x, y, base_yaw, state,
                            start_battery, end_battery, steps=25):
        for i in range(steps):
            t = (i + 1) / steps
            yaw = base_yaw + 20 * math.sin(i * 0.4)
            battery = start_battery + (end_battery - start_battery) * t
            self.add_frame(x, y, yaw, state, battery)

    def animate_charging(self, x, y, yaw, state, start_battery, steps=25):
        for i in range(1, steps + 1):
            t = i / steps
            battery = start_battery + (100 - start_battery) * t
            self.add_frame(x, y, yaw, state, battery)

    def capture_state(self, x, y, yaw, state, battery, steps=25):
        for _ in range(steps):
            self.add_frame(x, y, yaw, state, battery)

    def setup_plot(self):
        self.ax.clear()
        self.ax.set_xlim(-2, 12)
        self.ax.set_ylim(-2, 12)
        self.ax.set_aspect("equal")
        self.ax.grid(True)
        self.ax.set_xlabel("X position (m)")
        self.ax.set_ylabel("Y position (m)")
        self.ax.set_title("Smart Robot Animation")

        self.path_line, = self.ax.plot([], [], marker="o")
        self.robot_body, = self.ax.plot([], [], marker="o", markersize=12)
        self.info_text = self.ax.text(
            0.02, 0.98, "", transform=self.ax.transAxes, va="top"
        )

        self.path_x = []
        self.path_y = []
        self.arrow = None

        return self.path_line, self.robot_body, self.info_text

    def update(self, frame):
        x, y, yaw, state, battery = frame

        self.path_x.append(x)
        self.path_y.append(y)

        self.path_line.set_data(self.path_x, self.path_y)
        self.robot_body.set_data([x], [y])

        if self.arrow is not None:
            self.arrow.remove()

        dx = 0.8 * math.cos(math.radians(yaw))
        dy = 0.8 * math.sin(math.radians(yaw))
        self.arrow = self.ax.arrow(
            x, y, dx, dy,
            head_width=0.2,
            head_length=0.25,
            length_includes_head=True
        )

        self.info_text.set_text(
            f"Name: {self.robot.name}\n"
            f"State: {state}\n"
            f"Battery: {battery:.1f}%\n"
            f"Position: ({x:.2f}, {y:.2f})\n"
            f"Yaw: {yaw:.1f} deg"
        )

        return self.path_line, self.robot_body, self.info_text, self.arrow

    def build_animation(self):
        self.ani = FuncAnimation(
            self.fig,
            self.update,
            frames=self.frames,
            init_func=self.setup_plot,
            interval=100,
            blit=False,
            repeat=False,
            cache_frame_data=False
        )
        return self.ani

    def save_animation_gif(self, filename="robot_simulation.gif", fps=10):
        if not self.frames:
            raise ValueError("No frames found. Hãy cho robot thực hiện hành động trước.")

        self.ani = FuncAnimation(
            self.fig,
            self.update,
            frames=self.frames,
            init_func=self.setup_plot,
            interval=100,
            blit=False,
            repeat=False,
            cache_frame_data=False
        )

        self.ani.save(filename, writer="pillow", fps=fps)
        print(f"Saved GIF: {filename}")

    def show_in_notebook(self):
        if not self.frames:
            raise ValueError("No frames found. Hãy chạy robot trước khi hiển thị animation.")

        self.ani = self.build_animation()
        html = HTML(self.ani.to_jshtml())
        plt.close(self.fig)
        return html