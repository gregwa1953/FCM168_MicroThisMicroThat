#======================================
# BMP180-OLED.py
#======================================
# Combined demo written by G.D. Walters
# code from various sources
# -------------------------------------
# Demonstrates how to use a BMP180 Temperature/Pressure/Altitude sensor and
# a SSD1306 OLED Display together on a Raspberry Pi Pico
# -------------------------------------
# Imports
# -------------------------------------
from bmp180 import BMP180
from time import sleep
from machine import I2C, Pin    # create an I2C bus object accordingly to the port you are using
from ssd1306 import SSD1306_I2C
import framebuf

# Set the Width of the OLED Display
WIDTH = 128
# Set the Height of the OLED Display
HEIGHT = 32

# Initialize the I2C object on Buss 0
# Physical Pins SCL - 12 SDA 11 (SCL GP9, SDA GP8)
bus = I2C(0)
# Init oled display
oled = SSD1306_I2C(WIDTH, HEIGHT, bus)

# Initialize the BMP180 Device
bmp180 = BMP180(bus)
bmp180.oversample_sett = 2
# bmp180.baseline = 101325
bmp180.baseline = 102032   # Modified for San Marcos Tx

# Clear the OLED Display
oled.fill(0)
# Send the header to the OLED
oled.text("BMP180 Demo",5,5)
oled.show()

# Start a forever loop getting and displaying the temperature
while True:
    # Get the temperature (centigrade)
    tempc = bmp180.temperature
    # Convert it to Farenheit
    tempf = tempc*9/5+32
    # Get pressure and altitude 
    p = bmp180.pressure
    # Add an offset for San Marcos
    p = (p * 0.0002953)+ 0.7
    altitude = bmp180.altitude
    # Convert meters to feet
    altitude = altitude * 3.28084
    
    print("Temp: {0:.2f}C TempF: {1:.2f} Pressure: {2:.2f}  Altitude {3}".format(tempc,tempf,p,altitude))
    
    oled.text("Temp: "+str(round(tempf, 2)), 5,23)
    oled.show()
    sleep(2)
    oled.text("Temp: "+str(round(tempf, 2)), 5,23,0)
    oled.show()    
