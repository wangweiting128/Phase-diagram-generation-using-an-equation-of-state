import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq
from scipy.integrate import quad

print("Phase diagram for 1 mole of gas:")
a = float(input("a (atm*L^2/mol^2): "))
b = float(input("b (L/mol): "))
R = 0.08206  

def p(V,T):
    return R*T/(V-b)-a/(V**2)

def critical(a,b):
    Tc= 8*a/(27*R*b)
    Vc=3*b
    Pc=a/(27*b**2)
    return Tc,Vc,Pc

Tc,Vc,Pc=critical(a,b)
T_list=np.linspace(0.5*Tc,0.9995*Tc,40) 
Psat_list=[]

for T in T_list:
    V= np.linspace(1.05*b,10*b,200)
    P=p(V,T)
    p_max=np.max(P)
    p_min=max((1e-5, np.min(P)))

    def area_difference(Psat):
        try:
            def find_v(V):
                return p(V,T)-Psat
            Vl = brentq(find_v,1.01*b,0.999*Vc)
            Vg = brentq(find_v,1.001*Vc,50*b)
            area,_=quad(lambda V:p(V,T)-Psat,Vl,Vg,epsabs=1e-9, epsrel=1e-9, limit=200)
            return area
        except Exception:
            return np.nan

    try:
        def func(P):
            val = area_difference(P)
            if np.isnan(val):
                return 1e9
            else:
                return val
        sol = brentq(func, 1e-3, Pc, xtol=1e-9, rtol=1e-9, maxiter=200)
        Psat_list.append(sol)
    except:
        Psat_list.append(np.nan)


plt.figure(figsize=(12,5))

plt.subplot(1,2,1)
Vr = np.linspace(0.4,4.0,500)
for Tr in [0.85,0.9,0.95,1.0,1.05]:
    Pr = (8*Tr)/(3*Vr-1)-3/(Vr**2)
    plt.plot(Vr,Pr,label=f"$T_r={Tr}$")
plt.ylim(-0.5,2.5)
plt.title("P-V Isotherms (Reduced form)")
plt.legend()

print(Psat_list)
plt.subplot(1, 2, 2)
plt.plot(T_list, Psat_list, marker="o",color="red")
plt.scatter([Tc],[Pc],marker="x",color="blue",label="Critical point")
plt.xlabel("T(K)")
plt.ylabel("P(atm)")
plt.title("Liquid-Gas phase diagram")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
