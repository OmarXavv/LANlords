RICH SHIELD LIBRARY
===================

This is the rich shield library providing code and examples for programming the rich shield.
The IR Remote sensor support is not included in this library. There is a great library available 
that you can use to program this sensor. You need to install a separate library for this sensor
as described below. The library include examples of how to use the sensor.

Infra Red Remote Sensor
-----------------------

You need to install the library "IRremote by shirriff" in order to use the IR Remote sensor.

* How to install the IRremote library:
In Arduino IDE, go to menu option 'Sketch -> Include Library -> Manage Libraries' and search 
for "irremote". The "IRremote by shirriff" will show up in the list. Install that library. 

* How to use the IRremote sensor:
Learn how to use the sensor from an example. 
In Arduino IDE, go to menu option 'File -> Examples -> IRremote -> IRrecvDemo'. 
There are more examples that illustrate the usage of the IRremote sensor. Many different IR 
remotes can be used. You need to set pin 2 for the rich shield in the example.

int RECV_PIN = 2;
IRrecv irrecv(RECV_PIN);
