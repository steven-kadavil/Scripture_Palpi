#!/usr/bin/env python3
"""
Test script for speaker output
"""

import pyttsx3
import time

def test_speaker():
    """Test speaker output with text-to-speech"""
    
    try:
        # Initialize text-to-speech engine
        engine = pyttsx3.init()
        
        print("Initializing speaker...")
        
        # Get available voices
        voices = engine.getProperty('voices')
        print(f"Available voices: {len(voices)}")
        
        for i, voice in enumerate(voices):
            print(f"Voice {i}: {voice.name} ({voice.id})")
        
        # Set properties
        engine.setProperty('rate', 200)    # Speed of speech
        engine.setProperty('volume', 0.5)  # Volume (0.0 to 1.0)
    
        
        # Use first available voice
        if voices:
            engine.setProperty('voice', voices[51].id)
            print(f"Using voice: {voices[51].name}")
        
        # Test messages
        test_messages = [
            "Hello! This is a test of the speaker output.",
            "My name is Stephen and I'm testing the audio system.",
            "God is real and this speaker is working perfectly!",
            "Testing one, two, three. Can you hear me clearly?"
        ]
        
        print("\n=== Speaker Test ===")
        print("Make sure your speakers are connected and volume is up!")
        print()
        
        for i, message in enumerate(test_messages, 1):
            print(f"Test {i}: {message}")
            engine.say(message)
            engine.runAndWait()
            time.sleep(1)  # Pause between messages
        
        print("\n✅ Speaker test completed!")
        return True
        
    except Exception as e:
        print(f"❌ Error testing speaker: {e}")
        return False

def test_custom_message():
    """Test with a custom message"""
    
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 0.9)
        
        # Get user input
        message = input("\nEnter a message to speak (or press Enter for default): ")
        if not message:
            message = "Hello Stephen! This is your Christian AI assistant speaking through the speakers."
        
        print(f"Speaking: {message}")
        engine.say(message)
        engine.runAndWait()
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    print("=== Speaker Output Test ===")
    print("Make sure your speakers are connected!")
    print()
    
    # Test basic speaker functionality
    success = test_speaker()
    
    if success:
        print("\n🎉 Speaker is working! Testing custom message...")
        test_custom_message()
    else:
        print("\n❌ Speaker test failed. Check your connections.") 