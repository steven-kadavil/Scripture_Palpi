#!/usr/bin/env python3
"""
Test script for USB microphone speech recognition
"""

import speech_recognition as sr
import time

def test_microphone():
    """Test microphone and speech recognition"""
    
    # Initialize recognizer
    recognizer = sr.Recognizer()
    
    try:
        # Create microphone instance
        microphone = sr.Microphone()
        
        print("Initializing microphone...")
        
        # Adjust for ambient noise
        with microphone as source:
            print("Adjusting for ambient noise... Please be quiet for 2 seconds.")
            recognizer.adjust_for_ambient_noise(source, duration=2)
            print("Microphone ready!")
        
        # Listen for speech
        print("\nSpeak something now...")
        with microphone as source:
            print("Listening...")
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
        
        print("Processing speech...")
        
        # Convert to text
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        
        return text
        
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results: {e}")
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == "__main__":
    print("=== USB Microphone Test ===")
    print("Make sure your USB microphone is connected!")
    print()
    
    # Test microphone
    result = test_microphone()
    
    if result:
        print(f"\n✅ Success! Recognized: '{result}'")
    else:
        print("\n❌ Failed to recognize speech")
