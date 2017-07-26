import csv
import string

# Open the CSV File and read it in.
f = open('conference.csv')
data = f.read()

# Split the data into an array of countries.
elementsList = data.split('\n')

# print length of the list
length = len(elementsList)
# print the first element
print(elementsList[0])

# print the last element
print(elementsList[len(elementsList)-1])
# print all the elements
print(elementsList)

# Start your search algorithm here.
# Assume countryIwant is in the list of country names
countryIwant = input("Enter a name: ")

beginningIndex = 0
endingIndex = len(elementsList) - 1
index = int((endingIndex - beginningIndex) / 2)

while elementsList[index] != countryIwant:
    if countryIwant < elementsList[index]:
        beginningIndex = beginningIndex
        endingIndex = index
        index = int((endingIndex - beginningIndex) / 2) + beginningIndex
    elif countryIwant > elementsList[index]:
        beginningIndex = index + 1
        endingIndex = endingIndex
        index = int((endingIndex - beginningIndex) / 2) + beginningIndex
    else:
        print(index)

print(index)
