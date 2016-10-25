#! /usr/bin/python

cars = 100
drivers = 30 
spaceInCar = 4.0
passengers = 90
carsNotDriven = cars - drivers
carsDriven = drivers
carpoolCapacity = cars * spaceInCar
avgPassengerPerCar = passengers / carsDriven

print "Total", cars, " cars are Available"
print drivers, " drivers have joined"
print carsDriven, " cars are available for passengers"
print "In a car, ", avgPassengerPerCar, ", passengers will be accomodated"


