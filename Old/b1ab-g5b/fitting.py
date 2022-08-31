# Attempting astroPy polynomial fitting.
from astropy.modeling import models, fitting
import numpy as np
import scipy.stats as stats
from mathplotlib import pyplot as plt 

#Fixing CO 2-1 from B1 a
imcontsub(imagename='b1a17.image', linefile='test_line17.image', contfile='test_cont17.image', fitorder=4, chans='1~510, 1100~1150, 1960~2047')

#Trying to fix CO 2-1 from B1 b
imcontsub(imagename='b1b17.image', linefile='lineB17.image', contfile='contB17.image', fitorder=4, chans='1~700, 1030~1100, 1110~1200, 1270~1280, 1350~1355, 1400~1410, 1550~1555, 1600~1610, 2000~2047')

imcontsub(imagename='b1b17.image', linefile='line7B17.image', contfile='cont7B17.image', fitorder=4, chans='1~700, 1030~1100, 1110~1200, 170~1280, 1350~1355, 1400~1410, 1550~1555, 1600~1610,1780~1785, 2000~2047')

#importing fits image to casa 

importfits(fitsimage='brad17.fits', imagename='brad17.image')

# Importing B1 7m images to casa
importfits(fitsimage='', imagename='bcube#.image')
importfits(fitsimage='', imagename='bmfs#.image')

importfits(fitsimage='member.uid___A001_X133e_X40.Bania1_sci.spw16.cube.I.pbcor.fits', imagename='bcube16.image')
importfits(fitsimage='member.uid___A001_X133e_X40.Bania1_sci.spw16.mfs.I.pbcor.fits', imagename='bmfs16.image')

importfits(fitsimage='member.uid___A001_X133e_X40.Bania1_sci.spw18.cube.I.pbcor.fits', imagename='bcube18.image')
importfits(fitsimage='member.uid___A001_X133e_X40.Bania1_sci.spw18.mfs.I.pbcor.fits', imagename='bmfs18.image')

importfits(fitsimage='member.uid___A001_X133e_X40.Bania1_sci.spw20.cube.I.pbcor.fits', imagename='bcube20.image')
importfits(fitsimage='member.uid___A001_X133e_X40.Bania1_sci.spw20.mfs.I.pbcor.fits', imagename='bmfs20.image')

importfits(fitsimage='member.uid___A001_X133e_X40.Bania1_sci.spw22.cube.I.pbcor.fits', imagename='bcub22.image')
importfits(fitsimage='member.uid___A001_X133e_X40.Bania1_sci.spw22.mfs.I.pbcor.fits', imagename='bmfs22.image')

importfits(fitsimage='member.uid___A001_X133e_X40.Bania1_sci.spw24.cube.I.pbcor.fits', imagename='bcube24.image')
importfits(fitsimage='member.uid___A001_X133e_X40.Bania1_sci.spw24.mfs.I.pbcor.fits', imagename='bmfs24.image')

importfits(fitsimage='member.uid___A001_X133e_X40.Bania1_sci.spw26.cube.I.pbcor.fits', imagename='bcube26.image')
importfits(fitsimage='member.uid___A001_X133e_X40.Bania1_sci.spw26.mfs.I.pbcor.fits', imagename='bmfs26.image')

importfits(fitsimage='member.uid___A001_X133e_X40.Bania1_sci.spw28.cube.I.pbcor.fits', imagename='bcube28.image')
importfits(fitsimage='member.uid___A001_X133e_X40.Bania1_sci.spw28.mfs.I.pbcor.fits', imagename='bmfs28.image')

importfits(fitsimage='member.uid___A001_X133e_X40.Bania1_sci.spw30.cube.I.pbcor.fits', imagename='bcube30.image')
importfits(fitsimage='member.uid___A001_X133e_X40.Bania1_sci.spw30.mfs.I.pbcor.fits', imagename='bmfs30.image')

# Importing G5 7m images to casa
importfits(fitsimage='', imagename='gcube#.image')
importfits(fitsimage='', imagename='gmfs#.image')

importfits(fitsimage='member.uid___A001_X133e_X3a.G5_sci.spw16.cube.I.pbcor.fits', imagename='gcube16.image')
importfits(fitsimage='member.uid___A001_X133e_X3a.G5_sci.spw16.mfs.I.pbcor.fits', imagename='gmfs16.image')

