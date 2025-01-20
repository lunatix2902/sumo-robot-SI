
"""


Auteur: anonyme

Interface: microbit

Nom du projet: Hxhsbhs

Description: <span class="tooltip-title">Hxhsbhs</span><span class="tooltip-author">Anonyme</span><span class="tooltip-description">No-description</span>

Toolbox: vittascience

Mode: mixed

Blocks: <xml xmlns="https://developers.google.com/blockly/xml"><block type="forever" id="(1vr,;B6[1U*/a3S]FZa" x="-613" y="162"><statement name="DO"><block type="controls_if" id="]?^)txtJ@8PVGM/JIrxN"><mutation else="1"></mutation><value name="IF0"><block type="logic_compare" id="qOK$$w(-9,Ck|%}FG2Ft"><field name="OP">LT</field><value name="A"><block type="sensors_getGroveUltrasonicRanger" id="Q8oXriTm5utKx:CgKw{^"><mutation pin="true"></mutation><field name="SENSOR">GROVE</field><field name="DATA">DIST</field><field name="PIN">pin1</field></block></value><value name="B"><shadow type="math_number" id="Wf#w7/c%8Q||[urC]Hv:"><field name="NUM">1</field></shadow></value></block></value><statement name="DO0"><block type="robots_setCodoStop" id="(_r2C:c`o_;~EbmH0+I?"><next><block type="controls_if" id="KwLQ24ICvHP0zi8Hnu!Y"><mutation else="1"></mutation><value name="IF0"><block type="logic_compare" id="rZd*82gX|l-KmGoI1]h1"><field name="OP">EQ</field><value name="A"><block type="sensors_getGroveLineFinder" id=".9tT(b$1t:~0BY:oWxUb"><field name="PIN">pin1</field></block></value><value name="B"><shadow type="math_number" id="4-O(}8%j22pBK_s]T{sS"><field name="NUM">1</field></shadow><block type="logic_boolean" id="4cY;6VJ(i;A]2s{/9HIz"><field name="BOOL">TRUE</field></block></value></block></value><statement name="DO0"><block type="controls_whileUntil" id="6p5Y89QN-f={,X(R+Z.R"><field name="MODE">WHILE</field><value name="BOOL"><block type="logic_compare" id="T+[rA*K5dLJ,K?{e]|b8"><field name="OP">EQ</field><value name="A"><block type="sensors_getGroveLineFinder" id="4a58SbU]D9+f0M%[QR?8"><field name="PIN">pin1</field></block></value><value name="B"><shadow type="math_number" id="JL,YTL%eHSuYeGMECF.X"><field name="NUM">1</field></shadow><block type="logic_boolean" id="S,#_5cBsDl!VZiQWs~ny"><field name="BOOL">TRUE</field></block></value></block></value><statement name="DO"><block type="robots_setCodoGo" id="M]f9.Eenl46z7DBJkqkq"><field name="DIR">FORWARD</field><value name="SPEED"><shadow type="math_number" id="L=r^*t$22uLK~xf1g!/2"><field name="NUM">1023</field></shadow></value></block></statement></block></statement><statement name="ELSE"><block type="robots_setCodoStop" id="|Or;ZYOBXW@|p7ePcd(3"></block></statement></block></next></block></statement><statement name="ELSE"><block type="robots_setCodoTurn" id="c)hJH!10^lu)a4f7swj)"><field name="DIR">RIGHT</field><value name="SPEED"><shadow type="math_number" id="zJf$=;*/tMnnGBjcwE?g"><field name="NUM">1023</field></shadow></value></block></statement></block></statement></block><block type="on_start" id="G[=T#8yqB70`NFgYq}GP" deletable="false" x="313" y="413"></block></xml>

Projet généré par Vittascience.

Ce fichier contient le code textuel ainsi que le code blocs. Il peut être importé de nouveau

sur l'interface http://vittascience.com/microbit


"""

from microbit import *
from machine import time_pulse_us
import utime

# Ultrasonic on pin1
# Line Finder on pin1

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
  if getUltrasonicData(pin1, pin1, 'distance') < 1:
    codo_move('stop')
    if pin1.read_digital() == True:
      while pin1.read_digital() == True:
        codo_move('forward', 1023)
    else:
      codo_move('stop')
  else:
    codo_move('right', 1023)
