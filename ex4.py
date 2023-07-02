import math

a = float(input("Edge length: "))

surface = round(pow(a,2) * math.sqrt(3),4)
volume = round(pow(a,3) / 12 * math.sqrt(2),4)
height = round(a / 3 * math.sqrt(6),4)

print ("Surface:",surface)
print ("Volume:",volume)
print ("Height:",height)

