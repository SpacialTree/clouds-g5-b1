

# Trying to regrid moment 0 maps to compare them.

from astropy.io import fits
from astropy.utils.data import get_pkg_data_filename
from reproject import reproject_interp

from astropy.wcs import WCS
import matplotlib.pyplot as plt


hdu17 = fits.open(get_pkg_data_filename('smoothmom0_17_K.fits'))[0]
hdu29 = fits.open(get_pkg_data_filename('smoothmom0_29_K.fits'))[0]
hdu31 = fits.open(get_pkg_data_filename('smoothmom0_31_K.fits'))[0]


# array is the new image, footprint is what pixels in the new image were in the old one
# array, footprint = reproject_interp(hdu2, hdu1.header)

rpt17, foot17 = reproject_interp('smoothmom0_17_K.fits', hdu29.header)
rpt29, foot29 = reproject_interp(hdu29, hdu31.header)

fits.writeto(filename='rpt17-31.fits', data=rpt17, header=hdu17.header, overwrite=True)
fits.writeto('rpt29-31.fits', rpt29, hdu29.header, overwrite=True)



ax1 = plt.subplot(1,2,1, projection=WCS(hdu17.header))
ax1.imshow(rpt17, origin='lower', vmin=-2.e-4, vmax=5.e-4)
ax1.coords.grid(color='white')
ax1.coords['ra'].set_axislabel('Right Ascension')
ax1.coords['dec'].set_axislabel('Declination')
ax1.set_title('Reprojected spw17 image')


ax1 = plt.subplot(1,2,1, projection=None)
print(rpt17)


fits.writeto(filename='test1.fits', data=rpt17, header=hdu17.header, overwrite=True)
fits.writeto(filename='test1.1.fits', data=foot17, header=hdu17.header, overwrite=True)


imregrid(
                    imagename=etambimage,
                    template=vlaimage,
                    axes=[0, 1],
                    interpolation='cubic',
                    output=regridimage,
                    overwrite=True,
)

'''
imregrid(imagename='', template='',axes=[0,1],interpolation='',output='',overwrite=True)
'''

imregrid(imagename='smoothmom0_17_K.im',template='smoothmom0_31_K.im',axes=[0,1],interpolation='cubic',output='rpt17-31.im',overwrite=True)
imregrid(imagename='smoothmom0_29_K.im',template='smoothmom0_31_K.im',axes=[0,1],interpolation='cubic',output='rpt29-31.im',overwrite=True)



