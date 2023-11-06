import serial
import time
from tieui import TieUi

import serial.tools.list_ports

# Get a list of all available serial ports
ports = serial.tools.list_ports.comports()

# Print the names of the serial ports
for port in ports:
    print(f"Serial Port: {port.device}")

tie = TieUi(app_name="xHoUSKCV4NZ9DExW5MWHCo3B6ay1")

# Create empty lists to store the x (timestamps) and y (sensor values) data for the line chart
x_data = []
y_data = []

# Define the maximum number of data points to display
max_data_points = 25

# Define the line chart component
line_chart_settings = {
    "title": "Moisture Sensor Data Over Time",
    "chartSeries": [
        {"name": "Moisture Level", "data": y_data, "color": "#0077B6", 'categories': x_data },
    ],
    "categories": x_data
}
line_chart_component = tie.lineChart(line_chart_settings)
tie.add(line_chart_component)

# Define the serial port and baud rate
ser = serial.Serial('/dev/cu.usbmodem14101', baudrate=57600)  # Replace with your actual serial port

# Function to handle button click
def handle_button_click(item):
    ser.write(b"Move\n")  # Send "Move" command to Arduino
    tie.components[0]['settings']['chartSeries'][0]['data'] = y_data  # Update the chart (optional)
    tie.liveUpdate()

# Add a button to send the "Move" command
tie.add(tie.button({"id": "move-button", "label": "Move", "variant": "outlined"}, handle_button_click))

try:
    counter = 0
    while True:
        # Read data from the serial port (assuming it's a single numeric value)
        data = ser.readline().decode('utf-8').strip()  # Assuming the data is UTF-8 encoded
        
        # Add a timestamp (current time) to the x_data list
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        counter = counter + 1
        x_data.append(counter)
        
        # Convert the received data to float (assuming it's a numeric value)
        sensor_value = float(data)
        
        # Append the sensor value to the y_data list
        y_data.append(sensor_value)

        # Limit the number of data points to max_data_points
        if len(y_data) > max_data_points:
            x_data.pop(0)
            y_data.pop(0)

        # Update the line chart component in the TIE UI
        print(tie.components[0]['settings']['chartSeries'])
        tie.components[0]['settings']['chartSeries'][0]['data'] = y_data
        tie.components[0]['settings']['categories'] = x_data  # Update x-axis data
        tie.liveUpdate()

        # Wait for 1 second before reading again (adjust as needed)
        time.sleep(1)

except KeyboardInterrupt:
    # Close the serial port when the user interrupts the program (Ctrl+C)
    ser.close()
