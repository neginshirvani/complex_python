import cmath
import random


def baristow(coef, guess1, guess2, deg, roots):
    
    if(deg<1):
        return None
    
    if((deg == 1) and (coef[1])<0):
        roots.append(float(-coef[0])/float(coef[1]))
        return None
    
    if(deg == 2):
        delta = (coef[1]**2.0) - (4.0)*(coef[2])*(coef[0])
        S1 = (-coef[1] - cmath.sqrt(delta)) / (2.0 * coef[2])
        S2 = (-coef[1] + cmath.sqrt(delta)) / (2.0 * coef[2])
        
        roots.append(S1)
        roots.append(S2)
        return None
    
    Lenn = len(coef)
    b = [0]*Lenn
    c = [0]*Lenn
    b[Lenn -1] = coef[Lenn-1]
    b[Lenn -2] = coef[Lenn-2] + guess1*b[Lenn-1]
    j = Lenn - 3
    
    while(j >=0):
        b[j] = coef[j] + guess1*b[j+1] + guess2*b[j+2]
        j -= 1
        
    c[Lenn-1] = b[Lenn-1]
    c[Lenn-2] = b[Lenn-2] + guess1*c[Lenn-1]
    j = Lenn - 3
    
    while(j >= 0):
        c[j] = b[j] + guess1*c[j+1] + guess2*c[j+2]
        j -= 1
        
    Din = ((c[2]*c[2]) - (c[3]*c[1])) ** (-1.0)
    guess1 = guess1 + (Din) * ((c[2]) * (-b[1]) + (-c[3]) * (-b[0]))
    guess2 = guess2 + (Din) * ((-c[1]) * (-b[1]) + (c[2]) * (-b[0]))

    if(abs(b[0]) > 1E-14 or abs(b[1]) > 1E-14):
        return baristow(coef, guess1, guess2, deg, roots)
    
    
    if(deg >= 3):
        
        new_delta = ((-guess1)**(2.0)) - ((4.0)*(1.0)*(-guess2))
        S1 = (guess1 - (cmath.sqrt(new_delta))) / (2.0)
        S2 = (guess1 + (cmath.sqrt(new_delta))) / (2.0)
        
        roots.append(S1)
        roots.append(S2)
        return baristow(b[2:], guess1, guess2, deg-2, roots)
    


deg = int(input())#8
roots = []
coef = [2*random.random()]+[int(x) for x in input().split()]#[2*random.random(),2,3,7,6,-1,2,-1,-2]
#print(coef)
guess1 = random.random()
guess2 = random.random()
baristow(coef, guess1, guess2, deg, roots)
res1 = 0
res2 = 0

for guess1 in roots:
    print(guess1)
##    if guess1.imag >= 0:
##        res1 += guess1.real
##        res2 += guess1.imag
##print(res1,res2)
    
    
#print(res)


'''
5
-3 2 1 0 -1 -1
sum real sum imag
'''

'''ostad mn roo in code kar kardam va aval ye algorithm didam dakhel internet
va b dalil inke fqt 1 saat vaqt baqi moonde bood ino upload kardam va inke algorithm ro kamel motevajeh shodam
va fqt b khatere kamboode vaqt o feshare projea nashod k kamelesh konm va haghe inke nomre ham begiram az in tamrin nadaram
vli goftam laqal tozih dade basham baratoon
tashakor'''
    
    
