from multiprocessing import Pool, Lock, Process, Array, Queue, Pipe
import time
import pyrealsense2 as rs
import cv2 
import numpy as np
import math
from  pycreate2 import Create2
# from threading import Timer

def stop_bot(bot):
    bot.drive_stop()


def navigation(distance_pipe_right):
    port = "COM6"  
    bot = Create2(port)
    bot.start()
    bot.full()
    bot.drive_direct(40, 40)
    # r = Timer(15.0, stop_bot, (bot))
    # r.start()
    while True:
        if distance_pipe_right.recv() < 60:
            print("hooray")
            bot.drive_stop()
            break

def camera(distance_pipe_left):
    pipeline = rs.pipeline()
    pipeline.start()

    while True:
        frames = pipeline.wait_for_frames()
        depth = frames.get_depth_frame()
        if not depth: continue
        width = depth.get_width()
        height = depth.get_height()
        dist_to_center = depth.get_distance(width / 2, height / 2)*100
        distance_pipe_left.send(dist_to_center)

if __name__ == "__main__":
    distance_pipe_left, distance_pipe_right = Pipe()
    p1 = Process(target=navigation, args=(distance_pipe_right,))
    p2 = Process(target=camera, args=(distance_pipe_left,))
    p1.start()
    p2.start()
    p2.join()
    p1.join()
