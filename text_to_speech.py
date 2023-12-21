import pyttsx3

def speech(text):
    engine = pyttsx3.init()

    """ RATE"""
    #the current speaking rate
    rate = engine.getProperty('rate')
    print(f"Speed rate of speech: {rate}")
    #a new voice rate (adjust as needed)
    engine.setProperty('rate', 180)

    """VOLUME"""
    #the current volume level (min=0 and max=1)
    volume = engine.getProperty('volume')
    print(f"Volume of speech: {volume}")
    # Set the volume level between 0 and 1 (adjust as needed)
    engine.setProperty('volume', 1.0)

    #say the text
    engine.say(text)
    engine.runAndWait()

    """Saving Voice to a file"""
    engine.save_to_file(text, 'test.mp3')
    engine.runAndWait()
    engine.stop()

text = '''Machine learning is a subfield of artificial intelligence, 
which is broadly defined as the capability of a machine to imitate intelligent human behavior. 
Artificial intelligence systems are used to perform complex tasks in a way that is similar to how humans solve problems.'''
speech(text)
