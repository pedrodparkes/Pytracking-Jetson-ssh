import sys

from serial import Serial
# import serial.tools.list_ports
from struct import *
import time
import logging
import numpy as np

# Init logging module
logging.basicConfig(level=logging.INFO)
class Servo(Serial):
    def __init__(self, SerialPort = '/dev/ttyUSB0',
                 SerialSpeed = 115200,
                 ServoStartAngle = [90,90],
                 ServoTimeMs = [1,1]):
        self.SerialPort = SerialPort
        self.SerialSpeed = SerialSpeed
        try:
            self.serial_port = Serial(port=self.SerialPort, baudrate=self.SerialSpeed, timeout=1)
            logging.info(f"Serial port {str(self.SerialPort)} opened at speed {str(self.SerialSpeed)}")
        except:
            logging.error(f"Failed to open Serial port {str(self.SerialPort)} at speed {str(self.SerialSpeed)}")
            sys.exit(1)
        self.servo_angle = ServoStartAngle
        self.servo_time_ms = ServoTimeMs
        if len(self.servo_angle) != len(self.servo_time_ms):
            logging.error(f'Number of Servo angles != Number of Servo time values')
            logging.error("What\'s the number of Servos?")
            sys.exit(1)

    def set_servo_pos(self, ServoNum, Angle):
        self.servo_angle[ServoNum] = int(Angle)
        packet = self.__create_packet__()
        self.serial_port.write(packet)

    def set_servo_time_ms(self, ServoNum, TimeMs):
        self.servo_time_ms[ServoNum] = int(TimeMs)

    def __create_packet__(self):
        packet_to_send = pack("<4s4i", b'serv', self.servo_angle[0], self.servo_angle[1], self.servo_time_ms[0], self.servo_time_ms[1])
        return packet_to_send

    def get_servo_pos(self, ServoNum):
        return self.servo_angle[ServoNum]

    def get_servo_time_ms(self, ServoNum):
        return self.servo_time_ms[ServoNum]

# servo = Servo(SerialPort  = '/dev/cu.usbserial-01E8DCFD',
#               SerialSpeed = 115200)
# servo.set_servo_pos(0, 80)
# servo.set_servo_pos(1, 80)
# servo.set_servo_time_ms(0, 1000)
# servo.set_servo_time_ms(1, 1000)
# time.sleep(3)
# servo.set_servo_pos(0, 180)
# servo.set_servo_pos(1, 180)