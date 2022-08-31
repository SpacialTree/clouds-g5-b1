
# Have to start fixing G5 data, make moment maps, ratio maps, etc!!!!!!!!!
'''
importfits(fitsimage='', imagename='')

imcontsub(imagename='', linefile='', contfile='', fitorder=5, chans='')		# Fixing the baseline

immoments(imagename='', moments=[0], chans='', outfile='')
immoments(imagename='', moments=[1], chans='', includepix=[], outfile='')
immoments(imagename='', moments=[2], chans='', includepix=[], outfile='')

imsmooth(imagename='', targetres=True, major='40arcsec', minor='40arcsec', pa=0, outfile='')
immath(imagename='', mode='evalexpr', expr='1.222e6*IM0/F^2/40^2', outfile='')
imhead(imagename='smoothmom0_17_K.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
imregrid(imagename='', template='',axes=[0,1],interpolation='',output='',overwrite=True)
immath(imagename=['rpt17-31.im','rpt29-31.im'], mode='evalexpr', expr='(IM0/IM1) [IM0>190.0 && IM1>26.0]', outfile='ratio_12CO-13CO.im')
imhead(imagename='ratio_12CO-13CO.im', mode='put', hdkey='bunit', hdvalue='')


'''

'''
# First, import fits to casa
importfits(fitsimage='spw17_12CO/member.uid___A001_X133e_X3c.G5.spw17.I.sd.im.fits', imagename='spw17_12CO/grad17.im')
importfits(fitsimage='spw21_HC3N/member.uid___A001_X133e_X3c.G5.spw21.I.sd.im.fits', imagename='spw21_HC3N/grad21.im')
importfits(fitsimage='spw23_H2CO/member.uid___A001_X133e_X3c.G5.spw23.I.sd.im.fits', imagename='spw23_H2CO/grad23.im')
importfits(fitsimage='spw25_H2CO/member.uid___A001_X133e_X3c.G5.spw25.I.sd.im.fits', imagename='spw25_H2CO/grad25.im')
importfits(fitsimage='spw27_SiO/member.uid___A001_X133e_X3c.G5.spw27.I.sd.im.fits', imagename='spw27_SiO/grad27.im')
importfits(fitsimage='spw29_13CO/member.uid___A001_X133e_X3c.G5.spw29.I.sd.im.fits', imagename='spw29_13CO/grad29.im')
importfits(fitsimage='spw31_C18O/member.uid___A001_X133e_X3c.G5.spw31.I.sd.im.fits', imagename='spw31_C18O/grad31.im')

# Now to fix the images that need it.

imcontsub(imagename='', linefile='', contfile='', fitorder=5, chans='')

imcontsub(imagename='grad17.im', linefile='try1line.im', contfile='try1cont.im', fitorder=5, chans='0~150,335~345,1100~1160,1234~1240,1335~1345,1380~1440,1555~2047')
imcontsub(imagename='grad17.im', linefile='try2line.im', contfile='try2cont.im', fitorder=5, chans='0~150,1140~1150,1380~1440,1570~2047')
imcontsub(imagename='grad17.im', linefile='try3line.im', contfile='try3cont.im', fitorder=5, chans='0~120,1380~1390,1420~1440,1635~2047')
imcontsub(imagename='grad17.im', linefile='try4line.im', contfile='try4cont.im', fitorder=5, chans='0~150,1140~1150,1350~1440,1570~2047') 
imcontsub(imagename='grad17.im', linefile='try5line.im', contfile='try5cont.im', fitorder=5, chans='0~150,1125~1140,1380~1390,1420~1440,1575~2047') 
imcontsub(imagename='try4line.im', linefile='try6line.im', contfile='try6cont.im', fitorder=5, chans='0~135,1135~1140,1380~1440,1640~2047') 

imcontsub(imagename='grad29.im', linefile='try1line29.im', contfile='try1cont29.im', fitorder=5, chans='0~250,315~340,460~470,920~1023')
imcontsub(imagename='grad29.im', linefile='try2line29.im', contfile='try2cont29.im', fitorder=5, chans='0~250, 342~363,465~470,920~1023')
imcontsub(imagename='grad29.im', linefile='try3line29.im', contfile='try3cont29.im', fitorder=5, chans='0~250,342~363,920~1023')


imcontsub(imagename='grad27.im', linefile='try1line27.im', contfile='try1cont27.im', fitorder=5, chans='0~220,430~506')

imcontsub(imagename='grad21.im', linefile='try1line21.im', contfile='try1cont21.im', fitorder=5, chans='0~16, 200~400, 445~450')
imcontsub(imagename='grad21.im', linefile='try2line21.im', contfile='try2cont21.im', fitorder=5, chans='0~20, 200~400, 445~450')
imcontsub(imagename='grad21.im', linefile='try3line21.im', contfile='try3cont21.im', fitorder=5, chans='0~10, 200~400, 445~450') ###
imcontsub(imagename='grad21.im', linefile='try4line21.im', contfile='try4cont21.im', fitorder=6, chans='0~5, 200~400, 445~450')
imcontsub(imagename='grad21.im', linefile='try5line21.im', contfile='try5cont21.im', fitorder=5, chans='0~5, 65~70, 200~400, 445~450')
imcontsub(imagename='grad21.im', linefile='try6line21.im', contfile='try6cont21.im', fitorder=5, chans='0~1, 200~400, 445~450')
imcontsub(imagename='grad21.im', linefile='try7line21.im', contfile='try7cont21.im', fitorder=5, chans='0~5, 35~40, 65~70, 200~400, 445~450')
imcontsub(imagename='grad21.im', linefile='try8line21.im', contfile='try8cont21.im', fitorder=5, chans='0~5, 40~50, 65~70, 200~400, 445~450')
imcontsub(imagename='grad21.im', linefile='try9line21.im', contfile='try9cont21.im', fitorder=5, chans='15~18,195~408')
imcontsub(imagename='grad21.im', linefile='try10line21.im', contfile='try10cont21.im', fitorder=5, chans='200~395,440~450')

imcontsub(imagename='grad23.im', linefile='try1line23.im', contfile='try1cont23.im', fitorder=5, chans='0~240,400~500')

imcontsub(imagename='grad25.im', linefile='try1line25.im', contfile='try1cont25.im', fitorder=5, chans='0~175,205~210,227~254,432~511')

imcontsub(imagename='grad31.im', linefile='try1line31.im', contfile='try1cont31.im', fitorder=5, chans='0~190,300~355,460~490,845~1023')

# Change H3CN cube to CH3OH
imhead(imagename='fixed21_CH3OH.im', mode='put', hdkey='restfreq', hdvalue='218440050000')


# Moment Maps!
immoments(imagename='', moments=[0], chans='', outfile='')


immoments(imagename='spw17_12CO/fixed17.im', moments=[0], chans='', outfile='spw17_12CO/mom0_all17.im')
immoments(imagename='spw21_HC3N/fixed21_CH3OH.im', moments=[0], chans='', outfile='spw21_HC3N/mom0_all21.im')
immoments(imagename='spw23_H2CO/fixed23.im', moments=[0], chans='', outfile='spw23_H2CO/mom0_all23.im')
immoments(imagename='spw25_H2CO/fixed25.im', moments=[0], chans='', outfile='spw25_H2CO/mom0_all25.im')
immoments(imagename='spw27_SiO/fixed27.im', moments=[0], chans='', outfile='spw27_SiO/mom0_all27.im')
immoments(imagename='spw29_13CO/fixed29.im', moments=[0], chans='', outfile='spw29_13CO/mom0_all29.im')
immoments(imagename='spw31_C18O/fixed31.im', moments=[0], chans='', outfile='spw31_C18O/mom0_all31.im')


immoments(imagename='spw17_12CO/fixed17.im', moments=[0], chans='307~1125', outfile='spw17_12CO/mom0_G5_17.im')
immoments(imagename='spw21_HC3N/fixed21_CH3OH.im', moments=[0], chans='0~230', outfile='spw21_HC3N/mom0_G5_21.im')
immoments(imagename='spw23_H2CO/fixed23.im', moments=[0], chans='224~434', outfile='spw23_H2CO/mom0_G5_23.im')
immoments(imagename='spw25_H2CO/fixed25.im', moments=[0], chans='224~434', outfile='spw25_H2CO/mom0_G5_25.im')
immoments(imagename='spw27_SiO/fixed27.im', moments=[0], chans='224~434', outfile='spw27_SiO/mom0_G5_27.im')
immoments(imagename='spw29_13CO/fixed29.im', moments=[0], chans='460~869', outfile='spw29_13CO/mom0_G5_29.im')
immoments(imagename='spw31_C18O/fixed31.im', moments=[0], chans='460~869', outfile='spw31_C18O/mom0_G5_31.im')


immoments(imagename='spw17_12CO/grad17.im', moments=[0], chans='307~1125', outfile='spw17_12CO/mom0_G5_17.im')
immoments(imagename='spw21_HC3N/grad21.im', moments=[0], chans='0~230', outfile='spw21_HC3N/mom0_2_G5_21.im')
immoments(imagename='spw23_H2CO/grad23.im', moments=[0], chans='224~434', outfile='spw23_H2CO/mom0_2_G5_23.im')
immoments(imagename='spw25_H2CO/grad25.im', moments=[0], chans='224~434', outfile='spw25_H2CO/mom0_2_G5_25.im')
immoments(imagename='spw27_SiO/grad27.im', moments=[0], chans='224~434', outfile='spw27_SiO/mom0_2_G5_27.im')
immoments(imagename='spw29_13CO/grad29.im', moments=[0], chans='460~869', outfile='spw29_13CO/mom0_2_G5_29.im')
immoments(imagename='spw31_C18O/grad31.im', moments=[0], chans='460~869', outfile='spw31_C18O/mom0_2_G5_31.im')

immoments(imagename='spw29_13CO/try2line29.im', moments=[0], chans='460~869', outfile='spw29_13CO/mom0_3_G5_29.im')

immoments(imagename='spw21_HC3N/true21_CH3OH.im', moments=[0], chans='0~230', outfile='spw21_HC3N/mom0_21.im')


###
immoments(imagename='', moments=[1], chans='', includepix=[], outfile='')
immoments(imagename='', moments=[2], chans='', includepix=[], outfile='')


immoments(imagename='spw17_12CO/true17.im', moments=[1], chans='307~1125', outfile='spw17_12CO/mom1_1_G5_17.im')
immoments(imagename='spw17_12CO/true17.im', moments=[2], chans='307~1125', outfile='spw17_12CO/mom2_1_G5_17.im')
immoments(imagename='spw21_HC3N/true21.im', moments=[1], chans='0~230', outfile='spw21_HC3N/mom1_1_21.im')
immoments(imagename='spw21_HC3N/true21.im', moments=[2], chans='0~230', outfile='spw21_HC3N/mom2_1_21.im')
immoments(imagename='spw23_H2CO/true23.im', moments=[1], chans='224~434', outfile='spw23_H2CO/mom1_1_23.im')
immoments(imagename='spw23_H2CO/true23.im', moments=[2], chans='224~434', outfile='spw23_H2CO/mom2_1_23.im')
immoments(imagename='spw25_H2CO/true25.im', moments=[1], chans='224~434', outfile='spw25_H2CO/mom1_1_25.im')
immoments(imagename='spw25_H2CO/true25.im', moments=[2], chans='224~434', outfile='spw25_H2CO/mom2_1_25.im')
immoments(imagename='spw27_SiO/true27.im', moments=[1], chans='224~434', outfile='spw27_SiO/mom1_1_27.im')
immoments(imagename='spw27_SiO/true27.im', moments=[2], chans='224~434', outfile='spw27_SiO/mom2_1_27.im')
immoments(imagename='spw29_13CO/true29.im', moments=[1], chans='460~869', outfile='spw29_13CO/mom1_1_G5_29.im')
immoments(imagename='spw29_13CO/true29.im', moments=[2], chans='460~869', outfile='spw29_13CO/mom2_1_G5_29.im')
immoments(imagename='spw31_C18O/true31.im', moments=[1], chans='460~869', outfile='spw31_C18O/mom1_1_G5_31.im')
immoments(imagename='spw31_C18O/true31.im', moments=[2], chans='460~869', outfile='spw31_C18O/mom2_1_G5_31.im')



###
immoments(imagename='spw17_12CO/true17.im', moments=[1], chans='307~1125', includepix=[1.0, 25], outfile='spw17_12CO/mom1_3_G5_17.im')
immoments(imagename='spw17_12CO/true17.im', moments=[1], chans='307~1125', includepix=[1.0, 50], outfile='spw17_12CO/mom1_4_G5_17.im')
immoments(imagename='spw17_12CO/true17.im', moments=[1], chans='307~1125', includepix=[0.8, 50], outfile='spw17_12CO/mom1_5_G5_17.im')
immoments(imagename='spw17_12CO/true17.im', moments=[1], chans='307~1125', includepix=[1.0, 80], outfile='spw17_12CO/mom1_6_G5_17.im')
immoments(imagename='spw17_12CO/true17.im', moments=[1], chans='307~1125', includepix=[1.0, 100], outfile='spw17_12CO/mom1_7_G5_17.im')
immoments(imagename='spw17_12CO/true17.im', moments=[1], chans='307~1125', includepix=[1.0, 120], outfile='spw17_12CO/mom1_8_G5_17.im')
immoments(imagename='spw17_12CO/true17.im', moments=[1], chans='307~1125', includepix=[1.0, 150], outfile='spw17_12CO/mom1_9_G5_17.im')
immoments(imagename='spw17_12CO/true17.im', moments=[1], chans='307~1125', includepix=[1.0, 200], outfile='spw17_12CO/mom1_10_G5_17.im')
immoments(imagename='spw17_12CO/true17.im', moments=[1], chans='307~1125', includepix=[1.0, 250], outfile='spw17_12CO/mom1_11_G5_17.im')
immoments(imagename='spw17_12CO/true17.im', moments=[2], chans='307~1125', includepix=[1.0, 250], outfile='spw17_12CO/mom2_2_G5_17.im')

immoments(imagename='spw21_HC3N/true21.im', moments=[1], chans='0~230', includepix=[], outfile='spw21_HC3N/mom1_2_21.im')
immoments(imagename='spw21_HC3N/true21.im', moments=[2], chans='0~230', includepix=[], outfile='spw21_HC3N/mom2_2_21.im')
immoments(imagename='spw21_HC3N/true21_CH3OH.im', moments=[1], chans='0~230', outfile='spw21_HC3N/mom1_3_21.im')
immoments(imagename='spw21_HC3N/true21_CH3OH.im', moments=[2], chans='0~230', outfile='spw21_HC3N/mom2_3_21.im')
immoments(imagename='spw21_HC3N/true21_CH3OH.im', moments=[1], chans='0~230', includepix=[0.5,20], outfile='spw21_HC3N/mom1_4_21.im')
immoments(imagename='spw21_HC3N/true21_CH3OH.im', moments=[1], chans='0~230', includepix=[1.0,20], outfile='spw21_HC3N/mom1_5_21.im')
immoments(imagename='spw21_HC3N/true21_CH3OH.im', moments=[1], chans='0~230', includepix=[0.7,20], outfile='spw21_HC3N/mom1_6_21.im')
immoments(imagename='spw21_HC3N/true21_CH3OH.im', moments=[1], chans='0~230', includepix=[0.55,20], outfile='spw21_HC3N/mom1_7_21.im')
immoments(imagename='spw21_HC3N/true21_CH3OH.im', moments=[1], chans='0~230', includepix=[0.6,20], outfile='spw21_HC3N/mom1_8_21.im')
immoments(imagename='spw21_HC3N/true21_CH3OH.im', moments=[1], chans='0~230', includepix=[0.6,20], outfile='spw21_HC3N/mom1_21.im')
immoments(imagename='spw21_HC3N/true21_CH3OH.im', moments=[2], chans='0~230', includepix=[0.6,20], outfile='spw21_HC3N/mom2_21.im')

immoments(imagename='spw23_H2CO/true23.im', moments=[1], chans='224~434', includepix=[0.6,20], outfile='spw23_H2CO/mom1_2_23.im')
immoments(imagename='spw23_H2CO/true23.im', moments=[2], chans='224~434', includepix=[0.6,20], outfile='spw23_H2CO/mom2_2_23.im')

immoments(imagename='spw25_H2CO/true25.im', moments=[1], chans='224~434', includepix=[0.6,20], outfile='spw25_H2CO/mom1_2_25.im')
immoments(imagename='spw25_H2CO/true25.im', moments=[1], chans='224~434', includepix=[0.6,25], outfile='spw25_H2CO/mom1_3_25.im')
immoments(imagename='spw25_H2CO/true25.im', moments=[2], chans='224~434', includepix=[0.6,20], outfile='spw25_H2CO/mom2_2_25.im')

immoments(imagename='spw27_SiO/true27.im', moments=[1], chans='224~434', includepix=[0.6,20], outfile='spw27_SiO/mom1_2_27.im')
immoments(imagename='spw27_SiO/true27.im', moments=[2], chans='224~434', includepix=[0.6,20], outfile='spw27_SiO/mom2_2_27.im')

immoments(imagename='spw29_13CO/true29.im', moments=[1], chans='460~869', includepix=[1.0,25], outfile='spw29_13CO/mom1_2_G5_29.im')
immoments(imagename='spw29_13CO/true29.im', moments=[2], chans='460~869', includepix=[1.0,25], outfile='spw29_13CO/mom2_2_G5_29.im')

immoments(imagename='spw31_C18O/true31.im', moments=[1], chans='460~869', includepix=[1.0,25], outfile='spw31_C18O/mom1_2_G5_31.im')
immoments(imagename='spw31_C18O/true31.im', moments=[1], chans='460~869', includepix=[1.0,30], outfile='spw31_C18O/mom1_3_G5_31.im')
immoments(imagename='spw31_C18O/true31.im', moments=[1], chans='460~869', includepix=[0.9,30], outfile='spw31_C18O/mom1_4_G5_31.im')
immoments(imagename='spw31_C18O/true31.im', moments=[1], chans='460~869', includepix=[0.8,30], outfile='spw31_C18O/mom1_5_G5_31.im')
immoments(imagename='spw31_C18O/true31.im', moments=[1], chans='460~869', includepix=[0.5,35], outfile='spw31_C18O/mom1_6_G5_31.im')
immoments(imagename='spw31_C18O/true31.im', moments=[2], chans='460~869', includepix=[0.5,35], outfile='spw31_C18O/mom2_2_G5_31.im')

immoments(imagename='spw17_12CO/true17.im', moments=[1], chans='307~1125', includepix=[1.0, 250], outfile='spw17_12CO/mom1_G5_17.im')
immoments(imagename='spw17_12CO/true17.im', moments=[2], chans='307~1125', includepix=[1.0, 250], outfile='spw17_12CO/mom2_G5_17.im')
immoments(imagename='spw21_HC3N/true21_CH3OH.im', moments=[1], chans='0~230', includepix=[0.6,20], outfile='spw21_HC3N/mom1_21.im')
immoments(imagename='spw21_HC3N/true21_CH3OH.im', moments=[2], chans='0~230', includepix=[0.6,20], outfile='spw21_HC3N/mom2_21.im')
immoments(imagename='spw23_H2CO/true23.im', moments=[1], chans='224~434', includepix=[0.6,20], outfile='spw23_H2CO/mom1_23.im')
immoments(imagename='spw23_H2CO/true23.im', moments=[2], chans='224~434', includepix=[0.6,20], outfile='spw23_H2CO/mom2_23.im')
immoments(imagename='spw25_H2CO/true25.im', moments=[1], chans='224~434', includepix=[0.6,25], outfile='spw25_H2CO/mom1_25.im')
immoments(imagename='spw25_H2CO/true25.im', moments=[2], chans='224~434', includepix=[0.6,20], outfile='spw25_H2CO/mom2_25.im')
immoments(imagename='spw27_SiO/true27.im', moments=[1], chans='224~434', includepix=[0.6,20], outfile='spw27_SiO/mom1_27.im')
immoments(imagename='spw27_SiO/true27.im', moments=[2], chans='224~434', includepix=[0.6,20], outfile='spw27_SiO/mom2_27.im')
immoments(imagename='spw29_13CO/true29.im', moments=[1], chans='460~869', includepix=[1.0,25], outfile='spw29_13CO/mom1_G5_29.im')
immoments(imagename='spw29_13CO/true29.im', moments=[2], chans='460~869', includepix=[1.0,25], outfile='spw29_13CO/mom2_G5_29.im')
immoments(imagename='spw31_C18O/true31.im', moments=[1], chans='460~869', includepix=[0.5,35], outfile='spw31_C18O/mom1_G5_31.im')
immoments(imagename='spw31_C18O/true31.im', moments=[2], chans='460~869', includepix=[0.5,35], outfile='spw31_C18O/mom2_G5_31.im')

'''
'''
imsmooth(imagename='', targetres=True, major='40arcsec', minor='40arcsec', pa=0, outfile='')
immath(imagename='', mode='evalexpr', expr='1.222e6*IM0/F^2/40^2', outfile='')
imhead(imagename='smoothmom0_17_K.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
imregrid(imagename='', template='',axes=[0,1],interpolation='',output='',overwrite=True)
#Always check 3 sig values
immath(imagename=['rpt17-31.im','rpt29-31.im'], mode='evalexpr', expr='(IM0/IM1) [IM0>190.0 && IM1>26.0]', outfile='ratio_12CO-13CO.im')
imhead(imagename='ratio_12CO-13CO.im', mode='put', hdkey='bunit', hdvalue='')
'''
'''

imsmooth(imagename='mom0_G5_17.im', targetres=True, major='40arcsec', minor='40arcsec', pa=0, outfile='smoothmom0_17.im')
imsmooth(imagename='mom0_21.im', targetres=True, major='40arcsec', minor='40arcsec', pa=0, outfile='smoothmom0_21.im')
imsmooth(imagename='mom0_23.im', targetres=True, major='40arcsec', minor='40arcsec', pa=0, outfile='smoothmom0_23.im')
imsmooth(imagename='mom0_25.im', targetres=True, major='40arcsec', minor='40arcsec', pa=0, outfile='smoothmom0_25.im')
imsmooth(imagename='mom0_27.im', targetres=True, major='40arcsec', minor='40arcsec', pa=0, outfile='smoothmom0_27.im')
imsmooth(imagename='mom0_G5_29.im', targetres=True, major='40arcsec', minor='40arcsec', pa=0, outfile='smoothmom0_29.im')
imsmooth(imagename='mom0_G5_31.im', targetres=True, major='40arcsec', minor='40arcsec', pa=0, outfile='smoothmom0_31.im')


immath(imagename='smoothmom0_17.im', mode='evalexpr', expr='1.222e6*IM0/230.538000^2/40^2', outfile='smoothmom0_17_K.im')
immath(imagename='smoothmom0_29.im', mode='evalexpr', expr='1.222e6*IM0/220.398684^2/40^2', outfile='smoothmom0_29_K.im')
immath(imagename='smoothmom0_31.im', mode='evalexpr', expr='1.222e6*IM0/219.560358^2/40^2', outfile='smoothmom0_31_K.im')
immath(imagename='smoothmom0_21.im', mode='evalexpr', expr='1.222e6*IM0/218.44005^2/40^2', outfile='smoothmom0_21_K.im')
immath(imagename='smoothmom0_23.im', mode='evalexpr', expr='1.222e6*IM0/218.760066^2/40^2', outfile='smoothmom0_23_K.im')
immath(imagename='smoothmom0_25.im', mode='evalexpr', expr='1.222e6*IM0/218.222192^2/40^2', outfile='smoothmom0_25_K.im')
immath(imagename='smoothmom0_27.im', mode='evalexpr', expr='1.222e6*IM0/217.104980^2/40^2', outfile='smoothmom0_27_K.im')


imhead(imagename='smoothmom0_17_K.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
imhead(imagename='smoothmom0_29_K.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
imhead(imagename='smoothmom0_31_K.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
imhead(imagename='smoothmom0_21_K.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
imhead(imagename='smoothmom0_23_K.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
imhead(imagename='smoothmom0_25_K.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
imhead(imagename='smoothmom0_27_K.im', mode='put', hdkey='bunit', hdvalue='K.km/s')

imregrid(imagename='smoothmom0_17_K.im', template='smoothmom0_31_K.im',axes=[0,1],interpolation='cubic',output='17t31.im',overwrite=True)
imregrid(imagename='smoothmom0_29_K.im', template='smoothmom0_31_K.im',axes=[0,1],interpolation='cubic',output='29t31.im',overwrite=True)
imregrid(imagename='smoothmom0_21_K.im', template='smoothmom0_29_K.im',axes=[0,1],interpolation='cubic',output='21t29.im',overwrite=True)
imregrid(imagename='smoothmom0_23_K.im', template='smoothmom0_29_K.im',axes=[0,1],interpolation='cubic',output='23t29.im',overwrite=True)
imregrid(imagename='smoothmom0_25_K.im', template='smoothmom0_29_K.im',axes=[0,1],interpolation='cubic',output='25t29.im',overwrite=True)
imregrid(imagename='smoothmom0_27_K.im', template='smoothmom0_29_K.im',axes=[0,1],interpolation='cubic',output='27t29.im',overwrite=True)

immath(imagename=['17t31.im','29t31.im'], mode='evalexpr', expr='(IM0/IM1) [IM0>170.0&&IM1>6.0]', outfile='ratio_12CO-13CO.im')
immath(imagename=['17t31.im','smoothmom0_31_K.im'], mode='evalexpr', expr='(IM0/IM1) [IM0>170.0&&IM1>1.0]', outfile='ratio_12CO-C18O.im')
immath(imagename=['29t31.im','smoothmom0_31_K.im'], mode='evalexpr', expr='(IM0/IM1) [IM0>6.0&&IM1>1.0]', outfile='ratio_13CO-C18O.im')
immath(imagename=['21t29.im','smoothmom0_29_K.im'], mode='evalexpr', expr='IM0/IM1 [IM0>0.2&&IM1>7.0]', outfile='ratio_CH3OH-13CO.im')
immath(imagename=['23t29.im','smoothmom0_29_K.im'], mode='evalexpr', expr='IM0/IM1 [IM0>0.1&&IM1>7.0]', outfile='ratio_H2COa-13CO.im')
immath(imagename=['25t29.im','smoothmom0_29_K.im'], mode='evalexpr', expr='IM0/IM1 [IM0>0.1&&IM1>7.0]', outfile='ratio_H2COb-13CO.im')
immath(imagename=['27t29.im','smoothmom0_29_K.im'], mode='evalexpr', expr='IM0/IM1 [IM0>0.8&&IM1>7.0]', outfile='ratio_SiO-13CO.im')

imhead(imagename='ratio_12CO-13CO.im', mode='put', hdkey='bunit', hdvalue='')
imhead(imagename='ratio_12CO-C18O.im', mode='put', hdkey='bunit', hdvalue='')
imhead(imagename='ratio_13CO-C18O.im', mode='put', hdkey='bunit', hdvalue='')
imhead(imagename='ratio_CH3OH-13CO.im', mode='put', hdkey='bunit', hdvalue='')
imhead(imagename='ratio_H2COa-13CO.im', mode='put', hdkey='bunit', hdvalue='')
imhead(imagename='ratio_H2COb-13CO.im', mode='put', hdkey='bunit', hdvalue='')
imhead(imagename='ratio_SiO-13CO.im', mode='put', hdkey='bunit', hdvalue='')

###

imsmooth(imagename='mom0_23.im', targetres=True, major='40arcsec', minor='40arcsec', pa=0, outfile='smoothed_mom0_23.im')
imsmooth(imagename='mom0_25.im', targetres=True, major='40arcsec', minor='40arcsec', pa=0, outfile='smoothed_mom0_25.im')

immath(imagename='smoothed_mom0_23.im', mode='evalexpr', expr='1.222e6*IM0/218.760066^2/40^2', outfile='smoothed_mom0_23_K.im')	
immath(imagename='smoothed_mom0_25.im', mode='evalexpr', expr='1.222e6*IM0/218.222192^2/40^2', outfile='smoothed_mom0_25_K.im')	

imhead(imagename='smoothed_mom0_23_K.im', mode='put', hdkey='bunit', hdvalue='K.km/s')
imhead(imagename='smoothed_mom0_25_K.im', mode='put', hdkey='bunit', hdvalue='K.km/s')

imregrid(imagename='smoothed_mom0_23_K.im', template='smoothed_mom0_25_K.im',axes=[0,1],interpolation='cubic',output='23t25.im',overwrite=True)

# check 3 sig
immath(imagename=['23t25.im','smoothed_mom0_25_K.im'], mode='evalexpr', expr='IM0 / IM1 [IM0>0.1&&IM1>0.6]', outfile='smoothratio.im')
imhead(imagename='smoothratio.im', mode='put', hdkey='bunit', hdvalue='')

immath(imagename='smoothratio.im', mode='evalexpr', expr='(590 * IM0^2 + 2.88 * IM0 + 23.4)', outfile='smoothtemp.im')
imhead(imagename='smoothtemp.im', mode='put', hdkey='bunit', hdvalue='K')
'''

