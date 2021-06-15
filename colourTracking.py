from aivision import ColourTracking as ct
import cv2 

cap = cv2.VideoCapture(0)
#upper and lower values of green
up = np.array([65, 60, 60])
low = np.array([80, 255, 255])
#initializing the colour detector
cd = ct.ColourDetector(up,low)

while True:
  _,frame = cap.read()
  mask = cd.mask_colour(frame)# gives the name of the frame
  frame = cd.draw_rect(frame,mask,1000)# the third parameter is the limit, if the colour area if less than the limit specified rectangle won't be formed
  cv2.imshow("Colour tracking AI Vision")
  if cv2.waitKey(1) & 0xFF == ord('d'):
    break
cap.release()
cv2.destroyAllWindows()
