#list is a collection of objects or strings or numbers and contained with []
foosballers = [ "Mia",
  "Retta",
  "Augustine",
  "Jin",
  "Waylon",
  "Alphonso",
  "Sage",
  "Hubert",
  "Raymon",
  "Rebecca",
  "Monty",
  "Glen",
  "Christi",
  "Patrice",
  "Craig",
  "Dexter",
  "Wally",
  "Ian",
  "Pat"]
print(foosballers)
# Get the median player-- That is, the player exactly in the middle of the league (hint: You can get the total number of
# players with `len(foosballers)` and then divide that number by 2; You may want to use integer division (see: Numbers
# section) for this calculation).
numplayers = len(foosballers)
print(numplayers)
medianplayer = foosballers[int(numplayers/2)]
print(medianplayer)

# Get the five players in the middle of the league-- That is, in addition to the median player, also get the players
# two above and the two below.

print(foosballers[7:12])

# Add a fake player, called "Average Player," to the exact middle of the list, to show clearly who is above
# and below average

foosballers.insert(9, 'Average Player')
print(foosballers)

# Actually, that's not obvious enough. Find "Average Player," and change their name to uppercase: "AVERAGE PLAYER."
# That'll stand out.
foosballers[9] = 'AVERAGE PLAYER'
print(foosballers)

#Add five more players with names of your choosing, to the bottom of the list-- They are unranked and
# we must therefore assume they are terrible.
newfoosball = ['Chris', 'John', 'Corey', 'Tom', 'Henk']
foosballers = foosballers+newfoosball
print(foosballers)

#Oh no-- Now "AVERAGE PLAYER" is no longer in the middle! Find a way to fix this
del foosballers[9]
print(foosballers)
median = len(foosballers)//2
foosballers.insert(median,"AVERAGE PLAYER")
print(foosballers)

#"""Five more players show up, but they are ranked. Insert them at the appropriate location:
# - Lacy is one spot ahead of Hubert
# - Omar is one spot behind Rebecca
# - Otto is 8th best in the league
# - Chauncey is 10 spots from the bottom of the league
hubertindex = foosballers.index("Hubert")
print(hubertindex)
foosballers.insert(hubertindex, 'Lacy')
rebeccaindex = foosballers.index("Rebecca")
foosballers.insert((rebeccaindex+1),'Omar')
foosballers.insert(7,'Otto')
foosballers.insert(-10, 'Chauncey')
print(foosballers)