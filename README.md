# This uses Python with a simulated temperature sensor (such as DHT11/DHT22) and a Relay module to control a fan or AC.

## How it works:
- get_temperature() — Here I simulated the temperature with random numbers, but in real life you’d connect a DHT11, DHT22, or other temperature sensor and read from it.
- control_cooling_system() — Checks if temperature > 30°C, then prints the action (and in real use, it will trigger the relay to turn on/off your fan or AC).
- Loop — Reads the temperature every 2 seconds and updates the fan/AC status.

## 💡 If you want to run it on Raspberry Pi or Arduino:
- Replace get_temperature() with actual sensor reading code.
- Replace the print() commands for ON/OFF with GPIO commands to control a relay module.
  
## Support Me
If you find this project useful, you can support me on [ko-fi.com](https://www.ko-fi.com/codesnack).
