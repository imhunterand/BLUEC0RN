# BLUEC0RN
BLUEC0RN CLI tool to hack Bluetooth devices via speaker jamming, traffic spoofing &amp; device hijacking
- Opensource python tool for jamming bluetooth signals (in the making)
- Successful in jamming bluetooth speakers
- Does not work on Airpods or any other bluetooth devices yet ...

## Tool Preview
![image](https://github.com/imhunterand/BLUEC0RN/assets/109766416/63248b4e-cd6f-4d4f-9ecf-975a5f6b92db)


## Installation

1. Clone the repo and install basic requirements
```
git clone https://github.com/imhunterand/BLUEC0RN.git
cd BLUEC0RN
pip3 install -r requirements.txt
```
2. Install necessary packages
```
paru -Sy --noconfirm --needed bluez bluez-utils
```
## Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file:

```plaintext
.env 
```
keep the .env file under `/utils`.

## Table of Contents
1. Working of Bluetooth
2. Security Risks
3. Security Tips for Using Bluetooth
4. Applications Used
5. Malicious Attack
6. Attack Detection
7. Prevention Method
8. How AirPods Block Requests from Devices
