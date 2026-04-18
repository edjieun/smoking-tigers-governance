#!/usr/bin/env python3
"""
Create Notion records for 5 tool schema docs in the Smoking Tigers Documents DB,
then create a Strategy project linking all 5.
"""

import json
import os
import sys

try:
    import requests
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests", "--quiet"])
    import requests

NOTION_TOKEN = "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"
DOCUMENTS_DB_ID = "2fc6f6ac-689e-80cb-930a-fd4effe2bfef"
STRATEGY_DB_ID = "2c56f6ac-689e-8097-aae2-d3ac56077b61"

HEADERS = {
    "Authorization": f"Bearer {NOTION_TOKEN}",
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

GDOCS_FILE = os.path.expanduser("~/.openclaw/workspace/scripts/gdocs-results.json")

def create_document_record(title, doc_url):
    """Create a record in the Documents DB."""
    payload = {
        "parent": {"database_id": DOCUMENTS_DB_ID},
        "properties": {
            "Name": {
                "title": [{"text": {"content": title}}]
            },
            "Document Type": {
                "select": {"name": "Schema"}
            },
            "Google Doc": {
                "url": doc_url
            },
            "Date": {
                "date": {"start": "2026-03-25"}
            },
        }
    }
    resp = requests.post(
        "https://api.notion.com/v1/pages",
        headers=HEADERS,
        json=payload,
    )
    resp.raise_for_status()
    page = resp.json()
    page_id = page["id"]
    print(f"  ✅ Document record created: {title} → {page_id}")
    return page_id


def create_strategy_project(document_page_ids):
    """Create the strategy project with relations to all 5 document records."""
    relations = [{"id": pid} for pid in document_page_ids]
    payload = {
        "parent": {"database_id": STRATEGY_DB_ID},
        "properties": {
            "Name": {
                "title": [{"text": {"content": "STM Governance — Tool Schema Mapping"}}]
            },
            "Priority": {
                "select": {"name": "High"}
            },
            "Lifecycle": {
                "select": {"name": "Active"}
            },
            "Project Type": {
                "multi_select": [{"name": "Governance"}]
            },
            "Project Docs": {
                "relation": relations
            },
        }
    }
    resp = requests.post(
        "https://api.notion.com/v1/pages",
        headers=HEADERS,
        json=payload,
    )
    if not resp.ok:
        print(f"  ⚠️ Strategy project error: {resp.status_code} {resp.text}")
        # Try without Project Docs if relation fails
        payload["properties"].pop("Project Docs")
        resp = requests.post(
            "https://api.notion.com/v1/pages",
            headers=HEADERS,
            json=payload,
        )
        resp.raise_for_status()
        project_id = resp.json()["id"]
        print(f"  ✅ Strategy project created (without relations): {project_id}")
        return project_id, False
    
    project_id = resp.json()["id"]
    print(f"  ✅ Strategy project created with {len(document_page_ids)} linked docs: {project_id}")
    return project_id, True


def main():
    # Load Google Docs results
    with open(GDOCS_FILE) as f:
        gdocs = json.load(f)

    print("Step 3: Creating Notion document records...")
    document_page_ids = []
    for doc in gdocs:
        page_id = create_document_record(doc["title"], doc["url"])
        document_page_ids.append(page_id)

    print("\nStep 4: Creating strategy project...")
    project_id, linked = create_strategy_project(document_page_ids)

    # Save combined results
    output = {
        "google_docs": gdocs,
        "notion_document_page_ids": document_page_ids,
        "notion_project_id": project_id,
        "project_docs_linked": linked,
    }
    results_file = os.path.expanduser("~/.openclaw/workspace/scripts/final-results.json")
    with open(results_file, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\nAll done. Results at: {results_file}")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
