# Chat Module

This module contains a class called `ChatModule`, which provides speech recognition, text-to-speech conversion, and OpenAI API ability to generate a response to user input.

## Dependencies
This module requires the following packages installed:
- speech_recognition
- openai
- pyttsx3
- pyaudio

## Usage
To use this module, create an instance of `ChatModule` and call one of its methods, such as `run()` or `run_linux()`. These methods will prompt the user for input, recognize the input using speech recognition, generate a response using OpenAI, and convert the response to speech.

### Initialization
Upon creating a `ChatModule` instance, it initializes several objects:
- `sr`: a `Recognizer` object from the `speech_recognition` package
- `speechEngine`: a `pyttsx3` text-to-speech engine object
- `openai.api_key`: the API key for OpenAI, which can be obtained from https://platform.openai.com/account/api-keys

### Methods
The `ChatModule` class provides the following methods:

#### `record()`
This method prompts the user to speak and records audio using the default system microphone. It returns the recorded audio.

#### `record_linux()`
This method is similar to `record()`, but is specifically designed for Linux systems.

#### `recognize_audio(audio)`
This method takes an audio object as input and uses Google's speech recognition API to convert the audio to text. It returns the recognized text, or `None` if recognition fails.

#### `get_open_ai_response(text)`
This method takes a string of text as input and uses the OpenAI API to generate a response. It returns the generated response as a string, or `None` if the API call fails.

#### `say(text)`
This method takes a string of text as input and converts it to speech using the `speechEngine` object. It does not return anything.

#### `repeat_myself()`
This method continually prompts the user to speak, recognizes the input using `recognize_audio()`, and repeats the input using `say()`. It does not return anything and runs indefinitely until the program is terminated.

#### `run()`
This method prompts the user to speak, recognizes the input using `recognize_audio()`, generates a response using `get_open_ai_response()`, and converts the response to speech using `say()`. It prints the recognized text and generated response to the console. It does not return anything.

#### `run_linux()`
This method is similar to `run()`, but is specifically designed for Linux systems.

### Example Usage For Windows
```python
chat = ChatModule.ChatModule()
chat.run()
```

### Example Usage For Linux
```python
chat = ChatModule.ChatModule()
chat.run_linux()
```

This code creates a `ChatModule` instance and calls the `run()` (or `run_linux()`) method, which prompts the user to speak, recognizes the input, generates a response, and converts the response to speech.