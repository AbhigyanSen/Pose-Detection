import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture('Video (3).mp4')

VidWidth  = cap.get(cv2.CAP_PROP_FRAME_WIDTH)   # float `width`
VidHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)  # float `height`

# Fitting the Video in the Screen
if int(VidWidth) > 2000:
    ResWidth = int(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))/4)
    ResHeight = int(int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))/4)
else:
    ResWidth = VidWidth
    ResHeight = VidHeight

PrevTime = 0

mpPose = mp.solutions.pose
mpDraw = mp.solutions.drawing_utils
pose = mpPose.Pose()

while True:
    success, OrgImage = cap.read()
    ResImage = cv2.resize(OrgImage, (ResWidth, ResHeight))
    ImgRGB = cv2.cvtColor(ResImage, cv2.COLOR_BGR2RGB)
    
    # FPS
    CurrTime = time.time()
    FPS = 1/(CurrTime - PrevTime)
    PrevTime = CurrTime
    cv2.putText(ResImage, str(int(FPS)), (70, 50), cv2.FONT_HERSHEY_DUPLEX, 1, (128, 128, 128), 2, cv2.LINE_AA)
    
    Results = pose.process(ImgRGB)
    # print(Results.pose_landmarks)
    if Results.pose_landmarks:
        mpDraw.draw_landmarks(ResImage, Results.pose_landmarks, mpPose.POSE_CONNECTIONS, 
                              mpDraw.DrawingSpec(color=(8,255,8), thickness=2, circle_radius=2),    # Circle
                              mpDraw.DrawingSpec(color=(8, 255,8), thickness=2))                    # Connecting Line
        for LandmardID, Landmarks in enumerate(Results.pose_landmarks.landmark):
            Height, Width, Channel = ResImage.shape
            # print(LandmardID, Landmarks)
            xCenter, yCenter = int(Landmarks.x * Width), int(Landmarks.y * Height)
            # cv2.circle(ResImage, (xCenter, yCenter), 2, (8, 255, 8), cv2.FILLED)        
            
    cv2.imshow("Image", ResImage)
    
    cv2.waitKey(1)
