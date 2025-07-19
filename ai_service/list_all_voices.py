#!/usr/bin/env python3
import requests
import json
import subprocess
import os

def get_all_piper_voices():
    """Get list of all available Piper voices"""
    
    print("🌍 Fetching all available Piper voices...")
    
    # Piper voices are organized by language and region
    base_url = "https://huggingface.co/rhasspy/piper-voices/tree/v1.0.0"
    
    # Common language codes
    languages = [
        "en", "es", "fr", "de", "it", "pt", "nl", "pl", "ru", "ja", "ko", "zh", "ar", "hi", "ml"
    ]
    
    # English voices (most comprehensive)
    english_voices = [
        # US English
        {
            "name": "Amy (US - Medium)",
            "url": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/amy/medium/en_US-amy-medium.onnx",
            "config": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/amy/medium/en_US-amy-medium.onnx.json"
        },
        {
            "name": "Amy (US - Low)",
            "url": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/amy/low/en_US-amy-low.onnx",
            "config": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/amy/low/en_US-amy-low.onnx.json"
        },
        {
            "name": "Ryan (US - Medium)",
            "url": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/ryan/medium/en_US-ryan-medium.onnx",
            "config": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/ryan/medium/en_US-ryan-medium.onnx.json"
        },
        {
            "name": "Ryan (US - Low)",
            "url": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/ryan/low/en_US-ryan-low.onnx",
            "config": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/ryan/low/en_US-ryan-low.onnx.json"
        },
        # UK English
        {
            "name": "Amy (UK - Medium)",
            "url": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_GB/amy/medium/en_GB-amy-medium.onnx",
            "config": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_GB/amy/medium/en_GB-amy-medium.onnx.json"
        },
        {
            "name": "Ryan (UK - Medium)",
            "url": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_GB/ryan/medium/en_GB-ryan-medium.onnx",
            "config": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_GB/ryan/medium/en_GB-ryan-medium.onnx.json"
        },
        # Australian English
        {
            "name": "Amy (AU - Medium)",
            "url": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_AU/amy/medium/en_AU-amy-medium.onnx",
            "config": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_AU/amy/medium/en_AU-amy-medium.onnx.json"
        },
        {
            "name": "Ryan (AU - Medium)",
            "url": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_AU/ryan/medium/en_AU-ryan-medium.onnx",
            "config": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_AU/ryan/medium/en_AU-ryan-medium.onnx.json"
        }
    ]
    
    return english_voices

def download_voice(voice):
    """Download a specific voice"""
    model_name = voice["url"].split('/')[-1]
    config_name = voice["config"].split('/')[-1]
    
    print(f"📥 Downloading {voice['name']}...")
    
    # Download model
    if not os.path.exists(model_name):
        try:
            subprocess.run(['wget', voice["url"], '-O', model_name], check=True)
            print(f"✅ Downloaded {model_name}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to download {model_name}: {e}")
            return False
    
    # Download config
    if not os.path.exists(config_name):
        try:
            subprocess.run(['wget', voice["config"], '-O', config_name], check=True)
            print(f"✅ Downloaded {config_name}")
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to download {config_name}: {e}")
            return False
    
    return True

def test_voice(voice):
    """Test a specific voice"""
    model_name = voice["url"].split('/')[-1]
    
    if not os.path.exists(model_name):
        print(f"❌ {model_name} not found!")
        return False
    
    print(f"\n🎤 Testing {voice['name']}...")
    
    test_message = "Hello! This is a test of the voice system."
    
    # Create temp file
    with open('temp_voice_test.txt', 'w') as f:
        f.write(test_message)
    
    try:
        output_file = f"test_{voice['name'].replace(' ', '_').replace('(', '').replace(')', '')}.wav"
        
        subprocess.run([
            'piper', '--model', model_name,
            '--output_file', output_file,
            '--input_file', 'temp_voice_test.txt'
        ], check=True)
        
        print("🔊 Playing audio...")
        subprocess.run(['aplay', output_file], check=True)
        
        # Clean up
        os.remove('temp_voice_test.txt')
        os.remove(output_file)
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")
        # Clean up on error
        for file in ['temp_voice_test.txt', output_file]:
            if os.path.exists(file):
                os.remove(file)
        return False

def main():
    print("🎤 All Piper Voices Explorer")
    print("=" * 40)
    
    voices = get_all_piper_voices()
    
    print(f"\n📋 Found {len(voices)} English voices:")
    print("-" * 40)
    
    for i, voice in enumerate(voices, 1):
        print(f"{i}. {voice['name']}")
    
    print(f"\n🎯 Since you liked Ryan, here are the Ryan voices:")
    ryan_voices = [v for v in voices if "Ryan" in v["name"]]
    for voice in ryan_voices:
        print(f"   • {voice['name']}")
    
    print(f"\n🌍 Other languages available:")
    print("   • Spanish (es), French (fr), German (de)")
    print("   • Italian (it), Portuguese (pt), Dutch (nl)")
    print("   • Polish (pl), Russian (ru), Japanese (ja)")
    print("   • Korean (ko), Chinese (zh), Arabic (ar)")
    print("   • Hindi (hi), Malayalam (ml)")
    
    # Let user choose what to do
    print(f"\n🎵 What would you like to do?")
    print("1. Download and test all Ryan voices")
    print("2. Download and test a specific voice")
    print("3. Just see the list")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == "1":
        print(f"\n🎤 Downloading all Ryan voices...")
        for voice in ryan_voices:
            if download_voice(voice):
                test_voice(voice)
                input("Press Enter for next voice...")
    
    elif choice == "2":
        voice_num = input(f"Enter voice number (1-{len(voices)}): ")
        try:
            voice = voices[int(voice_num) - 1]
            if download_voice(voice):
                test_voice(voice)
        except (ValueError, IndexError):
            print("Invalid choice!")

if __name__ == "__main__":
    main() 