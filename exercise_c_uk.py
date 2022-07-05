#from tkinter.font import names


from ast import Num
import numbers
from optparse import Values


united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

# 1. Change the capital of Wales from `"Swansea"` to `"Cardiff"`.

united_kingdom[1][2] = "Cardiff"

# 2. Create a dictionary for Northern Ireland and add it to the `united_kingdom` list (The capital is Belfast, and the population is 1,811,000).

Northern_Ireland = {
  "name" : "Northern Ireland",
  "population" : 1811000,
  "capital" : "Belfast"
  } 
dictionary_copy = Northern_Ireland.copy()
united_kingdom.append(dictionary_copy)

# 3. Use a loop to print the names of all the countries in the UK.

for country in united_kingdom:
  print(country["name"])

# 4. Use a loop to find the total population of the UK.


#  #counter = 0 

for amount in united_kingdom:
    amount["population"]



print(amount["population"])
