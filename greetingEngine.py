#Import Module
import random

#Import Classes
from voiceEngine import Voice

class Greeting:
	
	def __init__(self):
		self.vcGreeting = Voice()
	
	def pagi(self):
		self.morningGreet = ['good morning mr, what\'s your plan today?',
							 'hello sir, good morning. have a nice day!',
							 'hello, morning sir. i hope the best for you today!']
		return self.vcGreeting.speaking(random.choice(self.morningGreet))
	
	def siang(self):
		self.noonGreet = ['good afternoon mr, how are you today?',
						  'afternoon sir, nice to know you!',
						  'hello sir, good afternoon. are you ok today?']
		return self.vcGreeting.speaking(random.choice(self.noonGreet))
		
	def sore(self):
		self.eveningGreet = ['hello mr, good evening!',
							 'good evening sir, may i help you?',
							 'hello, good evening master. can i help you?']
		return self.vcGreeting.speaking(random.choice(self.eveningGreet))
		
	def malam(self):
		self.nightGreet = ['good night sir! have a nice dream.',
							 'hello mr, good night and have a good sleep.',
							 'good night mr! enjoy your rest and see you tomorrow.']
		return self.vcGreeting.speaking(random.choice(self.nightGreet))
		
