
"""


Auteur: anonyme

Interface: microbit

Nom du projet: Hxhsbhs

Description: <span class="tooltip-title">Hxhsbhs</span><span class="tooltip-author">Anonyme</span><span class="tooltip-description">No-description</span>

Toolbox: vittascience

Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="forever" id="(1vr,;B6[1U*/a3S]FZa" x="-587" y="113"><statement name="DO"><block type="controls_whileUntil" id="tgHP5!.@KH_XH$@VNA^^"><field name="MODE">UNTIL</field><value name="BOOL"><block type="logic_compare" id="W${q%ge}fmZ?!^)f}`H}"><field name="OP">LT</field><value name="A"><block type="sensors_getGroveUltrasonicRanger" id="T{AdPniydX+Kdd;4V!;G"><mutation pin="true"></mutation><field name="SENSOR">GROVE</field><field name="DATA">DIST</field><field name="PIN">pin0</field></block></value><value name="B"><shadow type="math_number" id="x+=[)z/2LhBDm^1wFVN8"><field name="NUM">1</field></shadow></value></block></value><statement name="DO"><block type="robots_setCodoTurn" id="pi@PEDwmo[3*Cf7$o6l("><field name="DIR">RIGHT</field><value name="SPEED"><shadow type="math_number" id="}Cb37U~}DH+{vXLLu_L5"><field name="NUM">1023</field></shadow></value></block></statement><next><block type="controls_whileUntil" id="}pI6Wk4cXJ7@y+h7*cdO"><field name="MODE">WHILE</field><value name="BOOL"><block type="logic_compare" id="V6HN[nyh?._-+-a@Xq(Y"><field name="OP">EQ</field><value name="A"><block type="sensors_getGroveLineFinder" id="a0/1.FPT|Uz](EMb-r?)"><field name="PIN">pin8</field></block></value><value name="B"><shadow type="math_number" id="SMtDVhB`VSoWP]Nv`c##"><field name="NUM">1</field></shadow><block type="logic_boolean" id="EG[^B~0phBR6W^evC5ro"><field name="BOOL">TRUE</field></block></value></block></value><statement name="DO"><block type="robots_setCodoGo" id="-f3`Tanp%QKNP;KtggQ:"><field name="DIR">FORWARD</field><value name="SPEED"><shadow type="math_number" id="EdsCX@CIs(s2_Xm64=zk"><field name="NUM">1023</field></shadow></value></block></statement></block></next></block></statement></block><block type="on_start" id="G[=T#8yqB70`NFgYq}GP" deletable="false" x="313" y="413"></block></xml>

Projet généré par Vittascience.

Ce fichier contient le code textuel ainsi que le code blocs. Il peut être importé de nouveau

sur l'interface http://vittascience.com/microbit


"""

from microbit import *
from machine import time_pulse_us
import utime

# Ultrasonic on pin0
# Line Finder on pin8

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
  while not getUltrasonicData(pin0, pin0, 'distance') < 1:
    codo_move('right', 1023)
  while pin8.read_digital() == True:
    codo_move('forward', 1023)
