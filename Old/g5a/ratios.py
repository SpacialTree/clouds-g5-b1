imregrid(imagename='spw17_12CO/g5a.mom0.smK.L.12CO.spw17.im', template='spw29_13CO/g5a.mom0.smK.L.13CO.spw29.im',axes=[0,1],interpolation='cubic',output='ratios/g5a.smK29.L.12CO.spw17.im')
imregrid(imagename='spw21_CH3OH/g5a.mom0.smK.L.CH3OH.spw21.im', template='spw29_13CO/g5a.mom0.smK.L.13CO.spw29.im',axes=[0,1],interpolation='cubic',output='ratios/g5a.smK29.L.CH3OH.spw21.im')
imregrid(imagename='spw23_H2CO/g5a.mom0.smK.L.H2CO.spw23.im', template='spw29_13CO/g5a.mom0.smK.L.13CO.spw29.im',axes=[0,1],interpolation='cubic',output='ratios/g5a.smK29.L.H2CO.spw23.im')
imregrid(imagename='spw23_OCS/g5a.mom0.smK.L.OCS.spw23.im', template='spw29_13CO/g5a.mom0.smK.L.13CO.spw29.im',axes=[0,1],interpolation='cubic',output='ratios/g5a.smK29.L.OCS.spw23.im')
imregrid(imagename='spw25_H2CO/g5a.mom0.smK.L.H2CO.spw25.im', template='spw29_13CO/g5a.mom0.smK.L.13CO.spw29.im',axes=[0,1],interpolation='cubic',output='ratios/g5a.smK29.L.H2CO.spw25.im')
imregrid(imagename='spw27_SiO/g5a.mom0.smK.L.SiO.spw27.im', template='spw29_13CO/g5a.mom0.smK.L.13CO.spw29.im',axes=[0,1],interpolation='cubic',output='ratios/g5a.smK29.L.SiO.spw27.im')
imregrid(imagename='spw31_C18O/g5a.mom0.smK.L.C18O.spw31.im', template='spw29_13CO/g5a.mom0.smK.L.13CO.spw29.im',axes=[0,1],interpolation='cubic',output='ratios/g5a.smK29.L.C18O.spw31.im')
#[IM0>0.2&&IM1>6.0]
##### measure to 3sigma or something
immath(imagename=['ratios/g5a.smK29.R.12CO.spw17.im','ratios/g5a.smK29.R.13CO.spw29.im'], mode='evalexpr', expr='IM0/IM1 [IM1>2.0]', outfile='ratios/ratio.R.12CO-13CO.im')
immath(imagename=['ratios/g5a.smK29.R.12CO.spw17.im','ratios/g5a.smK29.R.C18O.spw31.im'], mode='evalexpr', expr='IM0/IM1 [IM1>0.1]', outfile='ratios/ratio.R.12CO-C18O.im')
immath(imagename=['ratios/g5a.smK29.R.13CO.spw29.im','ratios/g5a.smK29.R.C18O.spw31.im'], mode='evalexpr', expr='IM0/IM1 [IM1>0.1]', outfile='ratios/ratio.R.13CO-C18O.im')
immath(imagename=['ratios/g5a.smK29.R.CH3OH.spw21.im','ratios/g5a.smK29.R.13CO.spw29.im'], mode='evalexpr', expr='IM0/IM1 [IM1>2.0]', outfile='ratios/ratio.R.CH3OH-13CO.im')
immath(imagename=['ratios/g5a.smK29.R.H2CO.spw23.im','ratios/g5a.smK29.R.13CO.spw29.im'], mode='evalexpr', expr='IM0/IM1 [IM1>2.0]', outfile='ratios/ratio.R.H2COa-13CO.im')
immath(imagename=['ratios/g5a.smK29.R.OCS.spw23.im','ratios/g5a.smK29.R.13CO.spw29.im'],mode='evalexpr',expr='IM0/IM1 [IM1>2.0]',outfile='ratios/ratio.R.OCS-13CO.im')
immath(imagename=['ratios/g5a.smK29.R.H2CO.spw25.im','ratios/g5a.smK29.R.13CO.spw29.im'], mode='evalexpr', expr='IM0/IM1 [IM1>2.0]', outfile='ratios/ratio.R.H2COb-13CO.im')
immath(imagename=['ratios/g5a.smK29.R.SiO.spw27.im','ratios/g5a.smK29.R.13CO.spw29.im'], mode='evalexpr', expr='IM0/IM1 [IM1>2.0]', outfile='ratios/ratio.R.SiO-13CO.im')

imhead(imagename='ratios/ratio.R.12CO-13CO.im', mode='put', hdkey='bunit', hdvalue='')
imhead(imagename='ratios/ratio.R.12CO-C18O.im', mode='put', hdkey='bunit', hdvalue='')
imhead(imagename='ratios/ratio.R.13CO-C18O.i[IM0>0.2&&IM1>6.0]m', mode='put', hdkey='bunit', hdvalue='')
imhead(imagename='ratios/ratio.R.CH3OH-13CO.im', mode='put', hdkey='bunit', hdvalue='')
imhead(imagename='ratios/ratio.R.H2COa-13CO.im', mode='put', hdkey='bunit', hdvalue='')
imhead(imagename='ratios/ratio.R.H2COb-13CO.im', mode='put', hdkey='bunit', hdvalue='')
imhead(imagename='ratios/ratio.R.SiO-13CO.im', mode='put', hdkey='bunit', hdvalue='')




