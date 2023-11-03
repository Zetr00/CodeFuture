import math

def calculate_discriminant(a, b, c):
    return b**2 - 4*a*c

def calculate_roots(a, b, c):
    d = calculate_discriminant(a, b, c)
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        return x1, x2
    elif d == 0:
        x = -b / (2*a)
        return x
    else:
        return "Нет "
    
def calculate_probability(m, n):
    return m / n

def calculate_sum_of_independent_probabilities(pa, pb):
    return pa + pb

def calculate_sum_of_joint_probabilities(pa, pb, pab):
    return pa + pb - pab
