#!/usr/bin/env python3
"""
Download Alexa-style Loading Sound
"""

import subprocess
import os

def download_loading_sound():
    """Download an Alexa-style loading sound"""
    
    # Alexa-style loading sound URL (free sound effect)
    sound_url = "https://www.soundjay.com/misc/sounds/bell-ringing-05.wav"
    
    print("📥 Downloading Alexa-style loading sound...")
    
    try:
        # Download the sound
        subprocess.run(['wget', '-O', 'alexa_loading.wav', sound_url], check=True)
        print("✅ Loading sound downloaded!")
        
        # Test play it
        print("🔊 Testing loading sound...")
        subprocess.run(['aplay', 'alexa_loading.wav'], check=True)
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Download failed: {e}")
        
        # Fallback: create a simple chime
        print("📝 Creating simple chime sound...")
        subprocess.run([
            'ffmpeg', '-f', 'lavfi', '-i', 'sine=frequency=800:duration=0.3',
            '-f', 'lavfi', '-i', 'sine=frequency=1000:duration=0.3',
            '-filter_complex', 'amix=inputs=2:duration=longest',
            'alexa_loading.wav'
        ], check=True)
        
        print("✅ Simple chime created!")

if __name__ == "__main__":
    download_loading_sound() 