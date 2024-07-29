#!/usr/bin/env python3
# https://gist.github.com/Erol444/4aff71f4576637624d56dce4a60ad62e

import depthai as dai
import numpy as np
import sys
from pathlib import Path
import math
import cv2

def get_camera_intrinsics(device):
    calibFile = str((Path(__file__).parent / Path(f"calib_{device.getMxId()}.json")).resolve().absolute())
    if len(sys.argv) > 1:
        calibFile = sys.argv[1]

    calibData = device.readCalibration()
    calibData.eepromToJsonFile(calibFile)

    M_rgb, width, height = calibData.getDefaultIntrinsics(dai.CameraBoardSocket.CAM_A)
    print("\nRGB Camera Default intrinsics...")
    print(f"M_rgb: {M_rgb}")
    print(f"width: {width}")
    print(f"height: {height}")
    return M_rgb, width, height

def get_camera_intrinsics_scaled(device, scale_to_width=1280, scale_to_height=720):
    calibFile = str((Path(__file__).parent / Path(f"calib_{device.getMxId()}.json")).resolve().absolute())
    if len(sys.argv) > 1:
        calibFile = sys.argv[1]

    calibData = device.readCalibration()
    calibData.eepromToJsonFile(calibFile)

    M_rgb, width, height = calibData.getDefaultIntrinsics(dai.CameraBoardSocket.CAM_A)
    print("\nRGB Camera intrinsics Unscaled:")
    print(f"M_rgb_unscaled: {M_rgb}")
    print(f"width_unscaled: {width}")
    print(f"height_unscaled: {height}")

    if "OAK-1" in calibData.getEepromData().boardName or "BW1093OAK" in calibData.getEepromData().boardName:
        print(f"\nOAK-1 camera with {scale_to_width}x{scale_to_height}")
        M_rgb = np.array(calibData.getCameraIntrinsics(dai.CameraBoardSocket.CAM_A, scale_to_width, scale_to_height))
        print(f"RGB Camera intrinsics scaled to {scale_to_width}x{scale_to_height}:")
        print(f"M_rgb: {M_rgb}")

        D_rgb = np.array(calibData.getDistortionCoefficients(dai.CameraBoardSocket.CAM_A))
        print("RGB Distortion Coefficients:")
        [print(name + ": " + value) for (name, value) in
         zip(["k1", "k2", "p1", "p2", "k3", "k4", "k5", "k6", "s1", "s2", "s3", "s4", "τx", "τy"],
             [str(data) for data in D_rgb])]

        print(f'RGB FOV {calibData.getFov(dai.CameraBoardSocket.CAM_A)}')
        return M_rgb, D_rgb, width, height

    # else:
    #     M_rgb, width, height = calibData.getDefaultIntrinsics(dai.CameraBoardSocket.CAM_A)
    #     print("RGB Camera Default intrinsics...")
    #     print(M_rgb)
    #     print(width)
    #     print(height)
    #
    #     M_rgb = np.array(calibData.getCameraIntrinsics(dai.CameraBoardSocket.CAM_A, 3840, 2160))
    #     print("RGB Camera resized intrinsics... 3840 x 2160 ")
    #     print(M_rgb)
    #
    #
    #     M_rgb = np.array(calibData.getCameraIntrinsics(dai.CameraBoardSocket.CAM_A, 4056, 3040 ))
    #     print("RGB Camera resized intrinsics... 4056 x 3040 ")
    #     print(M_rgb)
    #
    #
    #     M_left, width, height = calibData.getDefaultIntrinsics(dai.CameraBoardSocket.CAM_B)
    #     print("LEFT Camera Default intrinsics...")
    #     print(M_left)
    #     print(width)
    #     print(height)
    #
    #     M_left = np.array(calibData.getCameraIntrinsics(dai.CameraBoardSocket.CAM_B, 1280, 720))
    #     print("LEFT Camera resized intrinsics...  1280 x 720")
    #     print(M_left)
    #
    #
    #     M_right = np.array(calibData.getCameraIntrinsics(dai.CameraBoardSocket.CAM_C, 1280, 720))
    #     print("RIGHT Camera resized intrinsics... 1280 x 720")
    #     print(M_right)
    #
    #     D_left = np.array(calibData.getDistortionCoefficients(dai.CameraBoardSocket.CAM_B))
    #     print("LEFT Distortion Coefficients...")
    #     [print(name+": "+value) for (name, value) in zip(["k1","k2","p1","p2","k3","k4","k5","k6","s1","s2","s3","s4","τx","τy"],[str(data) for data in D_left])]
    #
    #     D_right = np.array(calibData.getDistortionCoefficients(dai.CameraBoardSocket.CAM_C))
    #     print("RIGHT Distortion Coefficients...")
    #     [print(name+": "+value) for (name, value) in zip(["k1","k2","p1","p2","k3","k4","k5","k6","s1","s2","s3","s4","τx","τy"],[str(data) for data in D_right])]
    #
    #     print(f"RGB FOV {calibData.getFov(dai.CameraBoardSocket.CAM_A)}, Mono FOV {calibData.getFov(dai.CameraBoardSocket.CAM_B)}")
    #
    #     R1 = np.array(calibData.getStereoLeftRectificationRotation())
    #     R2 = np.array(calibData.getStereoRightRectificationRotation())
    #     M_right = np.array(calibData.getCameraIntrinsics(calibData.getStereoRightCameraId(), 1280, 720))
    #
    #     H_left = np.matmul(np.matmul(M_right, R1), np.linalg.inv(M_left))
    #     print("LEFT Camera stereo rectification matrix...")
    #     print(H_left)
    #
    #     H_right = np.matmul(np.matmul(M_right, R1), np.linalg.inv(M_right))
    #     print("RIGHT Camera stereo rectification matrix...")
    #     print(H_right)
    #
    #     lr_extrinsics = np.array(calibData.getCameraExtrinsics(dai.CameraBoardSocket.CAM_B, dai.CameraBoardSocket.CAM_C))
    #     print("Transformation matrix of where left Camera is W.R.T right Camera's optical center")
    #     print(lr_extrinsics)
    #
    #     l_rgb_extrinsics = np.array(calibData.getCameraExtrinsics(dai.CameraBoardSocket.CAM_B, dai.CameraBoardSocket.CAM_A))
    #     print("Transformation matrix of where left Camera is W.R.T RGB Camera's optical center")
    #     print(l_rgb_extrinsics)

