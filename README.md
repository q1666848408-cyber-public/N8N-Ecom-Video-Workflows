# N8N-Ecom-Video-Workflows

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)

> **Showcase** — ~15% skeleton. Core implementation not included.

24 n8n workflows automating the TikTok e-commerce video production cycle. Products flow from Kalodata selection through Apify download and Gemini analysis to script generation, with results written back to Feishu Bitable.

## Stack

- n8n (self-hosted, Docker)
- Python (custom n8n function nodes)
- Google Gemini API
- Apify (video download)
- Kalodata API
- Feishu (Lark) Bitable API

## Workflow Map

```
Kalodata: select top products
    └── Apify: download reference videos
         └── Gemini: multimodal video analysis
              └── Script generator node
                   └── Feishu Bitable: write results
```

24 workflows cover distinct sub-tasks: trend fetch, competitor analysis, hook generation, voiceover copy, caption writing, thumbnail prompt, batch processing, and more.

## Usage

```bash
# Start n8n via Docker Compose
docker compose up -d

# Import all workflows
for f in workflows/*.json; do
  n8n import:workflow --input="$f"
done

# Activate all workflows via CLI
n8n workflow:activate --all
```

## Structure

```
N8N-Ecom-Video-Workflows/
├── workflows/          # 24 exported n8n workflow JSON files
│   ├── 01-kalodata-fetch.json
│   ├── 02-apify-download.json
│   └── ...
├── custom-nodes/       # Python scripts used in Function nodes
├── docker-compose.yml
└── .env.example
```

## Requirements

- Docker and Docker Compose
- n8n >= 1.30
- Google Gemini API key
- Kalodata account
- Feishu app credentials
