#!/usr/bin/env python3
"""
Loading Sound System for Spiritual Assistant
Provides various loading sounds and indicators while processing
"""

import subprocess
import os
import time
import threading
from typing import Optional

class LoadingSoundSystem:
    """Manages loading sounds and indicators for the spiritual assistant"""
    
    def __init__(self):
        self.current_sound = None
        self.is_playing = False
        self.sound_thread = None
        
        # Available loading sounds
        self.loading_sounds = {
            "gentle_chime": {
                "description": "Soft spiritual chime",
                "file": "loading_chime.wav",
                "duration": 2.0
            },
            "peaceful_ambient": {
                "description": "Peaceful ambient tones", 
                "file": "peaceful_ambient.wav",
                "duration": 3.0
            },
            "voice_processing": {
                "description": "Voice says 'Processing...'",
                "type": "tts",
                "text": "Processing your request...",
                "duration": 2.0
            },
            "voice_thinking": {
                "description": "Voice says 'Thinking...'",
                "type": "tts", 
                "text": "Thinking...",
                "duration": 1.5
            },
            "simple_beep": {
                "description": "Simple beep sound",
                "file": "simple_beep.wav",
                "duration": 0.5
            }
        }
        
        # Default loading sound
        self.default_sound = "voice_processing"
    
    def create_loading_sounds(self):
        """Create basic loading sound files if they don't exist"""
        print("🎵 Creating loading sounds...")
        
        # Create simple beep using sox
        if not os.path.exists("simple_beep.wav"):
            try:
                subprocess.run([
                    'sox', '-n', 'simple_beep.wav', 
                    'trim', '0.0', '0.5', 'sine', '800'
                ], check=True)
                print("✅ Created simple_beep.wav")
            except (subprocess.CalledProcessError, FileNotFoundError):
                print("⚠️  Could not create beep (sox not installed)")
        
        # Create gentle chime using sox
        if not os.path.exists("loading_chime.wav"):
            try:
                subprocess.run([
                    'sox', '-n', 'loading_chime.wav',
                    'trim', '0.0', '2.0', 'sine', '440', 'sine', '880'
                ], check=True)
                print("✅ Created loading_chime.wav")
            except (subprocess.CalledProcessError, FileNotFoundError):
                print("⚠️  Could not create chime (sox not installed)")
    
    def play_loading_sound(self, sound_type: str = None, duration: float = None):
        """Play a loading sound"""
        if sound_type is None:
            sound_type = self.default_sound
        
        if sound_type not in self.loading_sounds:
            print(f"❌ Unknown loading sound: {sound_type}")
            return
        
        sound_config = self.loading_sounds[sound_type]
        
        # Stop any currently playing sound
        self.stop_loading_sound()
        
        # Start new sound in thread
        self.sound_thread = threading.Thread(
            target=self._play_sound_thread,
            args=(sound_config, duration)
        )
        self.sound_thread.daemon = True
        self.sound_thread.start()
        
        print(f"🎵 Playing loading sound: {sound_config['description']}")
    
    def _play_sound_thread(self, sound_config: dict, duration: float = None):
        """Play sound in background thread"""
        self.is_playing = True
        
        try:
            if sound_config.get("type") == "tts":
                # Generate TTS loading message
                self._play_tts_loading(sound_config["text"])
            else:
                # Play audio file
                self._play_audio_file(sound_config["file"], duration or sound_config["duration"])
        except Exception as e:
            print(f"❌ Error playing loading sound: {e}")
        finally:
            self.is_playing = False
    
    def _play_tts_loading(self, text: str):
        """Play TTS loading message using Piper"""
        try:
            # Use Ryan voice for loading messages
            voice_file = "en_US-ryan-medium.onnx"
            
            if not os.path.exists(voice_file):
                print("⚠️  Ryan voice not found, skipping TTS loading sound")
                return
            
            # Create temp file for text
            with open("temp_loading.txt", "w") as f:
                f.write(text)
            
            # Generate loading audio
            subprocess.run([
                'piper', '--model', voice_file,
                '--output_file', 'temp_loading.wav',
                '--input_file', 'temp_loading.txt'
            ], check=True, capture_output=True)
            
            # Play the audio
            if os.path.exists("temp_loading.wav"):
                subprocess.run(['aplay', 'temp_loading.wav'], check=True)
            
            # Clean up
            for file in ["temp_loading.txt", "temp_loading.wav"]:
                if os.path.exists(file):
                    os.remove(file)
                    
        except Exception as e:
            print(f"❌ Error with TTS loading sound: {e}")
    
    def _play_audio_file(self, filename: str, duration: float):
        """Play audio file for specified duration"""
        try:
            if os.path.exists(filename):
                # Play audio file
                subprocess.run(['aplay', filename], check=True)
            else:
                # Fallback to simple beep
                print(f"⚠️  {filename} not found, using fallback beep")
                subprocess.run(['aplay', '-D', 'hw:4,0', '-f', 'S16_LE', '-r', '22050', '-c', '1', '-t', 'wav'], 
                             input=b'\x00\x00' * int(22050 * duration), check=True)
        except Exception as e:
            print(f"❌ Error playing audio file: {e}")
    
    def stop_loading_sound(self):
        """Stop currently playing loading sound"""
        if self.is_playing:
            self.is_playing = False
            if self.sound_thread and self.sound_thread.is_alive():
                self.sound_thread.join(timeout=1.0)
            print("🛑 Stopped loading sound")
    
    def show_loading_indicator(self, message: str = "Processing..."):
        """Show visual loading indicator"""
        print(f"🔄 {message}")
    
    def process_with_loading(self, process_func, *args, **kwargs):
        """Process with loading sound and indicator"""
        # Start loading sound
        self.play_loading_sound()
        self.show_loading_indicator()
        
        try:
            # Run the actual process
            result = process_func(*args, **kwargs)
            return result
        finally:
            # Stop loading sound
            self.stop_loading_sound()
            print("✅ Processing complete!")
    
    def list_available_sounds(self):
        """List all available loading sounds"""
        print("🎵 Available Loading Sounds:")
        print("-" * 40)
        
        for i, (sound_id, config) in enumerate(self.loading_sounds.items(), 1):
            print(f"{i}. {sound_id}: {config['description']}")
        
        return list(self.loading_sounds.keys())

def test_loading_sounds():
    """Test the loading sound system"""
    print("🎵 Testing Loading Sound System")
    print("=" * 40)
    
    loader = LoadingSoundSystem()
    
    # Create basic sounds
    loader.create_loading_sounds()
    
    # List available sounds
    sounds = loader.list_available_sounds()
    
    print(f"\n🎯 Testing each loading sound:")
    print("-" * 30)
    
    for sound_id in sounds:
        print(f"\n🎵 Testing: {sound_id}")
        loader.play_loading_sound(sound_id)
        time.sleep(3)  # Wait for sound to finish
        loader.stop_loading_sound()
        
        response = input("Press Enter for next sound (or 'q' to quit): ")
        if response.lower() == 'q':
            break
    
    print("\n✅ Loading sound test completed!")

if __name__ == "__main__":
    test_loading_sounds() 