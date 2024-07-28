class PIDController:
    def __init__(self, Kp, Ki, Kd, fov_h, fov_v, width, height):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.prev_error_x = 0
        self.prev_error_y = 0
        self.integral_x = 0
        self.integral_y = 0
        self.fov_h = fov_h
        self.fov_v = fov_v
        self.width = width
        self.height = height
        self.angle_per_pixel_x = (fov_h / 2) / (width / 2)
        self.angle_per_pixel_y = (fov_v / 2) / (height / 2)

    def compute(self, error_x, error_y, dt):
        # PID calculations
        self.integral_x += error_x * dt
        self.integral_y += error_y * dt
        derivative_x = (error_x - self.prev_error_x) / dt
        derivative_y = (error_y - self.prev_error_y) / dt
        self.prev_error_x = error_x
        self.prev_error_y = error_y

        control_x = self.Kp * error_x + self.Ki * self.integral_x + self.Kd * derivative_x
        control_y = self.Kp * error_y + self.Ki * self.integral_y + self.Kd * derivative_y

        # Convert control to angle
        angle_x = control_x * self.angle_per_pixel_x
        angle_y = control_y * self.angle_per_pixel_y

        return angle_x*10, angle_y*10
#
# # Example usage:
# horizontal_fov = 34.50063232000597  # degrees
# vertical_fov = 19.815163113581676  # degrees
# camera_width = 1280  # Width in pixels
# camera_height = 720  # Height in pixels
#
# # Initialize the PID controller with camera parameters
# pid_controller = PIDController(Kp=0.1, Ki=0.01, Kd=0.05, fov_h=horizontal_fov, fov_v=vertical_fov, width=camera_width, height=camera_height)
#
# # Example control loop
# desired_bbox_center = np.array([camera_width // 2, camera_height // 2])  # Center of the frame
#
# # Simulating errors
# error_x = 50  # Example pixel error in x
# error_y = 30  # Example pixel error in y
# dt = 0.1  # Time step in seconds
#
# # Compute the servo angles
