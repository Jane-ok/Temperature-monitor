from w1thermsensor import W1ThermSensor

identity = { "0b23569a0c5c": "sensor_1", "0b23569be4b9" : "sensor_2", "0b2356cecbad" : "sensor_3"}
result_temp = {}

for sensorID in identity:
    for sensor in W1ThermSensor.get_available_sensors():
        if sensorID in sensor.id:
            result_temp[identity[sensorID]] = str(round(sensor.get_temperature(), 1))

print(result_temp)
