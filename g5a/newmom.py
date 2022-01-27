
from glob import glob
'''
names = glob('/lustre/aoc/students/sgramze/alma/G5/a/TP/2018.1.00862.S/fixfits/*')
#print(names)
print(str(names[0])[-7:-5])

for b in names:
    importfits(fitsimage=b,imagename='fixfits/g5a.spw'+b[-7:-5]+'.im')

imreframe(imagename='fixfits/g5a.spw21.im',output='fixfits/g5a.CH3OH.spw21.im',restfreq='218.44005GHz')
imreframe(imagename='fixfits/g5a.spw23.im',output='fixfits/g5a.OCS.spw23.im',restfreq='218.903355GHz')

names=glob('fixfits/g5a.J2.*.im')
#print(str(names[0])[0:11])
#print(str(names[0])[14:])

for b in names:
    imregrid(imagename=b,template='GALACTIC',output=b[0:11] + b[14:])

#immoments(imagename='fixfits/g5a.CH3OH.spw21.im',moments=[0],chans='67~246',outfile='fixfits/g5a.mom0.CH3OH.spw21.im')
#immoments(imagename='fixfits/g5a.OCS.spw23.im',moments=[0],chans='38~178',outfile='fixfits/g5a.mom0.OCS.spw23.im')
#immoments(imagename='fixfits/g5a.H2CO.spw23.im',moments=[0],chans='294~511',outfile='fixfits/g5a.mom0.H2CO.spw23.im')
#immoments(imagename='fixfits/g5a.H2CO.spw25.im',moments=[0],chans='294~511',outfile='fixfits/g5a.mom0.H2CO.spw25.im')
#immoments(imagename='fixfits/g5a.SiO.spw27.im',moments=[0],chans='294~511',outfile='fixfits/g5a.mom0.SiO.spw27.im')
#immoments(imagename='fixfits/g5a.C18O.spw31.im',moments=[0],chans='588~1023',outfile='fixfits/g5a.mom0.C18O.spw31.im')

immoments(imagename='fixfits/g5a.CH3OH.spw21.im',moments=[1],chans='67~246',outfile='fixfits/g5a.mom1.CH3OH.spw21.im',includepix=[1.0,500.0])
immoments(imagename='fixfits/g5a.H2CO.spw23.im',moments=[1],chans='294~511',outfile='fixfits/g5a.mom1.H2CO.spw23.im',includepix=[1.0,500.0])
immoments(imagename='fixfits/g5a.H2CO.spw25.im',moments=[1],chans='294~511',outfile='fixfits/g5a.mom1.H2CO.spw25.im',includepix=[1.0,500.0])
immoments(imagename='fixfits/g5a.SiO.spw27.im',moments=[1],chans='294~511',outfile='fixfits/g5a.mom1.SiO.spw27.im',includepix=[1.0,500.0])
immoments(imagename='fixfits/g5a.C18O.spw31.im',moments=[1],chans='588~1023',outfile='fixfits/g5a.mom1.C18O.spw31.im',includepix=[1.0,500.0])

immoments(imagename='fixfits/g5a.CH3OH.spw21.im',moments=[2],chans='67~246',outfile='fixfits/g5a.mom2.CH3OH.spw21.im',includepix=[1.0,500.0])
immoments(imagename='fixfits/g5a.H2CO.spw23.im',moments=[2],chans='294~511',outfile='fixfits/g5a.mom2.H2CO.spw23.im',includepix=[1.0,500.0])
immoments(imagename='fixfits/g5a.H2CO.spw25.im',moments=[2],chans='294~511',outfile='fixfits/g5a.mom2.H2CO.spw25.im',includepix=[1.0,500.0])
immoments(imagename='fixfits/g5a.SiO.spw27.im',moments=[2],chans='294~511',outfile='fixfits/g5a.mom2.SiO.spw27.im',includepix=[1.0,500.0])
immoments(imagename='fixfits/g5a.C18O.spw31.im',moments=[2],chans='588~1023',outfile='fixfits/g5a.mom2.C18O.spw31.im',includepix=[1.0,500.0])


immoments(imagename='spw21_CH3OH/g5a.CH3OH.spw21.im',moments=[0],chans='67~246',outfile='spw21_CH3OH/g5a.mom0.CH3OH.spw21.im',includepix=[1.0,500.0])
immoments(imagename='spw23_H2CO/g5a.H2CO.spw23.im',moments=[0],chans='294~511',outfile='spw23_H2CO/g5a.mom0.H2CO.spw23.im',includepix=[1.0,500.0])
immoments(imagename='spw25_H2CO/g5a.H2CO.spw25.im',moments=[0],chans='294~511',outfile='spw25_H2CO/g5a.mom0.H2CO.spw25.im',includepix=[1.0,500.0])
immoments(imagename='spw27_SiO/g5a.SiO.spw27.im',moments=[0],chans='294~511',outfile='spw27_SiO/g5a.mom0.SiO.spw27.im',includepix=[1.0,500.0])
immoments(imagename='spw31_C18O/g5a.C18O.spw31.im',moments=[0],chans='588~1023',outfile='spw31_C18O/g5a.mom0.C18O.spw31.im',includepix=[1.0,500.0])

immoments(imagename='spw17_12CO/g5a.12CO.spw17.im', moments=[0], chans='1~830', outfile='spw17_12CO/g5a.mom0.12CO.spw17.im',includepix=[1.0,500.0])
immoments(imagename='spw29_13CO/g5a.13CO.spw29.im', moments=[0], chans='588~1023', outfile='spw29_13CO/g5a.mom0.13CO.spw29.im',includepix=[1.0,500.0])

immoments(imagename='spw23_OCS/g5a.OCS.spw23.im',moments=[0],chans='38~178',outfile='spw23_OCS/g5a.mom0.OCS.spw23.im',includepix=[0.5,500.0])
immoments(imagename='spw23_OCS/g5a.OCS.spw23.im',moments=[1],chans='38~178',outfile='spw23_OCS/g5a.mom1.OCS.spw23.im',includepix=[0.75,500.0])
immoments(imagename='spw23_OCS/g5a.OCS.spw23.im',moments=[2],chans='38~178',outfile='spw23_OCS/g5a.mom2.OCS.spw23.im',includepix=[0.75,500.0])

immoments(imagename='spw25_H2CO/g5a.H2CO.spw25.im',moments=[0,1,2],outfile='spw25_H2CO/expr.H2CO.spw25',includepix=[1.0,500.0])
'''
'''
### Left
immoments(imagename='spw21_CH3OH/g5a.CH3OH.spw21.im',moments=[0],chans='67~246',outfile='spw21_CH3OH/g5a.mom0.m.CH3OH.spw21.im',includepix=[0.4,500.0])
immoments(imagename='spw23_H2CO/g5a.H2CO.spw23.im',moments=[0],chans='294~511',outfile='spw23_H2CO/g5a.mom0.m.H2CO.spw23.im',includepix=[0.5,500.0])
immoments(imagename='spw25_H2CO/g5a.H2CO.spw25.im',moments=[0],chans='294~511',outfile='spw25_H2CO/g5a.mom0.m.H2CO.spw25.im',includepix=[0.4,500.0])
immoments(imagename='spw27_SiO/g5a.SiO.spw27.im',moments=[0],chans='294~511',outfile='spw27_SiO/g5a.mom0.m.SiO.spw27.im',includepix=[0.45,500.0])
immoments(imagename='spw31_C18O/g5a.C18O.spw31.im',moments=[0],chans='588~1023',outfile='spw31_C18O/g5a.mom0.m.C18O.spw31.im',includepix=[0.5,500.0])

immoments(imagename='spw21_CH3OH/g5a.CH3OH.spw21.im',moments=[1],chans='67~246',outfile='spw21_CH3OH/g5a.mom1.m.CH3OH.spw21.im',includepix=[0.4,500.0])
immoments(imagename='spw23_H2CO/g5a.H2CO.spw23.im',moments=[1],chans='294~511',outfile='spw23_H2CO/g5a.mom1.m.H2CO.spw23.im',includepix=[0.5,500.0])
immoments(imagename='spw25_H2CO/g5a.H2CO.spw25.im',moments=[1],chans='294~511',outfile='spw25_H2CO/g5a.mom1.m.H2CO.spw25.im',includepix=[0.4,500.0])
immoments(imagename='spw27_SiO/g5a.SiO.spw27.im',moments=[1],chans='294~511',outfile='spw27_SiO/g5a.mom1.m.SiO.spw27.im',includepix=[0.45,500.0])
immoments(imagename='spw31_C18O/g5a.C18O.spw31.im',moments=[1],chans='588~1023',outfile='spw31_C18O/g5a.mom1.m.C18O.spw31.im',includepix=[0.5,500.0])

immoments(imagename='spw21_CH3OH/g5a.CH3OH.spw21.im',moments=[2],chans='67~246',outfile='spw21_CH3OH/g5a.mom2.m.CH3OH.spw21.im',includepix=[0.4,500.0])
immoments(imagename='spw23_H2CO/g5a.H2CO.spw23.im',moments=[2],chans='294~511',outfile='spw23_H2CO/g5a.mom2.m.H2CO.spw23.im',includepix=[0.5,500.0])
immoments(imagename='spw25_H2CO/g5a.H2CO.spw25.im',moments=[2],chans='294~511',outfile='spw25_H2CO/g5a.mom2.m.H2CO.spw25.im',includepix=[0.4,500.0])
immoments(imagename='spw27_SiO/g5a.SiO.spw27.im',moments=[2],chans='294~511',outfile='spw27_SiO/g5a.mom2.m.SiO.spw27.im',includepix=[0.45,500.0])
immoments(imagename='spw31_C18O/g5a.C18O.spw31.im',moments=[2],chans='588~1023',outfile='spw31_C18O/g5a.mom2.m.C18O.spw31.im',includepix=[0.5,500.0])
'''

