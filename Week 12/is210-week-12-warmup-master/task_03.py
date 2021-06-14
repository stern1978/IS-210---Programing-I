x = 4
try:
    x /= 0
except Exception as excep:
    x = 3
    raise excep
finally:
    x = 2
x = 1

print x
