from microbit import *
from machine import time_pulse_us
import utime

# Capteur de ligne sur pin12
# Capteur ultrasonique Grove (trigger et echo sur le même pin) sur pin0

# Fonction pour obtenir la distance mesurée par le capteur ultrasonique
def getUltrasonicData(pin, timeout_us=30000):
    pin.write_digital(0)
    utime.sleep_us(2)
    pin.write_digital(1)
    utime.sleep_us(10)
    pin.write_digital(0)
    
    duration = time_pulse_us(pin, 1, timeout_us) / 1e6  # Temps en secondes
    if duration > 0:
        # Calculer la distance en cm (vitesse du son 343 m/s, divisé par 2 pour aller-retour)
        return 343 * duration / 2 * 100
    else:
        return -1  # Retourne -1 si aucune mesure n'est disponible

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
            codo_controlLeftMotor([0, 0], 0)
            codo_controlRightMotor([0, 0], 0)
        else:
            display.scroll("'" + str(direction) + "' is not a direction")
    else:
        raise ValueError('The speed of codo motors must be set between 0 and 1023')

# Boucle principale
while True:
    # Vérifier l'état des capteurs de ligne
    if pin12.read_digital() == 1:  # Si toujours sur l'arène
        codo_move('stop')  # Stop en attendant un adversaire

        # Vérifier la distance avec le capteur ultrasonique
        distance = getUltrasonicData(pin0)

        if 0 < distance < 80:  # Si un adversaire est détecté à moins de 80 cm
            # Avancer pour attaquer
            codo_move('forward', 1023)
            utime.sleep(2)  # Durée de l'attaque
            codo_move('stop')

            # Vérifier si le robot est encore dans l'arène après l'attaque
            if pin12.read_digital() == 1:
                # Reculer pour battre en retraite
                codo_move('backward', 800)
                utime.sleep(1)  # Durée de la retraite
                codo_move('stop')

                # Se repositionner
                codo_move('right', 800)
                utime.sleep(0.75)  # Ajuster l'angle
                codo_move('stop')
            else:
                # Si hors de l'arène, avancer pour revenir
                codo_move('forward', 1023)
                utime.sleep(1.5)
                codo_move('stop')
        else:
            # Si aucun adversaire détecté, chercher en tournant
            codo_move('right', 600)
            utime.sleep(0.5)
            codo_move('stop')
    else:
        # Si le robot est hors de l'arène, reculer pour revenir
        codo_move('backward', 800)
        utime.sleep(1)
        codo_move('stop')
