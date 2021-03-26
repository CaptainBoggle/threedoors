import random
import math
import os
import turtle
history = []
def intput(inpt):
    while True:
        var = True
        try:
            res = int(input(inpt))

        except ValueError:
            print("Invalid input, please enter an integer!")
            var = False

        if var:
            return res

def strinput(inpt):
    while True:
        var = True
        try:
            res = str(input(inpt))

        except ValueError:
            print("Invalid input, please enter valid hexadecimal!!")
            var = False

        if var:
            return res





class Door:
    def __init__(self, doornum):
        self.doornum = doornum
        self.enemydif = random.randint(1, 100)
        self.enemysize = random.randint(1, 100)
        self.lootamount = random.randint(1, 100)
        self.lootquality = random.randint(1, 100)
        self.doordesc = classify(self)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def classify(d):
    if d.enemydif + d.enemysize + d.lootamount + d.lootquality > 390:
        opinion = random.choice(
            ["breathtaking", "incredible", "phenomenal", "mind-blowing", "absurd", "spectacular", "mind-boggling",
             "supreme", "awe-inspiring", "extraordinary"])
    elif d.enemydif + d.enemysize + d.lootamount + d.lootquality > 350:
        opinion = random.choice(
            ["fantastic", "astonishing", "dazzling", "tremendous", "stunning", "marvellous", "magnificent",
             "remarkable", "wonderful", "impressive"])
    elif d.enemydif + d.enemysize + d.lootamount + d.lootquality > 300:
        opinion = random.choice(
            ["great", "exceptional", "special", "grand", "majestic", "beautiful", "glorious", "brilliant", "spiffing",
             "splendid"])
    elif d.enemydif + d.enemysize + d.lootamount + d.lootquality > 200:
        opinion = random.choice(
            ["fine", "quaint", "admirable", "acceptable", "robust", "satisfactory", "pleasing", "comely", "pretty"])
    elif d.enemydif + d.enemysize + d.lootamount + d.lootquality > 150:
        opinion = random.choice(
            ["tolerable", "uninspired", "respectable", "passable", "adequate", "goodish", "unexceptional",
             "run-of-the-mill", "bog-standard", "cromulent"])
    elif d.enemydif + d.enemysize + d.lootamount + d.lootquality > 100:
        opinion = random.choice(
            ["mediocre", "inferior", "amateurish", "inane", "vacuous", "lesser", "lowly", "second-rate", "faulty",
             "unsound"])
    elif d.enemydif + d.enemysize + d.lootamount + d.lootquality > 50:
        opinion = random.choice(
            ["crummy", "malformed", "bad", "poor", "dreadful", "lousy", "disagreeable", "dire", "unpleasant", "awful"])
    else:
        opinion = random.choice(
            ["abhorrent", "godawful", "deplorable", "barbaric", "wretched", "appalling", "ghastly", "grisly",
             "cataclysmic", "abysmal"])

    if d.enemysize > 90 or d.lootamount > 90:
        size = random.choice(
            ['titanic', "colossal", "gargantuan", "immense", "stupendous", "enormous", "astronomical", "cosmic",
             "Herculean", "ginormous"])  # door size huge
    elif d.enemysize > 75 or d.lootamount > 75:
        size = random.choice(
            ["giant", "vast", "substantial", "huge", "massive", "immense", "towering", "monumental", "mighty",
             "towering"])  # door size large
    elif d.enemysize > 50 or d.lootamount > 50:
        size = random.choice(["midsize", "average", "medium", "moderate", "regular"])  # door size average
    elif d.enemysize > 25 or d.lootamount > 25:
        size = random.choice(["little", "small", "short", "cramped", "compact", "squat"])  # door size small
    else:
        size = random.choice(["miniature", "measly", "tiny", "minuscule", "puny", "pathetic"])  # door size tiny

    if d.enemydif > 90 or (d.enemydif > 70 and d.lootquality < 40 and d.lootamount < 40) or (
            d.enemysize < 20 and d.lootquality > 75):  # door should be heavy/thick if it has a very dangerous creature (with or without loot), if it has a dangerous creature without loot, or if it has a weak creature with high quality loot
        shape = random.choice(["heavy", "thick", "hulking", "dense", "bulky"])
    elif (d.enemydif < 20 and d.enemysize > 70) or ((d.lootamount + d.lootquality) > 150 and (
            d.enemydif + d.enemysize) < 50):  # the door for lots of little enemies or one big friendly one should be thin/light, and if it is a room with lots of loot and almost no enemies it should also be thin
        shape = random.choice(["paper-thin", "slight", "fine", "papery", "slender", "gossamer", "sheer"])
    else:  # average-shaped door
        shape = random.choice(["average-thickness", "scraggy", "slim", "classic"])

    if d.lootquality < 25:  # in order for doors to be in good condition with low loot quality, they need to have a high enemysize with a low enemydif
        if d.enemysize - d.enemydif > 50:
            condition = random.choice(
                ["pristine", "factory-new", "immaculate", "sterile", "spotless", "untouched", "unadulterated",
                 "stainless", "flawless", "unsullied", "clean"])  # good condition
        else:
            condition = random.choice(
                ["beat-up", "mangled", "dismal", "shabby", "busted", "broken", "dilapidated", "rough", "seedy",
                 "shredded", "crude", "fragmented"])  # bad condition
    elif d.lootquality < 75:  # about average loot quality, so it will be good unless enemydif is greater than enemysize
        if d.enemydif > d.enemysize:
            condition = random.choice(
                ["beat-up", "mangled", "dismal", "shabby", "busted", "broken", "dilapidated", "rough", "seedy",
                 "shredded", "crude", "fragmented"])  # bad condition
        else:
            condition = random.choice(
                ["pristine", "factory-new", "immaculate", "sterile", "spotless", "untouched", "unadulterated",
                 "stainless", "flawless", "unsullied", "clean"])  # good condition
    else:  # this is pretty high quality loot, so will be good condition unless there is some monster issue in there
        if d.enemydif + d.enemysize > 150:
            condition = random.choice(
                ["beat-up", "mangled", "dismal", "shabby", "busted", "broken", "dilapidated", "rough", "seedy",
                 "shredded", "crude", "fragmented"])  # bad condition
        else:
            condition = random.choice(
                ["pristine", "factory-new", "immaculate", "sterile", "spotless", "untouched", "unadulterated",
                 "stainless", "flawless", "unsullied", "clean"])  # good condition

    # large enemysize, high lootamount + low lootquality, very high enemydif + (low lootquality/lootamount) - all of these lead to high age.
    if d.enemysize + d.enemydif > 150 and d.lootquality < 40 and d.lootamount > d.lootquality:  # The perfect storm for a very, very old door
        age = str(random.randint(1000, 2000)) + " year-old"  # 1k<door<2k years
    elif d.lootquality + d.lootamount < 75:  # worthless room, could be a wide range of ages
        age = str(random.randint(1, 1500)) + " year-old"  # 1<door<1.5k years
    elif d.enemysize < 40 and (d.enemydif - d.lootquality) > 50:  # very dangerous, small creature, or just loot-poor
        age = str(random.randint(750, 1250)) + " year-old"  # 750<door<1.25k years
    elif d.lootquality + d.lootamount > 125 > d.enemysize + d.enemydif:  # near-unguarded room with great loot? must be very young
        age = str(random.randint(1, 10)) + " year-old"  # 1<door<10 years
    else:  # could be anything... but it will be a bit old
        age = str(random.randint(500, 1750)) + " year-old"  # 500<door<1.75k

    # now for the door materials. These will all be determined by the stat hierarchies.
    if d.enemysize < d.enemydif < d.lootquality < d.lootamount:
        material = "sandstone"
    elif d.enemysize < d.enemydif < d.lootamount < d.lootquality:
        material = "ruby"
    elif d.enemysize < d.lootquality < d.enemydif < d.lootamount:
        material = "lead"
    elif d.enemysize < d.lootquality < d.lootamount < d.enemydif:
        material = "uranium"
    elif d.enemysize < d.lootamount < d.enemydif < d.lootquality:
        material = "mercury"
    elif d.enemysize < d.lootamount < d.lootquality < d.enemydif:
        material = "plutonium"
    elif d.enemydif < d.enemysize < d.lootquality < d.lootamount:
        material = "glass"
    elif d.enemydif < d.enemysize < d.lootamount < d.lootquality:
        material = "crystal"
    elif d.enemydif < d.lootquality < d.enemysize < d.lootamount:
        material = "plastic"
    elif d.enemydif < d.lootquality < d.lootamount < d.enemysize:
        material = "brick"
    elif d.enemydif < d.lootamount < d.enemysize < d.lootquality:
        material = "diamond"
    elif d.enemydif < d.lootamount < d.lootquality < d.enemysize:
        material = "gold"
    elif d.lootquality < d.enemysize < d.enemydif < d.lootamount:
        material = "coal"
    elif d.lootquality < d.enemysize < d.lootamount < d.enemydif:
        material = "arsenic"
    elif d.lootquality < d.enemydif < d.enemysize < d.lootamount:
        material = "stone"
    elif d.lootquality < d.enemydif < d.lootamount < d.enemysize:
        material = "wooden"
    elif d.lootquality < d.lootamount < d.enemysize < d.enemydif:
        material = "foam"
    elif d.lootquality < d.lootamount < d.enemydif < d.enemysize:
        material = "perspex"
    elif d.lootamount < d.enemysize < d.enemydif < d.lootquality:
        material = "platinum"
    elif d.lootamount < d.enemysize < d.lootquality < d.enemydif:
        material = "radium"
    elif d.lootamount < d.enemydif < d.enemysize < d.lootquality:
        material = "silver"
    elif d.lootamount < d.enemydif < d.lootquality < d.enemysize:
        material = "osmium"
    elif d.lootamount < d.lootquality < d.enemysize < d.enemydif:
        material = "cloth"
    else:
        material = "tungsten"
    desctext = opinion + " " + size + " " + shape + " " + condition + " " + age + " " + material + " " + "door"
    return desctext


