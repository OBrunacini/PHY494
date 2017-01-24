# Heaviside step function

def heaviside(x):
	"""Heaviside Step Function"""

	theta = None
	if x < 0:
		theta = 0.
	elif x == 0:
		theta = 0.5
	else:
		theta = 1.
		
	return theta

x = 3
theta = heaviside(x)
print("Theta(" + str(x) + ") = " + str(theta))