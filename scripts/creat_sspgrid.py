import pickle
from alf_vars import *
from astropy.io import ascii as astro_ascii
import copy, numpy as np, pandas as pd
from linterp import *
import scipy
from scipy import constants

from velbroad import *
from set_pinit_priors import *
from setup import setup
from vacairconv import *
from read_data import read_data
from getm2l import getm2l
from getmass import getmass
from getmodel import getmodel
from contnormspec import contnormspec
from getvelz import getvelz
from str2arr import str2arr


alfvar = ALFVAR()
alfvar.filename = 'ldss3_Mar16v_n1600_Re4_wave3'
alfvar = read_data(alfvar)
alfvar.imf_type = 3
alfvar = setup(alfvar, onlybasic = True)
pickle.dump(alfvar, open('alfvar_sspgrid_irldss3_imftype3.p', "wb" ) )
