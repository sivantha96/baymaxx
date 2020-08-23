from multiprocessing import Pool, Lock, Process, Array, Queue, Pipe
import time
import cv2 
import numpy as np
import math


def stream_video(frame_connection, stream_connection):
    vid = cv2.VideoCapture(0)
    time.sleep(2)
    while True:
        if stream_connection.recv() == False:
            break
        ret, frame = vid.read()
        frame_connection.send(frame)
    vid.release()


def display_video(frame_connection, stream_connection):
    
    while True:
        stream_connection.send(True)
        frame = frame_connection.recv()
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):  # press 'q' button to quit
            stream_connection.send(False)
            break
    cv2.destroyAllWindows()


if __name__ == "__main__":
    
    video_frame_left, video_frame_right = Pipe()
    should_stream_left, should_stream_right = Pipe()
    p1 = Process(target=stream_video, args=(video_frame_left, should_stream_right))
    p2 = Process(target=display_video, args=(video_frame_right, should_stream_left))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
