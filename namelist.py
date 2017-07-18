
import csv
import string

# Open the CSV File and read it in.
f = open('countries.csv')
data = f.read()

# Split the data into an array of countries.
countries = data.split('\n')
length = len(countries)


# Start your search algorithm here.
#location is the country we give it
#countries is the list of countries
#def countries(countries, location):
#    first = 0
#    last = len-1
#    mid = (first + last) / 2
#    if location > mid:
#        for i in range(len(countries)):

location = input("Enter a country: ")
def country(countries, location):
    first = 0
    last = len(countries)-1
    found = False
    while first<=last and not found:
        midpoint = (first + last)//2
        if countries[midpoint] == location:
            found = True
            print("found")
        else:
            if location < countries[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    if found == False:
        print("Not found")

country(countries, location)



#    first = midpoint + 1
#    last = len - 1
#    mid = (first + last) / 2
