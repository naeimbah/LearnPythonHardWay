#Defining the values of the variables:
cars = 100
space_in_car = 4.0
drivers = 30.0
passengers = 90

cars_idle = cars - drivers
cars_driven = drivers

#Now doing some calculations on the variables:
carpool_capacity = cars_driven * space_in_car
avg_occupancy = carpool_capacity / cars

# We can put strings and values and then followed by strings easily:
print "There are cars", cars, "available"
print "There are drivers:", drivers, "who are working"
print "idle cars = ", cars_idle, "sitting"
print "Space in each car", space_in_car
print "people transported ", carpool_capacity, "by carpool is substantial"
print "Average occupancy: ",avg_occupancy," in plying car"
