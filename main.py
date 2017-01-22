#Import Module
import getpass
import time

#Import Class
from voiceEngine import Voice

#My LUNA
#def luna(in_data):
#	if "how are you" in in_data:

#Banner Motd
welcome = """
\t888       888          888                                         
\t888   o   888          888                                         
\t888  d8b  888          888                                         
\t888 d888b 888  .d88b.  888  .d8888b .d88b.  88888b.d88b.   .d88b.  
\t888d88888b888 d8P  Y8b 888 d88P"   d88""88b 888 "888 "88b d8P  Y8b 
\t88888P Y88888 88888888 888 888     888  888 888  888  888 88888888 
\t8888P   Y8888 Y8b.     888 Y88b.   Y88..88P 888  888  888 Y8b.     
\t888P     Y888  "Y8888  888  "Y8888P "Y88P"  888  888  888  "Y8888  
"""
banner = """
Project Name\t: Luna
Written By\t: MacGyver
Version\t\t: 0.0 (Alpha, 01/21/2017)

This application system is a basic AI for smart-home assistant. It's deployed as 
our personal usage. Access to this system is monitored by administrator, 
unauthorised access is prohibitted. Disconnect IMMEDIATELY if you're not 
authorised personel, OR you'll be reported to local law! 

Developed under GNU/Linux license by Open Source Center. Please visit us at
http://rpoernama.wordpress.com
"""
print(welcome)
print(80*"="+banner)
print(30*" "+"LEARN | CODE | SHARE"+"\n"+"="*80)

#Local Date & Time
tanggal = time.strftime('%B %d, %Y -')
pukul = time.strftime('%l:%M%p %Z')
print 24*" ",tanggal,pukul
print ""

#Login System
uid = raw_input('Username: ')
pwd = getpass.getpass('Password: ')

#Define Variable Imported from Classes
suara = Voice()
suara.speaking('Welcome '+uid+', Can I help you?')


