python3 -c "import random, math, functools;sum = lambda c, func, n=0, i=0: ( sum(c, func, (n+1 if func(random.uniform(0,0.5), random.uniform(0,0.5)) else n), i+1 ) ) if i < c else n;print(functools.reduce(lambda a,f: a+sum(994,f), iter([lambda x, y: (y <=  -math.sqrt(x - x*x) + 0.5), lambda x, y: (-y >= (1.2*x*x - 0.3)), lambda x, y: (y*y + x*x <= 0.25), lambda x, y: (-y >=  -0.3*math.sqrt(1 - (x*x*4))) ]), 0)/(4*994))"