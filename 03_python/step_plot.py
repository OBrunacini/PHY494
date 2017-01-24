# Heaviside step function

import matplotlib.pyplot as plt

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

tmax = 4
t, dt = -4, 0.5
x =[]
Theta = []

while t<= tmax:
	#print("time" + str(t))
	x.append(t)
	Theta.append(heaviside(t))
	t += dt


#heaviside(x)
print(x)
print(Theta)
#x = 3
#theta = heaviside(t)
#print("Theta(" + str(x) + ") = " + str(theta))

plt.plot(x, Theta, '-o', color="red", linewidth=2)
plt.show()