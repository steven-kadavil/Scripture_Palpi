#!/usr/bin/env python3
import subprocess
import os
import sys

def install_coqui():
    """Install Coqui TTS"""
    try:
        print("📦 Installing Coqui TTS...")
        subprocess.run([sys.executable, '-m', 'pip', 'install', 'TTS'], check=True)
        print("✅ Coqui TTS installed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install Coqui TTS: {e}")
        return False

def list_coqui_voices():
    """List available Coqui voices"""
    try:
        print("🔍 Listing available Coqui voices...")
        result = subprocess.run(['tts', '--list_models'], capture_output=True, text=True, check=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to list voices: {e}")
        return False

def test_coqui_voice(model_name, voice_name):
    """Test a specific Coqui voice"""
    print(f"\n🎤 Testing {voice_name}...")
    
    spiritual_message = "Peace be with you. God's love surrounds us all."
    
    # Create temp file
    with open('temp_coqui.txt', 'w') as f:
        f.write(spiritual_message)
    
    try:
        output_file = f"coqui_{voice_name.replace(' ', '_').replace('(', '').replace(')', '')}.wav"
        
        # Use Coqui TTS
        subprocess.run([
            'tts', '--model_name', model_name,
            '--text', spiritual_message,
            '--out_path', output_file
        ], check=True)
        
        print("🔊 Playing audio...")
        subprocess.run(['aplay', output_file], check=True)
        
        # Clean up
        os.remove(output_file)
        
        return True
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Error with {voice_name}: {e}")
        # Clean up on error
        if os.path.exists(output_file):
            os.remove(output_file)
        return False

def test_spiritual_voices():
    """Test voices that would be good for spiritual content"""
    
    # Some Coqui voices that might be good for spiritual content
    spiritual_voices = [
        {
            "name": "tts_models/en/ljspeech/tacotron2-DDC",
            "display_name": "LJSpeech (Female - Clear)",
            "description": "Clear, articulate female voice"
        },
        {
            "name": "tts_models/en/ljspeech/fast_pitch",
            "display_name": "LJSpeech (Female - FastPitch)",
            "description": "Fast, natural female voice"
        },
        {
            "name": "tts_models/en/vctk/vits",
            "display_name": "VCTK (Multi-Voice)",
            "description": "Multiple voices, including deep male voices"
        },
        {
            "name": "tts_models/en/ljspeech/glow-tts",
            "display_name": "LJSpeech (Female - GlowTTS)",
            "description": "Smooth, flowing female voice"
        }
    ]
    
    print("🎤 Testing Coqui TTS Spiritual Voices")
    print("=" * 50)
    
    for i, voice in enumerate(spiritual_voices, 1):
        print(f"\n{i}. {voice['display_name']}")
        print(f"   {voice['description']}")
        
        if test_coqui_voice(voice['name'], voice['display_name']):
            choice = input("Press Enter for next voice, or 'q' to quit: ")
            if choice.lower() == 'q':
                break

def test_vctk_speakers():
    """Test different VCTK speakers (has multiple voices)"""
    print("\n🎤 Testing VCTK Multi-Voice System...")
    print("VCTK has multiple speakers. Let's test a few:")
    
    # Some VCTK speakers that might be good for spiritual content
    vctk_speakers = [
        ("p225", "Male Speaker 1"),
        ("p226", "Male Speaker 2"), 
        ("p227", "Male Speaker 3"),
        ("p228", "Female Speaker 1"),
        ("p229", "Female Speaker 2")
    ]
    
    for speaker_id, speaker_name in vctk_speakers:
        print(f"\n🎤 Testing {speaker_name} ({speaker_id})...")
        
        spiritual_message = "Peace be with you. God's love surrounds us all."
        
        try:
            output_file = f"vctk_{speaker_id}.wav"
            
            subprocess.run([
                'tts', '--model_name', 'tts_models/en/vctk/vits',
                '--text', spiritual_message,
                '--speaker_idx', speaker_id,
                '--out_path', output_file
            ], check=True)
            
            print("🔊 Playing audio...")
            subprocess.run(['aplay', output_file], check=True)
            
            # Clean up
            os.remove(output_file)
            
            choice = input("Press Enter for next speaker, or 'q' to quit: ")
            if choice.lower() == 'q':
                break
                
        except subprocess.CalledProcessError as e:
            print(f"❌ Error with {speaker_name}: {e}")
            if os.path.exists(output_file):
                os.remove(output_file)

def main():
    print("🎤 Coqui TTS Test")
    print("=" * 30)
    
    # Install Coqui if needed
    if not install_coqui():
        print("❌ Cannot proceed without Coqui installation")
        return
    
    print("\n🎵 What would you like to do?")
    print("1. List all available voices")
    print("2. Test spiritual voices")
    print("3. Test VCTK multi-speaker system")
    print("4. All of the above")
    
    choice = input("Enter choice (1-4): ")
    
    if choice == "1":
        list_coqui_voices()
    
    elif choice == "2":
        test_spiritual_voices()
    
    elif choice == "3":
        test_vctk_speakers()
    
    elif choice == "4":
        list_coqui_voices()
        test_spiritual_voices()
        test_vctk_speakers()
    
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main() 