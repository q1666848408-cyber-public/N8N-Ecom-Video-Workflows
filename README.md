<div align="center">

# 🔄 n8n E-Commerce Video Workflows

[![n8n](https://img.shields.io/badge/n8n-Self--Hosted-EA4B71?style=flat-square&logo=n8n&logoColor=white)](https://n8n.io)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?style=flat-square&logo=docker&logoColor=white)](https://docker.com)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Gemini](https://img.shields.io/badge/Gemini-2.5%20Pro-4285F4?style=flat-square&logo=google&logoColor=white)](https://deepmind.google/gemini)

**24-workflow n8n orchestration for TikTok e-commerce — Kalodata sourcing → competitor scraping → Gemini analysis → Feishu writeback**

> ⚠️ **Showcase Only** — ~15% skeleton. Workflow JSONs, credentials & business logic not included.

</div>

---

## ✨ Overview

A self-hosted n8n instance orchestrates 24 production workflows that cover the full e-commerce content lifecycle: pulling product data from Kalodata, downloading competitor videos via Apify, running Gemini analysis to generate scripts and 6-grid storyboards, then writing everything back into Feishu Bitable.

---

## 🏗️ Architecture

```
                       ┌──────────────────────┐
                       │   Kalodata API       │
                       │   (product sourcing) │
                       └──────────┬───────────┘
                                  │
                                  ▼
   ┌────────────────────────────────────────────────────┐
   │            n8n (self-hosted, Docker)               │
   │                                                    │
   │   ┌──────────────────────────────────────────┐    │
   │   │  24 Workflows                            │    │
   │   │  · Source products from Kalodata         │    │
   │   │  · Download competitor videos (Apify)    │    │
   │   │  · 6-grid storyboard generation          │    │
   │   │  · Gemini AI analysis & prompts          │    │
   │   │  · Write back to Feishu Bitable          │    │
   │   └──────────────────────────────────────────┘    │
   │                                                    │
   │   ┌──────────────────────────────────────────┐    │
   │   │  Python Code Nodes                       │    │
   │   │  · storyboard_generator                  │    │
   │   │  · kalodata_api                          │    │
   │   │  · video_analysis_api                    │    │
   │   └──────────────────────────────────────────┘    │
   └────────────────────────────────────────────────────┘
                                  │
                                  ▼
                       ┌──────────────────────┐
                       │   Feishu Bitable     │
                       │   (final output)     │
                       └──────────────────────┘
```

---

## 📁 Structure

```
n8n-ecom-video-workflows/
├── workflows/
│   └── main-process.example.json  # Workflow JSON example
├── scripts/
│   ├── storyboard_generator.py    # 6-grid storyboard
│   └── kalodata_api.py            # Kalodata client
└── docker-compose.yml             # n8n + PostgreSQL stack
```

---

## 🔧 Tech Stack

| Layer | Technology |
|---|---|
| Orchestration | n8n (self-hosted) |
| Deploy | Docker Compose + PostgreSQL |
| Helper scripts | Python 3.10+ |
| LLM | Gemini 2.5 Pro |
| Video download | Apify |
| Output | Feishu Bitable |

---

<div align="center">
<sub>Showcase version · Production workflows not included · For portfolio reference only</sub>
</div>
