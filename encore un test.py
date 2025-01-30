from machine import Pin, PWM
import time
import utime

# Define motor pins
left_motor_forward = PWM(Pin(1))
left_motor_backward = PWM(Pin(2))
right_motor_forward = PWM(Pin(3))
right_motor_backward = PWM(Pin(4))

# Define sensors
black_line_left = Pin(8, Pin.IN)    # Left line detector
black_line_right = Pin(12, Pin.IN)  # Right line detector

# Grove Ultrasonic Sensor (assumes it's on Pin 0)
trigger = Pin(0, Pin.OUT)
echo = Pin(0, Pin.IN)

# Motor speed settings
MAX_SPEED = 1023
TURN_SPEED = 500
BACKWARD_SPEED = 400
BACKWARD_TIME = 0.5  # Time to move backward when line detected

# Function to measure distance
def get_distance():
    trigger.low()
    utime.sleep_us(2)
    trigger.high()
    utime.sleep_us(5)
    trigger.low()
    
    while echo.value() == 0:
        signal_off = utime.ticks_us()
    
    while echo.value() == 1:
        signal_on = utime.ticks_us()
    
    time_passed = signal_on - signal_off
    distance = (time_passed * 0.0343) / 2  # Convert to cm
    
    return distance

# Motor control functions
def move_forward(speed=MAX_SPEED):
    left_motor_forward.duty_u16(speed)
    right_motor_forward.duty_u16(speed)
    left_motor_backward.duty_u16(0)
    right_motor_backward.duty_u16(0)

def move_backward(speed=BACKWARD_SPEED):
    left_motor_forward.duty_u16(0)
    right_motor_forward.duty_u16(0)
    left_motor_backward.duty_u16(speed)
    right_motor_backward.duty_u16(speed)

def turn_in_place():
    left_motor_forward.duty_u16(TURN_SPEED)
    right_motor_backward.duty_u16(TURN_SPEED)
    left_motor_backward.duty_u16(0)
    right_motor_forward.duty_u16(0)

def stop_motors():
    left_motor_forward.duty_u16(0)
    right_motor_forward.duty_u16(0)
    left_motor_backward.duty_u16(0)
    right_motor_backward.duty_u16(0)

# Main loop
while True:
    distance = get_distance()
    line_left = black_line_left.value()
    line_right = black_line_right.value()

    if line_left == 1 or line_right == 1:  # If a black line is detected
        move_backward()
        time.sleep(BACKWARD_TIME)
        stop_motors()
    
    elif distance > 80:  # If no object detected
        turn_in_place()
    
    else:  # If an object is detected within 80cm
        move_forward(MAX_SPEED)
        time.sleep(1)  # Dash forward
        move_backward()
        time.sleep(0.5)
        stop_motors()
    
    time.sleep(0.1)  # Small delay to avoid excessive CPU usage
