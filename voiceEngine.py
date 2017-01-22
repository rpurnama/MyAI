#Import Module
import speech_recognition as sr
import pyttsx
import pyaudio
from gtts import gTTS
import os

#Create class Voice Comms
class Voice:
	
	#def __init__(self):
	#	self.data = ""
	
	#Method for convert text to speech (with PyTTSX - Offline Mode)
	def talking(self, somewords):
		self.talkEngine = pyttsx.init()
		self.talkEngine.setProperty('rate', 150)
		self.talkEngine.say(somewords)
		self.talkEngine.runAndWait()
	
	#Method for convert text to speech (with gTTS - Online Mode)
	def speaking(self, someWords):
		print(someWords)
		self.tts = gTTS(text=someWords, lang='en')
		self.tts.save("audiorec.mp3")
		os.system("mpg321 audiorec.mp3")
	
	#Method for convert speech to text (with PocketSphinx - Offline Mode)
	def hearing(self):
		self.recorder = sr.Recognizer()
		with sr.Microphone() as source:
			print("I\'m listening...")
			self.recorder.adjust_for_ambient_noise(source)
			self.audio = self.recorder.listen(source)
		
		self.data = ""
		try:
			self.data = self.recorder.recognize_sphinx(self.audio)
			#self.data = self.recorder.recognize_google(self.audio)
			print("You said: "+self.data)
		except sr.UnknownValueError:
			print("Speech Recognition Engine could not understand audio")
		except sr.RequestError as e:
			print("Speech Recognition Engine error; {0}".format(e))
			
		return self.data

	#Method for convert speech to text (with PocketSphinx - Online Mode)
	def listening(self):
		self.recorder = sr.Recognizer()
		with sr.Microphone() as source:
			print("I\'m listening...")
			self.recorder.adjust_for_ambient_noise(source)
			self.audio = self.recorder.listen(source)
		
		self.data = ""
		try:
			#self.data = self.recorder.recognize_sphinx(self.audio)
			self.data = self.recorder.recognize_google(self.audio)
			print("You said: "+self.data)
		except sr.UnknownValueError:
			print("Speech Recognition Engine could not understand audio")
		except sr.RequestError as e:
			print("Speech Recognition Engine error; {0}".format(e))
			
		return self.data
