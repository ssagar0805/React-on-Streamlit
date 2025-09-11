#!/usr/bin/env python3
"""
Simple HTTP server to serve React assets with correct MIME types
This solves the MIME type issue when embedding React components in Streamlit
"""

import http.server
import socketserver
import os
from pathlib import Path
import threading
import time

class ReactAssetsHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler that serves React assets with correct MIME types"""
    
    def __init__(self, *args, **kwargs):
        # Set the directory to serve from
        self.assets_dir = Path(__file__).parent / "tl_frontend" / "frontend" / "dist"
        super().__init__(*args, directory=str(self.assets_dir), **kwargs)
    
    def end_headers(self):
        # Set CORS headers to allow embedding in Streamlit
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        
        # Set correct MIME types based on file extension
        if self.path.endswith('.js'):
            self.send_header('Content-Type', 'application/javascript; charset=utf-8')
        elif self.path.endswith('.mjs'):
            self.send_header('Content-Type', 'application/javascript; charset=utf-8')
        elif self.path.endswith('.css'):
            self.send_header('Content-Type', 'text/css; charset=utf-8')
        elif self.path.endswith('.html'):
            self.send_header('Content-Type', 'text/html; charset=utf-8')
        elif self.path.endswith('.json'):
            self.send_header('Content-Type', 'application/json; charset=utf-8')
        
        super().end_headers()

def start_assets_server(port=8081):
    """Start the assets server in a background thread"""
    def run_server():
        try:
            with socketserver.TCPServer(("0.0.0.0", port), ReactAssetsHandler) as httpd:
                print(f"Assets server running on http://0.0.0.0:{port}")
                httpd.serve_forever()
        except Exception as e:
            print(f"Error starting assets server: {e}")
    
    # Run server in background thread
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()
    time.sleep(2)  # Give server time to start
    return server_thread

if __name__ == "__main__":
    # For standalone testing
    start_assets_server(8081)
    print("Assets server started. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopping assets server...")