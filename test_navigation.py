from  pycreate2 import Create2
import time

# setting up the port
# device manager -> COM ports -> USB serial port
port = "COM6"  

# setting up the robot using pycreate2 API
bot = Create2(port)

# start the robot
bot.start()

# setting the mode
# full / safe / passive / off
bot.full()

# navigating
bot.drive_direct(0, 100)
time.sleep(10)
bot.drive_stop()