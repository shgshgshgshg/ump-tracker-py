#proof of concept for ump app; this version built in python 3.10

#input variable (doubles as input from user)
prompt = input('')

#all variables:
strikes = 0
balls = 0
outs = 0
pitches_total = 0
pitches_current = 0
home_score = 0
away_score = 0
HOME_TEAM = ""
AWAY_TEAM = ""
play_active = True
inning_active = True
inning_part = 0

#the bool "play_active" tells the program whether the play is active, and when it's not a function resets certain variables to be able to continue the tracking
#the bool "inning active" tells the program whether the inning is being played, and if it is set to false associated variables will reset and/or change
#the var "inning_part" tells the program whether it is the top or bottom of the inning, and associates with the contants "HOME_TEAM" and "AWAY_TEAM"

#the following provides a system to have variables interconnect (e.g. if the strike count goes up to 3, it resets and the outs go to 1)

#this portion specifically works with changes to ball/strike/pitch count variables
while outs != 3:
    if prompt == 'strike':
        pitches_total == pitches_total + 1
        pitches_current == pitches_current + 1
        strikes =  strikes + 1
    elif prompt == 'ball':
        pitches_total == pitches_total + 1
        pitches_current == pitches_current + 1
        balls = balls + 1
#this next portion determines when to change the out/ball/strike variables based upon the already existing vars
while play_active == True:
    if strikes == 3:
        outs = outs + 1
        play_active = False
    elif balls == 4:
        play_active = False
    elif outs == 3:
        play_active = False
        inning_active = False