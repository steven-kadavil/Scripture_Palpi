#!/usr/bin/env python3
import os
import subprocess
import glob

def find_voice_files():
    """Find all voice model files that were downloaded"""
    
    print("🔍 Searching for voice model files...")
    
    # Common locations and patterns for voice files
    search_patterns = [
        "*.onnx",           # Piper voice models
        "*.onnx.json",      # Piper config files
        "*.wav",            # Generated audio files
        "*.mp3",            # Generated audio files
        "*.flac",           # Audio files
        "*.pth",            # PyTorch models
        "*.pt",             # PyTorch models
        "*.bin",            # Model files
        "*.model",          # Model files
        "*.ckpt",           # Checkpoint files
        "*.safetensors",    # Safe tensor files
    ]
    
    voice_files = []
    total_size = 0
    
    # Search in current directory and common locations
    search_dirs = [
        ".",                                    # Current directory
        os.path.expanduser("~"),                # Home directory
        os.path.expanduser("~/Scripture_Palpi"), # Project directory
        "/tmp",                                 # Temp directory
    ]
    
    for search_dir in search_dirs:
        if os.path.exists(search_dir):
            for pattern in search_patterns:
                files = glob.glob(os.path.join(search_dir, pattern))
                for file_path in files:
                    if os.path.isfile(file_path):
                        file_size = os.path.getsize(file_path)
                        voice_files.append((file_path, file_size))
                        total_size += file_size
    
    return voice_files, total_size

def remove_voice_files(voice_files):
    """Remove the voice model files"""
    
    print(f"🗑️  Removing {len(voice_files)} voice files...")
    
    removed_size = 0
    removed_count = 0
    
    for file_path, file_size in voice_files:
        try:
            os.remove(file_path)
            removed_size += file_size
            removed_count += 1
            print(f"✅ Removed: {file_path} ({file_size / (1024*1024):.1f} MB)")
        except Exception as e:
            print(f"❌ Could not remove {file_path}: {e}")
    
    return removed_count, removed_size

def check_disk_space():
    """Check current disk space"""
    
    print("\n📊 Current disk space:")
    
    try:
        result = subprocess.run(['df', '-h', '/'], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error checking disk space: {e}")

def main():
    print("🗑️  Voice Model File Cleanup")
    print("=" * 40)
    
    # Find voice files
    voice_files, total_size = find_voice_files()
    
    if not voice_files:
        print("✅ No voice model files found!")
        return
    
    print(f"\n📁 Found {len(voice_files)} voice files:")
    print(f"📊 Total size: {total_size / (1024*1024):.1f} MB")
    print("-" * 40)
    
    # Show the largest files
    voice_files.sort(key=lambda x: x[1], reverse=True)
    for i, (file_path, file_size) in enumerate(voice_files[:10]):  # Show top 10
        print(f"{i+1}. {file_path} ({file_size / (1024*1024):.1f} MB)")
    
    if len(voice_files) > 10:
        print(f"... and {len(voice_files) - 10} more files")
    
    print(f"\n🗑️  This will remove {total_size / (1024*1024):.1f} MB of voice files")
    
    confirm = input("\nRemove these voice files? (y/N): ")
    
    if confirm.lower() != 'y':
        print("Cleanup cancelled.")
        return
    
    # Remove the files
    removed_count, removed_size = remove_voice_files(voice_files)
    
    print(f"\n✅ Removed {removed_count} files")
    print(f"📊 Freed up {removed_size / (1024*1024):.1f} MB")
    
    # Check disk space after cleanup
    check_disk_space()
    
    print("\n🎯 Voice file cleanup completed!")
    print("🚀 Your system is now clean and ready for your spiritual assistant!")

if __name__ == "__main__":
    main() 