def generatemaths(size, dif, livesleft):
    lives = livesleft
    if dif == 1:  # cases for various enemy difficulty levels
        for i in range(size):  # addition
            num1 = random.randint(0, 100)
            num2 = random.randint(0, 100)
            sol = int(num1 + num2)
            if int(intput("What is " + str(num1) + " + " + str(num2) + "? ")) == int(sol):
                print("Correct!\n")
            else:
                print("Wrong! The correct answer was " + str(sol) + "\n")
                lives = lives - 1
            print("You now have "+str(lives)+" lives left.\n")

    elif dif == 2:
        for i in range(size):  # multiplication
            num1 = random.randint(0, 11)
            num2 = random.randint(0, 13)
            sol = int(num1 * num2)
            if int(intput("What is " + str(num1) + " * " + str(num2) + "? ")) == int(sol):
                print("Correct!\n")
            else:
                print("Wrong! The correct answer was " + str(sol) + "\n")
                lives = lives - 1
            print("You now have " + str(lives) + " lives left.\n")

    elif dif == 3:
        for i in range(size):  # division
            num1 = random.randint(1, 30)
            num2 = random.randint(1, 10)
            while num1 % num2 != 0:
                num1 = random.randint(1, 30)
                num2 = random.randint(1, 10)

            sol = int(num1 / num2)
            if int(intput("What is " + str(num1) + " / " + str(num2) + "? ")) == int(sol):
                print("Correct!\n")
            else:
                print("Wrong! The correct answer was " + str(sol) + "\n")
                lives = lives - 1
            print("You have " + str(lives) + " lives left.\n")

    elif dif == 4:
        for i in range(size):  # Greatest common denominator
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            sol = math.gcd(num1, num2)
            if int(intput(
                    "What is the greatest common denominator of " + str(num1) + " and " + str(num2) + "? ")) == int(
                    sol):
                print("Correct!\n")
            else:
                print("Wrong! The correct answer was " + str(sol) + "\n")
                lives = lives - 1
            print("You now have " + str(lives) + " lives left.\n")

    elif dif == 5:
        for i in range(size):  # find the discriminant
            num1 = random.randint(-100, 100)
            num2 = random.randint(-30, 30)
            num3 = random.randint(-10, 10)
            sol = int((num2 * num2) - (4 * num1 * num3))
            if int(intput("What is the discriminant of " + str(num1) + "x^2 + " + str(num2) + "x + " + str(
                    num3) + "? ")) == int(sol):
                print("Correct!\n")
            else:
                print("Wrong! The correct answer was " + str(sol) + "\n")
                lives = lives - 1
            print("You now have " + str(lives) + " lives left.\n")


    elif dif == 6:
        for i in range(size):  # hard multiplication
            num1 = random.randint(-25, 25)
            num2 = random.randint(-125, 125)
            sol = int(num1 * num2)
            if int(intput("What is " + str(num1) + " * " + str(num2) + "? ")) == int(sol):
                print("Correct!\n")
            else:
                print("Wrong! The correct answer was " + str(sol) + "\n")
                lives = lives - 1
            print("You now have " + str(lives) + " lives left.\n")

    elif dif == 7:
        for i in range(size):  # hard division
            num1 = random.randint(1, 1000)
            num2 = random.randint(11, 11)
            while num1 % num2 != 0:
                num1 = random.randint(1, 1000)
                num2 = random.randint(1, 11)
            sol = int(num1 / num2)
            if int(intput("What is " + str(num1) + " / " + str(num2) + "? ")) == int(sol):
                print("Correct!\n")
            else:
                print("Wrong! The correct answer was " + str(sol) + "\n")
                lives = lives - 1
            print("You now have " + str(lives) + " lives left.\n")

    elif dif == 8:
        for i in range(size):  # indices
            num1 = random.randint(1, 9)
            num2 = random.randint(0, 4)
            sol = int(num1 ** num2)
            if int(intput("What is " + str(num1) + " to the power of " + str(num2) + "? ")) == int(sol):
                print("Correct!\n")
            else:
                print("Wrong! The correct answer was " + str(sol) + "\n")
                lives = lives - 1
            print("You now have " + str(lives) + " lives left.\n")

    elif dif == 9:
        for i in range(size):  # binary conversion
            num1 = random.randint(0, 1024)
            sol = format(num1, 'b')
            if int(intput("What is " + str(num1) + " written in binary?\n0b")) == sol:
                print("Correct!\n")
            else:
                print("Wrong! The correct answer was " + str(sol) + "\n")
                lives = lives - 1
            print("You now have " + str(lives) + " lives left.\n")

    else:
        for i in range(size):  # hexadecimal conversion
            num1 = random.randint(0, 255)
            sol = format(num1, 'x')
            if str(strinput("What is " + str(num1) + " written in hexadecimal?\n0x")).lower() == str(sol).lower():
                print("Correct!\n")
            else:
                print("Wrong! The correct answer was " + str(sol) + "\n")
                lives = lives - 1
            print("You now have " + str(lives) + " lives left.\n")
    clear()
    return lives


