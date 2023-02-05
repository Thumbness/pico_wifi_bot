import tkinter as tk
import serial
import time
import typing

ser = serial.Serial('COM5')  # open serial port
print(ser.name)         # check which port was really used
# line = ser.readline() 
# print(line)

def led_control() -> None:
    state = var.get().encode()
    ser.write(state)

## Main Function ##

#Show window
root = tk.Tk()
root.title("Ardunio_gui")

var = tk.StringVar()

# Call Arduino function
function_select_label = tk.Label(root, text="Function:")
function_select_label.pack()
# submit_button = tk.Button(root, text="Turn LED on", command=change_led)
on_button = tk.Radiobutton(root, variable=var, text="LED ON", value='A', command=led_control)
off_button = tk.Radiobutton(root, variable=var, text="LED OFF", value='B', command=led_control)
# submit_button.pack()
on_button.pack()
off_button.pack()

root.mainloop()
ser.close()   