np.set_printoptions(suppress=True)

#resize intrinsics on host doesn't seem to work well for RGB 12MP
def resizeIntrinsicsFW(intrinsics, width, height, destWidth, destHeight, keepAspect=True):
    scaleH = destHeight / height
    scaleW = destWidth / width
    if keepAspect:
        scaleW = max(scaleW, scaleH)
        scaleH = scaleW

    scaleMat = np.array([[scaleW, 0, 0], [0, scaleH, 0], [0, 0, 1]])
    scaledIntrinscs = scaleMat @ intrinsics

    if keepAspect:
        if (scaleW * height > destHeight):
            scaledIntrinscs[1][2] -=(height * scaleW - destHeight) / 2.0
        elif (scaleW * width > destWidth):
            scaledIntrinscs[0][2] -= (width * scaleW - destWidth) / 2.0

    return scaledIntrinscs

def getHFov(intrinsics, width):
    fx = intrinsics[0][0]
    fov = 2 * 180 / (math.pi) * math.atan(width * 0.5 / fx)
    return fov

def getVFov(intrinsics, height):
    fy = intrinsics[1][1]
    fov = 2 * 180 / (math.pi) * math.atan(height * 0.5 / fy)
    return fov

def getDFov(intrinsics, w, h):
    fx = intrinsics[0][0]
    fy = intrinsics[1][1]
    return np.degrees(2*np.arctan(np.sqrt(w*w+h*h)/(((fx + fy) ))))

# EXAMPLE USAGE
# with dai.Device() as device:
#     calibData = device.readCalibration()
#     cameras = device.getConnectedCameras()
#     alpha = 1
#
#     get_camera_intrinsics(device)
#     get_camera_intrinsics_scaled(device, scale_to_width=1024, scale_to_height=768)
#
#     for cam in cameras:
#         M, width, height = calibData.getDefaultIntrinsics(cam)
#         M = np.array(M)
#         d = np.array(calibData.getDistortionCoefficients(cam))
#
#         hFov = getHFov(M, width)
#         vFov = getHFov(M, height)
#         dFov = getDFov(M, width, height)
#
#         print("\nFOV measurement from calib (e.g. after undistortion):")
#         print(f"{cam}, {width}x{height}")
#         print(f"Horizontal FOV: {hFov}")
#         print(f"Vertical FOV: {vFov}")
#         print(f"Diagonal FOV: {dFov}")
#         #####
#         M, _ = cv2.getOptimalNewCameraMatrix(M, d, (width, height), alpha)
#         hFov = getHFov(M, width)
#         vFov = getHFov(M, height)
#         dFov = getDFov(M, width, height)
#
#         print()
#         print(f"\nFOV measurement with optimal camera matrix and alpha={alpha} (e.g. full sensor FOV, without undistortion):")
#         print(f"{cam}")
#         print(f"Horizontal FOV: {hFov}")
#         print(f"Vertical FOV: {vFov}")
#         print(f"Diagonal FOV: {dFov}")
#
#         hFOV_scaled = getHFov(M, 720)
#         print(f"hFOV_scaled: {hFOV_scaled}")
#         vFOV_scaled = getVFov(M, 720)
#         print(f"vFOV_scaled: {vFOV_scaled}")