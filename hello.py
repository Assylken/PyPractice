import abc


def get(rem, var=''):
	if len(rem) == 0:
		print(var)
	for i in range(len(rem)):
		var2 = var + rem[i]
		rem2 = rem[0:i] + rem[i+1:]
		get(rem2, var2)
s = input()
get(s)