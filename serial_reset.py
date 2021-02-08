#!/usr/bin/python 
import serial
import time
import sys

if __name__ == '__main__':

    argv = sys.argv
    if len(argv) != 2:
        print("usage:\n python {} DEVICE".format(argv[0]))
        sys.exit()
   
    device = argv[1]

    ser = serial.Serial(device,115200,timeout=None)

    ser.dtr=False
    time.sleep(1)

    ser.close()
