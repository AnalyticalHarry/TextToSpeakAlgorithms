import pyttsx3

def speech(text):
        engine = pyttsx3.init() 

        """ RATE"""
        #current speaking rate
        rate = engine.getProperty('rate')   
        print()
        #printing current voice rate
        print(f"Speed rate of speech: {rate}") 
        #setting up new voice rate
        engine.setProperty('rate', 180)     


        """VOLUME"""
        #getting to know current volume level (min=0 and max=1)
        volume = engine.getProperty('volume')   
        print()
        #printing current volume level
        print(f"Volume of speech: {volume}")             
        #setting up volume level  between 0 and 1
        engine.setProperty('volume',1.0)    
        engine.say(text)
        engine.runAndWait()
        engine.stop()

        """Saving Voice to a file"""
        engine.save_to_file(text, 'test.mp3')
        engine.runAndWait()
    
text = ''' Machine learning is a subfield of artificial intelligence, 
which is broadly defined as the capability of a machine to imitate intelligent human behavior. 
Artificial intelligence systems are used to perform complex tasks in a way that is similar to how humans solve problems.'''
speech(text)
