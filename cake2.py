import math

def getNumberOfSlices(radius, height, volumeOfSlice):
    volume = height * (radius**2) * math.pi
    numberOfSlices = volume / volumeOfSlice
    return int(numberOfSlices)

numberOfSlices1 = getNumberOfSlices(10,10,100)
print(numberOfSlices1)