'''
### gonna have to split this up more
immoments(imagename='spw17_12CO/true17.im', moments=[0], chans='1125~1202', outfile='spw17_12CO/mom0_N3_17.im')
immoments(imagename='spw29_13CO/true29.im', moments=[0], chans='460~869', outfile='spw29_13CO/mom0_G5_29.im')
immoments(imagename='spw31_C18O/true31.im', moments=[0], chans='460~869', outfile='spw31_C18O/mom0_G5_31.im')

immoments(imagename='spw17_12CO/true17.im', moments=[0], chans='1202~1356', outfile='spw17_12CO/mom0_CM_17.im')
immoments(imagename='spw29_13CO/true29.im', moments=[0], chans='460~869', outfile='spw29_13CO/mom0_G5_29.im')
immoments(imagename='spw31_C18O/true31.im', moments=[0], chans='460~869', outfile='spw31_C18O/mom0_G5_31.im')

immoments(imagename='spw17_12CO/true17.im', moments=[0], chans='1356~1586', outfile='spw17_12CO/mom0_F3_17.im')
immoments(imagename='spw29_13CO/true29.im', moments=[0], chans='460~869', outfile='spw29_13CO/mom0_G5_29.im')
immoments(imagename='spw31_C18O/true31.im', moments=[0], chans='460~869', outfile='spw31_C18O/mom0_G5_31.im')
'''

