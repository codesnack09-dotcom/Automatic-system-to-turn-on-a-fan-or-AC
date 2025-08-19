import time
import random

# Simulated temperature reading (replace with actual sensor code)
def get_temperature():
    # For simulation, random temperature between 25°C and 35°C
    return round(random.uniform(25.0, 35.0), 1)

# Function to control fan or AC
def control_cooling_system(temperature):
    if temperature > 30:
        print(f"Temperature: {temperature}°C - Turning ON the fan/AC...")
        # Code to activate relay would go here
        # Example: GPIO.output(RELAY_PIN, GPIO.HIGH)
    else:
        print(f"Temperature: {temperature}°C - Turning OFF the fan/AC...")
        # Code to deactivate relay
        # Example: GPIO.output(RELAY_PIN, GPIO.LOW)

# Main loop
try:
    while True:
        temp = get_temperature()
        control_cooling_system(temp)
        time.sleep(2)  # Wait 2 seconds before reading again

except KeyboardInterrupt:
    print("Program stopped by user.")
