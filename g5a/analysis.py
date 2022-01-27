'''
imsmooth(imagename='', targetres=True, major='40arcsec', minor='40arcsec', pa=0, outfile='')
immath(imagename='', mode='evalexpr', expr='1.222e6*IM0/F^2/40^2', outfile='')
imhead(imagename='smoothmom0_17_K.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
imregrid(imagename='', template='',axes=[0,1],interpolation='',output='',overwrite=True)
#Always check 3 sig values
immath(imagename=['rpt17-31.im','rpt29-31.im'], mode='evalexpr', expr='(IM0/IM1) [IM0>190.0 && IM1>26.0]', outfile='ratio_12CO-13CO.im')
imhead(imagename='ratio_12CO-13CO.im', mode='put', hdkey='bunit', hdvalue='')

immath(imagename='smoothmom0_17.im', mode='evalexpr', expr='1.222e6*IM0/230.538000^2/40^2', outfile='smoothmom0_17_K.im')
immath(imagename='smoothmom0_29.im', mode='evalexpr', expr='1.222e6*IM0/220.398684^2/40^2', outfile='smoothmom0_29_K.im')
immath(imagename='smoothmom0_31.im', mode='evalexpr', expr='1.222e6*IM0/219.560358^2/40^2', outfile='smoothmom0_31_K.im')
immath(imagename='smoothmom0_21.im', mode='evalexpr', expr='1.222e6*IM0/218.44005^2/40^2', outfile='smoothmom0_21_K.im')
immath(imagename='smoothmom0_23.im', mode='evalexpr', expr='1.222e6*IM0/218.760066^2/40^2', outfile='smoothmom0_23_K.im')
immath(imagename='smoothmom0_25.im', mode='evalexpr', expr='1.222e6*IM0/218.222192^2/40^2', outfile='smoothmom0_25_K.im')
immath(imagename='smoothmom0_27.im', mode='evalexpr', expr='1.222e6*IM0/217.104980^2/40^2', outfile='smoothmom0_27_K.im')
'''
### Left Side
immoments(imagename='spw23_H2CO/g5a.H2CO.spw23.im',moments=[0],chans='294~511',outfile='analysis/g5a.mom0.L.H2CO.spw23.im')
immoments(imagename='spw25_H2CO/g5a.H2CO.spw25.im',moments=[0],chans='294~511',outfile='analysis/g5a.mom0.L.H2CO.spw25.im')
imsmooth(imagename='analysis/g5a.mom0.L.H2CO.spw23.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='analysis/mom0.L.smo.H2CO.spw23.im')
imsmooth(imagename='analysis/g5a.mom0.L.H2CO.spw25.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='analysis/mom0.L.smo.H2CO.spw25.im')

immath(imagename='analysis/mom0.L.smo.H2CO.spw23.im', mode='evalexpr', expr='1.222e6*IM0/218.760066^2/40^2', outfile='analysis/mom0.L.smoK.H2CO.spw23.im')
immath(imagename='analysis/mom0.L.smo.H2CO.spw25.im', mode='evalexpr', expr='1.222e6*IM0/218.222192^2/40^2', outfile='analysis/mom0.L.smoK.H2CO.spw25.im')

imhead(imagename='analysis/mom0.L.smoK.H2CO.spw23.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
imhead(imagename='analysis/mom0.L.smoK.H2CO.spw25.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
#see if them being gridded to galactic takes care of it
imregrid(imagename='analysis/mom0.L.smoK.H2CO.spw23.im', template='analysis/mom0.L.smoK.H2CO.spw25.im',axes=[0,1],interpolation='cubic',output='analysis/23t25.L.im',overwrite=True)
## check 3 sigma
immath(imagename=['analysis/23t25.L.im','analysis/mom0.L.smoK.H2CO.spw25.im'], mode='evalexpr', expr='IM0 / IM1 [IM0>0.25&&IM1>0.6]', outfile='analysis/smoothratio.L.im')
imhead(imagename='analysis/smoothratio.L.im', mode='put', hdkey='bunit', hdvalue='')
immath(imagename='analysis/smoothratio.L.im', mode='evalexpr', expr='(590 * IM0^2 + 2.88 * IM0 + 23.4)', outfile='analysis/smoothtemp.L.im')
imhead(imagename='analysis/smoothtemp.L.im', mode='put', hdkey='bunit', hdvalue='K')

### Right Side
immoments(imagename='spw23_H2CO/g5a.H2CO.spw23.im',moments=[0],chans='198~294',outfile='analysis/g5a.mom0.R.H2CO.spw23.im')
immoments(imagename='spw25_H2CO/g5a.H2CO.spw25.im',moments=[0],chans='198~294',outfile='analysis/g5a.mom0.R.H2CO.spw25.im')
imsmooth(imagename='analysis/g5a.mom0.R.H2CO.spw23.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='analysis/mom0.R.smo.H2CO.spw23.im')
imsmooth(imagename='analysis/g5a.mom0.R.H2CO.spw25.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='analysis/mom0.R.smo.H2CO.spw25.im')

immath(imagename='analysis/mom0.R.smo.H2CO.spw23.im', mode='evalexpr', expr='1.222e6*IM0/218.760066^2/40^2', outfile='analysis/mom0.R.smoK.H2CO.spw23.im')
immath(imagename='analysis/mom0.R.smo.H2CO.spw25.im', mode='evalexpr', expr='1.222e6*IM0/218.222192^2/40^2', outfile='analysis/mom0.R.smoK.H2CO.spw25.im')

imhead(imagename='analysis/mom0.R.smoK.H2CO.spw23.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
imhead(imagename='analysis/mom0.R.smoK.H2CO.spw25.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
#see if them being gridded to galactic takes care of it
imregrid(imagename='analysis/mom0.R.smoK.H2CO.spw23.im', template='analysis/mom0.R.smoK.H2CO.spw25.im',axes=[0,1],interpolation='cubic',output='analysis/23t25.R.im',overwrite=True)
## check 3 sigma
immath(imagename=['analysis/23t25.R.im','analysis/mom0.R.smoK.H2CO.spw25.im'], mode='evalexpr', expr='IM0 / IM1 [IM0>0.15&&IM1>0.5]', outfile='analysis/smoothratio.R.im')
imhead(imagename='analysis/smoothratio.R.im', mode='put', hdkey='bunit', hdvalue='')

immath(imagename='analysis/smoothratio.R.im', mode='evalexpr', expr='(590 * IM0^2 + 2.88 * IM0 + 23.4)', outfile='analysis/smoothtemp.R.im')
imhead(imagename='analysis/smoothtemp.R.im', mode='put', hdkey='bunit', hdvalue='K')

### Total Area
immoments(imagename='spw23_H2CO/g5a.H2CO.spw23.im',moments=[0],chans='198~447',outfile='analysis/g5a.mom0.tot.H2CO.spw23.im')
immoments(imagename='spw25_H2CO/g5a.H2CO.spw25.im',moments=[0],chans='198~447',outfile='analysis/g5a.mom0.tot.H2CO.spw25.im')

imsmooth(imagename='analysis/g5a.mom0.tot.H2CO.spw23.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='analysis/mom0.tot.smo.H2CO.spw23.im')
imsmooth(imagename='analysis/g5a.mom0.tot.H2CO.spw25.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='analysis/mom0.tot.smo.H2CO.spw25.im')

immath(imagename='analysis/mom0.tot.smo.H2CO.spw23.im', mode='evalexpr', expr='1.222e6*IM0/218.760066^2/40^2', outfile='analysis/mom0.tot.smoK.H2CO.spw23.im')
immath(imagename='analysis/mom0.tot.smo.H2CO.spw25.im', mode='evalexpr', expr='1.222e6*IM0/218.222192^2/40^2', outfile='analysis/mom0.tot.smoK.H2CO.spw25.im')

imhead(imagename='analysis/mom0.tot.smoK.H2CO.spw23.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
imhead(imagename='analysis/mom0.tot.smoK.H2CO.spw25.im', mode='put', hdkey='bunit', hdvalue='K.km/s')

#imregrid(imagename='', template='',axes=[0,1],interpolation='',output='',overwrite=True)
#imregrid(imagename='smoothed_mom0_23_K.im', template='smoothed_mom0_25_K.im',axes=[0,1],interpolation='cubic',output='23t25.im',overwrite=True)

#see if them being gridded to galactic takes care of it
imregrid(imagename='analysis/mom0.tot.smoK.H2CO.spw23.im', template='analysis/mom0.tot.smoK.H2CO.spw25.im',axes=[0,1],interpolation='cubic',output='analysis/23t25.tot.im',overwrite=True)
##check 3 sigma
immath(imagename=['analysis/23t25.tot.im','analysis/mom0.tot.smoK.H2CO.spw25.im'], mode='evalexpr', expr='IM0 / IM1 [IM0>0.2&&IM1>1.4]', outfile='analysis/smoothratio.tot.im')
imhead(imagename='analysis/smoothratio.tot.im', mode='put', hdkey='bunit', hdvalue='')

immath(imagename='analysis/smoothratio.tot.im', mode='evalexpr', expr='(590 * IM0^2 + 2.88 * IM0 + 23.4)', outfile='analysis/smoothtemp.tot.im')
imhead(imagename='analysis/smoothtemp.tot.im', mode='put', hdkey='bunit', hdvalue='K')
