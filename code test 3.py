from microbit import *
import utime

# moteurs P1 et P2
motor_left = pin1
motor_right = pin2

#capteur ultrasonique P8 et P12
ultrasonic_trigger = pin8
ultrasonic_echo = pin12


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


def mesurer_distance():
    # Envoi d'une impulsion sur la broche trigger
    ultrasonic_trigger.write_digital(0)
    utime.sleep_us(2)
    ultrasonic_trigger.write_digital(1)
    utime.sleep_us(10)
    ultrasonic_trigger.write_digital(0)

    while ultrasonic_echo.read_digital() == 0:
        pass
    start_time = utime.ticks_us()

    while ultrasonic_echo.read_digital() == 1:
        pass
    end_time = utime.ticks_us()


    duration = utime.ticks_diff(end_time, start_time)
    distance = (duration / 2) / 29.1
    return distance

while True:
    distance = mesurer_distance()
    display.scroll(str(int(distance)))

    if distance < 80:  
        avancer()
        sleep(500)
        stop()
    elif distance < 20: 
        tourner_droite()  
        sleep(500)
        avancer()
    else: 
        reculer()  
        sleep(1000)
        tourner_gauche()  
