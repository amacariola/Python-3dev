##################################################
#  FLASK APP FOR LIVE VIDEO STREAM VIA BROWSER   #
#  				                 #
#      note: for cctv camera use rstp            #
#  rstp://username:password@ip_address:544/user= #
#  username_password='password'_channel=channel_ #
#  number_stream=0.sdp'                          #
##################################################
 
from flask import Flask, render_template, Response
import cv2

app = Flask(__name__)

camera = cv2.VideoCapture(0) # Webcam live feed

def video_capture():
    while True:
       feed, frame = camera.read()
       if not feed:
          break
       else:
          ret, buffer = cv2.imencode('.jpg', frame)
          frame = buffer.tobytes()
          yield(b'--frame\r\n'
                b'Content-type: image/jpg\r\n\r\n' + frame + b'\r\n')


@app.route('/video-feed')

def video_feed():
    return Response(video_capture(), mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route('/')
def index():
    """Flask Video Streaming Home"""
    return  render_template('index.html')

if __name__ == '__main__':
   app.run(debug=True)   
