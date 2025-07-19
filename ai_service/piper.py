#!/usr/bin/env python3
import subprocess
import os
import sys

def install_piper():
    """Install Piper TTS if not already installed"""
    try:
        # Check if piper is already installed
        result = subprocess.run(['which', 'piper'], capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Piper is already installed!")
            return True
        
        print(" Installing Piper TTS...")
        
        # Alternative: install via pip
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'piper-tts'], check=True)
        
        print("✅ Piper installed successfully!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install Piper: {e}")
        return False

def download_all_voices():
    """Download multiple voice models for comparison"""
    
    # Different voices to test - each with different characteristics
    voices = [
        {
            "name": "Amy (Gentle & Warm)",
            "model": "en_US-amy-medium.onnx",
            "config": "en_US-amy-medium.onnx.json",
            "urls": [
                "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/amy/medium/en_US-amy-medium.onnx",
                "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/amy/medium/en_US-amy-medium.onnx.json"
            ]
        },
        {
            "name": "Ryan (Deep & Wise)",
            "model": "en_US-ryan-medium.onnx", 
            "config": "en_US-ryan-medium.onnx.json",
            "urls": [
                "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/ryan/medium/en_US-ryan-medium.onnx",
                "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/ryan/medium/en_US-ryan-medium.onnx.json"
            ]
        },
        {
            "name": "Ryan (Very Deep & Resonant)",
            "model": "en_US-ryan-low.onnx",
            "config": "en_US-ryan-low.onnx.json", 
            "urls": [
                "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/ryan/low/en_US-ryan-low.onnx",
                "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/ryan/low/en_US-ryan-low.onnx.json"
            ]
        }
    ]
    
    downloaded_voices = []
    
    for voice in voices:
        print(f"\n📥 Checking {voice['name']}...")
        
        # Check if both files exist
        if os.path.exists(voice['model']) and os.path.exists(voice['config']):
            print(f"✅ {voice['name']} already downloaded!")
            downloaded_voices.append(voice)
            continue
        
        # Download missing files
        for url in voice['urls']:
            filename = url.split('/')[-1]
            if not os.path.exists(filename):
                print(f"📥 Downloading {filename}...")
                try:
                    subprocess.run(['wget', url, '-O', filename], check=True)
                    print(f"✅ Downloaded {filename}")
                except subprocess.CalledProcessError as e:
                    print(f"❌ Failed to download {filename}: {e}")
                    break
        else:
            downloaded_voices.append(voice)
    
    return downloaded_voices

def test_all_voices():
    """Test all downloaded voices with spiritual content"""
    
    spiritual_messages = [
        "Peace be with you. God's love surrounds us all.",
        "In times of darkness, remember that light always returns.",
        "Faith is the bridge between dreams and reality.",
        "You are loved beyond measure, just as you are."
    ]
    
    voices = download_all_voices()
    
    if not voices:
        print("❌ No voices available for testing!")
        return
    
    print(f"\n🎤 Testing {len(voices)} voices...")
    print("=" * 60)
    
    for voice in voices:
        print(f"\n🎵 Testing: {voice['name']}")
        print("-" * 40)
        
        # Test with one spiritual message
        test_message = "Peace be with you. God's love surrounds us all."
        print(f"Message: {test_message}")
        
        # Create temp file
        with open('temp_test.txt', 'w') as f:
            f.write(test_message)
        
        try:
            # Generate speech
            output_file = f"test_{voice['name'].replace(' ', '_').replace('(', '').replace(')', '')}.wav"
            subprocess.run([
                'piper', '--model', voice['model'],
                '--output_file', output_file,
                '--input_file', 'temp_test.txt'
            ], check=True)
            
            # Play audio
            print("🔊 Playing audio...")
            subprocess.run(['aplay', output_file], check=True)
            
            # Clean up
            os.remove('temp_test.txt')
            os.remove(output_file)
            
            choice = input("\nPress Enter for next voice, or 'q' to quit: ")
            if choice.lower() == 'q':
                break
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Error with {voice['name']}: {e}")
            # Clean up on error
            for file in ['temp_test.txt', output_file]:
                if os.path.exists(file):
                    os.remove(file)

def piper_voice_comparison():
    """Compare all voices side by side"""
    print("🎤 Piper Voice Comparison")
    print("=" * 40)
    
    # Install piper if needed
    if not install_piper():
        print("❌ Cannot proceed without Piper installation")
        return
    
    # Test all voices
    test_all_voices()

if __name__ == "__main__":
    piper_voice_comparison()
