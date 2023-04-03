import os
import sys
import time

jobId = input("Enter jobsId: ")
lower = input("Enter lower bound of jobs range: ")
upper = input("Enter upper bound of jobs range: ")

for i in range(lower,upper+1):
  os.system("condor_release "+str(jobId)+"."+str(i))
  #time.sleep(1)