'''
### Right
immoments(imagename='spw17_12CO/g5a.12CO.spw17.im', moments=[0], chans='870~1253', outfile='spw17_12CO/g5a.mom0.R.12CO.spw17.im',includepix=[1.0,600.0])
immoments(imagename='spw21_CH3OH/g5a.CH3OH.spw21.im',moments=[0],chans='1~67',outfile='spw21_CH3OH/g5a.mom0.R.CH3OH.spw21.im',includepix=[0.4,500.0])
immoments(imagename='spw23_H2CO/g5a.H2CO.spw23.im',moments=[0],chans='198~294',outfile='spw23_H2CO/g5a.mom0.R.H2CO.spw23.im',includepix=[0.5,500.0])
immoments(imagename='spw23_OCS/g5a.OCS.spw23.im',moments=[0],chans='1~38',outfile='spw23_OCS/g5a.mom0.R.OCS.spw23.im',includepix=[0.5,500.0])
immoments(imagename='spw25_H2CO/g5a.H2CO.spw25.im',moments=[0],chans='198~294',outfile='spw25_H2CO/g5a.mom0.R.H2CO.spw25.im',includepix=[0.4,500.0])
immoments(imagename='spw27_SiO/g5a.SiO.spw27.im',moments=[0],chans='198~294',outfile='spw27_SiO/g5a.mom0.R.SiO.spw27.im',includepix=[0.45,500.0])
immoments(imagename='spw29_13CO/g5a.13CO.spw29.im', moments=[0], chans='396~588', outfile='spw29_13CO/g5a.mom0.R.13CO.spw29.im',includepix=[1.0,500.0])
immoments(imagename='spw31_C18O/g5a.C18O.spw31.im',moments=[0],chans='396~588',outfile='spw31_C18O/g5a.mom0.R.C18O.spw31.im',includepix=[0.5,500.0])

immoments(imagename='spw17_12CO/g5a.12CO.spw17.im', moments=[1], chans='870~1253', outfile='spw17_12CO/g5a.mom1.R.12CO.spw17.im',includepix=[1.0,600.0])
immoments(imagename='spw21_CH3OH/g5a.CH3OH.spw21.im',moments=[1],chans='1~67',outfile='spw21_CH3OH/g5a.mom1.R.CH3OH.spw21.im',includepix=[0.4,500.0])
immoments(imagename='spw23_H2CO/g5a.H2CO.spw23.im',moments=[1],chans='198~294',outfile='spw23_H2CO/g5a.mom1.R.H2CO.spw23.im',includepix=[0.5,500.0])
immoments(imagename='spw23_OCS/g5a.OCS.spw23.im',moments=[1],chans='1~38',outfile='spw23_OCS/g5a.mom1.R.OCS.spw23.im',includepix=[0.75,500.0])
immoments(imagename='spw25_H2CO/g5a.H2CO.spw25.im',moments=[1],chans='198~294',outfile='spw25_H2CO/g5a.mom1.R.H2CO.spw25.im',includepix=[0.4,500.0])
immoments(imagename='spw27_SiO/g5a.SiO.spw27.im',moments=[1],chans='198~294',outfile='spw27_SiO/g5a.mom1.R.SiO.spw27.im',includepix=[0.45,500.0])
immoments(imagename='spw29_13CO/g5a.13CO.spw29.im', moments=[1], chans='396~588', outfile='spw29_13CO/g5a.mom1.R.13CO.spw29.im',includepix=[1.0,500.0])
immoments(imagename='spw31_C18O/g5a.C18O.spw31.im',moments=[1],chans='396~588',outfile='spw31_C18O/g5a.mom1.R.C18O.spw31.im',includepix=[0.5,500.0])

immoments(imagename='spw17_12CO/g5a.12CO.spw17.im', moments=[2], chans='870~1253', outfile='spw17_12CO/g5a.mom2.R.12CO.spw17.im',includepix=[1.0,600.0])
immoments(imagename='spw21_CH3OH/g5a.CH3OH.spw21.im',moments=[2],chans='1~67',outfile='spw21_CH3OH/g5a.mom2.R.CH3OH.spw21.im',includepix=[0.4,500.0])
immoments(imagename='spw23_H2CO/g5a.H2CO.spw23.im',moments=[2],chans='198~294',outfile='spw23_H2CO/g5a.mom2.R.H2CO.spw23.im',includepix=[0.5,500.0])
immoments(imagename='spw23_OCS/g5a.OCS.spw23.im',moments=[2],chans='1~38',outfile='spw23_OCS/g5a.mom2.R.OCS.spw23.im',includepix=[0.75,500.0])
immoments(imagename='spw25_H2CO/g5a.H2CO.spw25.im',moments=[2],chans='198~294',outfile='spw25_H2CO/g5a.mom2.R.H2CO.spw25.im',includepix=[0.4,500.0])
immoments(imagename='spw27_SiO/g5a.SiO.spw27.im',moments=[2],chans='198~294',outfile='spw27_SiO/g5a.mom2.R.SiO.spw27.im',includepix=[0.45,500.0])
immoments(imagename='spw29_13CO/g5a.13CO.spw29.im', moments=[2], chans='396~588', outfile='spw29_13CO/g5a.mom2.R.13CO.spw29.im',includepix=[1.0,500.0])
immoments(imagename='spw31_C18O/g5a.C18O.spw31.im',moments=[2],chans='396~588',outfile='spw31_C18O/g5a.mom2.R.C18O.spw31.im',includepix=[0.5,500.0])
'''
'''
### Adjustments
immoments(imagename='spw21_CH3OH/g5a.CH3OH.spw21.im',moments=[0],chans='1~67',outfile='spw21_CH3OH/g5a.mom0.R.CH3OH.spw21.im',includepix=[0.7,500.0])
immoments(imagename='spw21_CH3OH/g5a.CH3OH.spw21.im',moments=[1],chans='1~67',outfile='spw21_CH3OH/g5a.mom1.R.CH3OH.spw21.im',includepix=[0.7,500.0])
immoments(imagename='spw21_CH3OH/g5a.CH3OH.spw21.im',moments=[2],chans='1~67',outfile='spw21_CH3OH/g5a.mom2.R.CH3OH.spw21.im',includepix=[0.7,500.0])

immoments(imagename='spw23_H2CO/g5a.H2CO.spw23.im',moments=[0],chans='198~294',outfile='spw23_H2CO/g5a.mom0.R.H2CO.spw23.im',includepix=[0.8,500.0])
immoments(imagename='spw23_H2CO/g5a.H2CO.spw23.im',moments=[1],chans='198~294',outfile='spw23_H2CO/g5a.mom1.R.H2CO.spw23.im',includepix=[0.8,500.0])
immoments(imagename='spw23_H2CO/g5a.H2CO.spw23.im',moments=[2],chans='198~294',outfile='spw23_H2CO/g5a.mom2.R.H2CO.spw23.im',includepix=[0.8,500.0])

immoments(imagename='spw25_H2CO/g5a.H2CO.spw25.im',moments=[0],chans='198~294',outfile='spw25_H2CO/g5a.mom0.R.H2CO.spw25.im',includepix=[0.7,500.0])
immoments(imagename='spw25_H2CO/g5a.H2CO.spw25.im',moments=[1],chans='198~294',outfile='spw25_H2CO/g5a.mom1.R.H2CO.spw25.im',includepix=[0.7,500.0])
immoments(imagename='spw25_H2CO/g5a.H2CO.spw25.im',moments=[2],chans='198~294',outfile='spw25_H2CO/g5a.mom2.R.H2CO.spw25.im',includepix=[0.7,500.0])

immoments(imagename='spw27_SiO/g5a.SiO.spw27.im',moments=[0],chans='198~294',outfile='spw27_SiO/g5a.mom0.R.SiO.spw27.im',includepix=[0.7,500.0])
immoments(imagename='spw27_SiO/g5a.SiO.spw27.im',moments=[1],chans='198~294',outfile='spw27_SiO/g5a.mom1.R.SiO.spw27.im',includepix=[0.7,500.0])
immoments(imagename='spw27_SiO/g5a.SiO.spw27.im',moments=[2],chans='198~294',outfile='spw27_SiO/g5a.mom2.R.SiO.spw27.im',includepix=[0.7,500.0])

immoments(imagename='spw31_C18O/g5a.C18O.spw31.im',moments=[0],chans='396~588',outfile='spw31_C18O/g5a.mom0.R.C18O.spw31.im',includepix=[1.5,500.0])
immoments(imagename='spw31_C18O/g5a.C18O.spw31.im',moments=[1],chans='396~588',outfile='spw31_C18O/g5a.mom1.R.C18O.spw31.im',includepix=[1.5,500.0])
immoments(imagename='spw31_C18O/g5a.C18O.spw31.im',moments=[2],chans='396~588',outfile='spw31_C18O/g5a.mom2.R.C18O.spw31.im',includepix=[1.5,500.0])

immoments(imagename='spw29_13CO/g5a.13CO.spw29.im', moments=[0], chans='396~588', outfile='spw29_13CO/g5a.mom0.R.13CO.spw29.im',includepix=[1.5,500.0])
immoments(imagename='spw29_13CO/g5a.13CO.spw29.im', moments=[1], chans='396~588', outfile='spw29_13CO/g5a.mom1.R.13CO.spw29.im',includepix=[1.5,500.0])
immoments(imagename='spw29_13CO/g5a.13CO.spw29.im', moments=[2], chans='396~588', outfile='spw29_13CO/g5a.mom2.R.13CO.spw29.im',includepix=[1.5,500.0])
'''
'''
### Both Sides
immoments(imagename='spw17_12CO/g5a.12CO.spw17.im', moments=[0], chans='256~1253', outfile='spw17_12CO/g5a.mom0.tot.12CO.spw17.im',includepix=[1.0,600.0])
immoments(imagename='spw21_CH3OH/g5a.CH3OH.spw21.im',moments=[0],chans='1~246',outfile='spw21_CH3OH/g5a.mom0.tot.CH3OH.spw21.im',includepix=[0.5,500.0])
immoments(imagename='spw23_H2CO/g5a.H2CO.spw23.im',moments=[0],chans='198~447',outfile='spw23_H2CO/g5a.mom0.tot.H2CO.spw23.im',includepix=[0.5,500.0])
immoments(imagename='spw23_OCS/g5a.OCS.spw23.im',moments=[0],chans='1~192',outfile='spw23_OCS/g5a.mom0.tot.OCS.spw23.im',includepix=[0.5,500.0])
immoments(imagename='spw25_H2CO/g5a.H2CO.spw25.im',moments=[0],chans='198~447',outfile='spw25_H2CO/g5a.mom0.tot.H2CO.spw25.im',includepix=[0.5,500.0])
immoments(imagename='spw27_SiO/g5a.SiO.spw27.im',moments=[0],chans='198~447',outfile='spw27_SiO/g5a.mom0.tot.SiO.spw27.im',includepix=[0.5,500.0])
immoments(imagename='spw29_13CO/g5a.13CO.spw29.im', moments=[0], chans='396~895', outfile='spw29_13CO/g5a.mom0.tot.13CO.spw29.im',includepix=[0.5,500.0])
immoments(imagename='spw31_C18O/g5a.C18O.spw31.im',moments=[0],chans='396~895',outfile='spw31_C18O/g5a.mom0.tot.C18O.spw31.im',includepix=[0.5,500.0])

immoments(imagename='spw17_12CO/g5a.12CO.spw17.im', moments=[1], chans='256~1253', outfile='spw17_12CO/g5a.mom1.tot.12CO.spw17.im',includepix=[1.0,600.0])
immoments(imagename='spw21_CH3OH/g5a.CH3OH.spw21.im',moments=[1],chans='1~246',outfile='spw21_CH3OH/g5a.mom1.tot.CH3OH.spw21.im',includepix=[0.5,500.0])
immoments(imagename='spw23_H2CO/g5a.H2CO.spw23.im',moments=[1],chans='198~447',outfile='spw23_H2CO/g5a.mom1.tot.H2CO.spw23.im',includepix=[0.5,500.0])
immoments(imagename='spw23_OCS/g5a.OCS.spw23.im',moments=[1],chans='1~192',outfile='spw23_OCS/g5a.mom1.tot.OCS.spw23.im',includepix=[0.5,500.0])
immoments(imagename='spw25_H2CO/g5a.H2CO.spw25.im',moments=[1],chans='198~447',outfile='spw25_H2CO/g5a.mom1.tot.H2CO.spw25.im',includepix=[0.5,500.0])
immoments(imagename='spw27_SiO/g5a.SiO.spw27.im',moments=[1],chans='198~447',outfile='spw27_SiO/g5a.mom1.tot.SiO.spw27.im',includepix=[0.5,500.0])
immoments(imagename='spw29_13CO/g5a.13CO.spw29.im', moments=[1], chans='396~895', outfile='spw29_13CO/g5a.mom1.tot.13CO.spw29.im',includepix=[0.5,500.0])
immoments(imagename='spw31_C18O/g5a.C18O.spw31.im',moments=[1],chans='396~895',outfile='spw31_C18O/g5a.mom1.tot.C18O.spw31.im',includepix=[0.5,500.0])

immoments(imagename='spw17_12CO/g5a.12CO.spw17.im', moments=[2], chans='256~1253', outfile='spw17_12CO/g5a.mom2.tot.12CO.spw17.im',includepix=[1.0,600.0])
immoments(imagename='spw21_CH3OH/g5a.CH3OH.spw21.im',moments=[2],chans='1~246',outfile='spw21_CH3OH/g5a.mom2.tot.CH3OH.spw21.im',includepix=[0.5,500.0])
immoments(imagename='spw23_H2CO/g5a.H2CO.spw23.im',moments=[2],chans='198~447',outfile='spw23_H2CO/g5a.mom2.tot.H2CO.spw23.im',includepix=[0.5,500.0])
immoments(imagename='spw23_OCS/g5a.OCS.spw23.im',moments=[2],chans='1~192',outfile='spw23_OCS/g5a.mom2.tot.OCS.spw23.im',includepix=[0.5,500.0])
immoments(imagename='spw25_H2CO/g5a.H2CO.spw25.im',moments=[2],chans='198~447',outfile='spw25_H2CO/g5a.mom2.tot.H2CO.spw25.im',includepix=[0.5,500.0])
immoments(imagename='spw27_SiO/g5a.SiO.spw27.im',moments=[2],chans='198~447',outfile='spw27_SiO/g5a.mom2.tot.SiO.spw27.im',includepix=[0.5,500.0])
immoments(imagename='spw29_13CO/g5a.13CO.spw29.im', moments=[2], chans='396~895', outfile='spw29_13CO/g5a.mom2.tot.13CO.spw29.im',includepix=[0.5,500.0])
immoments(imagename='spw31_C18O/g5a.C18O.spw31.im',moments=[2],chans='396~895',outfile='spw31_C18O/g5a.mom2.tot.C18O.spw31.im',includepix=[0.5,500.0])
'''
### Adjustments
immoments(imagename='spw21_CH3OH/g5a.CH3OH.spw21.im',moments=[1],chans='1~246',outfile='spw21_CH3OH/g5a.mom1.tot.CH3OH.spw21.im',includepix=[0.8,500.0])
immoments(imagename='spw21_CH3OH/g5a.CH3OH.spw21.im',moments=[2],chans='1~246',outfile='spw21_CH3OH/g5a.mom2.tot.CH3OH.spw21.im',includepix=[0.7,500.0])

