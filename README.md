# Python-Cisco-BGP-Temperature-Sensor
Using temperature sensor to control BGP routing

Loop every 20 seconds
- Read DHT22 temperature sensor connected to Raspberry Pi.
- Convert temperature to whole number (integer).
- Telnet into Cisco switch.
- Use temperature value to configure BGP local-preference in route-map.
- Route-map affects routes learned from AS 200 only.

- When hot, traffic routes through AS 200 (LabSW2).
- When cold, traffic routes through AS 300 (LabSW3).
