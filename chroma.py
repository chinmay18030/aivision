
from aivision import ChromaModule as cm 
import cv2 

#Capturing the initial frame for creation of background
while(True):
	cv2.waitKey(1000)
	ret,init_frame = cap.read()
	#check if the frame is returned then brake
	if(ret):
		break
# capturing the feed
cap = cv2.VideoCapture(0)
#giving the upper values and lower values of the colour
# btw these values are pf green
up = np.array([65, 60, 60])
low = np.array([80, 255, 255])
# initializing chroma 
chroma = cm.Chroma()

while True:
  _, frame = cap.read()
  chroma_effect = chroma.add_chroma(frame,init_frame)
  cv2.imshow("Chroma effect AI vision",chroma_effect)
  if cv2.waitKey(0) & 0xFF==ord('d'):
    break
  
