#!/usr/bin/env python3
"""KINTSUGI Short text overlays — transparent PNGs (1440x2560) for the gold-flow clip.
   3 beats: hook / concept (金継ぎ) / wisdom (傷も景色). Gold like the seam, lower-left."""
from PIL import Image, ImageDraw, ImageFont, ImageFilter

FONT = "/home/user/dan-documents/stillwave/assets/fonts/YujiBoku-Regular.ttf"
OUT = "/tmp/claude-0/-home-user-dan-documents/48780e4d-ee5f-5a8f-92df-523468e19c72/scratchpad"
W, H = 1440, 2560
CREAM = (245, 234, 210, 255)
SUBGOLD = (233, 216, 168, 255)

STOPS = [(0.00,(255,240,186)),(0.35,(240,205,112)),(0.62,(216,168,70)),(1.00,(150,96,32))]
def lerp(a,b,f): return tuple(int(a[i]+(b[i]-a[i])*f) for i in range(3))
def gcol(f):
    f=max(0.0,min(1.0,f))
    for i in range(len(STOPS)-1):
        f0,c0=STOPS[i]; f1,c1=STOPS[i+1]
        if f<=f1: return lerp(c0,c1,(f-f0)/(f1-f0))
    return STOPS[-1][1]

def gold_gradient(H_):
    col=Image.new("RGB",(1,H_))
    for y in range(H_): col.putpixel((0,y),gcol(y/H_))
    return col

def new(): return Image.new("RGBA",(W,H),(0,0,0,0))

def scrim(img, top, bot):
    """soft dark backing anchored to the LEFT third — fades out before the central seam"""
    s=Image.new("RGBA",(W,H),(0,0,0,0))
    ImageDraw.Draw(s).rounded_rectangle((-160, top, 495, bot), radius=140, fill=(0,0,0,160))
    img.alpha_composite(s.filter(ImageFilter.GaussianBlur(85)))

def draw_gold_kanji(img, chars, size, x0, y0, pitch):
    """glyphs at even centres, filled with a molten-gold gradient + glow"""
    f=ImageFont.truetype(FONT,size)
    mask=Image.new("L",(W,H),0); md=ImageDraw.Draw(mask)
    l0,_,r0,_=f.getbbox(chars[0]); c0=x0+(r0-l0)/2
    top=H; bot=0
    for i,ch in enumerate(chars):
        l,t,r,b=f.getbbox(ch)
        cx=c0+i*pitch
        md.text((cx-(l+(r-l)/2), y0), ch, font=f, fill=255)
        top=min(top,y0+t); bot=max(bot,y0+b)
    # glow
    glow=Image.new("RGBA",(W,H),(0,0,0,0))
    glow.paste((255,196,92,255),(0,0),mask.filter(ImageFilter.GaussianBlur(18)).point(lambda p:int(p*0.6)))
    img.alpha_composite(glow)
    # gradient fill spanning the ink height
    span=max(1,int(bot-top))
    grad=gold_gradient(span).resize((W,span)).convert("RGBA")
    canvas=Image.new("RGBA",(W,H),(0,0,0,0)); canvas.paste(grad,(0,int(top)))
    img.alpha_composite(Image.composite(canvas,Image.new("RGBA",(W,H),(0,0,0,0)),mask))

def draw_text(img, text, size, x, y, fill, ls=0):
    f=ImageFont.truetype(FONT,size)
    d=ImageDraw.Draw(img)
    if ls:
        cx=x
        for ch in text:
            d.text((cx,y),ch,font=f,fill=fill)
            w=d.textlength(ch,font=f); cx+=w+ls
    else:
        d.text((x,y),text,font=f,fill=fill)

# BIGGER kanji; all text shifted LEFT (x0=90) with smaller latin lines so nothing grazes the wandering seam.
X=90
# ---- BEFORE still: "Broken." (big, empty-crack frame has room) ----
before=new()
scrim(before,1430,1720)
ImageDraw.Draw(before).text((X,1500),"Broken.",font=ImageFont.truetype(FONT,168),fill=CREAM)
before.save(f"{OUT}/ov_before.png")

# ---- video beat A: "Then filled with gold." ----
filled=new()
scrim(filled,1320,1640)
d=ImageDraw.Draw(filled); ff=ImageFont.truetype(FONT,88)
for i,line in enumerate(["Then filled","with gold."]):
    d.text((X,1372+i*110),line,font=ff,fill=CREAM)
filled.save(f"{OUT}/ov_filled.png")

# ---- video beat B: concept 金継ぎ + KINTSUGI (big) ----
concept=new()
scrim(concept,1280,1680)
draw_gold_kanji(concept,["金","継","ぎ"],158,X,1320,150)
draw_text(concept,"KINTSUGI",74,X+4,1544,CREAM,ls=4)
concept.save(f"{OUT}/ov_concept.png")

# ---- AFTER still: wisdom 傷も景色 + sub (big, full-gold frame) ----
wisdom=new()
scrim(wisdom,1280,1620)
draw_gold_kanji(wisdom,["傷","も","景","色"],128,X,1320,124)
draw_text(wisdom,"Even the scar is scenery",36,X+4,1492,SUBGOLD,ls=1)
wisdom.save(f"{OUT}/ov_wisdom.png")

print("overlays saved to", OUT)
