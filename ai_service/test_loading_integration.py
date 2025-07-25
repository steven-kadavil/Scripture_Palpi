#!/usr/bin/env python3
"""
Test Loading Sound Integration
Quick test to verify loading sounds work with spiritual assistant
"""

import time
from loading_sounds import LoadingSoundSystem

def simulate_ai_processing():
    """Simulate AI processing time"""
    print("🤖 Simulating AI processing...")
    time.sleep(3)  # Simulate 3 seconds of processing
    return "Hello! This is a test response from your spiritual assistant."

def simulate_tts_generation():
    """Simulate TTS generation time"""
    print("🎤 Simulating TTS generation...")
    time.sleep(2)  # Simulate 2 seconds of TTS generation
    return True

def test_loading_integration():
    """Test the complete loading sound integration"""
    print("🧪 Testing Loading Sound Integration")
    print("=" * 40)
    
    # Initialize loading system
    loader = LoadingSoundSystem()
    
    # Create loading sounds
    print("🎵 Creating loading sounds...")
    loader.create_loading_sounds()
    
    # List available sounds
    print("\n📋 Available loading sounds:")
    loader.list_available_sounds()
    
    # Test each loading sound type
    test_sounds = ["voice_processing", "voice_thinking", "simple_beep"]
    
    for sound_type in test_sounds:
        print(f"\n🎵 Testing: {sound_type}")
        print("-" * 30)
        
        # Test AI processing with loading
        print("1. Testing AI processing with loading sound...")
        ai_response = loader.process_with_loading(simulate_ai_processing)
        print(f"   AI Response: {ai_response}")
        
        # Test TTS generation with loading
        print("\n2. Testing TTS generation with loading sound...")
        tts_result = loader.process_with_loading(simulate_tts_generation)
        print(f"   TTS Result: {tts_result}")
        
        # Ask user if they want to continue
        response = input(f"\nContinue to next sound? (y/n): ")
        if response.lower() != 'y':
            break
    
    print("\n✅ Loading sound integration test completed!")

def test_quick_conversation():
    """Test a quick conversation with loading sounds"""
    print("\n💬 Testing Quick Conversation with Loading")
    print("=" * 40)
    
    loader = LoadingSoundSystem()
    
    # Simulate a conversation flow
    conversation_steps = [
        ("Listening for input...", 1),
        ("Processing with AI...", 3),
        ("Generating speech...", 2),
        ("Playing response...", 1)
    ]
    
    for step, duration in conversation_steps:
        print(f"\n🔄 {step}")
        loader.play_loading_sound("voice_processing")
        time.sleep(duration)
        loader.stop_loading_sound()
        print(f"✅ {step} complete!")
    
    print("\n✅ Quick conversation test completed!")

def main():
    """Main test function"""
    print("🎵 Loading Sound Integration Tests")
    print("=" * 40)
    
    print("\n🎯 Choose a test:")
    print("1. Test loading sound integration")
    print("2. Test quick conversation flow")
    print("3. Test all loading sounds")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == "1":
        test_loading_integration()
    elif choice == "2":
        test_quick_conversation()
    elif choice == "3":
        from loading_sounds import test_loading_sounds
        test_loading_sounds()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main() 