#imregrid(imagename='',template='',axes='',interpolation='',output='',overwrite='')
'''
imregrid(imagename='spw17_12CO/mom0_G5_17.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom0_G5_17.gal.im',overwrite=True)
imregrid(imagename='spw17_12CO/mom1_G5_17.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom1_G5_17.gal.im',overwrite=True)
imregrid(imagename='spw17_12CO/mom2_G5_17.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom2_G5_17.gal.im',overwrite=True)

imregrid(imagename='spw21_HC3N/mom0_21.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom0_21.gal.im',overwrite=True)
imregrid(imagename='spw21_HC3N/mom1_21.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom1_21.gal.im',overwrite=True)
imregrid(imagename='spw21_HC3N/mom2_21.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom2_21.gal.im',overwrite=True)

imregrid(imagename='spw23_H2CO/mom0_23.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom0_23.gal.im',overwrite=True)
imregrid(imagename='spw23_H2CO/mom1_23.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom1_23.gal.im',overwrite=True)
imregrid(imagename='spw23_H2CO/mom2_23.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom2_23.gal.im',overwrite=True)

imregrid(imagename='spw25_H2CO/mom0_25.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom0_25.gal.im',overwrite=True)
imregrid(imagename='spw25_H2CO/mom1_25.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom1_25.gal.im',overwrite=True)
imregrid(imagename='spw25_H2CO/mom2_25.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom2_25.gal.im',overwrite=True)

imregrid(imagename='spw27_SiO/mom0_27.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom0_27.gal.im',overwrite=True)
imregrid(imagename='spw27_SiO/mom1_27.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom1_27.gal.im',overwrite=True)
imregrid(imagename='spw27_SiO/mom2_27.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom2_27.gal.im',overwrite=True)

imregrid(imagename='spw29_13CO/mom0_G5_29.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom0_G5_29.gal.im',overwrite=True)
imregrid(imagename='spw29_13CO/mom1_G5_29.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom1_G5_29.gal.im',overwrite=True)
imregrid(imagename='spw29_13CO/mom2_G5_29.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom2_G5_29.gal.im',overwrite=True)

imregrid(imagename='spw31_C18O/mom0_G5_31.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom0_G5_31.gal.im',overwrite=True)
imregrid(imagename='spw31_C18O/mom1_G5_31.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom1_G5_31.gal.im',overwrite=True)
imregrid(imagename='spw31_C18O/mom2_G5_31.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom2_G5_31.gal.im',overwrite=True)

imregrid(imagename='ratios/ratio_12CO-13CO.im',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/ratio_12CO-13CO.gal.im',overwrite=True)
imregrid(imagename='ratios/ratio_12CO-C18O.im',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/ratio_12CO-C18O.gal.im',overwrite=True)
imregrid(imagename='ratios/ratio_13CO-C18O.im',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/ratio_13CO-C18O.gal.im',overwrite=True)
imregrid(imagename='ratios/ratio_CH3OH-13CO.im',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/ratio_CH3OH-13CO.gal.im',overwrite=True)
imregrid(imagename='ratios/ratio_H2COa-13CO.im',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/ratio_H2COa-13CO.gal.im',overwrite=True)
imregrid(imagename='ratios/ratio_H2COb-13CO.im',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/ratio_H2COb-13CO.gal.im',overwrite=True)
imregrid(imagename='ratios/ratio_SiO-13CO.im',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/ratio_SiO-13CO.gal.im',overwrite=True)

imregrid(imagename='temps/smoothtemp.im',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/smoothtemp.gal.im',overwrite=True)
'''
'''
imregrid(imagename='spw17_12CO/mom0_2_B1_17.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom0_B1_17.gal.im',overwrite=True)
imregrid(imagename='spw17_12CO/mom1_B1_17.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom1_B1_17.gal.im',overwrite=True)
imregrid(imagename='spw17_12CO/mom2_B1_17.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom2_B1_17.gal.im',overwrite=True)

imregrid(imagename='spw29_13CO/mom0_2_B1_29.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom0_B1_29.gal.im',overwrite=True)
imregrid(imagename='spw29_13CO/mom1_B1_29.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom1_B1_29.gal.im',overwrite=True)
imregrid(imagename='spw29_13CO/mom2_B1_29.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom2_B1_29.gal.im',overwrite=True)

imregrid(imagename='spw31_C18O/mom0_2_B1_31.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom0_B1_31.gal.im',overwrite=True)
imregrid(imagename='spw31_C18O/mom1_B1_31.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom1_B1_31.gal.im',overwrite=True)
imregrid(imagename='spw31_C18O/mom2_B1_31.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom2_B1_31.gal.im',overwrite=True)

imregrid(imagename='spw21_HC3N/mom0_CH3OH_21.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom0_21.gal.im',overwrite=True)
imregrid(imagename='spw21_HC3N/mom1_2_CH3OH.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom1_21.gal.im',overwrite=True)
imregrid(imagename='spw21_HC3N/mom2_2_CH3OH.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom2_21.gal.im',overwrite=True)

imregrid(imagename='spw23_H2CO/mom0_2_23.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom0_23.gal.im',overwrite=True)
imregrid(imagename='spw23_H2CO/mom1_23.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom1_23.gal.im',overwrite=True)
imregrid(imagename='spw23_H2CO/mom2_23.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom2_23.gal.im',overwrite=True)

imregrid(imagename='spw25_H2CO/mom0_2_25.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom0_25.gal.im',overwrite=True)
imregrid(imagename='spw25_H2CO/mom1_25.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom1_25.gal.im',overwrite=True)
imregrid(imagename='spw25_H2CO/mom2_25.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom2_25.gal.im',overwrite=True)

imregrid(imagename='spw27_SiO/mom0_2_27.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom0_27.gal.im',overwrite=True)
imregrid(imagename='spw27_SiO/mom1_try2_27.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom1_27.gal.im',overwrite=True)
imregrid(imagename='spw27_SiO/mom2_27.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom2_27.gal.im',overwrite=True)
'''

