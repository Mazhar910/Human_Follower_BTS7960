import RPi.GPIO as GPIO
import time

class Driver:
    def __init__(self, RPWM, LPWM, L_EN, R_EN):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        self.R_EN = R_EN
        self.L_EN = L_EN
        self.RPWM = RPWM
        self.LPWM = LPWM

        GPIO.setup(self.RPWM, GPIO.OUT)
        GPIO.setup(self.LPWM, GPIO.OUT)
        GPIO.setup(self.L_EN, GPIO.OUT)
        GPIO.setup(self.R_EN, GPIO.OUT)
        GPIO.output(self.R_EN, True)
        GPIO.output(self.L_EN, True)
        self.rpwm = GPIO.PWM(self.RPWM, 100)
        self.lpwm = GPIO.PWM(self.LPWM, 100)
        self.rpwm.ChangeDutyCycle(0)  # For forward rotation
        self.lpwm.ChangeDutyCycle(0)  # For backward rotation
        self.rpwm.start(0)
        self.lpwm.start(0)

    def stop(self):
        self.lpwm.ChangeDutyCycle(0)
        self.rpwm.ChangeDutyCycle(0)
          
    def left_forward(self):
        self.rpwm.ChangeDutyCycle(75) 
    
    def right_forward(self):
        self.rpwm.ChangeDutyCycle(80)
    
    def reverse(self):
        self.lpwm.ChangeDutyCycle(60)

if __name__ == "__main__":
    driver1=Driver(19,26,20,21) #left
    driver2=Driver(9,27,10,11) #right
    
    #driver1.left_forward()
    #driver2.right_forward()
    
    driver1.stop()
    driver2.stop()
