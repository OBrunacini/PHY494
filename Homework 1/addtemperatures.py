def convert_temperature(temperature, scale):
	if scale == 'F':
		return 'K', (temperature - 32)*(5/9) + 273
	elif scale == 'K':
		return 'F', (temperature - 273.15)*(9/5) + 32

scale = input('(F) or (K)?')
given_temp = int(input('What is the given temperature:'))
y = convert_temperature(given_temp, scale)
print(given_temp, "degrees", scale, "is", y, "degrees")
print(given_temp + int(y))


#theta =  int(input("Enter a temperature in F: "))
#T = int(input("Enter a temperature in Kelvin: "))

#for theta in T:
#	T = (theta - 32) * (5/9) + 273.15
#	print(T+theta)
#print("conversion complete")
