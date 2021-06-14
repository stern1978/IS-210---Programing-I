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
print "[['a', 'c', 'd', 'e', 'f']]", '\n', f,  'My result'
