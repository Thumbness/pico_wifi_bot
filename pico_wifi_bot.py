import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine

ssid = 'Sherwizzle'
WPA2 = 'tofuopie8'



def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    networks = wlan.scan() 
    print("Available networks:\n")
    for line in networks:
        print(line[0].decode())
        wlan.connect(ssid, WPA2)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    pico_ip = wlan.ifconfig()[0]
    print(f'connected on {pico_ip}')
    return pico_ip
        
try:
    connect()
except KeyboardInterrupt:
    machine.reset()
    