imregrid(imagename='spw17_12CO/mom0_2_B1_17.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom0_B1_17.gal.im',overwrite=True)
imregrid(imagename='spw17_12CO/mom1_B1_17.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom1_B1_17.gal.im',overwrite=True)
imregrid(imagename='spw17_12CO/mom2_B1_17.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom2_B1_17.gal.im',overwrite=True)

imregrid(imagename='spw29_13CO/mom0_2_B1_29.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom0_B1_29.gal.im',overwrite=True)
imregrid(imagename='spw29_13CO/mom1_B1_29.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom1_B1_29.gal.im',overwrite=True)
imregrid(imagename='spw29_13CO/mom2_B1_29.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom2_B1_29.gal.im',overwrite=True)

imregrid(imagename='spw31_C18O/mom0_2_B1_31.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom0_B1_31.gal.im',overwrite=True)
imregrid(imagename='spw31_C18O/mom1_B1_31.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom1_B1_31.gal.im',overwrite=True)
imregrid(imagename='spw31_C18O/mom2_B1_31.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom2_B1_31.gal.im',overwrite=True)

imregrid(imagename='spw21_HC3N/mom0_CH3OH_21.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom0_21.gal.im',overwrite=True)
imregrid(imagename='spw21_HC3N/mom1_2_CH3OH.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom1_21.gal.im',overwrite=True)
imregrid(imagename='spw21_HC3N/mom2_2_CH3OH.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom2_21.gal.im',overwrite=True)

