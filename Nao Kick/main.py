import config
import connection
from connection import *
import vision_getandsaveimage as vg
import find_ball as fb
import kick
import time
import take_position as tp

vg.showNaoImage(config.IP,config.PORT,0)
tp.take_position()

names = list()
times = list()
keys = list()

names.append("HeadYaw")
times.append([ 2.40000])
keys.append([ -0.00158])

names.append("HeadPitch")
times.append([ 2.40000])
keys.append([ 0.51487])

motion.angleInterpolation(names, keys, times, True);

vg.showNaoImage(config.IP,config.PORT,1)

adjust = fb.findball()

print adjust[0]
print adjust[1]


if (adjust[1]==1):
        kick.adjust_front()
        print "Moving Front to adjust"
 
if (adjust[0]==5):
        kick.adjust_right()
        kick.kick_right()      
elif (adjust[0]==4):
        kick.adjust_left()
        kick.kick_left()      
elif (adjust[0]==3):
	kick.kick_right()
elif (adjust[0]==2):
	kick.kick_left()
elif (adjust[0]==1):
	kick.adjust_left()
	kick.kick_right()
elif (adjust[0]==0):
	kick.adjust_right()
	kick.kick_left()

time.sleep(5)
#motion = config.loadProxy("ALMotion")
config.PoseInit(motion)
	
	

		
		











