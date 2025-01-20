


from microbit import *

def tourner_sur_place():
  codo_move('forwars',1023)
  

def avancer():
  codo_move('forwars',1023)
  

def reculer():
  robot.set_motors_speed(-50, -50)


def stop_robot():
  robot.set_motors_speed(0, 0)
  

def detecter_presence():

  return ultrason.get_distance() <= distance_seuil

def detecter_ligne():
  
  return not ligne_gauche.get_line_detected() and not ligne_droite.get_line_detected()



ultrason = robot.ultrasonic_sensor()
ligne_gauche = robot.line_sensor_left()
ligne_droite = robot.line_sensor_right()

distance_seuil = 0.8

centre_distance = 0.4


while True:
  tourner_sur_place()
  if detecter_presence():
    stop_robot()
    avancer()
    while detecter_presence():
      time.sleep(0.1)
      
  if detecter_ligne():
    stop_robot()
    time.sleep(0.5)
    
    robot.set_motors_speed(-50, 50)
    
    time.sleep(1.8)
    
    stop_robot()
    avancer()
    time.sleep(centre_distance / 0.05)
    
    stop_robot()
  time.sleep(0.05)
  
