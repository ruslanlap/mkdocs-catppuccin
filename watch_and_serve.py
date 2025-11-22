#!/usr/bin/env python3
"""
MkDocs live reload with polling for VM environments.
This script uses polling instead of inotify to detect file changes.
"""
import os
import sys
import time
import hashlib
from pathlib import Path

def get_file_hash(filepath):
    """Get MD5 hash of a file."""
    try:
        with open(filepath, 'rb') as f:
            return hashlib.md5(f.read()).hexdigest()
    except:
        return None

def watch_and_rebuild(docs_dir='docs', config_file='mkdocs.yml', interval=1):
    """Watch files and rebuild when changes detected."""
    print(f"🔍 Watching {docs_dir}/ and {config_file} for changes...")
    print(f"⏱️  Polling interval: {interval} second(s)")
    print(f"🌐 Server: http://127.0.0.1:8000/mkdocs-catppuccin/")
    print(f"💡 Press Ctrl+C to stop\n")
    
    # Track file hashes
    file_hashes = {}
    
    def scan_files():
        """Scan all files and return their hashes."""
        hashes = {}
        
        # Watch config file
        if os.path.exists(config_file):
            hashes[config_file] = get_file_hash(config_file)
        
        # Watch all files in docs directory
        if os.path.exists(docs_dir):
            for root, dirs, files in os.walk(docs_dir):
                for file in files:
                    filepath = os.path.join(root, file)
                    hashes[filepath] = get_file_hash(filepath)
        
        return hashes
    
    # Initial scan
    file_hashes = scan_files()
    
    # Start mkdocs serve with polling observer
    import subprocess
    
    # Set environment variable to force polling
    env = os.environ.copy()
    env['PYTHONPATH'] = os.path.dirname(os.path.abspath(__file__))
    
    mkdocs_process = subprocess.Popen(
        [sys.executable, '-c', '''
import sys
import os

# Force polling observer before importing mkdocs
import watchdog.observers
from watchdog.observers import polling
watchdog.observers.Observer = polling.PollingObserver

# Now import and run mkdocs
from mkdocs.__main__ import cli

if __name__ == "__main__":
    sys.argv = ["mkdocs", "serve"]
    cli()
'''],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
        env=env
    )
    
    # Give server time to start
    time.sleep(2)
    
    try:
        while True:
            time.sleep(interval)
            
            # Scan for changes
            current_hashes = scan_files()
            
            # Check for changes
            changed_files = []
            for filepath, current_hash in current_hashes.items():
                old_hash = file_hashes.get(filepath)
                if old_hash != current_hash:
                    changed_files.append(filepath)
            
            # Check for deleted files
            for filepath in file_hashes:
                if filepath not in current_hashes:
                    changed_files.append(filepath + " (deleted)")
            
            if changed_files:
                print(f"\n📝 Changes detected:")
                for f in changed_files:
                    print(f"   - {f}")
                
                print("🔄 Rebuilding documentation...")
                
                # Rebuild
                result = subprocess.run(
                    [sys.executable, '-m', 'mkdocs', 'build', '--dirty'],
                    capture_output=True,
                    text=True
                )
                
                if result.returncode == 0:
                    print("✅ Build successful!")
                else:
                    print(f"❌ Build failed:\n{result.stderr}")
                
                # Update hashes
                file_hashes = current_hashes
                
    except KeyboardInterrupt:
        print("\n\n👋 Stopping server...")
        mkdocs_process.terminate()
        mkdocs_process.wait()
        print("✅ Server stopped")

if __name__ == '__main__':
    watch_and_rebuild()
