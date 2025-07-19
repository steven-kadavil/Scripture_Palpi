#!/usr/bin/env python3
import subprocess
import os

def check_voice_files():
    """Check what voice files exist"""
    print("🔍 Checking for voice files...")
    
    voice_files = [
        "en_US-amy-medium.onnx",
        "en_US-amy-medium.onnx.json", 
        "en_US-ryan-medium.onnx",
        "en_US-ryan-medium.onnx.json",
        "en_US-ryan-low.onnx",
        "en_US-ryan-low.onnx.json"
    ]
    
    existing_files = []
    for file in voice_files:
        if os.path.exists(file):
            print(f"✅ {file}")
            existing_files.append(file)
        else:
            print(f"❌ {file} - MISSING")
    
    return existing_files

def test_single_voice(model_file, voice_name):
    """Test a single voice"""
    if not os.path.exists(model_file):
        print(f"❌ {model_file} not found!")
        return False
    
    config_file = model_file + ".json"
    if not os.path.exists(config_file):
        print(f"❌ {config_file} not found!")
        return False
    
    print(f"\n🎤 Testing {voice_name}...")
    
    test_message = "This is a test of the voice system."
    
    # Create temp file
    with open('temp_debug.txt', 'w') as f:
        f.write(test_message)
    
    try:
        output_file = f"debug_{voice_name.replace(' ', '_')}.wav"
        
        print(f"🔊 Generating audio...")
        subprocess.run([
            'piper', '--model', model_file,
            '--output_file', output_file,
            '--input_file', 'temp_debug.txt'
        ], check=True)
        
        print(f"🔊 Playing audio...")
        subprocess.run(['aplay', output_file], check=True)
        
        # Clean up
        os.remove('temp_debug.txt')
        os.remove(output_file)
        
        print(f"✅ {voice_name} test completed!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error with {voice_name}: {e}")
        # Clean up on error
        for file in ['temp_debug.txt', output_file]:
            if os.path.exists(file):
                os.remove(file)
        return False

def main():
    print("🔍 Voice Debug Script")
    print("=" * 30)
    
    # Check what files exist
    existing_files = check_voice_files()
    
    if not existing_files:
        print("\n❌ No voice files found! Run the main piper.py script first.")
        return
    
    # Test each available voice
    voices_to_test = [
        ("en_US-amy-medium.onnx", "Amy (Medium)"),
        ("en_US-ryan-medium.onnx", "Ryan (Medium)"),
        ("en_US-ryan-low.onnx", "Ryan (Low)")
    ]
    
    print(f"\n🎤 Testing available voices...")
    
    for model_file, voice_name in voices_to_test:
        if os.path.exists(model_file):
            test_single_voice(model_file, voice_name)
            input("Press Enter for next voice...")

if __name__ == "__main__":
    main() 