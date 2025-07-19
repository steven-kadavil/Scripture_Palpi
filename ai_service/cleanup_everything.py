#!/usr/bin/env python3
import subprocess
import sys
import os
import shutil

def uninstall_coqui_packages():
    """Uninstall Coqui TTS and all related packages"""
    
    print("🧹 Uninstalling Coqui TTS packages...")
    
    # All packages that were installed for Coqui TTS
    packages_to_remove = [
        "TTS",
        "torch",
        "torchaudio", 
        "transformers",
        "spacy",
        "librosa",
        "scikit-learn",
        "numba",
        "scipy",
        "matplotlib",
        "pandas",
        "umap-learn",
        "einops",
        "encodec",
        "gruut",
        "nltk",
        "jieba",
        "pypinyin",
        "hangul_romanize",
        "jamo",
        "g2pkk",
        "bangla",
        "bnnumerizer",
        "bnunicodenormalizer",
        "unidecode",
        "num2words",
        "Babel",
        "dateparser",
        "gruut-ipa",
        "gruut-lang-en",
        "gruut-lang-de", 
        "gruut-lang-es",
        "gruut-lang-fr",
        "jsonlines",
        "networkx",
        "python-crfsuite",
        "aiohttp",
        "aiohappyeyeballs",
        "aiosignal",
        "attrs",
        "frozenlist",
        "multidict",
        "propcache",
        "yarl",
        "more_itertools",
        "typeguard",
        "audioread",
        "joblib",
        "decorator",
        "pooch",
        "soxr",
        "lazy_loader",
        "msgpack",
        "contourpy",
        "cycler",
        "fonttools",
        "kiwisolver",
        "pillow",
        "pyparsing",
        "python-dateutil",
        "docopt",
        "llvmlite",
        "pytz",
        "threadpoolctl",
        "cffi",
        "spacy-legacy",
        "spacy-loggers",
        "murmurhash",
        "cymem",
        "preshed",
        "thinc",
        "wasabi",
        "srsly",
        "sudachipy",
        "sudachidict_core",
        "sudachidict_full"
    ]
    
    print(f"📦 Attempting to uninstall {len(packages_to_remove)} packages...")
    
    for package in packages_to_remove:
        try:
            print(f"🗑️  Uninstalling {package}...")
            subprocess.run([sys.executable, '-m', 'pip', 'uninstall', '-y', package], 
                         capture_output=True, text=True)
        except Exception as e:
            print(f"⚠️  Could not uninstall {package}: {e}")
    
    print("✅ Package cleanup completed!")

def uninstall_rust():
    """Uninstall Rust compiler"""
    
    print("🦀 Uninstalling Rust...")
    
    try:
        # Check if rustup exists
        rustup_path = os.path.expanduser("~/.cargo/bin/rustup")
        if os.path.exists(rustup_path):
            # Uninstall Rust
            subprocess.run([rustup_path, "self", "uninstall", "-y"], check=True)
            print("✅ Rust uninstalled successfully!")
        else:
            print("⚠️  Rust not found, skipping...")
            
    except subprocess.CalledProcessError as e:
        print(f"❌ Error uninstalling Rust: {e}")

def remove_rust_directories():
    """Remove Rust directories manually"""
    
    print("🗂️  Removing Rust directories...")
    
    directories_to_remove = [
        os.path.expanduser("~/.cargo"),
        os.path.expanduser("~/.rustup")
    ]
    
    for directory in directories_to_remove:
        if os.path.exists(directory):
            try:
                shutil.rmtree(directory)
                print(f"✅ Removed {directory}")
            except Exception as e:
                print(f"❌ Could not remove {directory}: {e}")
        else:
            print(f"⚠️  {directory} not found, skipping...")

def clean_pip_cache():
    """Clean pip cache to free up space"""
    
    print("🧹 Cleaning pip cache...")
    
    try:
        subprocess.run([sys.executable, '-m', 'pip', 'cache', 'purge'], check=True)
        print("✅ Pip cache cleaned!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error cleaning cache: {e}")

def check_space_saved():
    """Check how much space was freed"""
    
    print("\n📊 Checking disk space...")
    
    try:
        result = subprocess.run(['df', '-h', '/'], capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"❌ Error checking disk space: {e}")

def main():
    print("🧹 Complete Coqui TTS & Rust Cleanup")
    print("=" * 50)
    
    print("This will remove:")
    print("• Coqui TTS and all dependencies (~200MB)")
    print("• Rust compiler and tools (~458MB)")
    print("• All related Python packages")
    print("• Pip cache")
    
    print(f"\nTotal space to be freed: ~658MB+")
    
    confirm = input("\nAre you sure you want to proceed? (y/N): ")
    
    if confirm.lower() != 'y':
        print("Cleanup cancelled.")
        return
    
    # Step 1: Uninstall Python packages
    uninstall_coqui_packages()
    
    # Step 2: Uninstall Rust
    uninstall_rust()
    
    # Step 3: Remove Rust directories
    remove_rust_directories()
    
    # Step 4: Clean cache
    clean_pip_cache()
    
    # Step 5: Check space saved
    check_space_saved()
    
    print("\n✅ Complete cleanup finished!")
    print("🎯 You now have a clean system with just Piper TTS and Google TTS.")
    print("🚀 Your spiritual assistant will be fast and efficient!")

if __name__ == "__main__":
    main() 