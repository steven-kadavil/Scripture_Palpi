import os
from gtts import gTTS

def google_tts_test():
    messages = [
        "Hello Stephen! This is Google Text-to-Speech.",
        "My name is Stephen and I'm testing the audio system.",
        "God is real and this speaker is working perfectly!",
        "Testing one, two, three. Can you hear me clearly?"
        "Power rangers RPM Get in Gear. fucks"
    ]
    
    for i, message in enumerate(messages, 1):
        print(f"Test {i}: {message}")
        tts = gTTS(text=message, lang='en', slow=False)
        tts.save(f'test_{i}.mp3')
        os.system(f'mpg123 test_{i}.mp3')
        os.remove(f'test_{i}.mp3')
        input("Press Enter for next message...")

if __name__ == "__main__":
    google_tts_test()