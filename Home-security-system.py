#HOME SECURITY AND INTRUDER DETECTION MANAGEMENT 

importsmtplib, email, os
fromemail.mime.base import MIMEBase
fromemail.mime.multipart import MIMEMultipart
fromemail.mime.text import MIMEText
from email import encoders
fromtwilio.rest import Client
importpyrebase
frompicamera import PiCamera
from time import sleep
fromdatetime import datetime
importRPi.GPIO as GPIO

cyan ='\033[36m'
white = '\033[37m'
red = '\033[1;31m'

sleep(2)
os.system("clear")
def banner():

print (cyan + "			██╗  ██╗ ██████╗ ███╗   ███╗███████╗    ███████╗███████╗ ██████╗██╗   ██╗██████╗ ██╗████████╗██╗   ██╗     ")
print (cyan + "			██║  ██║██╔═══██╗████╗ ████║██╔════╝    ██╔════╝██╔════╝██╔════╝██║   ██║██╔══██╗██║╚══██╔══╝╚██╗ ██╔╝     ")
print (cyan + "			███████║██║   ██║██╔████╔██║█████╗      ███████╗█████╗  ██║     ██║   ██║██████╔╝██║   ██║    ╚████╔╝      ")
print (cyan + "			██╔══██║██║   ██║██║╚██╔╝██║██╔══╝      ╚════██║██╔══╝  ██║     ██║   ██║██╔══██╗██║   ██║     ╚██╔╝       ")
print (cyan + "			██║  ██║╚██████╔╝██║ ╚═╝ ██║███████╗    ███████║███████╗╚██████╗╚██████╔╝██║  ██║██║   ██║      ██║        ")
print (cyan + "			╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝    ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═╝      ╚═╝        ")  
print (" ")                                                                                                                                                                                                 
print (cyan + "						███████╗██╗   ██╗███████╗████████╗███████╗███╗   ███╗ ")
print (cyan + "						██╔════╝╚██╗ ██╔╝██╔════╝╚══██╔══╝██╔════╝████╗ ████║ ")
print (cyan + "						███████╗ ╚████╔╝ ███████╗   ██║   █████╗  ██╔████╔██║ ")
print (cyan + "						╚════██║  ╚██╔╝  ╚════██║   ██║   ██╔══╝  ██║╚██╔╝██║ ")
print (cyan + "						███████║   ██║   ███████║   ██║   ███████╗██║ ╚═╝ ██║ ")
print (cyan + "						╚══════╝   ╚═╝   ╚══════╝   ╚═╝   ╚══════╝╚═╝     ╚═╝ ")

banner()
sleep(3)

print(white)
#*********************************************** GPIO setup *************************************************
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)

#*********************************************** Email parameters *************************************************
subject='Security Alert: A motion has been detected'
bodyText="""\
Hi,
A motion has been detected in your room.
Please check the attachement sent from rasperry pi security system.
Regards
Crypto_grapper_
"""
SMTP_SERVER='smtp.gmail.com'
SMTP_PORT=587
USERNAME='projectcseccxxxxxxx@gmail.com'
PASSWORD='xxxxxxxxxxxx'
RECIEVER_EMAIL='harixxxxxxx@gmail.com'

#*********************************************** Video finename and path *************************************************
filename_part1="surveillance"
file_ext=".mp4"
now = datetime.now()
current_datetime = now.strftime("%d-%m-%Y_%H:%M:%S")
filename=filename_part1+"_"+current_datetime+file_ext
filepath="/home/pi/python_code/capture/"


defsend_email():
message=MIMEMultipart()
message["From"]=USERNAME
message["To"]=RECIEVER_EMAIL
message["Subject"]=subject

message.attach(MIMEText(bodyText, 'plain'))
attachment=open(filepath+filename, "rb")

mimeBase=MIMEBase('application','octet-stream')
mimeBase.set_payload((attachment).read())

 encoders.encode_base64(mimeBase)
mimeBase.add_header('Content-Disposition', "attachment; filename= " +filename)

message.attach(mimeBase)
text=message.as_string()

session=smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
session.ehlo()
session.starttls()
session.ehlo()

session.login(USERNAME, PASSWORD)
session.sendmail(USERNAME, RECIEVER_EMAIL, text)
session.quit
print("Email sent")


defcapture_video():
camera.start_preview()
 camera.start_recording('/home/pi/python_code/capture/newvideo.h264')
camera.wait_recording(5)
camera.stop_recording()
camera.stop_preview()


defremove_file():
ifos.path.exists("/home/pi/python_code/capture/newvideo.h264"):
os.remove("/home/pi/python_code/capture/newvideo.h264")
else:
print("file does not exist")

ifos.path.exists(filepath+filename):
os.remove(filepath+filename)
else:
print("file does not exist")


#*************************************************** Initiate pi Camera **************************************************************************
camera=PiCamera()

#*************************************************** Main code for method call ********************************************************************
defsms_send():
	auth_sid = "xxxxxxxxxxxxxx77959a7c5d8b3"
	auth_token = "xxxxxxxxxxxxxxxxxd684331efde"

	client = Client(auth_sid, auth_token)

	message = "Home security alert INTRUDER in YOUR home Please check mail..."

	msg = client.messages.create(from_="+17377779303", body=message, to="+919790xxxxxx")

	print(msg.body)

def firebase():
	config = {
	  "apiKey": "AIzaSyDhz0qkxxxxxxxxxj-cQG5FCskxJlRvueHI",
	 "authDomain": "home-security-b24e5.firebaseapp.com",
	 "databaseURL": "https://home-security-xxxxxx.firebaseio.com",
	 "projectId": "home-security-b24e5",
	 "storageBucket": "home-security-b24e5.appspot.com",
	 "messagingSenderId": "34673215481",
	 "appId": "1:34673215481:xxxb:97xx8bc723b689650f5f28",
	 "measurementId": "G-041LXGYP3Z"
	}

	firebase = pyrebase.initialize_app(config)
	storage = firebase.storage()

	path_on_cloud = "images/hacker1.mp4"
	path_local = "hacker.mp4"
	storage.child(path_on_cloud).put(path_local)


try:
while True:
i = GPIO.input(11)
ifi==1:
print("\n\n")
print("           Motion Detected\n\n")
sleep(3)
capture_video()
sleep(2)
res=os.system("MP4Box -add /home/pi/python_code/capture/newvideo.h264 /home/pi/python_code/capture/newvideo.mp4")
os.system("mv /home/pi/python_code/capture/newvideo.mp4 "+filepath+filename)
send_email()
sms_send()
firebase()
sleep(2)
remove_file()
exceptKeyboardInterrupt:
print("Pressed Keyboad\n\n")
