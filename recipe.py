ingredient_amount={ \
"green pepper":"1", \
 "red pepper":"1", \
 "onion":"2",\
 "spices curry":"20g",\
 "tomato sauce":"two boxes",\
 "spaghetti noodles":"a large tray",\
 "oil":"little"\
 }

ingredient_directions ={ \
 "green pepper":"chop", \
  "red pepper":"chop", \
  "onion":"chop",\
  "spices curry":"sprinkle",\
  "tomato sauce":"open",\
  "spaghetti noodles":"without breaking, boil",\
  "oil":"add to water"\
}

for ingredient, amount in ingredient_amount.items():
     print(ingredient_directions[ingredient] + " " +  amount + " " + ingredient)
