import cv2 

vcap = cv2.VideoCapture('Video (1).mp4') # 0=camera
 
if vcap.isOpened(): 
    # get property 
    width  = vcap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float `width`
    height = vcap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float `height`
    # or
    # width  = vcap.get(3)  # float `width`
    # height = vcap.get(4)  # float `height`

    print(width, height)
    
    # fps = vcap.get(cv2.CAP_PROP_FPS)