def process_sensor_data(sensor):
    while True:
        data = sensor.get_data()
        if data:
            yield data

# Example usage
sensor = Sensor()
for data in process_sensor_data(sensor):
    # Analyze sensor data
    pass
