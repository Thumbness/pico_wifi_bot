# pico_wifi_bot
## A small robot/toy that can be controlled via a small browser app using MQTT

## What is it?
This project is dedicated towards learning/implementing a wide aspect of technologies.
It will be a small robot that has limited amount of actions that can be called via a web browser app

## Purpose
Learning the fundamental basics of IoT.
We're hoping to get just the basic functionality of the bot working, nothing too special for now.

  ## Current implementation idea:
  - 5 event driven functions that will action the bot (arms, body, LED's)
  - basic website that can 'publish' an enumeration of chars/ints that an MQTT or similar server will listen for,
  - PICO_bot will wait for MQTT server to publish char/int to PICO
  - Pico_bot performs function (action) correlating with received case 

# Things to learn:
## Fundamentals for RPi Pico
- Programming (flashing?) a pico via serial connectivity 
- pico WIFI connectivity (socket connectivity could come in handy for browser API calls)
- MQTT implementation (publish/subscribe)
- #How to do anything

## Hosting a basic website
- learning Django for creating basic website (nothing flashy)
- Host site on a server (potential for learning/utilising AWS free tier - EC2 instance for website)
- Basic HTML containing pico_bot movement function calls via MQTT api calls

## For later....
- Create a small tkinter GUI that the user can create a "sequence" of actions for the robot to perform
- More functionality for the bot (LED screen for eyes (user could draw a face and print to screen??) #idea

## Things to think about
There's a chance that i may not need to host a seperate MQTT server to listen for web-app signals, but for the purpose of learning

# Learning Resources:
- https://projects.raspberrypi.org/en/projects/get-started-pico-w/1
