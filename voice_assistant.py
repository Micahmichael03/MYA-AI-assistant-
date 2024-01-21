# import openai
# import pyttsx3
# import speech_recognition as sr
# import random

# # Set up OpenAI API
# openai.api_key = "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"
# model_id = "gpt-3.5-turbo"

# # Intialize the text to speech engine
# engine = pyttsx3.init()

# # change speech rate
# engine.setProperty("rate", 180)

# #get the avaiable voice
# voices = engine.getProperty('voices')

# # choose a voice based on the voice id
# engine.setProperty('voice', voices[1].id)

# # counter just for interaction
# interaction_counter = 0


# def transcribe_audio_to_text(filename):
#     recognizer = sr.Recognizer()
#     with sr.AudioFile(filename) as source:
#         audio = recognizer.record(source)
#         try:
#             return recognizer.recognize_google(audio)
#         except:
#             print("")
#             #print("Sorry could not recognize what you said")
            

# def ChatGPT_conversation(conversation):
#     response = openai.ChatCompletion.create(
#         model=model_id,
#         messages=conversation
#     )
    
#     api_useage = response['usage']
#     print('Total tokens consumed: {0}'. format(api_useage['total_tokens']))
#     conversation.append({'role':response.choices[0].message.role, 'content': response.choices[0].message.content})
#     return conversation


# def speak_text(text):
#     engine.say(text)
#     engine.runAndWait()
    
    
# # starting conversation
# conversation = []
# conversation.append({'role': 'user', 'content': 'Please, Act like Friday AI from Iron Man, make a 1 sentence phrase introducing yourself without saying something that sounds like this chat its already'})
# conversation = ChatGPT_conversation(conversation)
# print("{0}: {1}\n".format(conversation[-1]['role'].strip(),conversation[-1]['content'].strip()))
# speak_text = (conversation[-1]['content'].strip())


# def activate_assistant():
#     starting_chat_phrases = ["Yes sir, how may i assist you?",
#                              "Hey there, I am Mya", 
#                              "How can I help you?", 
#                              "What can I do for you?"
#                              "yes, I am here",
#                              "yes, what can I do for you?",
#                              "How can I help you?",
#                              "Mya here, How can I help you today?",
#                              "yes sir, what's on your mind?",
#                              "Mya ready to assist you",
#                              "At your service",
#                              "At your Command, Sir. How may i help you today?",
#                              "Yes, sir. How may i be of assistance to you right now?",
#                              "Yes boss. I'm here to help. what do you need from me?",
#                              "Yes, I'm listening. what can i do for you, sir?",
#                              "How can i assist you today, sir?",
#                              "Yes, sir. How can i make your day better?",
#                              "Yes boss, what's the plan?",
#                              "Yes, What's on your mind, sir?",
#                              ]
    
#     continued_chat_phrases = ["yes", "yes, sir", "yes boss", "I'm all ears"]
#     random_chat = ""
#     if(interaction_counter == 1):
#         random_chat = random.choice(starting_chat_phrases)
#     else:
#         random_chat = random.choice(continued_chat_phrases)
    
#     return random_chat


# # this is to append the user input and the ai assisent response to a text file chatlog.txt
# def append_to_log(text):
#     with open("chat_log.txt", "a") as f:
#         f.write(text + "\n")
        
# while True:

#     #wait for user to say "Mya"
#     print("Say 'Friday' to start...")
#     recognizer = sr.Recognizer()

#     with sr.Microphone() as source:
#         audio = recognizer.listen(source)
#         try:
#             transcription = recognizer.recognize_google(audio)
#             if "Mya" in transcription.lower():
#                 interaction_counter += 1
                
#                 # record audio
#                 filename = 'input.wav'
                
#                 readyToWork = activate_assistant()
#                 speak_text(readyToWork)
#                 print(readyToWork)
#                 recognizer = sr.Recognizer()
#                 with sr.Microphone() as source:
#                     source.pause_threshold = 1
#                     audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
#                     with open(filename, "wb") as f:
#                         f.write(audio.get_wav_data())
                        
#                         # transcribe audio to text
#                 text = transcribe_audio_to_text(filename)
                
#                 if text:
#                     print(f'You said: {text}')
#                     append_to_log(f"You: {text}\n")
                    
#                     # generate response using ChatGPT
#                     print(f"Friday says: {conversation}")
                    
#                     prompt = text
                    
#                     conversation.append({'role': 'User', 'content': prompt})
#                     conversation = ChatGPT_conversation(conversation)
                    
#                     print("{0}: {1}\n".format(conversation[-1]['role'].strip(), conversation[-1]['content'].strip()))   
                    
#                     append_to_log(f"Mya: {conversation[-1]['content'].strip()}\n")
                    
#                     # READ respose using text-to-speech
#                     speak_text(conversation[-1]['content'].strip())
#         except Exception as e:
#             continue
#             #print("An error occurred: {}".format(e)) 
                 