import os
import openai
import urllib.request
from datetime import datetime

#Sets my personal OpenAI API key as the API key that will be used for the program 
openai.api_key = os.getenv("OPENAI_API_KEY")

user_prompt = input("Write your prompt for the text-to-image generator: ")

#Interacts with the API to create the image
response = openai.Image.create(
    prompt = user_prompt,
    n = 1,
    size = "1024x1024"
)

#Provides the URL of the image that was created 
image_url = response['data'][0]['url']

#Prints the URL
print(image_url)

#Ensures that the file name will remain unique 
file_name = "image" + datetime.now().strftime('%Y-%m-%d-%H-%M-%S') + ".png"

#Downloads the URL into the file name 
urllib.request.urlretrieve(image_url, file_name)
