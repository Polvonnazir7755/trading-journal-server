from PIL import Image, ImageFilter
import numpy as np
from collections import deque

def cutout(src,dst,tol,feather=1.3):
    im=Image.open(src).convert('RGB'); a=np.asarray(im).astype(np.int16); h,w,_=a.shape
    border=np.concatenate([a[0,:],a[-1,:],a[:,0],a[:,-1]]); seed=np.median(border,axis=0)
    dist=np.sqrt(((a-seed)**2).sum(axis=2)); cand=dist<tol
    vis=np.zeros((h,w),bool); dq=deque()
    for x in range(w):
        for y in (0,h-1):
            if cand[y,x] and not vis[y,x]: vis[y,x]=True; dq.append((y,x))
    for y in range(h):
        for x in (0,w-1):
            if cand[y,x] and not vis[y,x]: vis[y,x]=True; dq.append((y,x))
    while dq:
        y,x=dq.popleft()
        for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
            ny,nx=y+dy,x+dx
            if 0<=ny<h and 0<=nx<w and cand[ny,nx] and not vis[ny,nx]:
                vis[ny,nx]=True; dq.append((ny,nx))
    al=np.where(vis,0,255).astype(np.uint8)
    m=Image.fromarray(al).filter(ImageFilter.GaussianBlur(feather))
    o=im.convert('RGBA'); o.putalpha(m); o.save(dst)
    print(dst, 'transparent%', round(vis.mean()*100,1))

import sys
cutout(sys.argv[1],sys.argv[2],float(sys.argv[3]))
