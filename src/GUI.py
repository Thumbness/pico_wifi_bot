import tkinter as tk
from tkinter import messagebox
import subprocess

def scan_for_networks():
    # Use subprocess library to scan for Networks
    output = subprocess.check_output(["netsh", "wlan", "show", "networks"])
    print(output)

    #Clean up SSID output
    output = output.decode("utf-8")
    print(output)

    #Store network SSID's in a list to select from
    ssid_list = []
    for line in output.split("\n"):
        if "SSID" in line:
            ssid_list.append(line.split(":")[1].strip())
    return ssid_list

def on_ssid_select(event):
    selection = listbox.curselection()
    if len(selection) == 0:
        return
    ssid = listbox.get(listbox.curselection()[0])
    messagebox.showinfo("Selected SSID", f"You selected: {ssid}")
    global selected_ssid
    selected_ssid = ssid
    ssid_entry.insert(0, selected_ssid)

def on_WPA2_submit():
    password = password_entry.get()
    if password:
        user_confirm = messagebox.askquestion("Authenticating", "Connect to " + selected_ssid + "?")
        if user_confirm == "yes":
            with open("user_network_authentication_check.txt", "w") as file:
                network_input = str(selected_ssid + ", " + password)
                file.write(network_input)
                root.destroy()
        else:
            ssid_entry.delete(0)
    else:
        messagebox.showerror("Error", "Please enter a password")


## Main Function ##

#Show window
selected_ssid = ''
root = tk.Tk()
root.title("Select Network")
menu_label = tk.Label(root, text="Select a network")
menu_label.pack()

# Show list of available ssid_list and user can click
listbox = tk.Listbox(root)
listbox.pack()
ssid_list = scan_for_networks()
for network in ssid_list:
    listbox.insert("end", network)
listbox.bind("<Button-1>", on_ssid_select)

#SSID selection
ssid_label = tk.Label(root, text="SSID:")
ssid_label.pack()
ssid_entry = tk.Entry(root, show=selected_ssid)
ssid_entry.pack()

# Password input GUI
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()
submit_button = tk.Button(root, text="Submit", command=on_WPA2_submit)
submit_button.pack()

root.mainloop()