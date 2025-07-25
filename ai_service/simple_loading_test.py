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
        # Create a simple beep sound (sine wave)
        import math
        sample_rate = 22050
        duration = 1.0  # 1 second
        frequency = 800  # 800 Hz beep
        
        # Generate sine wave
        samples = []
        for i in range(int(sample_rate * duration)):
            sample = int(32767 * math.sin(2 * math.pi * frequency * i / sample_rate))
            samples.extend([sample & 0xFF, (sample >> 8) & 0xFF])
        
        audio_data = bytes(samples)
        
        # Play through default audio device
        subprocess.run(['aplay', '-f', 'S16_LE', '-r', str(sample_rate), '-c', '1'], 
                      input=audio_data, check=True)
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