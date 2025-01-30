from microbit import *
import utime

# Configuration des moteurs (connectés aux broches P1 et P2)
motor_left = pin1
motor_right = pin2

# Configuration du capteur ultrasonique (connecté à P8 et P12)
ultrasonic_trigger = pin8
ultrasonic_echo = pin12

# Fonctions de contrôle des moteurs
def avancer():
    motor_left.write_digital(1)
    motor_right.write_digital(1)

def reculer():
    motor_left.write_digital(0)
    motor_right.write_digital(0)

def tourner_gauche():
    motor_left.write_digital(0)
    motor_right.write_digital(1)

def tourner_droite():
    motor_left.write_digital(1)
    motor_right.write_digital(0)

def stop():
    motor_left.write_digital(0)
    motor_right.write_digital(0)

# Fonction pour mesurer la distance avec le capteur ultrasonique
def mesurer_distance():
    # Envoi d'une impulsion sur la broche trigger
    ultrasonic_trigger.write_digital(0)
    utime.sleep_us(2)
    ultrasonic_trigger.write_digital(1)
    utime.sleep_us(10)
    ultrasonic_trigger.write_digital(0)

    # Lecture du temps de retour de l'écho
    while ultrasonic_echo.read_digital() == 0:
        pass
    start_time = utime.ticks_us()

    while ultrasonic_echo.read_digital() == 1:
        pass
    end_time = utime.ticks_us()

    # Calcul de la distance en centimètres
    duration = utime.ticks_diff(end_time, start_time)
    distance = (duration / 2) / 29.1
    return distance

# Boucle principale
while True:
    distance = mesurer_distance()
    display.scroll(str(int(distance)))

    if distance < 10:  # Si un adversaire est proche (< 10 cm)
        avancer()
        sleep(500)
        stop()
    elif distance < 20:  # Si un adversaire est détecté à une distance moyenne
        tourner_droite()  # Préparer une attaque
        sleep(500)
        avancer()
    else:  # Si aucun adversaire n'est détecté
        reculer()  # Bat en retraite
        sleep(1000)
        tourner_gauche()  # Se repositionner
