import cv2
import numpy as np

# Reading an image

img=cv2.imread("C:/Users/DjS/Desktop/Python projects/OCR/Test images/hindi-news-1.jpg")

#img_grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#img_b=img[:,:,0]
#img_r=img[:,:,1]
#img_g=img[:,:,2]
#new_img=np.hstack((img_b,img_r,img_g))




#img_crop=img[500:800,0:500]

#cv2.imshow("window",img_crop)
#cv2.waitKey(0)


#while True:
#    cv2.imshow("window",img)
#    if cv2.waitKey(1) & 0xFF==ord('x'):
#        break

flag=False
ix=-1
iy=-1

def crop(event,x,y,flags,params):
    global flag, ix, iy
    if event==1:
        flag=True
        ix=x
        iy=y

    elif event==0:
        if flag==True:
            cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),thickness=0,color=(0,0,0))

    elif event==4:
        fx=x
        fy=y

        flag=False
        cv2.rectangle(img,pt1=(ix,iy),pt2=(x,y),thickness=0,color=(0,0,0))
        cropping=img[iy:fy,ix:fx]
        cv2.imshow("new_Window",cropping)
        cv2.waitKey(0)



cv2.namedWindow(winname="Window")
cv2.setMouseCallback("Window",crop)

while True:
   cv2.imshow("Window",img)
   if cv2.waitKey(1) & 0xFF==ord('x'):
      break

cv2.destroyAllWindows()