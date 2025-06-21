class Launcher:
    def launchAPI():
        import subprocess
        script_to_run = "API.py"
        command = f'cd app/backend && python {script_to_run}'
        subprocess.Popen(['start', 'cmd', '/k', command], shell=True)
        print("API Launched \n\n")
    
    def launchWebApp():
        import http.server
        import socketserver
        import webbrowser

        PORT = 8000
        webbrowser.open(f"http://localhost:{PORT}/app/Frontend/WebHMD.html")

        Handler = http.server.SimpleHTTPRequestHandler

        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print(f"Serving at http://localhost:{PORT}/app/Frontend/WebHMD.html")
            httpd.serve_forever()

    def launch():
        Launcher.launchAPI()
        Launcher.launchWebApp()
        

