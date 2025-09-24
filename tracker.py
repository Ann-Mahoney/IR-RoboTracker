import RPi.GPIO as GPIO
import time
IN1, IN2, IN3, IN4 = 17, 18, 22, 23

GPIO.setmode(GPIO.BCM)
for pin in (IN1, IN2, IN3, IN4):
    print("I am running on line 7...")
    GPIO.setup(pin, GPIO.OUT)
    
def forward():
    print("Moving forward....")
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)

    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW) 
     
def backward():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)
    
def stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW) 
      
      
try:
    forward()
    time.sleep(2)
    stop()
    GPIO.cleanup()
except KeyboardInterrupt:
    GPIO.cleanup()