import openai
import speech_recognition as sr
import pyttsx3

# Create a recognizer instance
recognizer = sr.Recognizer()

# Initialize the OpenAI API client
api_key = "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"
openai.api_key = api_key

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 178)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


# Define a function to generate text from speech and get GPT-3.5-turbo response
def generate_response(audio_text):
    # Generate text using GPT-3.5-turbo
    response = openai.Completion.create(
        engine="text-davinci-002",  # Use "text-davinci-002" for GPT-3.5-turbo
        prompt=audio_text,
        max_tokens=50  # Adjust as needed
    )

    # Get the generated text
    generated_text = response.choices[0].text

    return generated_text


# Continuous conversation loop
while True:
    with sr.Microphone() as source:
        print("Say something...")
        audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Web Speech API
        recognized_text = recognizer.recognize_google(audio)

        # Print user's speech
        print("User: " + recognized_text)

        # Generate response from GPT-3.5-turbo
        gpt_response = generate_response(recognized_text)

        # Print GPT-3.5-turbo's response
        print("GPT-3.5-turbo: " + gpt_response)

        # Speak the response
        engine.say(gpt_response)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
    except sr.RequestError as e:
        print("Sorry, there was an error with the request: {0}".format(e))
