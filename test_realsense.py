import pyrealsense2 as rs
import time

pipeline = rs.pipeline()
pipeline.start()

while True:
    frames = pipeline.wait_for_frames()
    depth = frames.get_depth_frame()
    if not depth: continue

    width = depth.get_width()
    height = depth.get_height()

    dist_to_center = depth.get_distance(width / 2, height / 2)*100

    print(dist_to_center)
    time.sleep(1)
