# LymanTrans
Calculates H I Lyman transmission function for given column density, 
covering fraction, and Doppler velocity width

## Example Usage

Below are three different H I Lyman transmission functions which all
roughly give a Lyman continuum escape fraction of 50 % between 870 
and 900 Angstroms but produce different absorption line profiles.

``` python
from LymanTrans import *
from numpy import linspace
wave = linspace(800,1250,451)
# transmission object for N ~ 10^17 cm^-2, Cf = 1, b = 100 km s^-1
T1 = LymanTransmission(wave,17.0627,1.00,100).trans
# transmission object for N ~ 10^17.35 cm^-2, Cf = 0.65, b = 100 km s^-1
T2 = LymanTransmission(wave,17.3637,0.65,100).trans
# transmission object for N = 10^19 cm^-2, Cf = 0.5, b = 100 km s^-1
T3 = LymanTransmission(wave,19.0000,0.50,100).trans
```

Below are visualized the three different transmission functions.

<img width="480" alt="image of three different H I Lyman transmission functions for LyC escape of 50%" src="https://github.com/sflury/LymanTrans/blob/main/hi_lyman50.png">

## References

While this code is provided publicly, it did require quite a bit of effort to develop 
and document. I request that any use thereof be cited in any publications in which 
this code is used. Please cite it accordingly using the BibTeX provided below.

``` bibtex
@SOFTWARE{LymanTrans,
       author = {{Flury}, Sophia R.,
        title = "{LymanTrans}",
         year = 2025,
        month = jan,
      version = {0.1},
          url = {https://github.com/sflury/LymanTrans},
          doi = {10.5281/zenodo.14731368} }
```

The Zenodo DOI is also available here:

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.14731368.svg)](https://doi.org/10.5281/zenodo.14731368)


This transmission function uses the photoionization cross-sections from 
Verner et al. 1996 and atomic data from Mohr et al. 2008 (with optional
atomic data from Morton et al. 2003 in place of Mohr et al 2008).

### Verner et al. 1996
``` bibtex
@ARTICLE{1996ApJ...465..487V,
       author = {{Verner}, D.~A. and {Ferland}, G.~J. and {Korista}, K.~T. and {Yakovlev}, D.~G.},
        title = "{Atomic Data for Astrophysics. II. New Analytic Fits for Photoionization Cross Sections of Atoms and Ions}",
      journal = {\apj},
     keywords = {ATOMIC DATA, ATOMIC PROCESSES, Astrophysics, Physics - Atomic Physics},
         year = 1996,
        month = jul,
       volume = {465},
        pages = {487},
          doi = {10.1086/177435},
archivePrefix = {arXiv},
       eprint = {astro-ph/9601009},
 primaryClass = {astro-ph},
       adsurl = {https://ui.adsabs.harvard.edu/abs/1996ApJ...465..487V},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```

### Mohr et al. 2008
``` bibtex
@ARTICLE{2008RvMP...80..633M,
       author = {{Mohr}, Peter J. and {Taylor}, Barry N. and {Newell}, David B.},
        title = "{CODATA recommended values of the fundamental physical constants: 2006}",
      journal = {Reviews of Modern Physics},
     keywords = {06.20.Jr, 12.20.-m, Determination of fundamental constants, Quantum electrodynamics, Physics - Atomic Physics, Physics - Chemical Physics, Physics - Data Analysis, Statistics and Probability},
         year = 2008,
        month = apr,
       volume = {80},
       number = {2},
        pages = {633-730},
          doi = {10.1103/RevModPhys.80.633},
archivePrefix = {arXiv},
       eprint = {0801.0028},
 primaryClass = {physics.atom-ph},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2008RvMP...80..633M},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```

### Morton 2003
``` bibtex
@ARTICLE{2003ApJS..149..205M,
       author = {{Morton}, Donald C.},
        title = "{Atomic Data for Resonance Absorption Lines. III. Wavelengths Longward of the Lyman Limit for the Elements Hydrogen to Gallium}",
      journal = {\apjs},
     keywords = {Atomic Data, ISM: Atoms, Galaxies: Quasars: Absorption Lines, Stars: Atmospheres, Ultraviolet: General},
         year = 2003,
        month = nov,
       volume = {149},
       number = {1},
        pages = {205-238},
          doi = {10.1086/377639},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2003ApJS..149..205M},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```
## Licensing
This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.
