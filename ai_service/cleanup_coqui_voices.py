#!/usr/bin/env python3
import os
import subprocess
import shutil

def find_coqui_voice_models():
    """Find Coqui TTS voice models that were downloaded"""
    
    print("🔍 Searching for Coqui TTS voice models...")
    
    # Common locations where Coqui TTS stores models
    coqui_dirs = [
        os.path.expanduser("~/.local/share/tts"),
        os.path.expanduser("~/.cache/tts"),
        os.path.expanduser("~/tts_models"),
        os.path.expanduser("~/.tts"),
        "/tmp/tts",
        "/tmp/coqui_tts"
    ]
    
    found_models = []
    total_size = 0
    
    for model_dir in coqui_dirs:
        if os.path.exists(model_dir):
            print(f"📁 Found Coqui directory: {model_dir}")
            
            # Calculate size of the directory
            try:
                dir_size = 0
                file_count = 0
                
                for root, dirs, files in os.walk(model_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        try:
                            file_size = os.path.getsize(file_path)
                            dir_size += file_size
                            file_count += 1
                        except:
                            pass
                
                if dir_size > 0:
                    found_models.append((model_dir, dir_size, file_count))
                    total_size += dir_size
                    print(f"   📊 Size: {dir_size / (1024*1024):.1f} MB ({file_count} files)")
                    
            except Exception as e:
                print(f"   ❌ Error checking {model_dir}: {e}")
    
    return found_models, total_size

def remove_coqui_models(found_models):
    """Remove Coqui TTS voice models"""
    
    print(f"🗑️  Removing {len(found_models)} Coqui TTS directories...")
    
    removed_size = 0
    removed_count = 0
    
    for model_dir, dir_size, file_count in found_models:
        try:
            shutil.rmtree(model_dir)
            removed_size += dir_size
            removed_count += 1
            print(f"✅ Removed: {model_dir} ({dir_size / (1024*1024):.1f} MB)")
        except Exception as e:
            print(f"❌ Could not remove {model_dir}: {e}")
    
    return removed_count, removed_size

def find_large_voice_files():
    """Find any large voice-related files"""
    
    print("\n🔍 Searching for large voice files...")
    
    # Search for large files that might be voice models
    large_files = []
    
    search_dirs = [
        os.path.expanduser("~"),
        os.path.expanduser("~/Scripture_Palpi"),
        "/tmp"
    ]
    
    for search_dir in search_dirs:
        if os.path.exists(search_dir):
            try:
                for root, dirs, files in os.walk(search_dir):
                    for file in files:
                        file_path = os.path.join(root, file)
                        try:
                            file_size = os.path.getsize(file_path)
                            # Look for files larger than 10MB
                            if file_size > 10 * 1024 * 1024:  # 10MB
                                # Check if it's likely a voice model
                                if any(ext in file.lower() for ext in ['.pth', '.pt', '.onnx', '.bin', '.model', '.ckpt']):
                                    large_files.append((file_path, file_size))
                        except:
                            pass
            except:
                pass
    
    return large_files

def main():
    print("🗑️  Coqui TTS Voice Model Cleanup")
    print("=" * 40)
    
    # Find Coqui TTS models
    found_models, total_size = find_coqui_voice_models()
    
    if not found_models:
        print("✅ No Coqui TTS voice models found!")
    else:
        print(f"\n📁 Found {len(found_models)} Coqui TTS directories:")
        print(f"📊 Total size: {total_size / (1024*1024):.1f} MB")
        
        confirm = input(f"\nRemove these Coqui TTS voice models? (y/N): ")
        
        if confirm.lower() == 'y':
            removed_count, removed_size = remove_coqui_models(found_models)
            print(f"\n✅ Removed {removed_count} directories")
            print(f"📊 Freed up {removed_size / (1024*1024):.1f} MB")
    
    # Find other large voice files
    large_files = find_large_voice_files()
    
    if large_files:
        print(f"\n📁 Found {len(large_files)} large voice files:")
        large_files.sort(key=lambda x: x[1], reverse=True)
        
        for i, (file_path, file_size) in enumerate(large_files[:10]):
            print(f"{i+1}. {file_path} ({file_size / (1024*1024):.1f} MB)")
        
        if len(large_files) > 10:
            print(f"... and {len(large_files) - 10} more files")
        
        total_large_size = sum(size for _, size in large_files)
        print(f"\n📊 Total large files size: {total_large_size / (1024*1024):.1f} MB")
        
        confirm = input(f"\nRemove these large voice files? (y/N): ")
        
        if confirm.lower() == 'y':
            removed_count = 0
            removed_size = 0
            
            for file_path, file_size in large_files:
                try:
                    os.remove(file_path)
                    removed_count += 1
                    removed_size += file_size
                    print(f"✅ Removed: {file_path} ({file_size / (1024*1024):.1f} MB)")
                except Exception as e:
                    print(f"❌ Could not remove {file_path}: {e}")
            
            print(f"\n✅ Removed {removed_count} files")
            print(f"📊 Freed up {removed_size / (1024*1024):.1f} MB")
    
    # Check disk space
    print("\n📊 Current disk space:")
    try:
        result = subprocess.run(['df', '-h', '/'], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error checking disk space: {e}")
    
    print("\n🎯 Coqui TTS voice model cleanup completed!")

if __name__ == "__main__":
    main() 