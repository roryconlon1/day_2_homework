users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)

users["Jonathan"]["twitter"]

# 2. Get Erik's hometown

users["Erik"]["home_town"]

# 3. Get the list of Erik's lottery numbers

users["Erik"]["lottery_numbers"]

# 4. Get the species of Avril's pet Monty

users["Avril"]["pets"][0]["species"]
# 0 as the full list is a dictionary

# 5. Get the smallest of Erik's lottery numbers

min(users["Erik"]["lottery_numbers"])
#could also use variable to define the string of numbers
#then use sort to order them, sort always uses low to high, even alphabetiacally, if want opposite do reverse = true
#then extract the 0 index

# 6. Return an list of Avril's lottery numbers that are even

for num in users["Avril"]["lottery_numbers"]:
  if num % 2 == 0:
    print(num, end=" ")
  
  #avril_numbers = users["Avril"]["lottery_numbers"]
  #even_numbers = []  # need to make a new empty list to store the new list of just even
# for number in avrils_number:
#   if number % 2 == 0:
#     even_numbers.append(number)  # all numbers passed through from avrils_number variable and all that have remainder 0 when divided by 2 are added to even_numbers list
# make sure if print, is outside the loop!!

# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers

users["Erik"]["lottery_numbers"].append(7)

# 8. Change Erik's hometown to Edinburgh

users["Erik"]["home_town"] = "Edinburgh"

# 9. Add a pet dog to Erik called "fluffy"

users["Erik"]["pets"] = [{
  "dog" : "fluffy"    # this would replace everything already in erik pets
}]

#users["Erik"]["pets"].append({"name : fluffy", "species : dog"})

# 10. Add another person to the users dictionary

users["Rory"] = {"lottery_numbers" : [1, 2, 3, 4, 5, 6]}
