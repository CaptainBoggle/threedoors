
def generatedoors():
    global currentdoors
    currentdoors = {'1':'cringe','2':'epic','3':'weird'}
    print(currentdoors)

def opendoor(ch):
    print(currentdoors[ch])

sizes = 
states =
materials =


class Door():
    self.enemydif
    self.enemysize
    self.lootamount
    self.lootquality


def classify(d):
    if d.enemysize >= 90 or d.lootamount >= 90:
        # door size huge
    elif d.enemysize >= 75 or d.lootamount >= 75:
        # door size large
    elif d.enemysize >= 50 or d.lootamount >= 50:
        #door size average
    elif d.enemysize >= 25 or d.lootamount >= 25:
        # door size small
    else:
        # door size tiny

    if d.enemydif > 90 or (d.enemydif > 70 and d.lootquality < 40 and d.lootamount < 40) or (d.enemydif < 20 and d.lootquality > 75):
        # door should be heavy if it has a very dangerous creature (with or without loot), if it has a dangerous creature without loot, or if it has a weak creature with high quality loot
