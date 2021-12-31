#-------------------------------------------------------------------------------
# Name:        main.py
# Purpose:     To play the game of Hangman.
#
# Author:      Isaiah Sinclair
#
# Created:     13/01/2020
# Copyright:   (c) GRCI 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from random import randrange
from graphics import *
from time import sleep
import winsound

#Define button class:
class Button:
    def __init__(self, gw, center, width, height, label):
        w,h = width/2.0, height/2.0
        x,y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1,p2)
        self.rect.setFill(color_rgb(255, 204, 204))
        self.rect.setOutline('Light Grey')
        self.rect.draw(gw)
        self.label = Text(center, label)
        self.label.draw(gw)
        self.activate()

    def clicked(self, p):
        return (self.active and
            self.xmin <= p.getX() <= self.xmax and
            self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        sleep(0.075)
        self.active = True

    def deactivate(self):
        self.label.setFill('dark grey')
        self.rect.setWidth(1)
        sleep(0.2)
        winsound.PlaySound("Click2", winsound.SND_ASYNC)
        self.active = False

    def delete(self):
        self.label.undraw()
        self.rect.undraw()

def main():
    try:
        fullgameover = False
        while fullgameover == False:
            printintro()
            gw = GraphWin("Hangman Game", 700, 700)
            welcome, startbutton = startpage(gw)

            startpageclickchecker(gw, startbutton)
            undrawstartpage(welcome, startbutton)

            categorytext, fruitsbutton, nationsbutton, canadiancitiesbutton, soccerteamsbutton, topsongsbutton = categorypage(gw)
            categoryn = categorypageclickchecker(gw, fruitsbutton, nationsbutton, canadiancitiesbutton, soccerteamsbutton, topsongsbutton)
            undrawcategorypage(categorytext, fruitsbutton, nationsbutton, canadiancitiesbutton, soccerteamsbutton, topsongsbutton)

            diftext, easybutton, mediumbutton, hardbutton = difficultypage(gw)
            level = difficultypageclickchecker(gw, easybutton, mediumbutton, hardbutton)
            undrawdifficultypage(diftext, easybutton, mediumbutton, hardbutton)

            ingamegraphicslist = ingamegraphics(gw, categoryn)

            totallives = livesdeterminer(level)

            phrase = phrasefinder(categoryn)
            phrase, phraseguesstracker = mirrorlist(phrase)

            writeguesstracker(phraseguesstracker, gw)

            keys = keyboard(gw)

            gameover = False
            badguesses = 0
            win = "undetermined"

            while gameover == False:
                c = keyboardclicker(gw, keys)
                guess = guesschecker(c, phrase)

                if guess == True:
                    characteradder(phrase, phraseguesstracker, c)
                    writeguesstracker(phraseguesstracker, gw)
                    win = wincheck(phrase, phraseguesstracker)
                    if win == True:
                        gameover = True
                        fullgameover = True
                else:
                    badguesses += 1
                    drawhangman(badguesses, level, gw)
                    if badguesses == totallives:
                        win = False
                        gameover = True
                        fullgameover = True

            if win == True:
                won(gw)
            else:
                lose(phrase, gw)

            Quit, Playagain = quitbutton(gw)
            fullgameover = quitclicker(gw, Quit, Playagain)

            gw.close()
    except GraphicsError:
        gw.close()
        print("\nNext time don't click the 'X' in the top right corner. Instead play the game until finished, then press 'quit'.")
    except:
        gw.close()
        print("\nAn error has occurred. Please play the game as instructed.")

def keyboard(gw):
    Q = Button(gw, Point(80, 450), 50, 50, "Q")
    W = Button(gw, Point(140, 450), 50, 50, "W")
    E = Button(gw, Point(200, 450), 50, 50, "E")
    R = Button(gw, Point(260, 450), 50, 50, "R")
    T = Button(gw, Point(320, 450), 50, 50, "T")
    Y = Button(gw, Point(380, 450), 50, 50, "Y")
    U = Button(gw, Point(440, 450), 50, 50, "U")
    I = Button(gw, Point(500, 450), 50, 50, "I")
    O = Button(gw, Point(560, 450), 50, 50, "O")
    P = Button(gw, Point(620, 450), 50, 50, "P")
    #Second line of buttons
    A = Button(gw, Point(110, 510), 50, 50, "A")
    S = Button(gw, Point(170, 510), 50, 50, "S")
    D = Button(gw, Point(230, 510), 50, 50, "D")
    F = Button(gw, Point(290, 510), 50, 50, "F")
    G = Button(gw, Point(350, 510), 50, 50, "G")
    H = Button(gw, Point(410, 510), 50, 50, "H")
    J = Button(gw, Point(470, 510), 50, 50, "J")
    K = Button(gw, Point(530, 510), 50, 50, "K")
    L = Button(gw, Point(590, 510), 50, 50, "L")
    #Third Line of buttons
    Z = Button(gw, Point(170, 570), 50, 50, "Z")
    X = Button(gw, Point(230, 570), 50, 50, "X")
    C = Button(gw, Point(290, 570), 50, 50, "C")
    V = Button(gw, Point(350, 570), 50, 50, "V")
    B = Button(gw, Point(410, 570), 50, 50, "B")
    N = Button(gw, Point(470, 570), 50, 50, "N")
    M = Button(gw, Point(530, 570), 50, 50, "M")

    keys = [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S, T, U, V, W, X, Y, Z]

    return keys

#Prints the intro.
def printintro():
    print("This is the Hangman Game created by Isaiah Sinclair. Pick what category and what level you want and begin to play Hangman!")

#Prints startpage
def startpage(gw):
    gw.setBackground(color_rgb(255, 77, 77))
    welcome = Text(Point(350, 200), "Welcome to Hangman")
    welcome.setFace('helvetica')
    welcome.setStyle('bold italic')
    welcome.setFill('Light Grey')
    welcome.setSize(30)

    startbutton = Button(gw, Point(350, 500), 100, 50, "Start")
    startbutton.activate()

    welcome.draw(gw)

    return welcome, startbutton

def undrawstartpage(welcome, startbutton):
    welcome.undraw()
    startbutton.delete()

def quitbutton(gw):
    Quit = Button(gw, Point(625, 650), 50, 50, "Quit")
    Playagain = Button(gw, Point(525, 650), 100, 50, "Play Again")

    return Quit, Playagain

def startpageclickchecker(gw, startbutton):
    click = gw.getMouse()

    while startbutton.clicked(click) == False:
        click = gw.getMouse()

    startbutton.deactivate()

def categorypage(gw):
    categorytext = Text(Point(350, 100), "Select a Category.")
    categorytext.setSize(20)
    categorytext.setFace('helvetica')
    categorytext.setStyle('bold')
    categorytext.setFill('Light Grey')

    categorytext.draw(gw)

    fruitsbutton = Button(gw, Point(350, 200), 200, 70, "Fruits")
    nationsbutton = Button(gw, Point(350, 285), 200, 70, "Nations")
    canadiancitiesbutton = Button(gw, Point(350, 370), 200, 70, "Canadian Cities")
    soccerteamsbutton = Button(gw, Point(350 , 455), 200, 70, "Soccer Teams")
    topsongsbutton = Button(gw, Point(350, 540), 200, 70, "Top Songs")

    return categorytext, fruitsbutton, nationsbutton, canadiancitiesbutton, soccerteamsbutton, topsongsbutton

def categorypageclickchecker(gw, fruitsbutton, nationsbutton, canadiancitiesbutton, soccerteamsbutton, topsongsbutton):
    buttonchosen = False

    click = gw.getMouse()

    while buttonchosen == False:
        if fruitsbutton.clicked(click) == True:
            cat = "Fruits"
            fruitsbutton.deactivate()
            buttonchosen = True
        elif nationsbutton.clicked(click) == True:
            cat = "Nations"
            nationsbutton.deactivate()
            buttonchosen = True
        elif canadiancitiesbutton.clicked(click) == True:
            cat = "Canadian Cities"
            canadiancitiesbutton.deactivate()
            buttonchosen = True
        elif soccerteamsbutton.clicked(click) == True:
            cat = "Soccer Teams"
            soccerteamsbutton.deactivate()
            buttonchosen = True
        elif topsongsbutton.clicked(click) == True:
            cat = "Top Songs"
            topsongsbutton.deactivate()
            buttonchosen = True
        else:
            click = gw.getMouse()

    return cat

def undrawcategorypage(categorytext, fruitsbutton, nationsbutton, canadiancitiesbutton, soccerteamsbutton, topsongsbutton):
    categorytext.undraw()
    fruitsbutton.delete()
    nationsbutton.delete()
    canadiancitiesbutton.delete()
    soccerteamsbutton.delete()
    topsongsbutton.delete()

def difficultypage(gw):
    difintrotext = Text(Point(350, 100), "Select a Difficulty.")
    difintrotext.setSize(20)
    difintrotext.setFace('helvetica')
    difintrotext.setStyle('bold')
    difintrotext.setFill('Light Grey')

    difintrotext.draw(gw)

    easybutton = Button(gw, Point(350, 200), 200, 80, "Easy (9 Lives)")
    mediumbutton = Button(gw, Point(350, 350), 200, 80, "Medium (6 Lives)")
    hardbutton = Button(gw, Point(350, 500), 200, 80, "Hard (3 Lives)")

    return difintrotext, easybutton, mediumbutton, hardbutton

def difficultypageclickchecker(gw, easybutton, mediumbutton, hardbutton):
    buttonchosen = False

    click = gw.getMouse()

    while buttonchosen == False:
        if easybutton.clicked(click):
            level = 1
            easybutton.deactivate()
            buttonchosen = True
        elif mediumbutton.clicked(click):
            level = 2
            mediumbutton.deactivate()
            buttonchosen = True
        elif hardbutton.clicked(click):
            level = 3
            hardbutton.deactivate()
            buttonchosen = True
        else:
            click = gw.getMouse()

    return level

def undrawdifficultypage(diftext, easybutton, mediumbutton, hardbutton):
    diftext.undraw()
    easybutton.delete()
    mediumbutton.delete()
    hardbutton.delete()

def keyboardclicker(gw, keys):
    letter = False

    while letter == False:
        click = gw.getMouse()
        for i in keys:
            if i.clicked(click) == True:
                letter = i.getLabel()
                i.deactivate()
                break

    return letter

#Determines the amount of lives based on the level that is inputted.
def livesdeterminer(level):
    if level == 1:
        lives = 9
    elif level == 2:
        lives = 6
    else:
        lives = 3

    return lives

#Picks a random phrase.
def phrasefinder(cn):
    if cn == "Fruits":
        infile = open("fruits.txt", "r")
        phrasen = randrange(1, 103)
    elif cn == "Nations":
        infile = open("nations.txt", "r")
        phrasen = randrange(1, 198)
    elif cn == "Canadian Cities":
        infile = open("canadiancities.txt", "r")
        phrasen = randrange(1, 101)
    elif cn == "Soccer Teams":
        infile = open("soccerteams.txt", "r")
        phrasen = randrange(1, 128)
    else:
        infile = open("topsongs.txt", "r")
        phrasen = randrange(1, 108)

    for i in range(phrasen):
        phrase = infile.readline()
    phrase = phrase[0:-1]

    infile.close()

    return phrase

#Copies the list of the phrase, but then replaces any letter with an underscore.
def mirrorlist(phrase):
    phraseguesstracker = phrase

    phrase = list(phrase)
    phraseguesstracker = list(phraseguesstracker)

    counter = 0

    for i in phraseguesstracker:
        if 97 <= ord(i) <= 122 or 65 <= ord(i) <= 90:
            phraseguesstracker[counter] = "_"
        counter += 1

    return phrase, phraseguesstracker

#Gets an inputted guess from the user.
def inputguess():
    character = input("Input a character that you think will match.")

    return character

#Determines if the inputted guess is correct.
def guesschecker(c, phrase):
    guess = False

    for i in phrase:
        if i == (c.upper()):
            guess = True
            break
        elif i == (c.lower()):
            guess = True
            break

    return guess

#Adds a character to the list guess tracker if the character is correct.
def characteradder(phrase, guesstracker, c):
    counter = 0

    for i in phrase:
        if i == (c.upper()):
            guesstracker[counter] = phrase[counter]
        elif i == (c.lower()):
            guesstracker[counter] = phrase[counter]

        counter += 1

#Checks if there is a win.
def wincheck(phrase, guesstracker):
    return phrase == guesstracker

#Determine what is done when there is a win.
def won(gw):
    winsound.PlaySound("win95startupsound", winsound.SND_ASYNC)
    wintext = Text(Point(500, 100), "You won!")
    wintext.setFill("Light Grey")
    wintext.setFace('helvetica')
    wintext.setStyle('bold')
    wintext.setSize(30)

    wintext.draw(gw)

#Deterimes what is done when there is a loss.
def lose(phrase, gw):
    winsound.PlaySound("losssound", winsound.SND_ASYNC)
    writeguesstracker(phrase, gw)
    losstext = Text(Point(500, 100), "Sorry you Lost.")
    losstext.setFill("Light Grey")
    losstext.setFace('helvetica')
    losstext.setStyle('bold')
    losstext.setSize(30)

    losstext.draw(gw)

#Draws initial graphics that are displayed during playing the game.
def ingamegraphics(gw, cn):
    dividingline = Line(Point(0, 350), Point(700, 350))
    dividingline.setWidth(4)

    vpole = Line(Point(300, 300), Point(300, 50))
    vpole.setWidth(16)

    hpole = Line(Point(308, 42), Point(150, 42))
    hpole.setWidth(16)

    rope = Line(Point(158, 50), Point(158, 70))
    rope.setFill('Brown')

    platform = Rectangle(Point(225, 275), Point(375, 325))
    platform.setFill(color_rgb(51, 17, 0))

    categorytextstring = "Category: " + cn
    categorytext = Text(Point(150, 680), categorytextstring)
    categorytext.setFace('helvetica')
    categorytext.setStyle('bold')
    categorytext.setFill('Light Grey')

    dividingline.draw(gw)
    vpole.draw(gw)
    hpole.draw(gw)
    rope.draw(gw)
    platform.draw(gw)
    categorytext.draw(gw)

    ingamegraphicslist = [vpole, hpole, rope, platform]

    return ingamegraphicslist

def writeguesstracker(guesstracker, gw):
    x = 50
    y = 375
    for i in guesstracker:
        character = Text(Point(x, y), i)
        character.draw(gw)
        x += 25

def quitclicker(gw, Quit, Playagain):
    gameover = False

    while gameover == False:
        click = gw.getMouse()

        if Quit.clicked(click) == True:
            Quit.deactivate()
            Quit.delete()
            gameover = True
            fullgameover = True
        elif Playagain.clicked(click) == True:
            Playagain.deactivate()
            Playagain.delete()
            gameover = True
            fullgameover = False

    return fullgameover

def drawhangman(badguesses, level, gw):
    winsound.PlaySound("mistakeno", winsound.SND_ASYNC)

    if level == 1:
        if badguesses == 1:
            head = drawhead(gw)
        elif badguesses == 2:
            leye = drawleye(gw)
        elif badguesses == 3:
            reye = drawreye(gw)
        elif badguesses == 4:
            mouth = drawmouth(gw)
        elif badguesses == 5:
            body = drawbody(gw)
        elif badguesses == 6:
            larm = drawlarm(gw)
        elif badguesses == 7:
            rarm = drawrarm(gw)
        elif badguesses == 8:
            lleg = drawlleg(gw)
        else:
            rleg = drawrleg(gw)
    elif level == 2:
        if badguesses == 1:
            head = drawhead(gw)
            leye = drawleye(gw)
            reye = drawreye(gw)
            mouth = drawmouth(gw)
        elif badguesses == 2:
            body = drawbody(gw)
        elif badguesses == 3:
            larm = drawlarm(gw)
        elif badguesses == 4:
            rarm = drawrarm(gw)
        elif badguesses == 5:
            lleg = drawlleg(gw)
        else:
            rleg = drawrleg(gw)
    else:
        if badguesses == 1:
            head = drawhead(gw)
            leye = drawleye(gw)
            reye = drawreye(gw)
            mouth = drawmouth(gw)
        elif badguesses == 2:
            body = drawbody(gw)
            larm = drawlarm(gw)
            rarm = drawrarm(gw)
        else:
            lleg = drawlleg(gw)
            rleg = drawrleg(gw)

def drawhead(gw):
    head = Circle(Point(158, 100), 30)
    head.setFill('White')
    head.draw(gw)

    return head

def drawleye(gw):
    leye = Circle(Point(148, 90), 4)
    leye.setFill('Black')
    leye.draw(gw)

    return leye

def drawreye(gw):
    reye = Circle(Point(168, 90), 4)
    reye.setFill('Black')
    reye.draw(gw)

    return reye

def drawmouth(gw):
    mouth = Line(Point(151, 120), Point(165, 120))
    mouth.draw(gw)

    return mouth

def drawbody(gw):
    body = Line(Point(158, 130), Point(158, 230))
    body.draw(gw)

    return body

def drawlarm(gw):
    larm = Line(Point(158, 170), Point(128, 200))
    larm.draw(gw)

    return larm

def drawrarm(gw):
    rarm = Line(Point(158, 170), Point(188, 200))
    rarm.draw(gw)

    return rarm

def drawlleg(gw):
    lleg = Line(Point(158, 230), Point(128, 280))
    lleg.draw(gw)

    return lleg

def drawrleg(gw):
    rleg = Line(Point(158, 230), Point(188, 280))
    rleg.draw(gw)

    return rleg

##def highscoredecider(badguesses):
##    ifile = open("highscore.txt", "r")
##
##    chighscore = eval(ifile.readline())
##
##    ifile.close()
##
##    if badguesses < chighscore:
##        ofile = open("highscore.txt", "w")
##        print(badguesses, file=ofile)
##        ofile.close()

main()