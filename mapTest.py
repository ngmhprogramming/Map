print("+-----+\n")
print("|MAP|\n")
print("+-----+\n")
print("Welcome to the Map module test file! This file will teach you everything you need to use the map module. I hope it comes in handy!\n")
print("Import the map module:\n")
print("from map import *\n")
from map import *
print("Import the random module:\n")
print("from random import *\n")
from random import *
print("Create a map:\n")
print("park = Map(\"City Park\", \"The Park in the city of TOOM\", 15, 15)\n")
park = Map("City Park", "The Park in the city of TOOM", 15, 15)
print("Randomly generate 200 blocks of  grass:\n")
print("for times in range(200):\n")
print("    park.update(randint(1, 15), randint(1, 15), \"Grass\")\n")
for times in range(200):
    park.update(randint(1, 15), randint(1, 15), "Grass")
print("Randomly generate 20 flowers:\n")
print("for times in range(20):\n")
print("    park.update(randint(1, 15), randint(1, 15), \"Flowers\")\n")
for times in range(20):
    park.update(randint(1, 15), randint(1, 15), "Flowers")
print("Generate 5 fountains:\n")
print("park.update(8, 8, \"Fountain\")\n")
print("park.update(4, 4, \"Fountain\")\n")
print("park.update(4, 12, \"Fountain\")\n")
print("park.update(12, 4, \"Fountain\")\n")
print("park.update(12, 12, \"Fountain\")\n")
park.update(8, 8, "Fountain")
park.update(4, 4, "Fountain")
park.update(4, 12, "Fountain")
park.update(12, 4, "Fountain")
park.update(12, 12, "Fountain")
print("What's at x: 8, y:8?:\n")
print("print(park.location(8,8))\n")
print(park.location(8,8))
print("How many locations are there?:\n")
print("print(park.total())\n")
print(park.total())
print("What are the unique locations?:\n")
print("print(park.locations())\n")
print(park.locations())
print("Can I have a plain map?:\n")
print("print(park.show(\"P\"))\n")
print(park.show("P"))
print("Can I have a map with a border?:\n")
print("print(park.show(\"B\"))\n")
print(park.show("B"))
print("Can I have a map which is in a grid with a border?:\n")
print("print(park.show(\"G\"))\n")
print(park.show("G"))
