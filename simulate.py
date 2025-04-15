import random
import time

def simulate_gas_reading():
    # Randomly simulate gas levels in ppm (parts per million)
    return random.uniform(100, 1200)

# Test: Print simulated readings every 2 seconds
if __name__ == "__main__":
    while True:
        gas_level = simulate_gas_reading()
        print(f"Gas Level: {gas_level:.2f} ppm")
        time.sleep(2)
