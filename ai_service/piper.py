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
        
        print("�� Installing Piper TTS...")
        
        # Install piper using the official install script
        install_cmd = [
            'curl', '-s', 'https://raw.githubusercontent.com/rhasspy/piper/master/scripts/install.sh',
            '|', 'bash'
        ]
        
        # Alternative: install via pip
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'piper-tts'], check=True)
        
        print("✅ Piper installed successfully!")
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install Piper: {e}")
        return False

def download_voice_model():
    """Download a voice model for Piper"""
    voice_url = "https://huggingface.co/rhasspy/piper-voices/resolve/v1.0.0/en/en_US/amy/medium/en_US-amy-medium.onnx"
    voice_file = "en_US-amy-medium.onnx"
    
    if os.path.exists(voice_file):
        print(f"✅ Voice model {voice_file} already exists!")
        return voice_file
    
    print("📥 Downloading voice model...")
    try:
        subprocess.run(['wget', voice_url, '-O', voice_file], check=True)
        print(f"✅ Downloaded {voice_file}")
        return voice_file
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to download voice model: {e}")
        return None

def piper_tts_test():
    """Test Piper TTS with various messages"""
    print("🎤 Testing Piper TTS...")
    
    # Install piper if needed
    if not install_piper():
        print("❌ Cannot proceed without Piper installation")
        return
    
    # Download voice model if needed
    voice_file = download_voice_model()
    if not voice_file:
        print("❌ Cannot proceed without voice model")
        return
    
    messages = [
        "Hello Stephen! This is Piper Text-to-Speech.",
        "My name is Stephen and I'm testing the offline audio system.",
        "God is real and this speaker is working perfectly!",
        "Testing one, two, three. Can you hear me clearly?",
        "This is offline speech synthesis with high quality."
    ]
    
    for i, message in enumerate(messages, 1):
        print(f"\n�� Test {i}: {message}")
        
        # Create temporary text file
        with open(f'temp_message_{i}.txt', 'w') as f:
            f.write(message)
        
        try:
            # Run piper TTS
            cmd = [
                'piper', '--model', voice_file,
                '--output_file', f'piper_test_{i}.wav',
                '--input_file', f'temp_message_{i}.txt'
            ]
            
            subprocess.run(cmd, check=True)
            
            # Play the audio
            subprocess.run(['aplay', f'piper_test_{i}.wav'], check=True)
            
            # Clean up
            os.remove(f'temp_message_{i}.txt')
            os.remove(f'piper_test_{i}.wav')
            
            input("Press Enter for next message...")
            
        except subprocess.CalledProcessError as e:
            print(f"❌ Error in test {i}: {e}")
            # Clean up on error
            for file in [f'temp_message_{i}.txt', f'piper_test_{i}.wav']:
                if os.path.exists(file):
                    os.remove(file)

def piper_quick_test():
    """Quick test with direct command"""
    print("🚀 Quick Piper Test...")
    
    test_message = "Hello! This is a quick Piper TTS test."
    
    try:
        # Use echo to pipe text directly to piper
        cmd = f'echo "{test_message}" | piper --model en_US-amy-medium.onnx --output_file quick_test.wav'
        subprocess.run(cmd, shell=True, check=True)
        
        # Play the audio
        subprocess.run(['aplay', 'quick_test.wav'], check=True)
        
        # Clean up
        os.remove('quick_test.wav')
        
        print("✅ Quick test completed!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Quick test failed: {e}")

if __name__ == "__main__":
    print("🎤 Piper TTS Test Script")
    print("=" * 40)
    
    choice = input("Choose test type:\n1. Full test with multiple messages\n2. Quick test\nEnter choice (1 or 2): ")
    
    if choice == "1":
        piper_tts_test()
    elif choice == "2":
        piper_quick_test()
    else:
        print("Invalid choice. Running full test...")
        piper_tts_test()
