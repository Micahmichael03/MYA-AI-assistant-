import speech_recognition as sr
import openai
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from time import ctime
import webbrowser
import time
import random


# # Set up OpenAI API
# openai.api_key = "Key_here"
# model_id = "gpt-3.5-turbo"

# Initialize speech recognition engine
Listener = sr.Recognizer() #
engine = pyttsx3.init() # Initialize the text to speech engine

# Set the voice property to a female voice (if available)
voices = engine.getProperty('voices') # Get a list of available voices
engine.setProperty('voice', voices[1].id) # 1 is the index of the female voice

# counter just for interaction
# interaction_counter = 0 #

# def transcribe_audio_to_text(filename): #
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(filename) as source:
#         audio = recognizer.record(source)
#         try:
#             return recognizer.recognize_google(audio)
#         except:
#             print("")
#             #print('Skipping unknown error')


# def ChatGPT_conversation(conversation):  #
#     response = openai.ChatCompletion.create(
#         model=model_id,
#         messages=conversation
#     )
    
#     api_useage = response['usage']
#     print('Total tokens consumed: {0}'. format(api_useage['total_tokens']))
#     conversation.append({'role':response.choices[0].message.role, 'content': response.choices[0].message.content})
#     return conversation

# Greet the user
engine.say("Hey there, I am Mya")
engine.say("How can I help you?")
engine.runAndWait()

# # starting conversation
# conversation = []
# conversation.append({'role': 'user', 'content': 'You are a helpful assistant.'})
# conversation = ChatGPT_conversation(conversation)
# print("{0}: {1}\n".format(conversation[-1]['role'].strip(),conversation[-1]['content'].strip()))
# speak_text = (conversation[-1]['content'].strip())

# def activate_assistant():
#     starting_chat_phrases = [       "Yes sir, how may I assist you?",
#                                     "Yes, What can I do for you?",
#                                     "How can I help you, sir?",
#                                     "Friday at your service, what do you need?",
#                                     "Friday here, how can I help you today?",
#                                     "Yes, what can I do for you today?",
#                                     "Yes sir, what's on your mind?",
#                                     "Friday ready to assist, what can I do for you?",
#                                     "At your command, sir. How may I help you today?",
#                                     "Yes, sir. How may I be of assistance to you right now?",
#                                     "Yes boss, I'm here to help. What do you need from me?",
#                                     "Yes, I'm listening. What can I do for you, sir?",
#                                     "How can I assist you today, sir?",
#                                     "Friday here, ready and eager to help. What can I do for you?",
#                                     "Yes, sir. How can I make your day easier?",
#                                     "Yes boss, what's the plan? How can I assist you today?",
#                                     "Yes, I'm here and ready to assist. What's on your mind, sir?"
#                             ]
    
#     continued_chat_phrases = ["yes", "yes, sir", "yes boss", "I'm all ears"]
#     random_chat = ""
#     if(interaction_counter == 1):
#         random_chat = random.choice(starting_chat_phrases)
#     else:
#         random_chat = random.choice(continued_chat_phrases)
    
#     return random_chat

# def append_to_log(text):
#     with open("chat_log.txt", "a") as f:
#         f.write(text + "\n")


def speak(word):
    engine.setProperty("rate", 180)
    engine.setProperty("volume", 0.9)
    engine.say(str(word))
    engine.runAndWait()
    engine.stop()
    
# def speak_text(text):
#         engine.say(text)
#         engine.runAndWait()
        
# while True:

#     #wait for users to say "Friday"
#     print("Say 'Friday' to start...")
#     recognizer = sr.Recognizer()

#     with sr.Microphone() as source:
#         audio = recognizer.listen(source)
#         try:
#             transcription = recognizer.recognize_google(audio)
#             if "friday" in transcription.lower():
#                 interaction_counter += 1
#                 # Record audio
#                 filename = "input.wav"
#                 readyToWork = activate_assistant()
#                 speak_text(readyToWork)
#                 print(readyToWork)
#                 recognizer = sr.Recognizer()
#                 with sr.Microphone() as source:
#                     source.pause_threshold = 1
#                     audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
#                     with open(filename, "wb") as f:
#                         f.write(audio.get_wav_data())

#                 # Transcribe audio to text
#                 text = transcribe_audio_to_text(filename)
#                 if text:
#                     print(f"You said: {text}")
#                     append_to_log(f"You: {text}\n")

#                     # Generate response using chatGPT
#                     print(f"Friday says: {conversation}")

#                     prompt = text
#                     conversation.append({'role': 'user', 'content': prompt})
#                     conversation = ChatGPT_conversation(conversation)

#                     print('{0}: {1}\n'.format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))

#                     append_to_log(f"Mya: {conversation[-1]['content'].strip()}\n")

#                     # Read response using text-to-speech
#                     speak_text(conversation[-1]['content'].strip())

#                     # In future maybe a conversation.clear to decrease input tokens as the conversation evolves ...
                        
#         except Exception as e:
#             continue
#             #print("An error occurred: {}".format(e))
    
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            Listener.adjust_for_ambient_noise(source)  # Adjust for ambient noise
            voice = Listener.listen(source)
            print("Recognizing...")
            command = Listener.recognize_google(voice)
            command = command.lower()
            if "mya" in command:  # Check for "mya" in the recognized command
                command = command.replace("mya", "")
                print(command)
    except sr.UnknownValueError:
        pass
    except sr.RequestError:
        speak("I'm sorry, but I couldn't request results at the moment. Please try again later.")
    return command

def play_music(song):
    speak("playing " + song)
    pywhatkit.playonyt(song)

def get_current_time():
    current_time = datetime.datetime.now().strftime("%H:%M %p")
    print(current_time)
    speak("Current time is " + current_time)

def get_person_info(query):
    person = query.replace("who is", "")
    info = wikipedia.summary(person, 1)
    print(info)
    speak(info)

def tell_joke():
    joke = pyjokes.get_joke()
    speak(joke)

def greeting():
    speak("Hello, I am Mya, your personal assistant. How can I help you?")

def farewell():
    speak("Goodbye")
    exit()

def introduce():
    speak("My name is Mya. How can I help you?")

def find_location(location):
    speak("What is the location you want to find?")
    url = 'https://google.com/maps/place/' + location + '/&amp;'
    webbrowser.open(url)
    speak('Here is the location of ' + location)

def perform_search(query):
    speak("What do you want to search for?")
    search = take_command()  # Use the speech recognition to get the search query
    url = 'https://google.com/search?q=' + search
    webbrowser.open(url)
    speak('Here is what I found for ' + search)

def run_Mya():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play", "")
        play_music(song)
    elif "time" in command:
        get_current_time()
    elif "who is" in command:  # Simplify the "who is" command
        get_person_info(command)
    elif "date" in command:
        speak("Sorry, I have a headache")
    elif "are you single" in command:
        speak("I am in a relationship with Wi-Fi")
    elif "joke" in command:
        tell_joke()
    elif "hello" in command:
        greeting()
    elif "how are you" in command:
        speak("I am fine, thank you.")
    elif "goodbye" in command or "stop" in command:
        farewell()
    elif "what is your name" in command:
        introduce()
    elif "where are you" in command:
        speak("I am in your computer")
    elif "what time is it" in command or "what is the time" in command:
        speak(ctime())
    elif "search" in command:
        perform_search(command)
    elif "find location" in command:
        find_location(command)
    else:
        speak("Please say the command again")

time.sleep(1)

while 1:
    run_Mya()
