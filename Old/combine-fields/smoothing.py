'''
imsmooth(imagename='', targetres=True, major='40arcsec', minor='40arcsec', pa=0, outfile='')
immath(imagename='', mode='evalexpr', expr='1.222e6*IM0/F^2/40^2', outfile='')
imhead(imagename='smoothmom0_17_K.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
imregrid(imagename='', template='',axes=[0,1],interpolation='',output='',overwrite=True)
#Always check 3 sig values
immath(imagename=['rpt17-31.im','rpt29-31.im'], mode='evalexpr', expr='(IM0/IM1) [IM0>190.0 && IM1>26.0]', outfile='ratio_12CO-13CO.im')
imhead(imagename='ratio_12CO-13CO.im', mode='put', hdkey='bunit', hdvalue='')
'''

imsmooth(imagename='spw17_12CO/g5.mom0.tot.12CO.spw17.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw17_12CO/g5.mom0.sm.tot.12CO.spw17.im')
imsmooth(imagename='spw21_CH3OH/g5.mom0.tot.CH3OH.spw21.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw21_CH3OH/g5.mom0.sm.tot.CH3OH.spw21.im')
imsmooth(imagename='spw23_H2CO/g5.mom0.tot.H2CO.spw23.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw23_H2CO/g5.mom0.sm.tot.H2CO.spw23.im')
imsmooth(imagename='spw23_OCS/g5.mom0.tot.OCS.spw23.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw23_OCS/g5.mom0.sm.tot.OCS.spw23.im')
imsmooth(imagename='spw25_H2CO/g5.mom0.tot.H2CO.spw25.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw25_H2CO/g5.mom0.sm.tot.H2CO.spw25.im')
imsmooth(imagename='spw27_SiO/g5.mom0.tot.SiO.spw27.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw27_SiO/g5.mom0.sm.tot.SiO.spw27.im')
imsmooth(imagename='spw29_13CO/g5.mom0.tot.13CO.spw29.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw29_13CO/g5.mom0.sm.tot.13CO.spw29.im')
imsmooth(imagename='spw31_C18O/g5.mom0.tot.C18O.spw31.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw31_C18O/g5.mom0.sm.tot.C18O.spw31.im')

#12CO
immath(imagename='spw17_12CO/g5.mom0.sm.tot.12CO.spw17.im', mode='evalexpr', expr='1.222e6*IM0/230.538000^2/40^2', outfile='spw17_12CO/g5.mom0.smK.tot.12CO.spw17.im')
#CH3OH
immath(imagename='spw21_CH3OH/g5.mom0.sm.tot.CH3OH.spw21.im', mode='evalexpr', expr='1.222e6*IM0/218.44005^2/40^2', outfile='spw21_CH3OH/g5.mom0.smK.tot.CH3OH.spw21.im')
#H2CO spw23
immath(imagename='spw23_H2CO/g5.mom0.sm.tot.H2CO.spw23.im', mode='evalexpr', expr='1.222e6*IM0/218.760066^2/40^2', outfile='spw23_H2CO/g5.mom0.smK.tot.H2CO.spw23.im')
#OCS 
immath(imagename='spw23_OCS/g5.mom0.sm.tot.OCS.spw23.im', mode='evalexpr', expr='1.222e6*IM0/218.903355^2/40^2', outfile='spw23_OCS/g5.mom0.smK.tot.OCS.spw23.im')
#H2CO spw25
immath(imagename='spw25_H2CO/g5.mom0.sm.tot.H2CO.spw25.im', mode='evalexpr', expr='1.222e6*IM0/218.222192^2/40^2', outfile='spw25_H2CO/g5.mom0.smK.tot.H2CO.spw25.im')
#SiO
immath(imagename='spw27_SiO/g5.mom0.sm.tot.SiO.spw27.im', mode='evalexpr', expr='1.222e6*IM0/217.104980^2/40^2', outfile='spw27_SiO/g5.mom0.smK.tot.SiO.spw27.im')
#13CO
immath(imagename='spw29_13CO/g5.mom0.sm.tot.13CO.spw29.im', mode='evalexpr', expr='1.222e6*IM0/220.398684^2/40^2', outfile='spw29_13CO/g5.mom0.smK.tot.13CO.spw29.im')
#C18O
immath(imagename='spw31_C18O/g5.mom0.sm.tot.C18O.spw31.im', mode='evalexpr', expr='1.222e6*IM0/219.560358^2/40^2', outfile='spw31_C18O/g5.mom0.smK.tot.C18O.spw31.im')

imhead(imagename='spw17_12CO/g5.mom0.smK.tot.12CO.spw17.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
imhead(imagename='spw21_CH3OH/g5.mom0.smK.tot.CH3OH.spw21.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
imhead(imagename='spw23_H2CO/g5.mom0.smK.tot.H2CO.spw23.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
imhead(imagename='spw23_OCS/g5.mom0.smK.tot.OCS.spw23.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
imhead(imagename='spw25_H2CO/g5.mom0.smK.tot.H2CO.spw25.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
imhead(imagename='spw27_SiO/g5.mom0.smK.tot.SiO.spw27.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
imhead(imagename='spw29_13CO/g5.mom0.smK.tot.13CO.spw29.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
imhead(imagename='spw31_C18O/g5.mom0.smK.tot.C18O.spw31.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
