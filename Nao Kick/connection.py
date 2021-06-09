import os
import sys
import time
import config
 
     

####
# Create motion proxy
print "Creating motion proxy"
try:
  
  motion = config.loadProxy("ALMotion")
  config.StiffnessOn(motion)
  config.PoseInit(motion)
  
  
 

except Exception,e:
  print "Error when creating motion proxy:"
  print str(e)
  exit(1)
####
# Create proxy on ALVideoDevice

print "Creating ALVideoDevice proxy"

try:
  cam = config.loadProxy("ALVideoDevice")
  #cam.kCameraSelectID=1
except Exception,e:
  print "Error when creating vision proxy:"
  print str(e)
  exit(1)








