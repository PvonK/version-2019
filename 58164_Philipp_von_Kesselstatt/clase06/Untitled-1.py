from Cafe import Premium

coffee = Premium()
coffee.sensores(500, 500, 500, 500, 500)
coffee.sensor_vaso(True)

print(coffee.cafePremium(5, True, True))