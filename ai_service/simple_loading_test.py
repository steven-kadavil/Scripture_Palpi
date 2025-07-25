#!/usr/bin/env python3
"""
Simple Alexa-style Loading Sound Test
"""

import subprocess
import time
import threading

def play_loading_sound():
    """Play a simple loading sound"""
    try:
        # Simple beep sound using aplay
        subprocess.run(['aplay', '-f', 'S16_LE', '-r', '22050', '-c', '1', '-t', 'wav'], 
                      input=b'\x00\x00' * int(22050 * 2), check=True)
        print("✅ Loading sound played")
    except Exception as e:
        print(f"❌ Error: {e}")

def test_loading():
    """Test loading sound in background"""
    print("🎵 Testing Alexa-style loading sound...")
    
    # Start loading sound in background
    sound_thread = threading.Thread(target=play_loading_sound)
    sound_thread.start()
    
    print("🔄 Processing... (loading sound should play)")
    time.sleep(3)  # Simulate processing
    
    print("✅ Done!")

if __name__ == "__main__":
    test_loading() 