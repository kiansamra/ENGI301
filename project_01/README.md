# Exercise Tracker

## Introduction
This repository provides the code needed to run the Exercise Tracker on the PocketBeagle.  For more information on the Exercise Tracker and setting up the hardware, please visit the [hackster.io](https://www.hackster.io/kiansamra/exercise-tracker-2aaf67) page.

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

## Usage
## Usage
The tracker will run when the PocketBeagle is powered on. The switch on the breadboard must be flicked on (to the side away from the pullup resistor) to initiate tracking.  The tracker can also be run from the Cloud9 IDE with the following commands
```sh
debian@beaglebone:/var/lib/cloud9/ENGI301/python/project_01$ ./run
```
