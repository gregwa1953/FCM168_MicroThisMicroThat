# i2cscan.py
# Searches the i2c bus for i2c devices

import machine
sda = machine.Pin(8)
scl = machine.Pin(9)
i2c=machine.I2C(0,sda=sda,scl=scl,freq=400000)
devices=i2c.scan()
if devices:
    for dev in devices:
        print(hex(dev))
