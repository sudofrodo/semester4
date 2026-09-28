temp = int(input("Please enter room temperature : "))
if temp >= 30:
	print("Fan is turned on. Temperature was " , temp , "deg C")
else:
	print("Fan is turned off. Temperature was " , temp , "deg C")

light = input("Please enter room light level (h or l) : ")
if light == 'h':
	print("Light is turned on. Light was low.")
else:
	print("Light is turned off. Light was high.")

