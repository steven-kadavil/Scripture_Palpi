#!/usr/bin/env python3
import subprocess
import os

def download_spiritual_voices():
    """Download voices perfect for spiritual content"""
    
    voices = [
        {
            "name": "Ryan (Deep & Wise)",
            "url": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/ryan/medium/en_US-ryan-medium.onnx",
            "config": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/ryan/medium/en_US-ryan-medium.onnx.json"
        },
        {
            "name": "Ryan (Deep & Resonant)", 
            "url": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/ryan/low/en_US-ryan-low.onnx",
            "config": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/ryan/low/en_US-ryan-low.onnx.json"
        },
        {
            "name": "Amy (Warm & Gentle)",
            "url": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/amy/medium/en_US-amy-medium.onnx", 
            "config": "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/amy/medium/en_US-amy-medium.onnx.json"
        }
    ]
    
    for voice in voices:
        model_name = voice["url"].split('/')[-1]
        config_name = voice["config"].split('/')[-1]
        
        print(f"�� Downloading {voice['name']}...")
        
        # Download model
        if not os.path.exists(model_name):
            subprocess.run(['wget', voice["url"], '-O', model_name], check=True)
        
        # Download config
        if not os.path.exists(config_name):
            subprocess.run(['wget', voice["config"], '-O', config_name], check=True)
        
        print(f"✅ Downloaded {voice['name']}")

def test_spiritual_voices():
    """Test different voices with spiritual content"""
    
    spiritual_messages = [
        "Peace be with you. God's love surrounds us all.",
        "In times of darkness, remember that light always returns.",
        "Faith is the bridge between dreams and reality.",
        "You are loved beyond measure, just as you are.",
        "Every moment is a gift, every breath a blessing."
    ]
    
    voices = [
        ("en_US-ryan-medium.onnx", "Ryan (Medium)"),
        ("en_US-ryan-low.onnx", "Ryan (Deep)"), 
        ("en_US-amy-medium.onnx", "Amy (Gentle)")
    ]
    
    for model_file, voice_name in voices:
        if not os.path.exists(model_file):
            print(f"❌ {voice_name} not found, skipping...")
            continue
            
        print(f"\n🎤 Testing {voice_name}...")
        print("=" * 50)
        
        for i, message in enumerate(spiritual_messages, 1):
            print(f"\n{i}. {message}")
            
            # Create temp file
            with open(f'temp_spiritual_{i}.txt', 'w') as f:
                f.write(message)
            
            try:
                # Generate speech
                subprocess.run([
                    'piper', '--model', model_file,
                    '--output_file', f'spiritual_{voice_name}_{i}.wav',
                    '--input_file', f'temp_spiritual_{i}.txt'
                ], check=True)
                
                # Play audio
                subprocess.run(['aplay', f'spiritual_{voice_name}_{i}.wav'], check=True)
                
                # Clean up
                os.remove(f'temp_spiritual_{i}.txt')
                os.remove(f'spiritual_{voice_name}_{i}.wav')
                
                input("Press Enter for next message...")
                
            except subprocess.CalledProcessError as e:
                print(f"❌ Error: {e}")

if __name__ == "__main__":
    print("🙏 Spiritual Voice Test")
    print("=" * 40)
    
    # Download voices
    download_spiritual_voices()
    
    # Test voices
    test_spiritual_voices() 