importfits(fitsimage='member.uid___A001_X133e_X3a.G5_sci.spw18.cube.I.pbcor.fits', imagename='gcube18.image')
importfits(fitsimage='member.uid___A001_X133e_X3a.G5_sci.spw18.mfs.I.pbcor.fits', imagename='gmfs18.image')

importfits(fitsimage='member.uid___A001_X133e_X3a.G5_sci.spw20.cube.I.pbcor.fits', imagename='gcube20.image')
importfits(fitsimage='member.uid___A001_X133e_X3a.G5_sci.spw20.mfs.I.pbcor.fits', imagename='gmfs20.image')

importfits(fitsimage='member.uid___A001_X133e_X3a.G5_sci.spw22.cube.I.pbcor.fits', imagename='gcube22.image')
importfits(fitsimage='member.uid___A001_X133e_X3a.G5_sci.spw22.mfs.I.pbcor.fits', imagename='gmfs22.image')

importfits(fitsimage='member.uid___A001_X133e_X3a.G5_sci.spw24.cube.I.pbcor.fits', imagename='gcub24.image')
importfits(fitsimage='member.uid___A001_X133e_X3a.G5_sci.spw24.mfs.I.pbcor.fits', imagename='gmfs24.image')

importfits(fitsimage='member.uid___A001_X133e_X3a.G5_sci.spw26.cube.I.pbcor.fits', imagename='gcube26.image')
importfits(fitsimage='member.uid___A001_X133e_X3a.G5_sci.spw26.mfs.I.pbcor.fits', imagename='gmfs26.image')

importfits(fitsimage='member.uid___A001_X133e_X3a.G5_sci.spw28.cube.I.pbcor.fits', imagename='gcube28.image')
importfits(fitsimage='member.uid___A001_X133e_X3a.G5_sci.spw28.mfs.I.pbcor.fits', imagename='gmfs28.image')

importfits(fitsimage='member.uid___A001_X133e_X3a.G5_sci.spw30.cube.I.pbcor.fits', imagename='gcube30.image')
importfits(fitsimage='member.uid___A001_X133e_X3a.G5_sci.spw30.mfs.I.pbcor.fits', imagename='gmfs30.image')


imcontsub(imagename='', linefile='', contfile='', fitorder=int, chans='')

# Bania 1 a fit fixing
'''
imcontsub(imagename='', linefile='', contfile='', fitorder=5, chans='')
'''
imcontsub(imagename='brad21.image', linefile='try1_line21.image', contfile='try1_cont21.image', fitorder=5, chans='1~5, 20~30, 100~460')

imcontsub(imagename='brad23.image', linefile='try1_line23.image', contfile='try1_cont23.image', fitorder=4, chans='1~20, 30~254, 335~508')

imcontsub(imagename='brad25.image', linefile='try1_line25.image', contfile='try1_cont25.image', fitorder=4, chans='1~240, 350~435, 455~509')

imcontsub(imagename='brad27.image', linefile='try1_line27.image', contfile='try1_cont27.image', fitorder=4, chans='1~270, 340~508')

imcontsub(imagename='brad29.image', linefile='try1_line29.image', contfile='try1_cont29.image', fitorder=4, chans='1~95, 130~139, 168~204, 301~318, 340~355, 445~495, 750~1020')
imcontsub(imagename='brad29.image', linefile='try2_line29.image', contfile='try2_cont29.image', fitorder=4, chans='1~85, 183~194, 448~478, 753~789, 863~889, 956~1023')

imcontsub(imagename='brad31.image', linefile='try1_line31.image', contfile='try1_cont31.image', fitorder=4, chans='77~92, 137~200, 266~269, 387~400, 417~427, 455~485, 516~523, 716~1023')

#Bania 1 b fit fixing
imcontsub(imagename='brad17.image', linefile='try1_line17.image', contfile='try1_cont17.image', fitorder=5, chans='1~665, 1113~1182, 1258~1272, 1562~1581, 1990~2046')

imcontsub(imagename='brad21.image', linefile='try1_line21.image', contfile='try1_cont21.image', fitorder=5, chans='22~29, 81~475')

imcontsub(imagename='brad23.image', linefile='try1_line23.image', contfile='try1_cont23.image', fitorder=5, chans='1~226, 321~511')

