import random


def generatedoors():
    global currentdoors
    currentdoors = {'1':'cringe','2':'epic','3':'weird'}
    print(currentdoors)

def opendoor(ch):
    print(currentdoors[ch])

class Door():
    def __init__(self):
        self.enemydif
        self.enemysize
        self.lootamount
        self.lootquality


def classify(d):

    if d.enemydif + d.enemysize + d.lootamount + d.lootquality > 390:
        opinion = random.choice(["breathtaking","incredible","phenomenal","mind-blowing","absurd","spectacular","mind-boggling","supreme","awe-inspiring","extraordinary"])
    elif d.enemydif + d.enemysize + d.lootamount + d.lootquality > 350:
        opinion = random.choice(["fantastic","astonishing","dazzling","tremendous","stunning","marvellous","magnificent","remarkable","wonderful","impressive"])
    elif d.enemydif + d.enemysize + d.lootamount + d.lootquality > 300:
        opinion = random.choice(["great","exceptional","special","grand","majestic","beautiful","glorious","brilliant","spiffing","splendid"])
    elif d.enemydif + d.enemysize + d.lootamount + d.lootquality > 200:
        opinion = random.choice(["fine","quaint","admirable","quality","acceptable","robust","satisfactory","pleasing","comely","pretty"])
    elif d.enemydif + d.enemysize + d.lootamount + d.lootquality > 150:
        opinion = random.choice(["tolerable","uninspired","respectable","passable","adequate","goodish","unexceptional","run-of-the-mill","bog-standard","cromulent"])
    elif d.enemydif + d.enemysize + d.lootamount + d.lootquality > 100:
        opinion = random.choice(["mediocre","inferior","amateurish","inane","vacuous","lesser","lowly","second-rate","faulty","unsound"])
    elif d.enemydif + d.enemysize + d.lootamount + d.lootquality > 50:
        opinion = random.choice(["crummy","malformed","bad","poor","dreadful","lousy","disagreeable","dire","unpleasant","awful"])
    else:
        opinion = random.choice(["abhorrent","godawful","deplorable","barbaric","wretched","appalling","ghastly","grisly","cataclysmic","abysmal"])

    if d.enemysize > 90 or d.lootamount > 90:
        size = random.choice(['titanic',"colossal","gargantuan","immense","stupendous","enormous","astronomical","cosmic","Herculean","ginormous"])# door size huge
    elif d.enemysize > 75 or d.lootamount > 75:
        size = random.choice(["giant","vast","substantial","huge","massive","immense","towering","monumental","mighty","towering"])# door size large
    elif d.enemysize > 50 or d.lootamount > 50:
        size = random.choice(["midsize","average","medium","moderate","regular"]) #door size average
    elif d.enemysize > 25 or d.lootamount > 25:
        size = random.choice(["little","small","short","cramped","compact","squat"]) # door size small
    else:
        size = random.choice(["miniature","measly","tiny","minuscule","puny","pathetic"])# door size tiny

    if d.enemydif > 90 or (d.enemydif > 70 and d.lootquality < 40 and d.lootamount < 40) or (d.enemysize < 20 and d.lootquality > 75): # door should be heavy/thick if it has a very dangerous creature (with or without loot), if it has a dangerous creature without loot, or if it has a weak creature with high quality loot
        shape = random.choice(["heavy","thick","hulking","dense","bulky"])
    elif (d.enemydif < 20 and d.enemysize > 70) or ((d.lootamount+d.lootquality) > 150 and (d.enemydif+d.enemysize) < 50): # the door for lots of little enemies or one big friendly one should be thin/light, and if it is a room with lots of loot and almost no enemies it should also be thin
        shape = random.choice(["paper-thin","slight","fine","papery","slender","gossamer","sheer"])
    else: #average-shaped door
        shape = random.choice(["average-thickness","scraggy","slim"])
    

    if d.lootquality < 25: # in order for doors to be in good condition with low loot quality, they need to have a high enemysize with a low enemydif
        if d.enemysize - d.enemydif > 50:
            condition = # good condition
        else:
            condition = random.choice(["beat-up","mangled","dismal","shabby","busted","broken","dilapidated","rough","seedy","shredded","crude","fragmented"]) # bad condition
    elif d.lootquality < 75: #about average loot quality, so it will be good unless enemydif is greater than enemysize
        if d.enemydif > d.enemysize: 
            condition = random.choice(["beat-up","mangled","dismal","shabby","busted","broken","dilapidated","rough","seedy","shredded","crude","fragmented"])# bad condition
        else:
            conditon =# good condition
    else: # this is pretty high quality loot, so will be good condition unless there is some monster issue in there
        if d.enemydif + d.enemysize > 150:
            condition = random.choice(["beat-up","mangled","dismal","shabby","busted","broken","dilapidated","rough","seedy","shredded","crude","fragmented"])# bad condition
        else:
            condition = # good condition
     
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
    
    
    
    
