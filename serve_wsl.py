#!/usr/bin/env python3
"""
MkDocs development server for WSL2 environments.
Uses aggressive polling with manual rebuild triggers.
"""
import os
import sys
import time
import hashlib
import subprocess
import threading
from pathlib import Path

def get_dir_hash(directory):
    """Get combined hash of all files in directory."""
    hash_md5 = hashlib.md5()
    
    for root, dirs, files in sorted(os.walk(directory)):
        # Skip hidden directories and site directory
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'site']
        
        for file in sorted(files):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'rb') as f:
                    hash_md5.update(f.read())
            except:
                pass
    
    return hash_md5.hexdigest()

def watch_and_rebuild():
    """Watch for changes and rebuild."""
    print("🔍 WSL2 File Watcher Active")
    print("📁 Watching: docs/ and mkdocs.yml")
    print("⏱️  Check interval: 0.5 seconds (aggressive)")
    print("")
    
    last_docs_hash = get_dir_hash('docs')
    last_config_hash = hashlib.md5(open('mkdocs.yml', 'rb').read()).hexdigest() if os.path.exists('mkdocs.yml') else None
    
    while True:
        time.sleep(0.5)  # Check every 500ms
        
        # Check docs directory
        current_docs_hash = get_dir_hash('docs')
        current_config_hash = hashlib.md5(open('mkdocs.yml', 'rb').read()).hexdigest() if os.path.exists('mkdocs.yml') else None
        
        if current_docs_hash != last_docs_hash or current_config_hash != last_config_hash:
            print(f"\n📝 [{time.strftime('%H:%M:%S')}] Changes detected! Rebuilding...")
            
            # Rebuild
            result = subprocess.run(
                [sys.executable, '-m', 'mkdocs', 'build', '--dirty'],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print(f"✅ [{time.strftime('%H:%M:%S')}] Build successful!")
            else:
                print(f"❌ [{time.strftime('%H:%M:%S')}] Build failed:")
                print(result.stderr)
            
            last_docs_hash = current_docs_hash
            last_config_hash = current_config_hash

def main():
    """Start server and watcher."""
    print("🚀 Starting MkDocs server for WSL2...")
    print("")
    
    # Start mkdocs serve in a separate process (without live reload)
    server_process = subprocess.Popen(
        [sys.executable, '-m', 'mkdocs', 'serve', '--no-livereload', '--dev-addr', '127.0.0.1:8000'],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    
    # Give server time to start
    time.sleep(2)
    
    print("🌐 Server running at: http://127.0.0.1:8000/mkdocs-catppuccin/")
    print("💡 Manually refresh browser (F5) after seeing 'Build successful!'")
    print("⚠️  This is a WSL2 workaround - file watching doesn't work natively")
    print("")
    
    # Start watcher in a thread
    watcher_thread = threading.Thread(target=watch_and_rebuild, daemon=True)
    watcher_thread.start()
    
    try:
        # Keep main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n👋 Shutting down...")
        server_process.terminate()
        server_process.wait()
        print("✅ Server stopped")

if __name__ == '__main__':
    main()
