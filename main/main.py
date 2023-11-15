import pickle
import cv2
import mediapipe as mp
import numpy as np
import time
import os
from os.path import abspath
from inspect import getsourcefile
import sign_manager as manager
import ctypes

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)


'''
from pywinauto.findwindows    import find_window
from pywinauto.win32functions import SetForegroundWindow
SetForegroundWindow(find_window(title='taskeng.exe'))
'''

audios_path =  os.path.dirname(abspath(getsourcefile(lambda:0)) )
with open(audios_path+"\sounds.py") as f:
    exec(f.read())

model_dict = pickle.load(open(r'model.p', 'rb'))
model = model_dict['model']
cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3, max_num_hands=1)

alphabet = {
    0: 'A',
    1: 'B',
    2: 'C',
    3: 'D',
    4: 'E',
    5: 'F',
    6: 'G',
    7: 'H',
    8: 'I',
    9: 'K',
    10: 'L',
    11: 'M',
    12: 'N',
    13: 'O',
    14: 'P',
    15: 'Q',
    16: 'R',
    17: 'S',
    18: 'T',
    19: 'U',
    20: 'V',
    21: 'W',
    22: 'X',
    23: 'Y'
}

global predicted_character,previous_predicted_character
previous_predicted_character=None
predicted_character = None
global action_state  
action_state = True

while True:
    #print("tick")
    #time.sleep(6.0 - ((time.time() - starttime) % 6.0))
    normalization = []
    x_ = []
    y_ = []
    ret, frame = cap.read()
    H, W, C = frame.shape
    

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = hands.process(frame_rgb)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame,  # image to draw
                hand_landmarks,  # model output
                mp_hands.HAND_CONNECTIONS,  # hand connections
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())

        for hand_landmarks in results.multi_hand_landmarks:
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                x_.append(x)
                y_.append(y)
                
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                normalization.append(x - min(x_))
                normalization.append(y - min(y_))

        x1 = int(min(x_) * W) - 10
        y1 = int(min(y_) * H) - 10
        x2 = int(max(x_) * W) - 10
        y2 = int(max(y_) * H) - 10

        normalization = normalization[:42]
        prediction = model.predict([np.asarray(normalization)])
        #print(max(model.predict_proba([np.asarray(normalization)])[0]))
        confidence_threshold = 0.8
        
        predicted_character = alphabet[int(prediction[0])]

        
        if previous_predicted_character!=predicted_character:
            starttime = time.time()
            #print('you changed character from {} to {}'.format(previous_predicted_character,predicted_character))
            previous_predicted_character = predicted_character   
        else:
            if time.time()-starttime<1.5:
                #print(time.time()-starttime)
                #print('hold character')
                pass
            else:
                
                if predicted_character == 'I':
                    action_state = True
                if action_state==True:
                    manager.sign_manager(predicted_character)
                    starttime = time.time()
                if predicted_character == 'B':
                    action_state = False
                if predicted_character == 'Y':
                    quit()
                starttime = time.time()

        #it returns string of the label inside a list example ["0"]
        #print(prediction)

        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 0), 4)
        cv2.putText(frame, predicted_character, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 0, 0), 3,
                    cv2.LINE_AA)
        
    
    

    cv2.namedWindow("sign assistant",cv2.WINDOW_NORMAL)
    cv2.resizeWindow("sign assistant", 280,200)
    cv2.moveWindow('sign assistant',screensize[0]-280,screensize[1]-300)
    cv2.setWindowProperty('sign assistant', cv2.WND_PROP_TOPMOST, 1)
    cv2.imshow("sign assistant", frame)

    cv2.waitKey(1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
