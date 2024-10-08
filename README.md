# KlipperScreen-Encoder-Driver
[![CC BY 4.0][cc-by-shield]][cc-by]

A driver to allow the use of KlipperScreen on printer screens with a builtin encoder and no touchscreen.

Originally designed for [this Anycubic Kobra screen driver](https://github.com/jokubasver/Anycubic-Kobra-Go-Neo-LCD-Driver)

# Setup

## Hardware
![SW: 22, A: 27, B: 17](https://github.com/wil-sys/KlipperScreen-Encoder-Driver/blob/main/img/GPIOEnc.png?raw=true)
The default pin mapping is 
```
Switch -> GPIO 22
Encoder A -> GPIO 27
Encoder B -> GPIO 17
```

## Software
Ensure that you have evdev installed on your system by running 
```
sudo python3 -m pip install evdev
```
Clone the repository into your home folder
```
cd ~
git clone https://github.com/SomeSpaceNerd/KlipperScreen-Encoder-Driver.git
```
Create a systemd service file to run the script at startup

First create the file
```
sudo nano /etc/systemd/system/EncoderMouse.service
```

Then put the following contents into it  
(Note you may need to change the directoy of either the repository, python3, or both)
```
[Unit]
Description=Encoder Mouse emulator Service
After=multi-user.target

[Service]
ExecStart=/usr/bin/python3 /home/pi/KlipperScreen-Encoder-Driver/EncoderMouse.py
WorkingDirectory=/home/pi/KlipperScreen-Encoder-Driver/
StandardOutput=inherit
StandardError=inherit
Restart=always
StartLimitBurst=500
StartLimitIntervalSec=0

[Install]
WantedBy=multi-user.target
```
Then hit ctrl+X, Y, then enter to exit the editor.

Run the following three commands to setup and run the service 
```
sudo systemctl daemon-reload
sudo systemctl enable EncoderMouse.service
sudo systemctl start EncoderMouse.service
```

Ensure that the service is running
```
sudo systemctl status EncoderMouse.service
```

At this point you will probably not see a mouse cursor on KlipperScreen, if you don't, add the following line to your klipperscreen.conf
```
show_cursor: True
```
# Usage
Use the encoder knob to move the mouse depending on the mode.
You can switch between X and Y mode by pressing the button momentarily.
You can left click by holding the button for as long as the hold_time is set in the python script.

# Footer
This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
