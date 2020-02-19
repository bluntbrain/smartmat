from datetime import datetime
print("Smart Doormat V1.0")

weight = input()
yogesh = 86
chetan = 90

if (weight == yogesh):
	print("Hi Yogesh! How are you doing today")
elif (weight == chetan):
	print("Hi Chetan! How are you doing today")
print("Weight ="+ str(weight))
print("Data pushed to cloud!!")

timestamp = 1545730073
dt_object = datetime.fromtimestamp(timestamp)
print("dt_object ="+ str(dt_object))
print("type(dt_object) ="+ str(type(dt_object)))
