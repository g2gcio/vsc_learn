# Your solution appears to be looping over the wrong thing:
#
# for number_of_places in fraser:
# For 9 places, this turns out be something like:
#
# for "9" in "3.141592653589793":
# Which loops three times, one for each "9" found in the string. We can fix your code:

from math import pi

fraser = str(pi)

length_of_pi = []

number_of_places = 12
# number_of_places = int(raw_input("Enter the number of decimal places you want: "))

for places in range(number_of_places + 1):  # +1 for decimal point
    length_of_pi.append(str(fraser[places]))

print ("".join(length_of_pi))
