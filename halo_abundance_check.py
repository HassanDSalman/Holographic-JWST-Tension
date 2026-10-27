"""
Real calculation: effect of lowering the collapse threshold delta_c on halo abundance.
Planck 2018 cosmology, Eisenstein-Hu (1998) no-wiggle transfer function,
Sheth-Tormen and Press-Schechter mass functions. Needs: numpy, scipy.
Not compared to JWST data (no data files included). Accuracy of the power spectrum: a few percent.
"""
import numpy as np
from scipy.integrate import quad
from scipy.interpolate import interp1d
trap = getattr(np, "trapezoid", None) or np.trapz

h, Om, Ob, ns, s8 = 0.6736, 0.3153, 0.0493, 0.9649, 0.811
Th = 2.7255 / 2.7
rho_m = 2.775e11 * h**2 * Om            # Msun/Mpc^3
DC0 = 1.686

def T_EH(k):                            # k in 1/Mpc
    om, ob, fb = Om*h**2, Ob*h**2, Ob/Om
    s = 44.5*np.log(9.83/om)/np.sqrt(1+10*ob**0.75)
    a = 1-0.328*np.log(431*om)*fb+0.38*np.log(22.3*om)*fb**2
    gam = Om*h*(a+(1-a)/(1+(0.43*k*s)**4))
    q = (k/h)*Th**2/gam
    L = np.log(2*np.e+1.8*q); C = 14.2+731/(1+62.5*q)
    return L/(L+C*q**2)

lnk = np.linspace(np.log(1e-5), np.log(1e3), 6000); k = np.exp(lnk)
Pk = k**ns*T_EH(k)**2
W = lambda x: 3*(np.sin(x)-x*np.cos(x))/x**3
sig2 = lambda R: trap(k**3*Pk*W(k*R)**2/(2*np.pi**2), lnk)
A = s8**2/sig2(8/h)

def D(z):                                # linear growth, normalised to D(0)=1
    E = lambda a: np.sqrt(Om/a**3+(1-Om))
    Dun = lambda a: 2.5*Om*E(a)*quad(lambda x: 1/(x*E(x))**3, 0, a)[0]
    return Dun(1/(1+z))/Dun(1.0)

Ms = np.logspace(6, 14, 300)
Rs = (3*Ms/(4*np.pi*rho_m))**(1/3)
_ls = interp1d(np.log(Ms), np.log([np.sqrt(A*sig2(R)) for R in Rs]))
sigma = lambda M, z: np.exp(_ls(np.log(M)))*D(z)

def dndlnM(M, z, dc=DC0, mf="ST"):
    e = 1e-3
    dls = (np.log(sigma(M*(1+e), z))-np.log(sigma(M/(1+e), z)))/(2*e)
    nu = dc/sigma(M, z)
    if mf == "PS":
        f = np.sqrt(2/np.pi)*nu*np.exp(-nu**2/2)
    else:
        a, p, Aq = 0.707, 0.3, 0.3222
        f = Aq*np.sqrt(2*a/np.pi)*(1+(a*nu**2)**-p)*nu*np.exp(-a*nu**2/2)
    return f*rho_m/M*abs(dls)

def n_gt(M, z, dc, mf):
    Mg = np.logspace(np.log10(M), 13.5, 200)
    return trap([dndlnM(m, z, dc, mf) for m in Mg], np.log(Mg))

if __name__ == "__main__":
    print("Boost in n(>M) when delta_c is lowered by eps   (Sheth-Tormen | Press-Schechter)")
    for z in (10, 15):
        for M in (1e9, 1e10, 1e11):
            row = []
            for eps in (0.02, 0.03, 0.05, 0.10):
                st = n_gt(M, z, DC0*(1-eps), "ST")/n_gt(M, z, DC0, "ST")
                ps = n_gt(M, z, DC0*(1-eps), "PS")/n_gt(M, z, DC0, "PS")
                row.append(f"eps={eps:.2f}: {st:5.2f}|{ps:6.2f}")
            print(f"z={z:2d}  M={M:.0e}  " + "  ".join(row))
    print("\nsigma8(z=0) = %.3f for any delta_c (delta_c does not enter sigma(M))." % np.sqrt(A*sig2(8/h)))
