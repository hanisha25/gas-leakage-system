import csv
import random

# Generate mock gas readings and labels
def generate_data(filename='mock_gas_data.csv', samples=500):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Gas Level', 'Status'])  # headers

        for _ in range(samples):
            gas_level = round(random.uniform(100, 1200), 2)

            if gas_level < 400:
                status = 'Safe'
            elif 400 <= gas_level < 700:
                status = 'Warning'
            else:
                status = 'Leak'

            writer.writerow([gas_level, status])

    print(f"{samples} rows of data saved to {filename}")

# Run the function
generate_data()
