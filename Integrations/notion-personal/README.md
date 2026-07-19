# notion-personal

Raw Notion API helpers for the personal workspace. The hosted claude.ai connector covers reads and writes but cannot upload local files; this lane fills that gap.

## upload_icon.py

Uploads a local image via the Notion File Upload API and sets it as a page icon.

```
python3 upload_icon.py --page <page_id> --file <path/to/image.png>
```

Environment: `NOTION_PERSONAL_TOKEN` — internal integration secret, sourced from the repo `.env` by reference (see `Manual/secrets-inventory.md`). The integration must be connected to the target page's database via the database's Connections menu.

Flow: create a file upload object, send the bytes as multipart form data, patch the page icon with the upload ID.

First consumer: travel project flag icons per the `journey-planner` skill (flag set at `~/Library/Mobile Documents/com~apple~CloudDocs/Personal Development/Resources/Images/Notion Icons/`).
