import json, os, webbrowser, requests
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse

auth_code = None

class OAuthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global auth_code
        params = parse_qs(urlparse(self.path).query)
        if "code" in params:
            auth_code = params["code"][0]
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Authorization successful. Close this tab.")
    def log_message(self, format, *args):
        pass

def main():
    print("Google Ads OAuth Setup")
    oauth_path = input("Path to OAuth JSON file: ").strip()
    with open(oauth_path) as f:
        data = json.load(f)
    creds = data.get("installed") or data.get("web")
    client_id = creds["client_id"]
    client_secret = creds["client_secret"]
    developer_token = input("Developer token: ").strip()
    customer_id = input("Customer ID: ").strip()
    login_customer_id = input("MCC ID (blank if none): ").strip()
    auth_url = (f"https://accounts.google.com/o/oauth2/v2/auth"
                f"?client_id={client_id}&redirect_uri=http://localhost:8080"
                f"&response_type=code&scope=https://www.googleapis.com/auth/adwords"
                f"&access_type=offline&prompt=consent")
    webbrowser.open(auth_url)
    HTTPServer(("localhost", 8080), OAuthHandler).handle_request()
    if not auth_code:
        print("Authorization failed.")
        return
    tokens = requests.post("https://oauth2.googleapis.com/token", data={
        "code": auth_code, "client_id": client_id,
        "client_secret": client_secret,
        "redirect_uri": "http://localhost:8080",
        "grant_type": "authorization_code"
    }).json()
    if "refresh_token" not in tokens:
        print(f"Failed: {tokens}")
        return
    lines = [f"developer_token: {developer_token}",
             f"client_id: {client_id}",
             f"client_secret: {client_secret}",
             f"refresh_token: {tokens['refresh_token']}",
             "use_proto_plus: True"]
    if login_customer_id:
        lines.append(f"login_customer_id: {login_customer_id}")
    open("google-ads.yaml", "w").write("\n".join(lines))
    print("google-ads.yaml created.")

if __name__ == "__main__":
    main()
