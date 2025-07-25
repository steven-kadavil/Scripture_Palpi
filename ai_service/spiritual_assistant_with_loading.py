#!/usr/bin/env python3
"""
Spiritual Assistant with Loading Sounds
Complete voice assistant with loading indicators
"""

import speech_recognition as sr
import subprocess
import os
import time
import threading
from loading_sounds import LoadingSoundSystem

class SpiritualAssistant:
    """Complete spiritual assistant with loading sounds"""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.loading_system = LoadingSoundSystem()
        self.is_listening = False
        self.voice_file = "en_US-ryan-medium.onnx"
        
        # Spiritual context for AI responses
        self.spiritual_context = """
        You are a wise, compassionate Christian spiritual assistant. 
        Provide thoughtful, uplifting responses that reflect Christian values.
        Be encouraging, supportive, and spiritually insightful.
        Keep responses concise but meaningful.
        """
        
        print("🙏 Initializing Spiritual Assistant...")
        self._initialize_system()
    
    def _initialize_system(self):
        """Initialize the assistant systems"""
        print("🔧 Setting up systems...")
        
        # Create loading sounds
        self.loading_system.create_loading_sounds()
        
        # Adjust microphone for ambient noise
        print("🎤 Adjusting microphone for ambient noise...")
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
        
        # Check if Ryan voice is available
        if not os.path.exists(self.voice_file):
            print("⚠️  Ryan voice not found. Please download it first.")
            print("   Run: python3 Voice_output_test.py")
        
        print("✅ Spiritual Assistant ready!")
    
    def listen_for_input(self) -> str:
        """Listen for voice input and return text"""
        print("\n🎤 Listening for your question...")
        
        try:
            with self.microphone as source:
                print("👂 Speak now...")
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
            
            print("🔄 Processing speech...")
            text = self.recognizer.recognize_google(audio)
            print(f"📝 You said: '{text}'")
            return text
            
        except sr.UnknownValueError:
            print("❌ Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"❌ Speech recognition error: {e}")
            return None
        except Exception as e:
            print(f"❌ Error: {e}")
            return None
    
    def get_ai_response(self, user_input: str) -> str:
        """Get AI response (simulated for now)"""
        # TODO: Replace with actual AI API call
        # For now, provide spiritual responses
        
        spiritual_responses = {
            "hello": "Hello! May God's peace be with you today. How can I help you on your spiritual journey?",
            "how are you": "I'm doing well, thank you for asking. I'm here to support you in your faith and spiritual growth.",
            "prayer": "Prayer is a beautiful way to connect with God. Remember, He always listens with love and understanding.",
            "bible": "The Bible is God's living word, full of wisdom and guidance for our daily lives. What specific passage or topic interests you?",
            "faith": "Faith is a gift from God that grows stronger through trust, prayer, and experiencing His love in our lives.",
            "love": "God's love is unconditional and everlasting. He loves you more than you can imagine, just as you are.",
            "peace": "Peace comes from knowing that God is in control and that He works all things for good for those who love Him.",
            "hope": "Hope in Christ is an anchor for our souls. Even in difficult times, we can trust in His promises and love.",
            "help": "I'm here to help you! Whether you need spiritual guidance, prayer support, or just someone to talk to about your faith.",
            "thank you": "You're very welcome! It's a blessing to be able to help you on your spiritual journey. God bless you!"
        }
        
        # Find best matching response
        user_lower = user_input.lower()
        for key, response in spiritual_responses.items():
            if key in user_lower:
                return response
        
        # Default spiritual response
        return "Thank you for sharing that with me. Remember that God loves you and is always with you. Is there anything specific about your faith journey I can help you with?"
    
    def speak_response(self, text: str):
        """Convert text to speech and play it"""
        if not os.path.exists(self.voice_file):
            print("❌ Ryan voice not found!")
            return False
        
        try:
            # Create temp file for text
            with open("temp_response.txt", "w") as f:
                f.write(text)
            
            output_file = "spiritual_response.wav"
            
            # Generate speech
            subprocess.run([
                'piper', '--model', self.voice_file,
                '--output_file', output_file,
                '--input_file', 'temp_response.txt'
            ], check=True)
            
            # Play the response
            print("🔊 Speaking response...")
            subprocess.run(['aplay', output_file], check=True)
            
            # Clean up
            os.remove("temp_response.txt")
            os.remove(output_file)
            
            return True
            
        except Exception as e:
            print(f"❌ Error speaking response: {e}")
            return False
    
    def process_with_loading(self, process_func, *args, **kwargs):
        """Process with loading sound and indicator"""
        return self.loading_system.process_with_loading(process_func, *args, **kwargs)
    
    def run_conversation(self):
        """Run a complete conversation with loading sounds"""
        print("\n🙏 Spiritual Assistant Conversation")
        print("=" * 40)
        print("💡 Try saying: hello, prayer, bible, faith, love, peace, hope, help, thank you")
        print("🛑 Say 'goodbye' to exit")
        print("-" * 40)
        
        while True:
            # Listen for input
            user_input = self.listen_for_input()
            
            if user_input is None:
                continue
            
            if user_input.lower() in ['goodbye', 'exit', 'quit', 'stop']:
                self.speak_response("Goodbye! May God bless you and keep you. Peace be with you.")
                break
            
            # Process with loading sound
            print(f"\n🔄 Processing: '{user_input}'")
            
            # Get AI response with loading
            ai_response = self.process_with_loading(
                self.get_ai_response, 
                user_input
            )
            
            if ai_response:
                print(f"🤖 AI Response: {ai_response}")
                
                # Speak response with loading
                self.process_with_loading(
                    self.speak_response,
                    ai_response
                )
            
            print("\n" + "-" * 40)
    
    def test_systems(self):
        """Test all systems"""
        print("🧪 Testing Spiritual Assistant Systems")
        print("=" * 40)
        
        # Test loading sounds
        print("\n🎵 Testing loading sounds...")
        self.loading_system.list_available_sounds()
        
        # Test voice input
        print("\n🎤 Testing voice input...")
        test_input = self.listen_for_input()
        if test_input:
            print(f"✅ Voice input works: '{test_input}'")
        else:
            print("❌ Voice input failed")
        
        # Test AI response
        print("\n🤖 Testing AI response...")
        test_response = self.get_ai_response("hello")
        print(f"✅ AI response: '{test_response}'")
        
        # Test voice output
        print("\n🔊 Testing voice output...")
        if self.speak_response("Hello! This is a test of the spiritual assistant voice system."):
            print("✅ Voice output works!")
        else:
            print("❌ Voice output failed")
        
        print("\n✅ System test completed!")

def main():
    """Main function"""
    print("🙏 Spiritual Assistant with Loading Sounds")
    print("=" * 50)
    
    assistant = SpiritualAssistant()
    
    print("\n🎯 What would you like to do?")
    print("1. Run conversation mode")
    print("2. Test all systems")
    print("3. Test loading sounds only")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == "1":
        assistant.run_conversation()
    elif choice == "2":
        assistant.test_systems()
    elif choice == "3":
        assistant.loading_system.test_loading_sounds()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main() 