def generatedoors():
    currentdoors = [Door(0), Door(1), Door(2)]
    return currentdoors






def generateloot(amount, qual, mod, lives):
    clear()
    print("Now lets take a look at that loot...")
    choicedict = {0: "Power!", 1: "Knowledge!", 2: "Sight!", 3: "Luck!"}
    for i in range(math.floor(amount)):
        modchoice = random.randrange(5)
        if modchoice == 4 and lives <= 10 - math.floor(qual / 10):
            lives += (math.floor(qual / 10) + 1)
            print("You healed " + str((math.floor(qual / 10) + 1)) + " lives!")
        else:
            if modchoice == 4:
                modchoice = random.randrange(4)
            mod[modchoice] += (math.floor(qual/5) + 1)
            print("You gained " + str((math.floor(qual/5) + 1)) + " " + choicedict[modchoice])
    for i in range(len(mod)):
        if mod[i] >= 90:
            mod[i] = 90

    print("\n")
    print("You now have "+str(lives)+" lives, "+str(mod[0])+" power, "+str(mod[1])+" knowledge, "+str(mod[0])+" sight, and "+str(mod[0])+" luck.")
    return [mod, lives]


def endgame(his):
    history =his
    turtle.speed(20)
    turtle.pd()
    clear()
    print(history)
    print("You have died!")
    for i in history:
        if i == 1:
            turtle.seth(135)
            turtle.forward(20)
            turtle.back(20)
            turtle.seth(90)
            turtle.forward(12)
            turtle.back(12)
            turtle.seth(45)
            turtle.forward(20)

        elif i == 2:
            turtle.seth(135)
            turtle.forward(20)
            turtle.back(20)
            turtle.seth(45)
            turtle.forward(20)
            turtle.back(20)
            turtle.seth(90)
            turtle.forward(12)

        else:
            turtle.seth(45)
            turtle.forward(20)
            turtle.back(20)
            turtle.seth(90)
            turtle.forward(12)
            turtle.back(12)
            turtle.seth(135)
            turtle.forward(20)



