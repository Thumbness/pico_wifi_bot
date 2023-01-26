import network
import socket
from time import sleep
from picozero import pico_temp_sensor, pico_led
import machine

### To Do: ###
# Create GUI that allows PICO to scan for access points and for user to select SSID and input SSID PW
# Research into how to flash code to PICO, such that GUI runs on Boot


def get_wifi_cred():
    with open("user_network_authentication_check.txt", "r") as f:
        line = f.readline()
        line = line.split() 
        ssid = line[0]
        WPA2 = line[1]
    return ssid, WPA2

def connect(ssid, WPA2):
    #Connect to WLAN
    print(ssid, WPA2)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, WPA2)
    print(wlan.ifconfig())
        
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
        
    pico_ip = wlan.ifconfig()[0]
    print(f'connected on {pico_ip}')
    return pico_ip

def open_socket(pico_ip):
    address = (pico_ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    print(connection)
    return connection

def webpage(temperature, state):
    #Template HTML
    html = f"""
            <!DOCTYPE html>
            <html>
            <body>
                <form action="./lighton">
                    <input type="submit" value="Light on" />
                </form>
                <form action="./lightoff">
                    <input type="submit" value="Light off" />
                </form>
                <p>LED is {state} </p>
                <p>Temperature is {temperature}</p>
            </body>
            </html>
            """
    return str(html)

def serve(connection):
    #Start a web server
    state = 'OFF'
    pico_led.off()
    temperature = 0
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        try:
            request = request.split()[1]
        except IndexError:
            pass
        if request == '/lighton?':
            pico_led.on()
            state = 'ON'
        elif request == '/lightoff?':
            pico_led.off()
            state = 'OFF'
        temperature = pico_temp_sensor.temp
        print(request)
        html = webpage(temperature, state)
        client.send(html)
        client.close()
        
def main():
    try:
        ssid, WPA2 = get_wifi_cred()
        pico_ip = connect(ssid, WPA2)
        connection = open_socket(pico_ip)
        serve(connection)
        
    except KeyboardInterrupt:
        machine.reset()

if __name__ == '__main__':
    main()

