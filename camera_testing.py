import time, cv2 
import numpy as np
import math

vid = cv2.VideoCapture(1)
time.sleep(2)

while True:
    ret, frame = vid.read()
    cv2.imshow("frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):  # press 'q' button to quit
        stream_connection.send(False)
        break
vid.release()
cv2.destroyAllWindows()