imregrid(imagename='spw23_H2CO/mom0_2_23.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom0_23.gal.im',overwrite=True)
imregrid(imagename='spw23_H2CO/mom1_23.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom1_23.gal.im',overwrite=True)
imregrid(imagename='spw23_H2CO/mom2_23.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom2_23.gal.im',overwrite=True)

imregrid(imagename='spw25_H2CO/mom0_2_25.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom0_25.gal.im',overwrite=True)
imregrid(imagename='spw25_H2CO/mom1_25.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom1_25.gal.im',overwrite=True)
imregrid(imagename='spw25_H2CO/mom2_25.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom2_25.gal.im',overwrite=True)

imregrid(imagename='spw27_SiO/mom0_3_27.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom0_27.gal.im',overwrite=True)
imregrid(imagename='spw27_SiO/mom1_27.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom1_27.gal.im',overwrite=True)
imregrid(imagename='spw27_SiO/mom2_27.image',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/mom2_27.gal.im',overwrite=True)

imregrid(imagename='ratios/ratio_12CO-13CO.im',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/ratio_12CO-13CO.gal.im',overwrite=True)
imregrid(imagename='ratios/ratio_12CO-C18O.im',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/ratio_12CO-C18O.gal.im',overwrite=True)
imregrid(imagename='ratios/ratio_13CO-C18O.im',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/ratio_13CO-C18O.gal.im',overwrite=True)
imregrid(imagename='ratios/ratio_CH3OH-13CO.im',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/ratio_CH3OH-13CO.gal.im',overwrite=True)
imregrid(imagename='ratios/ratio_H2COa-13CO.im',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/ratio_H2COa-13CO.gal.im',overwrite=True)
imregrid(imagename='ratios/ratio_H2COb-13CO.im',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/ratio_H2COb-13CO.gal.im',overwrite=True)
imregrid(imagename='ratios/ratio_SiO-13CO.im',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/ratio_SiO-13CO.gal.im',overwrite=True)

imregrid(imagename='temps/smoothtemp.im',template='GALACTIC',axes=[0,1],interpolation='cubic',output='galcoords/smoothtemp.gal.im',overwrite=True)


































