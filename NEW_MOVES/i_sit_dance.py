# Choregraphe bezier export in Python.

import sys
import time

from naoqi import ALProxy


def main(robotIP, port):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.04, 1, 2, 3, 4, 5, 6, 7, 8])
    keys.append([[0.164903, [3, -0.0133333, 0], [3, 0.32, 0]], [-0.122173, [3, -0.32, 0], [3, 0.333333, 0]], [0.164903, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.122173, [3, -0.333333, 0], [3, 0.333333, 0]], [0.164903, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.122173, [3, -0.333333, 0], [3, 0.333333, 0]], [0.164903, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.122173, [3, -0.333333, 0], [3, 0.333333, 0]], [0.164903, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([0.04, 1, 2, 3, 4, 5, 6, 7, 8])
    keys.append([[-0.0360643, [3, -0.0133333, 0], [3, 0.32, 0]], [0.598648, [3, -0.32, 0], [3, 0.333333, 0]], [-0.0360643, [3, -0.333333, 0.194022], [3, 0.333333, -0.194022]], [-0.565487, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.0360643, [3, -0.333333, -0.194022], [3, 0.333333, 0.194022]], [0.598648, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.0360643, [3, -0.333333, 0.194022], [3, 0.333333, -0.194022]], [-0.565487, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.0360643, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([0.04, 2, 4, 6, 8])
    keys.append([[0.830136, [3, -0.0133333, 0], [3, 0.653333, 0]], [0.830136, [3, -0.653333, 0], [3, 0.666667, 0]], [0.830136, [3, -0.666667, 0], [3, 0.666667, 0]], [0.830136, [3, -0.666667, 0], [3, 0.666667, 0]], [0.830136, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([0.04, 2, 4, 6, 8])
    keys.append([[-0.0100937, [3, -0.0133333, 0], [3, 0.653333, 0]], [-0.0100937, [3, -0.653333, 0], [3, 0.666667, 0]], [-0.0100937, [3, -0.666667, 0], [3, 0.666667, 0]], [-0.0100937, [3, -0.666667, 0], [3, 0.666667, 0]], [-0.0100937, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0.04, 2, 4, 6, 8])
    keys.append([[-1.28494, [3, -0.0133333, 0], [3, 0.653333, 0]], [-1.28494, [3, -0.653333, 0], [3, 0.666667, 0]], [-1.28494, [3, -0.666667, 0], [3, 0.666667, 0]], [-1.28494, [3, -0.666667, 0], [3, 0.666667, 0]], [-1.28494, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.04, 2, 4, 6, 8])
    keys.append([[-0.455231, [3, -0.0133333, 0], [3, 0.653333, 0]], [-0.455231, [3, -0.653333, 0], [3, 0.666667, 0]], [-0.455231, [3, -0.666667, 0], [3, 0.666667, 0]], [-0.455231, [3, -0.666667, 0], [3, 0.666667, 0]], [-0.455231, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0.04, 2, 4, 6, 8])
    keys.append([[0.289465, [3, -0.0133333, 0], [3, 0.653333, 0]], [0.289465, [3, -0.653333, 0], [3, 0.666667, 0]], [0.289465, [3, -0.666667, 0], [3, 0.666667, 0]], [0.289465, [3, -0.666667, 0], [3, 0.666667, 0]], [0.289465, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([0.04, 2, 4, 6, 8])
    keys.append([[-1.53008, [3, -0.0133333, 0], [3, 0.653333, 0]], [-1.53008, [3, -0.653333, 0], [3, 0.666667, 0]], [-1.53008, [3, -0.666667, 0], [3, 0.666667, 0]], [-1.53008, [3, -0.666667, 0], [3, 0.666667, 0]], [-1.53008, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([0.04, 2, 4, 6, 8])
    keys.append([[0.277429, [3, -0.0133333, 0], [3, 0.653333, 0]], [0.277429, [3, -0.653333, 0], [3, 0.666667, 0]], [0.277429, [3, -0.666667, 0], [3, 0.666667, 0]], [0.277429, [3, -0.666667, 0], [3, 0.666667, 0]], [0.277429, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([0.04, 2, 4, 6, 8])
    keys.append([[-0.625036, [3, -0.0133333, 0], [3, 0.653333, 0]], [-0.625036, [3, -0.653333, 0], [3, 0.666667, 0]], [-0.625036, [3, -0.666667, 0], [3, 0.666667, 0]], [-0.625036, [3, -0.666667, 0], [3, 0.666667, 0]], [-0.625036, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([0.04, 2, 4, 6, 8])
    keys.append([[1.39468, [3, -0.0133333, 0], [3, 0.653333, 0]], [1.39468, [3, -0.653333, 0], [3, 0.666667, 0]], [1.39468, [3, -0.666667, 0], [3, 0.666667, 0]], [1.39468, [3, -0.666667, 0], [3, 0.666667, 0]], [1.39468, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.04, 1, 2, 3, 4, 5, 6, 7, 8])
    keys.append([[0.906264, [3, -0.0133333, 0], [3, 0.32, 0]], [0.876155, [3, -0.32, 0], [3, 0.333333, 0]], [0.906264, [3, -0.333333, 0], [3, 0.333333, 0]], [0.876155, [3, -0.333333, 0], [3, 0.333333, 0]], [0.906264, [3, -0.333333, 0], [3, 0.333333, 0]], [0.876155, [3, -0.333333, 0], [3, 0.333333, 0]], [0.906264, [3, -0.333333, 0], [3, 0.333333, 0]], [0.876155, [3, -0.333333, 0], [3, 0.333333, 0]], [0.906264, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.04, 1, 2, 3, 4, 5, 6, 7, 8])
    keys.append([[0.0291358, [3, -0.0133333, 0], [3, 0.32, 0]], [1.12574, [3, -0.32, 0], [3, 0.333333, 0]], [0.0291358, [3, -0.333333, 0], [3, 0.333333, 0]], [1.12574, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0291358, [3, -0.333333, 0], [3, 0.333333, 0]], [1.12574, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0291358, [3, -0.333333, 0], [3, 0.333333, 0]], [1.12574, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0291358, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0.04, 2, 4, 6, 8])
    keys.append([[0.0337945, [3, -0.0133333, 0], [3, 0.653333, 0]], [0.0337945, [3, -0.653333, 0], [3, 0.666667, 0]], [0.0337945, [3, -0.666667, 0], [3, 0.666667, 0]], [0.0337945, [3, -0.666667, 0], [3, 0.666667, 0]], [0.0337945, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([0.04, 1, 2, 3, 4, 5, 6, 7, 8])
    keys.append([[0.464258, [3, -0.0133333, 0], [3, 0.32, 0]], [0.853466, [3, -0.32, 0], [3, 0.333333, 0]], [0.464258, [3, -0.333333, 0], [3, 0.333333, 0]], [0.853466, [3, -0.333333, 0], [3, 0.333333, 0]], [0.464258, [3, -0.333333, 0], [3, 0.333333, 0]], [0.853466, [3, -0.333333, 0], [3, 0.333333, 0]], [0.464258, [3, -0.333333, 0], [3, 0.333333, 0]], [0.853466, [3, -0.333333, 0], [3, 0.333333, 0]], [0.464258, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([0.04, 2, 4, 6, 8])
    keys.append([[0.0234019, [3, -0.0133333, 0], [3, 0.653333, 0]], [0.0234019, [3, -0.653333, 0], [3, 0.666667, 0]], [0.0234019, [3, -0.666667, 0], [3, 0.666667, 0]], [0.0234019, [3, -0.666667, 0], [3, 0.666667, 0]], [0.0234019, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.04, 2, 4, 6, 8])
    keys.append([[1.5356, [3, -0.0133333, 0], [3, 0.653333, 0]], [1.5356, [3, -0.653333, 0], [3, 0.666667, 0]], [1.5356, [3, -0.666667, 0], [3, 0.666667, 0]], [1.5356, [3, -0.666667, 0], [3, 0.666667, 0]], [1.5356, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.04, 2, 4, 6, 8])
    keys.append([[0.587258, [3, -0.0133333, 0], [3, 0.653333, 0]], [0.587258, [3, -0.653333, 0], [3, 0.666667, 0]], [0.587258, [3, -0.666667, 0], [3, 0.666667, 0]], [0.587258, [3, -0.666667, 0], [3, 0.666667, 0]], [0.587258, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.04, 2, 4, 6, 8])
    keys.append([[0.293898, [3, -0.0133333, 0], [3, 0.653333, 0]], [0.293898, [3, -0.653333, 0], [3, 0.666667, 0]], [0.293898, [3, -0.666667, 0], [3, 0.666667, 0]], [0.293898, [3, -0.666667, 0], [3, 0.666667, 0]], [0.293898, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([0.04, 2, 4, 6, 8])
    keys.append([[-1.52861, [3, -0.0133333, 0], [3, 0.653333, 0]], [-1.52861, [3, -0.653333, 0], [3, 0.666667, 0]], [-1.52861, [3, -0.666667, 0], [3, 0.666667, 0]], [-1.52861, [3, -0.666667, 0], [3, 0.666667, 0]], [-1.52861, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([0.04, 2, 4, 6, 8])
    keys.append([[-0.268145, [3, -0.0133333, 0], [3, 0.653333, 0]], [-0.268145, [3, -0.653333, 0], [3, 0.666667, 0]], [-0.268145, [3, -0.666667, 0], [3, 0.666667, 0]], [-0.268145, [3, -0.666667, 0], [3, 0.666667, 0]], [-0.268145, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([0.04, 1, 2, 3, 4, 5, 6, 7, 8])
    keys.append([[-0.625036, [3, -0.0133333, 0], [3, 0.32, 0]], [-0.617847, [3, -0.32, 0], [3, 0.333333, 0]], [-0.625036, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.617847, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.625036, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.617847, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.625036, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.617847, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.625036, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([0.04, 2, 4, 6, 8])
    keys.append([[1.40409, [3, -0.0133333, 0], [3, 0.653333, 0]], [1.40409, [3, -0.653333, 0], [3, 0.666667, 0]], [1.40409, [3, -0.666667, 0], [3, 0.666667, 0]], [1.40409, [3, -0.666667, 0], [3, 0.666667, 0]], [1.40409, [3, -0.666667, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.04, 1, 2, 3, 4, 5, 6, 7, 8])
    keys.append([[0.699182, [3, -0.0133333, 0], [3, 0.32, 0]], [0.876155, [3, -0.32, 0], [3, 0.333333, 0]], [0.699182, [3, -0.333333, 0], [3, 0.333333, 0]], [0.876155, [3, -0.333333, 0], [3, 0.333333, 0]], [0.699182, [3, -0.333333, 0], [3, 0.333333, 0]], [0.876155, [3, -0.333333, 0], [3, 0.333333, 0]], [0.699182, [3, -0.333333, 0], [3, 0.333333, 0]], [0.876155, [3, -0.333333, 0], [3, 0.333333, 0]], [0.699182, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.04, 1, 2, 3, 4, 5, 6, 7, 8])
    keys.append([[0.236517, [3, -0.0133333, 0], [3, 0.32, 0]], [-1.12574, [3, -0.32, 0], [3, 0.333333, 0]], [0.236517, [3, -0.333333, 0], [3, 0.333333, 0]], [-1.12574, [3, -0.333333, 0], [3, 0.333333, 0]], [0.236517, [3, -0.333333, 0], [3, 0.333333, 0]], [-1.12574, [3, -0.333333, 0], [3, 0.333333, 0]], [0.236517, [3, -0.333333, 0], [3, 0.333333, 0]], [-1.12574, [3, -0.333333, 0], [3, 0.333333, 0]], [0.236517, [3, -0.333333, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.04, 2, 4, 6, 8])
    keys.append([[-0.029779, [3, -0.0133333, 0], [3, 0.653333, 0]], [-0.029779, [3, -0.653333, 0], [3, 0.666667, 0]], [-0.029779, [3, -0.666667, 0], [3, 0.666667, 0]], [-0.029779, [3, -0.666667, 0], [3, 0.666667, 0]], [-0.029779, [3, -0.666667, 0], [3, 0, 0]]])

    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        motion = ALProxy("ALMotion", robotIP, port)
        #  motion = ALProxy("ALMotion")
        motion.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
        print err


if __name__ == "__main__":
    robotIP = "127.0.0.1"
    port = 9559

    if len(sys.argv) <= 1:
        print "(robotIP default: 127.0.0.1)"
    elif len(sys.argv) <= 2:
        robotIP = sys.argv[1]
    else:
        port = int(sys.argv[2])
        robotIP = sys.argv[1]

    start = time.time()
    main(robotIP, port)
    end = time.time()
    duration = end - start
    print ("%.2f seconds elapsed" % duration)
