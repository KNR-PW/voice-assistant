import speech_recognition as sr
import openai
import pyttsx3


class ChatModule:
    def __init__(self):
        self.sr = sr.Recognizer()
        self.speechEngine = pyttsx3.init()
        openai.api_key = "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"

    def record(self):
        with sr.Microphone() as source:
            audio = self.sr.listen(source)
        return audio

    def recognize_audio(self, audio):
        try:
            text = self.sr.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
        return None

    def get_open_ai_response(self, text):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=text,
                max_tokens=256,
                n=1,
                stop=None,
                temperature=0.5,
            )

            return response.choices[0].text
        except openai.Error as e:
            print(f"Error querying OpenAI API: {e}")

    def say(self, text):
        self.speechEngine.setProperty('rate', 120)  # Speed in words per minute
        self.speechEngine.setProperty('volume', 1.0)  # Volume, from 0 to 1
        self.speechEngine.say(text)
        self.speechEngine.runAndWait()

    def run(self):
        self.say("Say something!")
        audio = self.record()
        text = self.recognize_audio(audio)
        print(f"You said: {text}")

        if text is not None:
            response = self.get_open_ai_response(text)
            print(f"AI answer: {response}")
            if response is not None:
                self.say(response)
