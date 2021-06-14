#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""This module assigns players to teams"""

USER = []

def matchmaking(players, teams=3, min_team=1, max_team=None):
    """This function matches players with a team play of even numbers.

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
        players split evenly by number of teams and team size.

    Examples:
        >>> players = [('a', 1), ('b', 0), ('c', 1), ('d', 1), ('e', 1), ('f', 1)]
        >>> matchmaking(players, teams=1, min_team=1, max_team=1)
        [['a']]

        >>> players = [('a', 1), ('b', 0), ('c', 1), ('d', 1), ('e', 1), ('f', 1)]
        >>> matchmaking(players, teams=2, min_team=1, max_team=1)
        [['a'], ['c']]

        >>> players = [('a', 1), ('b', 0), ('c', 1), ('d', 1), ('e', 1), ('f', 1)]
        >>> matchmaking(players, teams=2, min_team=1, max_team=2)
        [['a', 'd'], ['c', 'e']]

        >>> players = [('a', 1), ('b', 0), ('c', 1), ('d', 1), ('e', 1), ('f', 1)]
        >>> matchmaking(players, teams=2, min_team=3)
        False

        >>> players = [('a', 1), ('b', 0), ('c', 1), ('d', 1), ('e', 1), ('f', 1)]
        >>> matchmaking(players, teams=6, min_team=1)
        False

        >>> players = [('a', 1), ('b', 0), ('c', 1), ('d', 1), ('e', 1), ('f', 1)]
        >>> matchmaking(players, teams=1, min_team=1)
        [['a', 'c', 'd', 'e', 'f']]

    """
    valid_user(matchmaking)

    try:
        while len(USER) != max_team*teams:
            del USER[-1]

    except:
        if len(USER)%teams*min_team != 0:
            return False

        elif len(USER)%teams:
            while len(USER) != teams:
                del USER[-1]

    game = [USER[i::teams] for i in xrange(teams)]
    return game

def valid_user(matchmaking):
    """This function removes players with a bad connection.

    Args:
        matchmaking: (function)

    Returns:
        A list of players with a good connections.

    Examples:
        >>> valid_user(matchmaking)
        ['a', 'c', 'd', 'e', 'f']
    """
    for player in players:
        if player[-1] == False:
            continue
        else:
            USER.extend(list(player[:-1]))
