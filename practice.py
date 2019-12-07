s = "In a distant, but not so unrealistic, future \ where mankind has abandoned earth because it has \ become covered with trash from products sold by \ the powerful multi-national Buy N Large corporation, \
WALLE, a garbage collecting robot has been left to \ clean up the mess. Mesmerized with trinkets of Earth's \ history and show tunes, WALLE is alone on Earth except \
for a sprightly pet cockroach. One day, EVE, a sleek \ (and dangerous) reconnaissance robot, is sent to Earth to \ find proof that life is once again sustainable."
print(len(s))
print(s.lower())
print(s.replace("WALLE", "WALL-E"))
print(s.count("Earth"))
print(s.replace ("EVE", "eve"))
print(s.upper())
v = "home is there far away"
a = (v.split(' '))
d = sorted(a, key=len)
print(' '.join(d))
a = 10
b = 9
result = a < 11 and b == 6
print(result)
t = a > 11 or b != 6
print(t)
r = result is not t
print(r)













