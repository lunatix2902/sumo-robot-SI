
from microbit import *
from machine import time_pulse_us
import utime

# Line Finder on pin12
# Line Finder on pin8
# Ultrasonic on pin0

def getUltrasonicData(trig, echo, data='distance', timeout_us=30000):
  trig.write_digital(0)
  utime.sleep_us(2)
  trig.write_digital(1)
  utime.sleep_us(10)
  trig.write_digital(0)
  echo.read_digital()
  duration = time_pulse_us(echo, 1, timeout_us)/1e6 # t_echo in seconds
  if duration > 0:
    if data == 'distance':
      #sound speed, round-trip/2, get in cm
      return 343 * duration/2 * 100
    elif data == 'duration':
      return duration
    else:
      raise ValueError("Data option '" + data + "' is not valid")
  else:
    return -1

def codo_controlLeftMotor(cmd, speed):
  pin13.write_analog(cmd[0] * speed)
  pin14.write_analog(cmd[1] * speed)

def codo_controlRightMotor(cmd, speed):
  pin15.write_analog(cmd[0] * speed)
  pin16.write_analog(cmd[1] * speed)

def codo_move(direction, speed = 1023):
  if (speed >= 0 and speed <= 1023):
    if direction == 'forward':
      codo_controlLeftMotor([0, 1], speed)
      codo_controlRightMotor([0, 1], speed)
    elif direction == 'backward':
      codo_controlLeftMotor([1, 0], speed)
      codo_controlRightMotor([1, 0], speed)
    elif direction == 'right':
      codo_controlLeftMotor([0, 1], speed)
      codo_controlRightMotor([1, 0], speed)
    elif direction == 'left':
      codo_controlLeftMotor([1, 0], speed)
      codo_controlRightMotor([0, 1], speed)
    elif direction == 'stop':
      codo_controlLeftMotor([0, 0], speed)
      codo_controlRightMotor([0, 0], speed)
    else:
      display.scroll("'" + str(direction) + "' is not a direction")
  else:
    raise ValueError('The speed of codo motors have to be set between 0 and 255')

while True:
  while pin12.read_digital() == True or pin8.read_digital() == True:
    while not getUltrasonicData(pin0, pin0, 'duration') > 250:
      codo_move('right', 250)
      codo_move('stop')
      utime.sleep(1)
      codo_move('forward', 1023)
      utime.sleep(1)
      codo_move('right', 650)
      utime.sleep(0.75)
      codo_move('forward', 800)
      utime.sleep(1)
      codo_move('right', 800)
