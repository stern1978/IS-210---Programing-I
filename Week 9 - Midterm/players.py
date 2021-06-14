#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This is the players list."""

def matchmaking(players, teams=3, min_team=1, max_team=None):
    

    #VALID USERS WORKS - DON'T CHANGE
    USER = []
    for player in players:
        if player[-1] == False:
            continue
        else:
            player = list(player[:1])
            USER.extend(player)

    #CREATE TEAMS NEEDS WORK
    if teams*min_team > len(USER):
        print 'if ran'
        return False

    while len(USER) != max_team*teams:
        print 'while ran'
        del USER[-1]

    else:
        teams == min_team
        print 'elif ran'
        return USER



    #RETURN GAME WORKS - DON'T CHANGE
    game = [USER[i::teams] for i in xrange(teams)]
    return game


players = [('a', 1), ('b', 0), ('c', 1), ('d', 1), ('e', 1), ('f', 1)]
#players = [('a', 1), ('b', 0), ('c', 1), ('d', 1), ('e', 1), ('f', 1), ('g', 1), ('h', 1), ('i', 1), ('j', 1), ('k', 1)]

aa = matchmaking(players)
print "xx"
a = matchmaking(players, teams=1, min_team=1, max_team=1)
print "[['a']]", '\n', a, 'My result'

b = matchmaking(players, teams=2, min_team=1, max_team=1)
print "[['a'], ['c']]", '\n', b, 'My result'

c = matchmaking(players, teams=2, min_team=1, max_team=2)
print "[['a', 'd'], ['c', 'e']]", '\n', c, 'My result'

d = matchmaking(players, teams=2, min_team=3)
print 'False', '\n', d, 'My result'

e = matchmaking(players, teams=6, min_team=1)
print 'False', '\n', e, 'My result'

f = matchmaking(players, teams=1, min_team=1)
print "[['a', 'c', 'd', 'e', 'f']]", '\n', f,  'My result'#not working
#fails because of 'None' type can be multiplied

