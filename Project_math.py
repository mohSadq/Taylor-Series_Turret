pi = 3.141592653589
def taylor_series(z):
    #Calculate arctan using 11 terms of the power series
    terms = []
    for n in range(11):
        z_power = 2 * n + 1
        terms.append (( (-1) ** n) * ( (z ** z_power) / z_power ) )

    terms = sum(terms)
    return terms * 180 / pi

def atan(x,y):

    if x == 0 : x = 0.00001 # to avoid y / 0
    z = y / x
    #z reduction since taylor series only works  |z| <= 1
    if z > 1 :
        angle = 90 - taylor_series(1/z)
    elif z < -1 : angle = -90 - taylor_series(1/z)
    else : angle = taylor_series(z)
    #Quadrants
    if x < 0  : angle = angle + 180
    elif x > 0 and y < 0 :angle = angle + 360

    return angle

