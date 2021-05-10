import cv2
import face_recognition as fr

def biometricLogin():
    webCamStream = cv2.VideoCapture(0)

    usr2Face = fr.load_image_file('images/testsample2.jpg')
    usr2FaceEncodings = fr.face_encodings(usr2Face)[0]
    usr1Face = fr.load_image_file('images/testsample1.jpg')
    usr1FaceEncodings = fr.face_encodings(usr1Face)[0]
    usr3Face = fr.load_image_file('images/testsample3.jpg')
    usr3FaceEncodings = fr.face_encodings(usr3Face)[0]

    knownFaceEncodings = [usr2FaceEncodings, usr1FaceEncodings, usr3FaceEncodings]
    knownUsrs = ["Cyberkid", "TaylorSwift", "Smirutha"]

    allFaceLocations = []
    allFaceEncodings = []
    allFaceNames = []

    usrName = 'Unknown face'

    while True:
        ret,currentFrame = webCamStream.read()
        currentFrameSmall = cv2.resize(currentFrame,(0,0),fx=0.25,fy=0.25)
        allFaceLocations = fr.face_locations(currentFrameSmall,number_of_times_to_upsample=1,model='hog')
        allFaceEncodings = fr.face_encodings(currentFrameSmall,allFaceLocations)

        for currentFaceLocation,currentFaceEncoding in zip(allFaceLocations,allFaceEncodings):

            top_pos,right_pos,bottom_pos,left_pos = currentFaceLocation

            top_pos = top_pos*4
            right_pos = right_pos*4
            bottom_pos = bottom_pos*4
            left_pos = left_pos*4

            allMatches = fr.compare_faces(knownFaceEncodings, currentFaceEncoding)

            if True in allMatches:
                firstMatchIndex = allMatches.index(True)
                usrName = knownUsrs[firstMatchIndex]
                print("Authorized user: "+str(usrName))
            else:
                print("Unauthorized access: ALERT !")

            cv2.rectangle(currentFrame,(left_pos,top_pos),(right_pos,bottom_pos),(255,0,0),2)

            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(currentFrame, usrName, (left_pos,bottom_pos), font, 0.5, (255,255,255),1)

        cv2.imshow("Webcam Video",currentFrame)

        # if usrName in knownUsrs:
        #     print("Authorized user: "+str(usrName))
        # else:
        #     print("Unauthorized access: ALERT !")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    webCamStream.release()
    cv2.destroyAllWindows()

    # return usrName
    print(str(usrName)+" has logged in.")
biometricLogin()





















