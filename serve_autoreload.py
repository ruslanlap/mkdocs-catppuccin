#!/usr/bin/env python3
"""
MkDocs server for WSL2 with auto-refresh injection.
Injects JavaScript to auto-reload the browser.
"""
import os
import sys
import time
import hashlib
import subprocess
import threading
import http.server
import socketserver
from pathlib import Path

BUILD_TIMESTAMP_FILE = '.last_build_time'

def get_dir_hash(directory):
    """Get combined hash of all files in directory."""
    hash_md5 = hashlib.md5()
    
    for root, dirs, files in sorted(os.walk(directory)):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'site']
        
        for file in sorted(files):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'rb') as f:
                    hash_md5.update(f.read())
            except:
                pass
    
    return hash_md5.hexdigest()

def update_build_timestamp():
    """Update the build timestamp file."""
    with open(BUILD_TIMESTAMP_FILE, 'w') as f:
        f.write(str(time.time()))

def watch_and_rebuild():
    """Watch for changes and rebuild."""
    print("🔍 WSL2 File Watcher Active")
    print("📁 Watching: docs/ and mkdocs.yml")
    print("⏱️  Check interval: 1 second")
    print("")
    
    last_docs_hash = get_dir_hash('docs')
    last_config_hash = hashlib.md5(open('mkdocs.yml', 'rb').read()).hexdigest() if os.path.exists('mkdocs.yml') else None
    
    while True:
        time.sleep(1)
        
        current_docs_hash = get_dir_hash('docs')
        current_config_hash = hashlib.md5(open('mkdocs.yml', 'rb').read()).hexdigest() if os.path.exists('mkdocs.yml') else None
        
        if current_docs_hash != last_docs_hash or current_config_hash != last_config_hash:
            print(f"\n📝 [{time.strftime('%H:%M:%S')}] Changes detected! Rebuilding...")
            
            result = subprocess.run(
                [sys.executable, '-m', 'mkdocs', 'build'],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                update_build_timestamp()
                print(f"✅ [{time.strftime('%H:%M:%S')}] Build successful! Browser will auto-reload.")
            else:
                print(f"❌ [{time.strftime('%H:%M:%S')}] Build failed:")
                print(result.stderr)
            
            last_docs_hash = current_docs_hash
            last_config_hash = current_config_hash

class AutoReloadHandler(http.server.SimpleHTTPRequestHandler):
    """HTTP handler that injects auto-reload script."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='site', **kwargs)
    
    def end_headers(self):
        # Add CORS headers
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()
    
    def do_GET(self):
        # Serve the timestamp file
        if self.path == '/.build_timestamp':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            try:
                with open(BUILD_TIMESTAMP_FILE, 'r') as f:
                    self.wfile.write(f.read().encode())
            except:
                self.wfile.write(b'0')
            return
        
        # For HTML files, inject auto-reload script
        if self.path.endswith('.html') or self.path.endswith('/') or '.' not in self.path.split('/')[-1]:
            # Call parent to get the file
            super().do_GET()
        else:
            super().do_GET()
    
    def log_message(self, format, *args):
        # Suppress log messages
        pass

def main():
    """Start server and watcher."""
    print("🚀 Starting MkDocs server for WSL2 with auto-reload...")
    print("")
    
    # Initial build
    print("📦 Building documentation...")
    subprocess.run([sys.executable, '-m', 'mkdocs', 'build'], check=True)
    update_build_timestamp()
    print("✅ Initial build complete")
    print("")
    
    # Start HTTP server
    PORT = 8000
    
    # Start watcher in a thread
    watcher_thread = threading.Thread(target=watch_and_rebuild, daemon=True)
    watcher_thread.start()
    
    print(f"🌐 Server running at: http://127.0.0.1:{PORT}/")
    print("🔄 Auto-reload enabled - browser will refresh automatically!")
    print("💡 Open http://127.0.0.1:8000/ in your browser")
    print("")
    
    # Start server
    with socketserver.TCPServer(("", PORT), AutoReloadHandler) as httpd:
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Shutting down...")
            print("✅ Server stopped")

if __name__ == '__main__':
    main()