def rundoor(doorindex, modifiers, livesleft,currentdoors,his):
    global history
    clear()
    lives = livesleft
    results = []
    ltamnt = currentdoors[doorindex].lootamount
    ltqual = currentdoors[doorindex].lootquality
    edif = currentdoors[doorindex].enemydif
    esize = currentdoors[doorindex].enemysize

    if esize - modifiers[0] < 0 or edif - modifiers[1] < 0:
        print("This room appears to be free of any monsters...\n")
    else:
        lives = generatemaths(math.floor((esize - modifiers[0]) / 10) + 1, math.floor((edif - modifiers[1]) / 10) + 1,
                              lives)

    if lives <= 0:
        endgame(his)
    else:
        return generateloot(math.floor((ltamnt + modifiers[2]) / 10) + 1, math.floor((ltqual + modifiers[3]) / 10),
                            modifiers, lives)

def mainfunction():
    # init: print title, clear, print description, clear, print have fun + copyright, clear, first door,  proceed to main gameplay loop
    mods = [0, 0, 0, 0]
    history = []
    lives = 10
    #main loop
    while True:
        doors = generatedoors()
        print("\n")
        print("You notice that at the back of the room, there are three doors, each beckoning you in a different way...\nDespite this, you may only choose one, so which will it be?")
        print("Will you choose the first door, the "+doors[0].doordesc+"?")
        print("Or will you enter the second door, the "+doors[1].doordesc+"?")
        print("Or perhaps the third door, the "+doors[2].doordesc+"?")
        print("Please enter 1, 2, or 3. Prepare for the worst... Or the best!")
        chce=int(intput("Choice: "))
        while chce not in [1,2,3]:
            print("That is not a door, please enter 1, 2 or 3.")
            chce=int(intput("Choice: "))

        result = rundoor(chce-1,mods,lives,doors,history)
        history.append(chce)
        mods = result[0]
        if mods[2] >= 60:
            mods[2] = 60
        if mods[3] >= 60:
            mods[3] = 60
        lives = result[1]
        for i in doors:
            del i

if __name__ == '__main__':
    mainfunction()