imcontsub(imagename='brad27.image', linefile='try1_line27.image', contfile='try1_cont27.image', fitorder=5, chans='1~243, 302~502')

imcontsub(imagename='brad29.image', linefile='try1_line29.image', contfile='try1_cont29.image', fitorder=4, chans='1~50, 244~257, 430~488, 673~1020')

imcontsub(imagename='brad31.image', linefile='try4_line31.image', contfile='try4_cont31.image', fitorder=5, chans='93~211, 251~280, 322~355, 418~480, 625~1020')

# Moment maps for Bania 1 a
immoments(imagename='fixed17.image', moments=[0], chans='560~1064', outfile='mom0_B1_17.image')
immoments(imagename='fixed17.image', moments=[0], chans='1134~1260', outfile='mom0_F3_17.image')
immoments(imagename='fixed17.image', moments=[0], chans='1261~1423', outfile='mom0_CM_17.image')
immoments(imagename='fixed17.image', moments=[0], chans='1424~1771', outfile='mom0_N3_17.image')
immoments(imagename='fixed17.image', moments=[0], chans='1771~2000', outfile='mom0_LR_17.image')

immoments(imagename='fixed17.image', moments=[0], chans='500~778', outfile='1test17.image')
immoments(imagename='fixed17.image', moments=[0], chans='778~1036', outfile='2test17.image')

immoments(imagename='fixed21.image', moments=[0], chans='1~456', outfile='mom0_1_21.image')

immoments(imagename='fixed23.image', moments=[0], chans='1~500', outfile='mom0_1_23.image')
immoments(imagename='fixed23.image', moments=[0], chans='1~305', outfile='1test23.image')
immoments(imagename='fixed23.image', moments=[0], chans='305~500', outfile='2test23.image')

immoments(imagename='fixed25.image', moments=[0], chans='1~500', outfile='mom0_1_25.image')
immoments(imagename='fixed25.image', moments=[0], chans='1~305', outfile='1test25.image')
immoments(imagename='fixed25.image', moments=[0], chans='305~500', outfile='2test25.image')

immoments(imagename='fixed27.image', moments=[0], chans='1~510', outfile='mom0_1_27.image')
immoments(imagename='fixed27.image', moments=[0], chans='1~293', outfile='1test27.image')
immoments(imagename='fixed27.image', moments=[0], chans='293~510', outfile='2test27.image')

immoments(imagename='fixed29.image', moments=[0], chans='511~716', outfile='mom0_B1_29.image')
immoments(imagename='fixed29.image', moments=[0], chans='410~510', outfile='mom0_F3_29.image')
immoments(imagename='fixed29.image', moments=[0], chans='345~422', outfile='mom0_CM_29.image')
immoments(imagename='fixed29.image', moments=[0], chans='230~345', outfile='mom0_N3_29.image')
immoments(imagename='fixed29.image', moments=[0], chans='115~218', outfile='mom0_LR_29.image')

immoments(imagename='fixed31.image', moments=[0], chans='480~725', outfile='mom0_B1_31.image')
immoments(imagename='fixed31.image', moments=[0], chans='400~470', outfile='mom0_F3_31.image')
immoments(imagename='fixed31.image', moments=[0], chans='345~387', outfile='mom0_CM_31.image')
immoments(imagename='fixed31.image', moments=[0], chans='200~335', outfile='mom0_N3_31.image')
immoments(imagename='fixed31.image', moments=[0], chans='93~150', outfile='mom0_LR_31.image')
immoments(imagename='fixed31.image', moments=[0], chans='480~515', outfile='1test31.image')
immoments(imagename='fixed31.image', moments=[0], chans='1~200', outfile='2test31.image')

# Bania 1 b Moment Maps
immoments(imagename='fixed17.image', moments=[0], chans='716~1150', outfile='mom0_B1_17.image')
immoments(imagename='fixed17.image', moments=[0], chans='1146~1217', outfile='mom0_F3_17.image')
immoments(imagename='fixed17.image', moments=[0], chans='1228~1310', outfile='mom0_CM_17.image')
immoments(imagename='fixed17.image', moments=[0], chans='1315~1458', outfile='mom0_N3_17.image')
immoments(imagename='fixed17.image', moments=[0], chans='1470~2046', outfile='mom0_LR_17.image')

immoments(imagename='fixed21.image', moments=[0], chans='1~200', outfile='mom0_1_21.image')

