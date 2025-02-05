from microbit import *
import utime

# Fonction pour obtenir la distance du capteur ultrason
def getUltrasonicData(trig, echo, data='distance', timeout_us=30000):
    trig.write_digital(0)
    utime.sleep_us(2)
    trig.write_digital(1)
    utime.sleep_us(10)
    trig.write_digital(0)
    echo.read_digital()
    duration = time_pulse_us(echo, 1, timeout_us) / 1e6  # durée en secondes
    if duration > 0:
        if data == 'distance':
            return 343 * duration / 2 * 100  # distance en cm
        elif data == 'duration':
            return duration
        else:
            raise ValueError("Option de données '" + data + "' invalide")
    else:
        return -1

# Fonction pour contrôler les moteurs
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
        raise ValueError('La vitesse des moteurs doit être comprise entre 0 et 255')

utime.sleep(5)

while True:
    # Si la ligne est noire devant, avancer
    if pin8.read_digital() == True:
        if getUltrasonicData(pin1, pin1, 'distance') > 10:  # Si la distance est supérieure à 10 cm
            codo_move('right', 600)
        elif getUltrasonicData(pin1, pin1, 'distance') < 10:  # Si la distance est inférieure à 10 cm
            while getUltrasonicData(pin1, pin1, 'distance') < 10:  # Avancer tant que l'obstacle est à moins de 10 cm
                codo_move('forward', 1023)
    # Si le détecteur de ligne ne détecte pas, reculer un peu
    else:
        codo_move('backward', 600)
        utime.sleep(1)
      
