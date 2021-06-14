#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module assigns players to teams"""

players = [('a', 1), ('b', 0), ('c', 1), ('d', 1), ('e', 1), ('f', 1)]

def matchmaking(players, teams=3, min_team=1, max_team=None):
    """This function matches players with a valid connection for team play of
        even numbers.

    Args:
        players (list): a list of tuples of usernames and
        connection strength for each user.
        teams (int, optional): The number of teams to
        build for this game, defaults to 3
        min_team (int, optional): The minimum number of players per team,
        defaults to 1.
        max_team (int, optional): The maximum number of players per team,
        defaults to None

    Returns:
        players split evenly by number of teams.

    Examples:

    """
    game = [players[i::teams] for i in xrange(teams)]

    valid(matchmaking)
    while len(players)%teams != 0:
            del players[-1]
    return game

                       
def valid(matchmaking):
    for player in players:
        if player[-1] == False:
            players.remove(player)
        else:
            if player in players[-1] == True:
                return list(players)

#def valteam(matchmaking):
#    if valid(players) < min_team or valid(players) > max_team:
#        return False


a = matchmaking(players, teams=1, min_team=1, max_team=1)
print "[['a']] - - ", a
print len(players)
b = matchmaking(players, teams=2, min_team=1, max_team=1)
print "[['a'], ['c']] - - ", b
print len(players)
c = matchmaking(players, teams=2, min_team=1, max_team=2)
print "[['a', 'd'], ['c', 'e']] - - ", c
print len(players)
d = matchmaking(players, teams=2, min_team=3, max_team=None)
print 'False - - ' , d
print len(players)
e = matchmaking(players, teams=6, min_team=1, max_team=None)
print 'False - - ', e
print len(players)
f = matchmaking(players, teams=1, min_team=1, max_team=None)
print "[['a', 'c', 'd', 'e', 'f']] - - ", f
print len(players)