immoments(imagename='fixed23.image', moments=[0], chans='226~321', outfile='mom0_1_23.image')

immoments(imagename='fixed25.image', moments=[0], chans='1~450', outfile='mom0_1_25.image')
immoments(imagename='fixed25.image', moments=[0], chans='240~330', outfile='mom0_2_25.image')
immoments(imagename='fixed25.image', moments=[0], chans='150~220', outfile='test25.image')

immoments(imagename='fixed27.image', moments=[0], chans='1~480', outfile='mom0_1_27.image')
immoments(imagename='fixed27.image', moments=[0], chans='238~328', outfile='mom0_2_27.image')

immoments(imagename='fixed29.image', moments=[0], chans='485~639', outfile='mom0_B1_29.image')
immoments(imagename='fixed29.image', moments=[0], chans='409~447', outfile='mom0_F3_29.image')
immoments(imagename='fixed29.image', moments=[0], chans='358~409', outfile='mom0_CM_29.image')
immoments(imagename='fixed29.image', moments=[0], chans='281~358', outfile='mom0_N3_29.image')
immoments(imagename='fixed29.image', moments=[0], chans='127~255', outfile='mom0_LR_29.image')

immoments(imagename='fixed31.image', moments=[0], chans='483~663', outfile='mom0_B1_31.image')
immoments(imagename='fixed31.image', moments=[0], chans='393~483', outfile='mom0_F3_31.image')
immoments(imagename='fixed31.image', moments=[0], chans='357~393', outfile='mom0_CM_31.image')
immoments(imagename='fixed31.image', moments=[0], chans='273~333', outfile='mom0_N3_31.image')
immoments(imagename='fixed31.image', moments=[0], chans='93~213', outfile='mom0_LR_31.image')
immoments(imagename='fixed31.image', moments=[0], chans='213~258', outfile='mom0_test_31.image')


# Make sure that moment maps are over same velocities for all
# B1a
immoments(imagename='fixed17.image', moments=[0], chans='562~1074', outfile='mom0_2_B1_17.image')
immoments(imagename='fixed21.image', moments=[0], chans='242~370', outfile='mom0_2_21.image')
immoments(imagename='fixed23.image', moments=[0], chans='242~370', outfile='mom0_2_23.image')
immoments(imagename='fixed25.image', moments=[0], chans='242~370', outfile='mom0_2_25.image')
immoments(imagename='fixed27.image', moments=[0], chans='242~370', outfile='mom0_2_27.image')
immoments(imagename='fixed29.image', moments=[0], chans='485~741', outfile='mom0_2_B1_29.image')
immoments(imagename='fixed31.image', moments=[0], chans='485~741', outfile='mom0_2_B1_31.image')

immoments(imagename='fixed17.image', moments=[0], chans='1125~1202', outfile='mom0_2_F3_17.image')
immoments(imagename='fixed17.image', moments=[0], chans='1202~1356', outfile='mom0_2_CM_17.image')
immoments(imagename='fixed17.image', moments=[0], chans='1356~1586', outfile='mom0_2_N3_17.image')
immoments(imagename='fixed17.image', moments=[0], chans='1637~1765', outfile='mom0_2_LR_17.image')

immoments(imagename='fixed29.image', moments=[0], chans='421~460', outfile='mom0_2_F3_29.image')
immoments(imagename='fixed29.image', moments=[0], chans='345~421', outfile='mom0_2_CM_29.image')
immoments(imagename='fixed29.image', moments=[0], chans='230~345', outfile='mom0_2_N3_29.image')
immoments(imagename='fixed29.image', moments=[0], chans='140~204', outfile='mom0_2_LR_29.image')

immoments(imagename='fixed31.image', moments=[0], chans='421~460', outfile='mom0_2_F3_31.image')
immoments(imagename='fixed31.image', moments=[0], chans='345~421', outfile='mom0_2_CM_31.image')
immoments(imagename='fixed31.image', moments=[0], chans='230~345', outfile='mom0_2_N3_31.image')
immoments(imagename='fixed31.image', moments=[0], chans='140~204', outfile='mom0_2_LR_31.image')

immoments(imagename='fixed21.image', moments=[0], chans='0~129', outfile='mom0_3_21.image')
immoments(imagename='fixed21.image', moments=[0], chans='0~70', outfile='mom0_5_21.image')
immoments(imagename='fixed21.image', moments=[0], chans='70~129', outfile='mom0_6_21.image')

