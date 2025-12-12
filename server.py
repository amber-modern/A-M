#!/usr/bin/env python3
"""
Simple HTTP server for the static Squarespace export.
Serves files with proper MIME types and handles common routes.
"""

import http.server
import socketserver
import os
import mimetypes
from pathlib import Path

PORT = 8001

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom request handler with better MIME types and routing."""
    
    def end_headers(self):
        # Add CORS headers if needed
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def guess_type(self, path):
        """Override to provide better MIME type detection."""
        # Ensure common file types are served correctly
        if path.endswith('.js'):
            return 'application/javascript'
        elif path.endswith('.css'):
            return 'text/css'
        elif path.endswith('.json'):
            return 'application/json'
        elif path.endswith('.svg'):
            return 'image/svg+xml'
        
        # Use mimetypes module directly for compatibility
        mimetype, _ = mimetypes.guess_type(path)
        return mimetype if mimetype else 'application/octet-stream'
    
    def translate_path(self, path):
        """Handle routing - serve index.html for root."""
        # Remove query string
        path = path.split('?')[0]
        
        # Remove fragment
        path = path.split('#')[0]
        
        # Default to index.html for root
        if path == '/' or path == '':
            path = '/index.html'
        
        # Remove leading slash for file system access
        if path.startswith('/'):
            path = path[1:]
        
        return path

def main():
    """Start the server."""
    os.chdir(Path(__file__).parent)
    
    Handler = CustomHTTPRequestHandler
    
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Server running at http://localhost:{PORT}/")
        print(f"Serving directory: {os.getcwd()}")
        print("\nPress Ctrl+C to stop the server")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\nServer stopped.")

if __name__ == '__main__':
    main()

