import random

count = 1
herohp = random.randrange(50,101)
monsterhp = random.randrange(50,101)
print("hero HP:", herohp, ", monster HP:", monsterhp)
while herohp > 0 or  monsterhp > 0:
  heroattck = random.randrange(-10,20)
  monsterattck = random.randrange(-10,20)
  herohp = herohp - monsterattck
  monsterhp = monsterhp - heroattck
  print("hero HP: ", herohp, ", heroattck:", heroattck, end = '')
  if heroattck > 0:
    print("success", end = '')
  else:
    print("fail", end = '')
  print("<-> monster(HP:", monsterhp, ", attck:", monsterattck, end = '')
  if monsterattck > 0:
    print("success")
  else:
    print("fail")
  count += 1
print("-----------------------------------")
print("Total phase:", count,",")
if herohp > monsterhp:
  print("hero win")
else:
  print("monster win")
