
def generatedoors():
    global currentdoors
    currentdoors = {'1':'cringe','2':'epic','3':'weird'}
    print(currentdoors)

def opendoor(ch):
    print(currentdoors[ch])


material


class Door():
    self.enemydif
    self.enemysize
    self.lootamount
    self.lootquality


def classify(d):

    if d.enemydif + d.enemysize + d.lootamount + d.lootquality > 390:
        #very very good opinion
    elif d.enemydif + d.enemysize + d.lootamount + d.lootquality > 350:
        #very good opinion
    elif d.enemydif + d.enemysize + d.lootamount + d.lootquality > 300:
        # pretty good opinion
    elif d.enemydif + d.enemysize + d.lootamount + d.lootquality > 200:
        # a bit above average
    elif d.enemydif + d.enemysize + d.lootamount + d.lootquality > 150:
        # a bit below average
    elif d.enemydif + d.enemysize + d.lootamount + d.lootquality > 100:
        # fairly bad
    elif d.enemydif + d.enemysize + d.lootamount + d.lootquality > 50:
        # very bad
    else:
        #terrible

    if d.enemysize > 90 or d.lootamount > 90:
        # door size huge
    elif d.enemysize > 75 or d.lootamount > 75:
        # door size large
    elif d.enemysize > 50 or d.lootamount > 50:
        #door size average
    elif d.enemysize > 25 or d.lootamount > 25:
        # door size small
    else:
        # door size tiny

    if d.enemydif > 90 or (d.enemydif > 70 and d.lootquality < 40 and d.lootamount < 40) or (d.enemysize < 20 and d.lootquality > 75): # door should be heavy/thick if it has a very dangerous creature (with or without loot), if it has a dangerous creature without loot, or if it has a weak creature with high quality loot
    
    elif (d.enemydif < 20 and d.enemysize > 70) or ((d.lootamount+d.lootquality) > 150 and (d.enemydif+d.enemysize) < 50): # the door for lots of little enemies or one big friendly one should be thin/light, and if it is a room with lots of loot and almost no enemies it should also be thin
    
    else: #average-shaped door
    

    if d.lootquality < 25: # in order for doors to be in good condition with low loot quality, they need to have a high enemysize with a low enemydif
        if d.enemysize - d.enemydif > 50:
            # good condition
        else:
            # bad condition
    elif d.lootquality < 75: #about average loot quality, so it will be good unless enemydif is greater than enemysize
        if d.enemydif > d.enemysize: 
            # bad condition
        else:
            # good condition
    else: # this is pretty high quality loot, so will be good condition unless there is some monster issue in there
        if d.enemydif + d.enemysize > 150:
            # bad condition
        else:
            # good condition
     
    #large enemysize, high lootamount + low lootquality, very high enemydif + (low lootquality/lootamount) - all of these lead to high age. 
    if d.enemysize + d.enemydif > 150 and d.lootquality < 40 and d.lootamount > d.lootquality: # The perfect storm for a very, very old door
        # 1k<door<2k years
    elif d.lootquality + d.lootamount < 75: # worthless room, could be a wide range of ages
        # 1<door<1.5k years
    elif d.enemysize < 40 and (d.enemydif-d.lootquality) > 50: # very dangerous, small creature, or just loot-poor
        # 750<door<1.25k years
    elif d.lootquality + d.lootamount > 125 and d.enemysize + d.enemydif < 125: # near-unguarded room with great loot? must be very young
        # 1<door<10 years\
    else: #could be anything... but it will be a bit old
        # 500<door<1.75k

    # now for the door materials. These will all be determined by the stat hierarchies.
    if d.enemysize < d.enemydif < d.lootquality < d.lootamount: material = "sandstone"
    elif d.enemysize < d.enemydif < d.lootamount < d.lootquality: material = "ruby"
    elif d.enemysize < d.lootquality < d.enemydif < d.lootamount: material = "lead"
    elif d.enemysize < d.lootquality < d.lootamount < d.enemydif: material = "uranium"
    elif d.enemysize < d.lootamount < d.enemydif < d.lootquality: material = "mercury"
    elif d.enemysize < d.lootamount < d.lootquality < d.enemydif: material = "plutonium"
    elif d.enemydif < d.enemysize < d.lootquality < d.lootamount: material = "glass"
    elif d.enemydif < d.enemysize < d.lootamount < d.lootquality: material = "crystal"
    elif d.enemydif < d.lootquality < d.enemysize < d.lootamount: material = "plastic"
    elif d.enemydif < d.lootquality < d.lootamount < d.enemysize: material = "brick"
    elif d.enemydif < d.lootamount < d.enemysize < d.lootquality: material = "diamond" 
    elif d.enemydif < d.lootamount < d.lootquality < d.enemysize: material = "gold"
    elif d.lootquality < d.enemysize < d.enemydif < d.lootamount: material = "coal"
    elif d.lootquality < d.enemysize < d.lootamount < d.enemydif: material = "arsenic"
    elif d.lootquality < d.enemydif < d.enemysize < d.lootamount: material = "stone"
    elif d.lootquality < d.enemydif < d.lootamount < d.enemysize: material = "wooden"
    elif d.lootquality < d.lootamount < d.enemysize < d.enemydif: material = "foam"
    elif d.lootquality < d.lootamount < d.enemydif < d.enemysize: material = "perspex"
    elif d.lootamount < d.enemysize < d.enemydif < d.lootquality: material = "platinum"
    elif d.lootamount < d.enemysize < d.lootquality < d.enemydif: material = "radium"
    elif d.lootamount < d.enemydif < d.enemysize < d.lootquality: material = "silver"
    elif d.lootamount < d.enemydif < d.lootquality < d.enemysize: material = "osmium"
    elif d.lootamount < d.lootquality < d.enemysize < d.enemydif: material = "cloth"
    else: material = "tungsten"
    
    
    
    
