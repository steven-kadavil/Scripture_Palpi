#!/usr/bin/env python3
import subprocess
import os

def get_verified_voices():
    """Get list of voices we know work"""
    
    # Only voices we've confirmed work
    verified_voices = [
        {
            "name": "Amy (US - Medium)",
            "model": "en_US-amy-medium.onnx",
            "config": "en_US-amy-medium.onnx.json",
            "urls": [
                "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/amy/medium/en_US-amy-medium.onnx",
                "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/amy/medium/en_US-amy-medium.onnx.json"
            ]
        },
        {
            "name": "Ryan (US - Medium)",
            "model": "en_US-ryan-medium.onnx",
            "config": "en_US-ryan-medium.onnx.json", 
            "urls": [
                "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/ryan/medium/en_US-ryan-medium.onnx",
                "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/ryan/medium/en_US-ryan-medium.onnx.json"
            ]
        },
        {
            "name": "Ryan (US - Low)",
            "model": "en_US-ryan-low.onnx",
            "config": "en_US-ryan-low.onnx.json",
            "urls": [
                "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/ryan/low/en_US-ryan-low.onnx",
                "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/ryan/low/en_US-ryan-low.onnx.json"
            ]
        }
    ]
    
    return verified_voices

def download_voice(voice):
    """Download a specific voice"""
    print(f"📥 Downloading {voice['name']}...")
    
    # Download both files
    for url in voice['urls']:
        filename = url.split('/')[-1]
        if not os.path.exists(filename):
            try:
                subprocess.run(['wget', url, '-O', filename], check=True)
                print(f"✅ Downloaded {filename}")
            except subprocess.CalledProcessError as e:
                print(f"❌ Failed to download {filename}: {e}")
                return False
    
    return True

def test_voice(voice):
    """Test a specific voice"""
    if not os.path.exists(voice['model']):
        print(f"❌ {voice['model']} not found!")
        return False
    
    print(f"\n🎤 Testing {voice['name']}...")
    
    spiritual_message = "Peace be with you. God's love surrounds us all."
    
    # Create temp file
    with open('temp_spiritual.txt', 'w') as f:
        f.write(spiritual_message)
    
    try:
        output_file = f"test_{voice['name'].replace(' ', '_').replace('(', '').replace(')', '')}.wav"
        
        subprocess.run([
            'piper', '--model', voice['model'],
            '--output_file', output_file,
            '--input_file', 'temp_spiritual.txt'
        ], check=True)
        
        print("🔊 Playing audio...")
        subprocess.run(['aplay', output_file], check=True)
        
        # Clean up
        os.remove('temp_spiritual.txt')
        os.remove(output_file)
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        # Clean up on error
        for file in ['temp_spiritual.txt', output_file]:
            if os.path.exists(file):
                os.remove(file)
        return False

def main():
    print("🎤 Verified Piper Voices")
    print("=" * 30)
    
    voices = get_verified_voices()
    
    print(f"\n📋 {len(voices)} verified voices:")
    print("-" * 30)
    
    for i, voice in enumerate(voices, 1):
        print(f"{i}. {voice['name']}")
    
    print(f"\n🎯 Ryan voices (best for spiritual content):")
    ryan_voices = [v for v in voices if "Ryan" in v["name"]]
    for voice in ryan_voices:
        print(f"   • {voice['name']}")
    
    print(f"\n🎵 What would you like to do?")
    print("1. Download and test all Ryan voices")
    print("2. Download and test all voices")
    print("3. Download and test a specific voice")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == "1":
        print(f"\n🎤 Downloading all Ryan voices...")
        for voice in ryan_voices:
            if download_voice(voice):
                test_voice(voice)
                input("Press Enter for next voice...")
    
    elif choice == "2":
        print(f"\n🎤 Downloading all voices...")
        for voice in voices:
            if download_voice(voice):
                test_voice(voice)
                input("Press Enter for next voice...")
    
    elif choice == "3":
        voice_num = input(f"Enter voice number (1-{len(voices)}): ")
        try:
            voice = voices[int(voice_num) - 1]
            if download_voice(voice):
                test_voice(voice)
        except (ValueError, IndexError):
            print("Invalid choice!")

if __name__ == "__main__":
    main() 