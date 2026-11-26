from PIL import Image, ImageFilter
import numpy as np, sys
rng=np.random.default_rng(11)
src,out_full,out_prev=sys.argv[1:4]
im=Image.open(src).convert('RGB'); W,H=im.size
HZ=1084
base=np.asarray(im).astype(np.float32); lum=base.mean(axis=2)
yy,xx=np.mgrid[0:H,0:W].astype(np.float32)
# weight map: left-heavy, none near moon, thinning at horizon
fx=np.clip(1.35-xx/2400,0,1)
fm=np.clip((np.hypot(xx-2650,yy-620)-650)/650,0,1)
fh=np.clip((HZ-30-yy)/220,0,1)
wmap=fx*fm*fh
# faint milky band: diagonal from upper-left down toward the horizon
d=( (xx*0.42 + yy) - 1050 )/260
band=np.exp(-d**2)*np.clip(1.1-xx/2200,0,1)*fh
sky=np.zeros((H,W),np.float32)
n=5200
xs=rng.uniform(0,W,n); ys=rng.uniform(0,HZ,n)
# extra stars concentrated in the band
m2=2600; t=rng.uniform(0,1,m2)
bx=rng.uniform(0,2200,m2); by=1050-bx*0.42+rng.normal(0,170,m2)
xs=np.concatenate([xs,bx]); ys=np.concatenate([ys,by])
mag=rng.power(0.28,len(xs))
for x,y,m in zip(xs,ys,mag):
    if not (0<=x<W and 0<=y<HZ): continue
    b=m*wmap[int(y),int(x)]
    if b<0.05: continue
    xi,yi=int(x),int(y)
    if m>0.93:
        sky[yi-1:yi+2,xi-1:xi+2]+=b*230
    else:
        sky[yi,xi]+=b*255
s=np.asarray(Image.fromarray(np.clip(sky,0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(1.0))).astype(np.float32)*2.4
glow=np.asarray(Image.fromarray(np.clip(band*255,0,255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(60))).astype(np.float32)*0.10
s=s+glow
s*=np.clip((40-lum)/20,0,1)   # only over dark sky
# reflection
ref=np.zeros_like(s); L=min(H-HZ,HZ); ref[HZ:HZ+L]=s[HZ-L:HZ][::-1]
r=Image.fromarray(np.clip(ref,0,255).astype(np.uint8))
r=r.filter(ImageFilter.GaussianBlur(1.4))
ref=np.asarray(r).astype(np.float32)
# horizontal smear for water
k=np.ones(9)/9
ref=np.apply_along_axis(lambda row: np.convolve(row,k,'same'),1,ref)*3.2*0.5
depth=np.clip(1-(yy-HZ)/900,0.35,1)   # fainter toward the viewer
ref*=depth*np.clip((45-lum)/20,0,1)
tint=np.array([0.90,0.95,1.0])
out=np.clip(base+(s[...,None]+ref[...,None])*tint,0,255).astype(np.uint8)
o=Image.fromarray(out); o.save(out_full,quality=95)
o.resize((1920,1080),Image.LANCZOS).save(out_prev,quality=92)
