from numpy import pi,exp,arctan,sqrt,where,array,sum,log10,arange,ones,argmax
from pandas import read_csv
from scipy.special import wofz
# constants
global log_sig,c,RH,wion
log_sig = -14.8247 # classical absorption cross-section in cm^2, b in km/s, w in Ang
c    = 2.99792458e5 # speed of light in km/s
RH   = 1.0973731568e-3 # Rydberg in 1/Ang
# atomic data
# wavelengths and ocilator strengths from 2008RvMP...80..633M
abs = read_csv('./tab/mohr2008_lyman.csv')
# photoionization cross section from 1996ApJ...465..487V
phion = read_csv('./tab/verner1996_photoion.dat',sep='\s+',\
        names=['Z','N','Eth','Emax','E0','sig0','ya','P','yw','y0','y1'])
# Lyman limit from h c / E_ion
wion =  12398.4198/phion['Eth'].values[0]

class LymanTransmission(object):
    def __init__(self,wave,N,Cf,b):
        self.Wavelength  = wave
        self.Trans       = self.trans(wave,N,Cf,b)
    # generalized photoionization cross-section
    # returns a_v in units of 1e-18 cm^2
    def av_sig(self,nu,Z,N,h = 4.135667662e-15):
        i = where((phion['Z'].values==Z)&(phion['N'].values==N))[0]
        x = h*nu/phion['E0'].values[i]-phion['y0'].values[i]
        y = sqrt(x**2+phion['y1'].values[i]**2)
        Fy = ((x-1)**2+phion['yw'][i].values**2)*y**(0.5*phion['P'].values[i]-5.5)*\
                    (1+sqrt(y/phion['ya'].values[i]))**-phion['P'].values[i]
        anu = phion['sig0'].values[i]*Fy
        return anu
    # H I transmission in the FUV and EUV
    # given H I column density (in log[cm^-2] ) and covering fraction,
    # and the gas velocity (in [km s^-1])
    def trans(self,w,N,Cf,b):
        # bound-free optical depth (photoionization)
        pha = self.av_sig(c*1e13/w,1,1)
        # bound-bound optical depth (absorption)
        # recalling that optical depth is additive, not multiplicative
        # so that all line profiles are co-added
        phi = array([wofz((w/abs['wave'].values[i]-1)*c/b).real *
                abs['f'].values[i]*abs['wave'].values[i]/b \
                for i in abs.index]).sum(axis=0)
        tau = phi * 10.**(N+log_sig)
        # below Lyman limit, bound-free, above Lyman limit, bound-bound
        tau[w<wion] = pha[w<wion] * 10.**(N-18)
        # interpolate over region not covered by atomic data
        # accounting for the gas velocity
        imin = argmax(w[w<1/RH])
        imax = argmax(phi[w<abs['wave'].values[-1]*(1+5*b/c)])
        m = (phi[imax]*10.**(N+log_sig)-pha[imin]*10.**(N-18))/(w[imax]-w[imin])
        b = pha[imin]*10.**(N-18) - m*w[imin]
        tau[imin:imax] = m*w[imin:imax]+b
        # return transmission, accounting for C
        return Cf*exp(-tau)+1-Cf