immoments(imagename='fixed23.image', moments=[0], chans='102~140', outfile='mom0_t1_23.image')
immoments(imagename='fixed23.image', moments=[0], chans='180~210', outfile='mom0_t2_23.image')


immoments(imagename='fixed25.image', moments=[0], chans='344~383', outfile='mom0_t1_25.image')






# B1b
immoments(imagename='fixed17.image', moments=[0], chans='562~1074', outfile='mom0_2_B1_17.image')
immoments(imagename='fixed21.image', moments=[0], chans='242~370', outfile='mom0_2_21.image')
immoments(imagename='fixed23.image', moments=[0], chans='242~370', outfile='mom0_2_23.image')
immoments(imagename='fixed25.image', moments=[0], chans='242~370', outfile='mom0_2_25.image')
immoments(imagename='fixed27.image', moments=[0], chans='242~370', outfile='mom0_3_27.image')
immoments(imagename='fixed29.image', moments=[0], chans='485~741', outfile='mom0_2_B1_29.image')
immoments(imagename='fixed31.image', moments=[0], chans='485~741', outfile='mom0_2_B1_31.image')

immoments(imagename='fixed17.image', moments=[0], chans='1125~1217', outfile='mom0_2_F3_17.image')
immoments(imagename='fixed17.image', moments=[0], chans='1228~1330', outfile='mom0_2_CM_17.image')
immoments(imagename='fixed17.image', moments=[0], chans='1330~1586', outfile='mom0_2_N3_17.image')
immoments(imagename='fixed17.image', moments=[0], chans='1637~1765', outfile='mom0_2_LR_17.image')

immoments(imagename='fixed29.image', moments=[0], chans='414~460', outfile='mom0_2_F3_29.image')
immoments(imagename='fixed29.image', moments=[0], chans='358~409', outfile='mom0_2_CM_29.image')
immoments(imagename='fixed29.image', moments=[0], chans='230~358', outfile='mom0_2_N3_29.image')
immoments(imagename='fixed29.image', moments=[0], chans='140~204', outfile='mom0_2_LR_29.image')

immoments(imagename='fixed31.image', moments=[0], chans='414~460', outfile='mom0_2_F3_31.image')
immoments(imagename='fixed31.image', moments=[0], chans='358~409', outfile='mom0_2_CM_31.image')
immoments(imagename='fixed31.image', moments=[0], chans='230~358', outfile='mom0_2_N3_31.image')
immoments(imagename='fixed31.image', moments=[0], chans='140~204', outfile='mom0_2_LR_31.image')

immoments(imagename='test19.image', moments=[0], chans='958~1037', outfile='mom0_test_19.image')

immoments(imagename='fixed25.image', moments=[0], chans='172~210', outfile='mom0_CM_25.image')
immoments(imagename='fixed25.image', moments=[0], chans='420~481', outfile='mom0_t1_25.image')
immoments(imagename='fixed25.image', moments=[0], chans='306~351', outfile='mom0_t2_25.image')

immoments(imagename='fixed21.image', moments=[0], chans='263~304', outfile='mom0_3_21.image')
immoments(imagename='fixed21.image', moments=[0], chans='0~129', outfile='mom0_CH3OH_21.image')

immoments(imagename='fixed23.image', moments=[0], chans='96~157', outfile='mom0_t1_23.image')
immoments(imagename='fixed27.image', moments=[0], chans='190~240', outfile='mom0_t1_27.image')

immoments(imagename='fixed31.image', moments=[0], chans='0~93', outfile='mom0_t1_31.image')


immoments(imagename='spw24_H2CO/bcube24.image', moments=[0], chans='160~250', outfile='spw24_H2CO/mom0_try2_24.image')




immoments(imagename='spw23_H2CO/fixed23.image', moments=[0], includepix=[0.4, 20.0], chans='242~370', outfile='temps/mom0_mskd2_23.image')
immoments(imagename='spw25_H2CO/fixed25.image', moments=[0], includepix=[0.4, 20.0], chans='242~370', outfile='temps/mom0_mskd2_25.image')


immoments(imagename='fixed21.image', moments=[0], chans='0~129', outfile='mom0_CH3OH_2_21.image')





