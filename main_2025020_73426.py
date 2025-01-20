


from microbit import *

def tourner_sur_place():
  codo_move('right',1023)
  

def avancer():
  codo_move('forwars',1023)
  




def stop_robot():
  codo_move('stop')
  



def detecter_ligne():
   #a faire




distance_max = 0.8

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
    
    stop_robot()
    avancer()
    time.sleep(centre_distance / 0.05)
    
    stop_robot()
  time.sleep(0.05)
  
