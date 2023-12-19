from openai import OpenAI
from IPython.display import display

#function called chat_gpt that takes one argument recognized_text.
def chat_gpt(recognized_text):  
    #API_KEY variable to a specific API key.
    API_KEY = openai.api_key = 'Api Key here'   
    #client object to interact with the OpenAI API.
    client = OpenAI(  
         #pass the API key to the client.
        api_key=API_KEY 
    )
    #recognized_text argument in the prompt variable.
    prompt = recognized_text  
    #client to create a chat completion.
    chat_completion = client.chat.completions.create(  
        messages=[
            {
                #"user" for the message.
                "role": "user",  
                #recognized_text.
                "content": prompt  
            },
        ],
        #LLM model 
        model="gpt-3.5-turbo"  
    )
    #the content of the completed chat response.
    text_to_speak = (chat_completion.choices[0].message.content)  
    #content of the response to the console.
    print(text_to_speak)  

chat_gpt("Hello World")