from microbit import *
from machine import time_pulse_us
import utime

# Capteur ultrasonique (trigger et echo) sur pin0
# Détecteurs de ligne sur pin12 et pin8

# Fonction pour mesurer la distance avec le capteur ultrasonique
def getUltrasonicData(trig_echo, timeout_us=30000):
    trig_echo.write_digital(0)
    utime.sleep_us(2)
    trig_echo.write_digital(1)
    utime.sleep_us(10)
    trig_echo.write_digital(0)
    duration = time_pulse_us(trig_echo, 1, timeout_us) / 1e6  # Temps en secondes
    if duration > 0:
        # Calcul de la distance en cm (vitesse du son = 343 m/s)
        return 343 * duration / 2 * 100
    else:
        return -1

# Fonctions pour contrôler les moteurs gauche et droit
def codo_controlLeftMotor(cmd, speed):
    pin13.write_analog(cmd[0] * speed)
    pin14.write_analog(cmd[1] * speed)

def codo_controlRightMotor(cmd, speed):
    pin15.write_analog(cmd[0] * speed)
    pin16.write_analog(cmd[1] * speed)

# Fonction pour contrôler le mouvement du robot
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
            display.scroll("'" + str(direction) + "' is not a valid direction")
    else:
        raise ValueError("Speed must be between 0 and 1023")

# Boucle principale
while True:
    # Si les deux capteurs de ligne détectent que le robot est encore dans l'arène
    if pin12.read_digital() == 1 and pin8.read_digital() == 1:
        # Mesurer la distance avec le capteur ultrasonique
        distance = getUltrasonicData(pin0)

        if 0 < distance < 80:  # Adversaire détecté à moins de 80 cm
            # Avancer pour attaquer
            codo_move('forward', 1023)
            utime.sleep(2)  # Durée de l'attaque
            codo_move('stop')

            # Reculer pour se repositionner
            codo_move('backward', 800)
            utime.sleep(1)  # Durée de la retraite
            codo_move('stop')

            # Tourner pour se repositionner
            codo_move('right', 800)
            utime.sleep(0.75)  # Ajuster l'angle de rotation
            codo_move('stop')

        else:
            # Aucun adversaire détecté, faire un mouvement de recherche
            codo_move('right', 600)
            utime.sleep(0.5)
            codo_move('stop')
    else:
        # Si le robot est proche d'une ligne (hors arène), battre en retraite
        codo_move('backward', 800)
        utime.sleep(1)  # Durée de la retraite
        codo_move('stop')
        codo_move('left', 800)  # Tourner pour revenir dans l'arène
        utime.sleep(0.75)
        codo_move('stop')
