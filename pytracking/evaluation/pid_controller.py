class PIDController:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.prev_error = 0
        self.integral = 0

    def compute(self, angle_error, dt):
        # PID calculations
        self.integral += angle_error * dt
        derivative = (angle_error - self.prev_error) / dt
        self.prev_error = angle_error

        control_signal = self.Kp * angle_error + self.Ki * self.integral + self.Kd * derivative

        return control_signal