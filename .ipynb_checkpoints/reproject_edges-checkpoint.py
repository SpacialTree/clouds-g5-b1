from spectral_cube import SpectralCube
import numpy as np
import matplotlib.pyplot as plt

# Read in a spectral cube
cubename = '/orange/adamginsburg/cmz/g5/G5/sum/newcombination/g5.H2CO.spw23_test.fits' # Example data
cube = SpectralCube.read(cubename)

mom0 = cube.moment0()
repro_mom0 = mom0.reproject(mom0.header)

mom0_mask = np.isfinite(mom0)
repro_mom0_mask = np.isfinite(repro_mom0)

edges = np.logical_xor(mom0_mask, repro_mom0_mask)

plt.imshow(edges)