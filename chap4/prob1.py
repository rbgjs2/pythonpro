import random

mood = random.randrange(5)

print("I sense your energy. Your true emotions are coming across myscreen.")
print("You are...")

if mood == 0:
  # happy
  print("------------")
  print("|          |")
  print("| 0     0  |")
  print("|    <     |")
  print("|          |")
  print("| \      / |")
  print("|  \    /  |")
  print("|   ....   |")
  print("------------")
elif mood == 1:
  # sad
  print("------------")
  print("|          |")
  print("| @     @  |")
  print("| |  <  |  |")
  print("|          |")
  print("|  =====   |")
  print("|          |")
  print("|          |")
  print("------------")
elif mood == 2:
  # neutral
  print("------------")
  print("|          |")
  print("| 0     0  |")
  print("|   <      |")
  print("|          |")
  print("|  -----   |")
  print("|          |")
  print("|          |")
  print("------------")
elif mood == 3:
  # suprised
  print("------------")
  print("|  ^   ^   |")
  print("|  @   @   |")
  print("|          |")
  print("|   <      |")
  print("|   ...    |")
  print("|  .   .   |")
  print("|   ...    |")
  print("------------")
elif mood == 4:
  # angry
  print("------------")
  print("|...   ... |")
  print("| o     o  |")
  print("|   <      |")
  print("|          |")
  print("|  -----   |")
  print("|  -----   |")
  print("|          |")
  print("------------")
print("...today.")
print("")
print("Press the enter key to quit.")

