import cv2
import os
def newjar3(x,x1,imgpath):
    
    img = cv2.imread(imgpath)
    cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Radius of circle
    radius = 28
    #color all circle
    thickness = -1
    liste2=[(0,0,255),(0,127,255),
        
        (0,255,255),
        (0,255,0), 
        (255,0,0),
        (50,0,15),
        (255,0,127)]
    liste1=[(45, 420), 
      (110, 420), 
       (175, 420), 
        (240, 420), 
         (45, 340) , 
       (110, 340), 
      (175, 340),
       (240, 340),
       (45, 265),
       (110, 265),
       (175, 265),
       (240, 265),
       (45, 190),
       (110, 190),
        (175, 190),
       (240, 190)
      ]  
    color=liste2[x1]
    i=0
    itr=iter(liste1)
    while i<x:
         cv2.circle(img, next(itr), radius, color, thickness)
         i=i+1
   

    
    
    imgpath2 = app.get_asset_url('newimg.png')
    
    return cv2.imwrite(imgpath2, img)