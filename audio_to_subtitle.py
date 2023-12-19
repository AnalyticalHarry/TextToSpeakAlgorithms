import speech_recognition as sr

def record():
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        print("Listening for voice input...")
    
        try:
            audio = recognizer.listen(source, timeout=10)
            print("Audio input received. Recognizing...")
    
            # Recognize the speech
            text = recognizer.recognize_google(audio)
            print("Recognized Text: " + text)
    
        except sr.WaitTimeoutError:
            print("No speech input detected. Exiting.")

record()
print(text)