immoments(imagename='spw23_H2CO/g5a.H2CO.spw23.im',moments=[2],chans='294~511',outfile='mom0/g5a.mom2.6L.H2CO.spw23.im',includepix=[0.75,500.0])

immoments(imagename='spw23_H2CO/g5a.H2CO.spw23.im',moments=[1],chans='198~447',outfile='mom1/g5a.mom1.4tot.H2CO.spw23.im',includepix=[0.75,500.0])
immoments(imagename='spw23_H2CO/g5a.H2CO.spw23.im',moments=[2],chans='198~447',outfile='mom1/g5a.mom2.4tot.H2CO.spw23.im',includepix=[0.75,500.0])

immoments(imagename='spw23_OCS/g5a.OCS.spw23.im',moments=[1],chans='1~192',outfile='mom1/g5a.mom1.4tot.OCS.spw23.im',includepix=[0.75,500.0])
immoments(imagename='spw23_OCS/g5a.OCS.spw23.im',moments=[2],chans='1~192',outfile='mom1/g5a.mom2.4tot.OCS.spw23.im',includepix=[0.75,500.0])

immoments(imagename='spw27_SiO/g5a.SiO.spw27.im',moments=[1],chans='198~447',outfile='mom1/g5a.mom1.4tot.SiO.spw27.im',includepix=[0.8,500.0])
immoments(imagename='spw27_SiO/g5a.SiO.spw27.im',moments=[2],chans='198~447',outfile='mom1/g5a.mom2.4tot.SiO.spw27.im',includepix=[0.8,500.0])


