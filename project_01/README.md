# Exercise Tracker

## Introduction
This repository provides the code needed to run the Exercise Tracker on the PocketBeagle.  For more information on the Exercise Tracker and setting up the hardware, please visit the [hackster.io](https://www.hackster.io/kiansamra/exercise-tracker-2aaf67) page.

## Setting Up the PocketBeagle
Download the [image file](bone-debian-10.11-iot-armhf-2022-02-03-4gb.img.xz).
With a programmable SD card inserted into your PocketBeagle, use an SD card flasher like [Etcher](https://etcher.balena.io/) to flash the PocketBeagle with the file.

## Dependencies
* Python Package Manager (PIP)
* Adafruit BBIO library

### Follow the instructions below to install these dependencies
Run the following shell commands in your terminal window
* Update the Linux Advanced Package Tool (apt) and install the Build-Essential package
```sh
  sudo apt-get update
  sudo apt-get install build-essential python-dev python setuptools python-smbus -y
 ```
 * Installing pip
 Install the version compatible with your version of python (version 2.x.x vs version 3.x.x)
 ```sh
 sudo apt-get install python-pip -y
 sudo apt-get install python3-pip -y
 ```
 * Install zip
 ```sh
 sudo apt-get install zip
 ```
* Install the required Adafruit libraries
```sh
sudo pip3 install --upgrade setuptools
sudo pip3 install --upgrade Adafruit_BBIO
```

## Installing the Software
Create a new directory where you want to install the software files for the Exercise Tracker from this github repository.  cd into the new directory you created and then enter the following command (make sure to change chosen_directory to your directory path)
```sh
debian@beaglebone: /var/lib/cloud9/chosen_directory$ git clone https://github.com/kiansamra/ENGI301/tree/main/project_01
```

## Usage
The tracker will run when the PocketBeagle is powered on. The switch on the breadboard must be flicked on (to the side away from the pullup resistor) to initiate tracking.  The tracker can also be run from the Cloud9 IDE with the following command (make sure to change chosen_directory to your directory path)
```sh
debian@beaglebone:/var/lib/cloud9/chosen_directory$ ./sudo run
```
