import json, os
from google.oauth2 import service_account
from googleapiclient.discovery import build

CONFIG_FILE = "config.json"
OUTPUT_DIR = "data/forms"
KEY_FILE = "service-account-key.json"
SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets.readonly",
    "https://www.googleapis.com/auth/drive.readonly"
]

def get_service(api, version):
    creds = service_account.Credentials.from_service_account_file(KEY_FILE, scopes=SCOPES)
    return build(api, version, credentials=creds)

def get_sheet_id(drive_service, form_title):
    results = drive_service.files().list(
        q=f"name='{form_title}' and mimeType='application/vnd.google-apps.spreadsheet'",
        fields="files(id, name)"
    ).execute()
    files = results.get("files", [])
    if not files:
        return None
    return files[0]["id"]

def fetch_responses(sheets_service, sheet_id):
    result = sheets_service.spreadsheets().values().get(
        spreadsheetId=sheet_id,
        range="A:Z"
    ).execute()
    rows = result.get("values", [])
    if not rows:
        return []
    headers = rows[0]
    return [dict(zip(headers, row)) for row in rows[1:]]

def save(data, filename):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"  Saved {len(data)} rows to {path}")

def main():
    with open(CONFIG_FILE) as f:
        config = json.load(f)

    forms = config.get("google_forms", [])
    if not forms:
        print("No forms configured.")
        print("Add to config.json:")
        print('  "google_forms": [')
        print('    {"title": "Contact Form Responses", "output": "contact_leads.json"},')
        print('    {"title": "Enquiry Form Responses", "output": "enquiry_leads.json"}')
        print('  ]')
        return

    print("Fetching Google Forms data...")
    drive_service = get_service("drive", "v3")
    sheets_service = get_service("sheets", "v4")

    all_leads = []
    for form in forms:
        title = form.get("title", "")
        output = form.get("output", "leads.json")
        print(f"  Looking for: {title}")
        sheet_id = get_sheet_id(drive_service, title)
        if not sheet_id:
            print(f"  Not found: {title}")
            print(f"  Make sure the sheet is shared with the service account email")
            continue
        responses = fetch_responses(sheets_service, sheet_id)
        save(responses, output)
        all_leads.extend(responses)

    if all_leads:
        save(all_leads, "all_leads.json")
        print(f"Forms fetch complete. {len(all_leads)} total responses.")
    else:
        print("No responses found.")

if __name__ == "__main__":
    main()
