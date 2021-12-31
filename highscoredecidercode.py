#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Isaiah Sinclair
#
# Created:     19-01-2020
# Copyright:   (c) Isaiah Sinclair 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def highscoredecider(badguesses):
    ifile = open("highscore.txt", "r")

    chighscore = eval(ifile.readline())

    ifile.close()

    if badguesses < chighscore:
        ofile = open("highscore.txt", "w")
        print(badguesses, file=ofile)
        ofile.close()


highscoredecider(5)