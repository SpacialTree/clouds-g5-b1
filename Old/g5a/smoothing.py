###12CO
#Total
imsmooth(imagename='spw17_12CO/g5a.mom0.tot.12CO.spw17.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw17_12CO/g5a.mom0.sm.tot.12CO.spw17.im')
immath(imagename='spw17_12CO/g5a.mom0.sm.tot.12CO.spw17.im', mode='evalexpr', expr='1.222e6*IM0/230.538000^2/40^2', outfile='spw17_12CO/g5a.mom0.smK.tot.12CO.spw17.im')
imhead(imagename='spw17_12CO/g5a.mom0.smK.tot.12CO.spw17.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
#Right
imsmooth(imagename='spw17_12CO/g5a.mom0.R.12CO.spw17.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw17_12CO/g5a.mom0.sm.R.12CO.spw17.im')
immath(imagename='spw17_12CO/g5a.mom0.sm.R.12CO.spw17.im', mode='evalexpr', expr='1.222e6*IM0/230.538000^2/40^2', outfile='spw17_12CO/g5a.mom0.smK.R.12CO.spw17.im')
imhead(imagename='spw17_12CO/g5a.mom0.smK.R.12CO.spw17.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
#Left
imsmooth(imagename='spw17_12CO/g5a.mom0.L.12CO.spw17.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw17_12CO/g5a.mom0.sm.L.12CO.spw17.im')
immath(imagename='spw17_12CO/g5a.mom0.sm.L.12CO.spw17.im', mode='evalexpr', expr='1.222e6*IM0/230.538000^2/40^2', outfile='spw17_12CO/g5a.mom0.smK.L.12CO.spw17.im')
imhead(imagename='spw17_12CO/g5a.mom0.smK.L.12CO.spw17.im', mode='put', hdkey='bunit', hdvalue='K.km/s')

###CH3OH
#Total
imsmooth(imagename='spw21_CH3OH/g5a.mom0.tot.CH3OH.spw21.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw21_CH3OH/g5a.mom0.sm.tot.CH3OH.spw21.im')
immath(imagename='spw21_CH3OH/g5a.mom0.sm.tot.CH3OH.spw21.im', mode='evalexpr', expr='1.222e6*IM0/218.44005^2/40^2', outfile='spw21_CH3OH/g5a.mom0.smK.tot.CH3OH.spw21.im')
imhead(imagename='spw21_CH3OH/g5a.mom0.smK.tot.CH3OH.spw21.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
#Right
imsmooth(imagename='spw21_CH3OH/g5a.mom0.R.CH3OH.spw21.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw21_CH3OH/g5a.mom0.sm.R.CH3OH.spw21.im')
immath(imagename='spw21_CH3OH/g5a.mom0.sm.R.CH3OH.spw21.im', mode='evalexpr', expr='1.222e6*IM0/218.44005^2/40^2', outfile='spw21_CH3OH/g5a.mom0.smK.R.CH3OH.spw21.im')
imhead(imagename='spw21_CH3OH/g5a.mom0.smK.R.CH3OH.spw21.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
#Left
imsmooth(imagename='spw21_CH3OH/g5a.mom0.L.CH3OH.spw21.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw21_CH3OH/g5a.mom0.sm.L.CH3OH.spw21.im')
immath(imagename='spw21_CH3OH/g5a.mom0.sm.L.CH3OH.spw21.im', mode='evalexpr', expr='1.222e6*IM0/218.44005^2/40^2', outfile='spw21_CH3OH/g5a.mom0.smK.L.CH3OH.spw21.im')
imhead(imagename='spw21_CH3OH/g5a.mom0.smK.L.CH3OH.spw21.im', mode='put', hdkey='bunit', hdvalue='K.km/s')

###H2CO spw23
#Total
imsmooth(imagename='spw23_H2CO/g5a.mom0.tot.H2CO.spw23.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw23_H2CO/g5a.mom0.sm.tot.H2CO.spw23.im')
immath(imagename='spw23_H2CO/g5a.mom0.sm.tot.H2CO.spw23.im', mode='evalexpr', expr='1.222e6*IM0/218.760066^2/40^2', outfile='spw23_H2CO/g5a.mom0.smK.tot.H2CO.spw23.im')
imhead(imagename='spw23_H2CO/g5a.mom0.smK.tot.H2CO.spw23.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
#Right
imsmooth(imagename='spw23_H2CO/g5a.mom0.R.H2CO.spw23.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw23_H2CO/g5a.mom0.sm.R.H2CO.spw23.im')
immath(imagename='spw23_H2CO/g5a.mom0.sm.R.H2CO.spw23.im', mode='evalexpr', expr='1.222e6*IM0/218.760066^2/40^2', outfile='spw23_H2CO/g5a.mom0.smK.R.H2CO.spw23.im')
imhead(imagename='spw23_H2CO/g5a.mom0.smK.R.H2CO.spw23.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
#Left
imsmooth(imagename='spw23_H2CO/g5a.mom0.L.H2CO.spw23.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw23_H2CO/g5a.mom0.sm.L.H2CO.spw23.im')
immath(imagename='spw23_H2CO/g5a.mom0.sm.L.H2CO.spw23.im', mode='evalexpr', expr='1.222e6*IM0/218.760066^2/40^2', outfile='spw23_H2CO/g5a.mom0.smK.L.H2CO.spw23.im')
imhead(imagename='spw23_H2CO/g5a.mom0.smK.L.H2CO.spw23.im', mode='put', hdkey='bunit', hdvalue='K.km/s')

###OCS
#Total
imsmooth(imagename='spw23_OCS/g5a.mom0.tot.OCS.spw23.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw23_OCS/g5a.mom0.sm.tot.OCS.spw23.im')
immath(imagename='spw23_OCS/g5a.mom0.sm.tot.OCS.spw23.im', mode='evalexpr', expr='1.222e6*IM0/218.903355^2/40^2', outfile='spw23_OCS/g5a.mom0.smK.tot.OCS.spw23.im')
imhead(imagename='spw23_OCS/g5a.mom0.smK.tot.OCS.spw23.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
#Right
imsmooth(imagename='spw23_OCS/g5a.mom0.R.OCS.spw23.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw23_OCS/g5a.mom0.sm.R.OCS.spw23.im')
immath(imagename='spw23_OCS/g5a.mom0.sm.R.OCS.spw23.im', mode='evalexpr', expr='1.222e6*IM0/218.903355^2/40^2', outfile='spw23_OCS/g5a.mom0.smK.R.OCS.spw23.im')
imhead(imagename='spw23_OCS/g5a.mom0.smK.R.OCS.spw23.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
#Left
imsmooth(imagename='spw23_OCS/g5a.mom0.L.OCS.spw23.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw23_OCS/g5a.mom0.sm.L.OCS.spw23.im')
immath(imagename='spw23_OCS/g5a.mom0.sm.L.OCS.spw23.im', mode='evalexpr', expr='1.222e6*IM0/218.903355^2/40^2', outfile='spw23_OCS/g5a.mom0.smK.L.OCS.spw23.im')
imhead(imagename='spw23_OCS/g5a.mom0.smK.L.OCS.spw23.im', mode='put', hdkey='bunit', hdvalue='K.km/s')

###H2CO spw25
#Total
imsmooth(imagename='spw25_H2CO/g5a.mom0.tot.H2CO.spw25.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw25_H2CO/g5a.mom0.sm.tot.H2CO.spw25.im')
immath(imagename='spw25_H2CO/g5a.mom0.sm.tot.H2CO.spw25.im', mode='evalexpr', expr='1.222e6*IM0/218.222192^2/40^2', outfile='spw25_H2CO/g5a.mom0.smK.tot.H2CO.spw25.im')
imhead(imagename='spw25_H2CO/g5a.mom0.smK.tot.H2CO.spw25.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
#Right
imsmooth(imagename='spw25_H2CO/g5a.mom0.R.H2CO.spw25.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw25_H2CO/g5a.mom0.sm.R.H2CO.spw25.im')
immath(imagename='spw25_H2CO/g5a.mom0.sm.R.H2CO.spw25.im', mode='evalexpr', expr='1.222e6*IM0/218.222192^2/40^2', outfile='spw25_H2CO/g5a.mom0.smK.R.H2CO.spw25.im')
imhead(imagename='spw25_H2CO/g5a.mom0.smK.R.H2CO.spw25.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
#Left
imsmooth(imagename='spw25_H2CO/g5a.mom0.L.H2CO.spw25.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw25_H2CO/g5a.mom0.sm.L.H2CO.spw25.im')
immath(imagename='spw25_H2CO/g5a.mom0.sm.L.H2CO.spw25.im', mode='evalexpr', expr='1.222e6*IM0/218.222192^2/40^2', outfile='spw25_H2CO/g5a.mom0.smK.L.H2CO.spw25.im')
imhead(imagename='spw25_H2CO/g5a.mom0.smK.L.H2CO.spw25.im', mode='put', hdkey='bunit', hdvalue='K.km/s')

###SiO
#Total
imsmooth(imagename='spw27_SiO/g5a.mom0.tot.SiO.spw27.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw27_SiO/g5a.mom0.sm.tot.SiO.spw27.im')
immath(imagename='spw27_SiO/g5a.mom0.sm.tot.SiO.spw27.im', mode='evalexpr', expr='1.222e6*IM0/217.104980^2/40^2', outfile='spw27_SiO/g5a.mom0.smK.tot.SiO.spw27.im')
imhead(imagename='spw27_SiO/g5a.mom0.smK.tot.SiO.spw27.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
#Right
imsmooth(imagename='spw27_SiO/g5a.mom0.R.SiO.spw27.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw27_SiO/g5a.mom0.sm.R.SiO.spw27.im')
immath(imagename='spw27_SiO/g5a.mom0.sm.R.SiO.spw27.im', mode='evalexpr', expr='1.222e6*IM0/217.104980^2/40^2', outfile='spw27_SiO/g5a.mom0.smK.R.SiO.spw27.im')
imhead(imagename='spw27_SiO/g5a.mom0.smK.R.SiO.spw27.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
#Left
imsmooth(imagename='spw27_SiO/g5a.mom0.L.SiO.spw27.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw27_SiO/g5a.mom0.sm.L.SiO.spw27.im')
immath(imagename='spw27_SiO/g5a.mom0.sm.L.SiO.spw27.im', mode='evalexpr', expr='1.222e6*IM0/217.104980^2/40^2', outfile='spw27_SiO/g5a.mom0.smK.L.SiO.spw27.im')
imhead(imagename='spw27_SiO/g5a.mom0.smK.L.SiO.spw27.im', mode='put', hdkey='bunit', hdvalue='K.km/s')

###13CO
#Total
imsmooth(imagename='spw29_13CO/g5a.mom0.tot.13CO.spw29.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw29_13CO/g5a.mom0.sm.tot.13CO.spw29.im')
immath(imagename='spw29_13CO/g5a.mom0.sm.tot.13CO.spw29.im', mode='evalexpr', expr='1.222e6*IM0/220.398684^2/40^2', outfile='spw29_13CO/g5a.mom0.smK.tot.13CO.spw29.im')
imhead(imagename='spw29_13CO/g5a.mom0.smK.tot.13CO.spw29.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
#Right
imsmooth(imagename='spw29_13CO/g5a.mom0.R.13CO.spw29.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw29_13CO/g5a.mom0.sm.R.13CO.spw29.im')
immath(imagename='spw29_13CO/g5a.mom0.sm.R.13CO.spw29.im', mode='evalexpr', expr='1.222e6*IM0/220.398684^2/40^2', outfile='spw29_13CO/g5a.mom0.smK.R.13CO.spw29.im')
imhead(imagename='spw29_13CO/g5a.mom0.smK.R.13CO.spw29.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
#Left
imsmooth(imagename='spw29_13CO/g5a.mom0.L.13CO.spw29.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw29_13CO/g5a.mom0.sm.L.13CO.spw29.im')
immath(imagename='spw29_13CO/g5a.mom0.sm.L.13CO.spw29.im', mode='evalexpr', expr='1.222e6*IM0/220.398684^2/40^2', outfile='spw29_13CO/g5a.mom0.smK.L.13CO.spw29.im')
imhead(imagename='spw29_13CO/g5a.mom0.smK.L.13CO.spw29.im', mode='put', hdkey='bunit', hdvalue='K.km/s')

###C18O
#Total
imsmooth(imagename='spw31_C18O/g5a.mom0.tot.C18O.spw31.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw31_C18O/g5a.mom0.sm.tot.C18O.spw31.im')
immath(imagename='spw31_C18O/g5a.mom0.sm.tot.C18O.spw31.im', mode='evalexpr', expr='1.222e6*IM0/219.560358^2/40^2', outfile='spw31_C18O/g5a.mom0.smK.tot.C18O.spw31.im')
imhead(imagename='spw31_C18O/g5a.mom0.smK.tot.C18O.spw31.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
#Right
imsmooth(imagename='spw31_C18O/g5a.mom0.R.C18O.spw31.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw31_C18O/g5a.mom0.sm.R.C18O.spw31.im')
immath(imagename='spw31_C18O/g5a.mom0.sm.R.C18O.spw31.im', mode='evalexpr', expr='1.222e6*IM0/219.560358^2/40^2', outfile='spw31_C18O/g5a.mom0.smK.R.C18O.spw31.im')
imhead(imagename='spw31_C18O/g5a.mom0.smK.R.C18O.spw31.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
#Left
imsmooth(imagename='spw31_C18O/g5a.mom0.L.C18O.spw31.im', targetres=True, major='35arcsec', minor='35arcsec', pa=0, outfile='spw31_C18O/g5a.mom0.sm.L.C18O.spw31.im')
immath(imagename='spw31_C18O/g5a.mom0.sm.L.C18O.spw31.im', mode='evalexpr', expr='1.222e6*IM0/219.560358^2/40^2', outfile='spw31_C18O/g5a.mom0.smK.L.C18O.spw31.im')
imhead(imagename='spw31_C18O/g5a.mom0.smK.L.C18O.spw31.im', mode='put', hdkey='bunit', hdvalue='K.km/s')

