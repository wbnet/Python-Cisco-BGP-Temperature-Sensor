import time
import board
import adafruit_dht

import getpass
import telnetlib

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4)

while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])


    myTemp = temperature_c
    # myTemp = myTemp - 20
    print(myTemp)

    myTemp = round(myTemp)
    print(myTemp)

    myTemp = int(myTemp)
    print(myTemp)

    # Configure BGP on Cisco switch

    HOST = "10.10.10.10"
    # user = input("Enter your username: ")
    # password = getpass.getpass()

    user = "dave"
    password = "MyPass"
    # myTemp = 10

    tn = telnetlib.Telnet(HOST)

    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")

    # tn.write(b"show interfaces description | include up\n")

    tn.write(b"conf t\n")
    tn.write(b"route-map rm_as_200_in\n")

    # tn.write(b"set local-preference 20\n")

    # tn.write(b"set local-preference {0}\n".format(temperature))
    # Error "AttributeError: 'bytes' object has no attribute 'format'"

    myConfig = "set local-preference %s\n" % myTemp
    # myBytes = myConfig.encode('utf-8')
    myBytes = myConfig.encode()

    # tn.write(b"%s" % myConfig)
    tn.write(b"%s" % myBytes)

    tn.write(b"end\n")
    tn.write(b"clear ip bgp * soft\n")

    # tn.write(b"show route-map\n")
    # tn.write(b"show ip bgp\n")

    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))

    time.sleep(20.0)
