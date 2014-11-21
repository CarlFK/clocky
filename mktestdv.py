#!/usr/bin/python

# makes test.dv 
# single frame dv files used as inputs for dvswitch.

import Image, ImageDraw, ImageFont

import subprocess
from optparse import OptionParser

def shell(cmd):
        if not isinstance(cmd,list):
                cmd = cmd.split()
        print cmd
        return subprocess.Popen(cmd)

fontdir='/usr/share/fonts/truetype/freefont'

def mktest(slide_size,p):

    im=Image.new("RGBA",slide_size,colors[0])
    draw = ImageDraw.Draw(im)
    steps = 10
    for i in xrange(steps):
        # j goes from 0 to 1, k goes from 1 to 0.
        j = i/float(steps)
        k = 1-j
        # print i,j,k
        center = slide_size[0]/2,slide_size[1]/2
        fill=[
            (256*j,256*j,256*k),
            (256*j,256*k,256*k),
            (256*j,256*k,256*j),
            ][p-1]
        draw.rectangle([
          (center[0]-(slide_size[0]*k/2),center[1]-(slide_size[1]*k/2)),
          (center[0]+(slide_size[0]*k/2),center[1]+(slide_size[1]*k/2))
          ], fill=fill)

    font = ImageFont.truetype('%s/FreeSans.ttf'%fontdir, 400 )
    text=str(p)
    (width, height)=font.getsize(text)
    x,y=center[0]-width/2, center[1]-height/2 +40
    draw.text((x,y),text,fill='white',font=font)

    name='test-%s'%p
    pngname,dvname="/tmp/%s.png"%name,"/home/carl/temp/%s.dv"%name
    im.save(pngname, format='PNG')
    shell("ffmpeg -loop_input -i %s -f s16le -i /dev/zero -target ntsc-dv -vframes 2 -y %s" % (pngname,dvname) ).wait()
        

if __name__=='__main__':

    slide_size=(720,480)
    # slide_size=(360,288)
    colors=('#0c002b','#d8d2c3')
    # colors=('white','#d8d2c3')

    mktest(slide_size,1)
    mktest(slide_size,2)
    mktest(slide_size,3)

