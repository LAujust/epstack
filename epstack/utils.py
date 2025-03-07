import requests
import numpy as np
import pandas as pd
import subprocess
import os,sys, glob
import matplotlib.pyplot as plt
from astropy.stats import bayesian_blocks
from astropy.io import fits
from astropy.coordinates import SkyCoord
import astropy.units as u
import re