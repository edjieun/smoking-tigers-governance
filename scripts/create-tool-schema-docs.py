#!/usr/bin/env python3
"""
Create 5 Google Docs from tool schema markdown files and set sharing to "anyone with link can view".
"""

import json
import os
import sys
from pathlib import Path

# Install dependencies if needed
try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "google-api-python-client", "google-auth", "--quiet"])
    from google.oauth2 import service_account
    from googleapiclient.discovery import build

CREDENTIALS_FILE = os.path.expanduser("~/.openclaw/credentials/google-service-account.json")
FOLDER_ID = "1xXxfiMp_RLRQOXp0j7N2JO3B5P71MBk1"

SCOPES = [
    "https://www.googleapis.com/auth/drive",
    "https://www.googleapis.com/auth/documents",
]

DOCS_BASE = os.path.expanduser("~/.openclaw/workspace/docs")

SCHEMA_DOCS = [
    {
        "title": "STM Tool Schema: GitHub",
        "file": "tool-schema-github.md",
    },
    {
        "title": "STM Tool Schema: Notion",
        "file": "tool-schema-notion.md",
    },
    {
        "title": "STM Tool Schema: Discord",
        "file": "tool-schema-discord.md",
    },
    {
        "title": "STM Tool Schema: Mattermost",
        "file": "tool-schema-mattermost.md",
    },
    {
        "title": "STM Tool Schema: OpenClaw",
        "file": "tool-schema-openclaw.md",
    },
]


def get_services():
    creds = service_account.Credentials.from_service_account_file(
        CREDENTIALS_FILE, scopes=SCOPES
    )
    drive_service = build("drive", "v3", credentials=creds)
    docs_service = build("docs", "v1", credentials=creds)
    return drive_service, docs_service


def create_doc(drive_service, docs_service, title, content):
    """Create a Google Doc in the target folder with the given content."""
    # Create empty doc in the folder
    file_metadata = {
        "name": title,
        "mimeType": "application/vnd.google-apps.document",
        "parents": [FOLDER_ID],
    }
    file = drive_service.files().create(
        body=file_metadata,
        fields="id,webViewLink",
        supportsAllDrives=True,
    ).execute()

    doc_id = file["id"]
    doc_url = file["webViewLink"]

    # Insert content into the doc
    requests = [
        {
            "insertText": {
                "location": {"index": 1},
                "text": content,
            }
        }
    ]
    docs_service.documents().batchUpdate(
        documentId=doc_id, body={"requests": requests}
    ).execute()

    return doc_id, doc_url


def set_anyone_can_view(drive_service, doc_id):
    """Set the doc to be viewable by anyone with the link."""
    permission = {
        "type": "anyone",
        "role": "reader",
    }
    drive_service.permissions().create(
        fileId=doc_id,
        body=permission,
        supportsAllDrives=True,
    ).execute()


def main():
    drive_service, docs_service = get_services()
    results = []

    for doc_info in SCHEMA_DOCS:
        filepath = os.path.join(DOCS_BASE, doc_info["file"])
        with open(filepath, "r") as f:
            content = f.read()

        print(f"Creating: {doc_info['title']}...", flush=True)
        doc_id, doc_url = create_doc(drive_service, docs_service, doc_info["title"], content)
        set_anyone_can_view(drive_service, doc_id)

        results.append({
            "title": doc_info["title"],
            "id": doc_id,
            "url": doc_url,
        })
        print(f"  ✅ Created: {doc_url}", flush=True)

    # Save results to file for next step
    output_file = os.path.expanduser("~/.openclaw/workspace/scripts/gdocs-results.json")
    with open(output_file, "w") as f:
        json.dump(results, f, indent=2)

    print(f"\nResults saved to: {output_file}", flush=True)
    return results


if __name__ == "__main__":
    main()
