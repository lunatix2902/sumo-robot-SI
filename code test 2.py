from microbit import *
from machine import time_pulse_us
import utime

# Line Finder sur pin12 et pin8
# Capteur ultrasonique sur pin0


def getUltrasonicData(trig, echo, data='distance', timeout_us=30000):
    trig.write_digital(0)
    utime.sleep_us(2)
    trig.write_digital(1)
    utime.sleep_us(10)
    trig.write_digital(0)
    echo.read_digital()
    duration = time_pulse_us(echo, 1, timeout_us) / 1e6 
    if duration > 0:
        if data == 'distance':
            return 343 * duration / 2 * 100
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


def codo_move(direction, speed=1023):
    if 0 <= speed <= 1023:
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
        raise ValueError('The speed of codo motors must be set between 0 and 1023')


while True:
    # Vérifier l'état des capteurs de ligne
    while pin12.read_digital() == True and pin8.read_digital() == True:
        codo_move('stop')  # Stop en attendant un adversaire
        
       
        distance = getUltrasonicData(pin0, pin0, 'distance')
        
        if distance > 0 and distance < 80:  # Si un adversaire est détecté à moins de 80 cm
           
            codo_move('forward', 1023)
            utime.sleep(2)  # Durée de l'attaque
            codo_move('stop')
            
            if pin12.read_digital() == True and pin8.read_digital == True: 
            
              
                codo_move('backward', 800)
                utime.sleep(1)  # Durée de la retraite
                codo_move('stop')
            
            else:
              codo_move('forward', 1023)
              utime.sleep(2.5)
            
          
            codo_move('right', 800)
            utime.sleep(0.75)  # Ajustez la durée pour un bon angle
            codo_move('stop')
        else:
            codo_move('right', 600)
            utime.sleep(0.5)
            codo_move('stop')
