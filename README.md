# AI Service Typhoon

> AI-powered service knowledge base for Typhoon coffee roasters.

## Overview

Structured knowledge base for AI-assisted service support of **Typhoon Roasters** — fully-electric and gas convection coffee roasters manufactured by Typhoon Roasters s.r.o. (Prague, Czech Republic).

Built from:
- **203 real service cases** from Monday.com (board ⚙️ service tasks, ID: 1641421174)
- **14 official manuals** covering all models (2.5 kg – 30 kg), destoner, software, commissioning
- **18 troubleshooting categories** organized by component/symptom
- **7 standard diagnostic procedures** extracted from real case solutions
- **6 model-specific issue profiles**

## Repository Structure

```
AI-service-Typhoon/
├── README.md
├── troubleshooting/              # 18 categories: symptom → diagnosis → solution
│   ├── 01_heaters.md             # 22 cases — ★★★★★
│   ├── 02_sensors.md             # 26 cases — ★★★★★
│   ├── 03_main_motor.md          # 18 cases — ★★★★☆
│   ├── 04_temperature_loss.md    # 15 cases — ★★★★☆
│   ├── 05_smoke.md               #  7 cases — ★★★☆☆
│   ├── 06_vfd.md                 #  8 cases — ★★★☆☆
│   ├── 07_seals.md               #  6 cases — ★★★☆☆
│   ├── 08_rcd.md                 #  4 cases — ★★★☆☆
│   ├── 09_actuators.md           #  5 cases — ★★☆☆☆
│   ├── 10_airflow.md             #  6 cases — ★★☆☆☆
│   ├── 11_electrical.md          # 10 cases — ★★★☆☆
│   ├── 12_impeller.md            #  5 cases — ★★☆☆☆
│   ├── 13_cyclone.md             #  7 cases — ★★☆☆☆
│   ├── 14_filter.md              #  4 cases — ★☆☆☆☆ (⚠️ FIRE RISK)
│   ├── 15_software.md            #  7 cases — ★★☆☆☆
│   ├── 16_cooling_table.md       #  6 cases — ★☆☆☆☆
│   ├── 17_glass_lights.md        #  6 cases — ★★☆☆☆
│   └── 18_destoner.md            #  2 cases — ★☆☆☆☆
├── standard_procedures/          # Step-by-step instructions
│   ├── heater_resistance_check.md
│   ├── relay_check.md
│   ├── front_alignment.md
│   ├── kinco_vfd_check.md
│   ├── spacer_adjustment.md
│   ├── phase_check.md
│   └── cyclone_mesh_cleaning.md
├── manuals/                      # Full content from PDF manuals
│   ├── general_manual.md
│   ├── roaster_5kg_pro.md
│   ├── roaster_10kg_pro.md
│   ├── roaster_25kg_pro.md
│   ├── roaster_20kg_industrial.md
│   ├── roaster_2.5kg_pro.md
│   ├── commissioning_2.5_5kg.md
│   ├── commissioning_20kg.md
│   ├── software_instructions.md
│   ├── destoner_manual.md
│   └── troubleshooting_shoproasters.md
├── models/                       # Model-specific known issues
│   ├── typhoon_2.5kg.md
│   ├── typhoon_5kg.md
│   ├── typhoon_10_electro.md
│   ├── typhoon_20_electro.md
│   ├── typhoon_20_gas.md
│   └── typhoon_30_electro.md
└── data/
    └── extracted_text/           # Raw text from PDF/DOCX
```

## Roaster Models Covered

| Model | Type | Power | Cases | Top Issues |
|-------|------|-------|-------|------------|
| Typhoon 2.5 kg / Cyclone / PRO | Shop roaster | Electric, 380V | Many | Motor, heaters, RCD, impeller |
| Typhoon 5 kg / PRO | Shop roaster | Electric, 380V | Most | Heaters, **wire burnout (5kg-specific!)**, sensors |
| Typhoon 10 kg Electro / PRO | Hybrid | Electric, 380V | Moderate | Sensor divergence, seals, VFD, actuators |
| Typhoon 20 kg Industrial Electric | Industrial | Electric, 380V | Moderate | Seals/smoke, VFD, lower sensor gaps |
| Typhoon 20 kg Gas | Industrial | Gas | Some | VFD, burner temp, pressure relay |
| Typhoon 30 kg Electric | Industrial | Electric, 380V | Few | Sensors (design: beans enter opening), jaw motor |
| Destoner (V-5/V-20/V-30/V-60) | Auxiliary | 0.8–1.5 kW | 2 | Stones in bunker, RCD trips |

## Key Technical Specs

- **Roasting method:** 100% convection (hot air), fluidized bed
- **Energy efficiency:** ~0.3 kWh/kg
- **Throughput:** Up to 6–7 batches/hour (no cooldown)
- **Control:** Kinco PLC + touchscreen
- **Connectivity:** Ethernet (IP 192.168.0.210), Artisan/Cropster compatible
- **Warranty:** 24 months, remote diagnostics/updates

## ⚠️ Critical Systemic Issues

1. **RCD not tested at factory** — roasters not tested through RCD/GFCI connection (known since June, case TRE-286). New installations may trip RCD due to neutral wire on grounding bus.
2. **5 kg wire burnout** — recurring wire burnout to main switch is a model-specific defect on Typhoon 5 kg.
3. **Condensate fire risk** — one serious case of condensate catching fire in exhaust pipe → filter destroyed. Regular pipe cleaning mandatory.
4. **30 electro sensor design** — beans fly into upper sensor opening. Needs protective plate riveted from inside.

## AI Service (Chat Prototype)

Interactive AI-powered chat for diagnosing roaster issues, built on the knowledge base above.

### Quick Start

```bash
# 1. Clone
git clone https://github.com/neistoviu/AI-service-Typhoon.git
cd AI-service-Typhoon

# 2. Install dependencies
pip install -r requirements.txt

# 3. Set API key
cp .env.example .env
# Edit .env and paste your OpenAI API key

# 4. Run
python run.py
```

Open **http://localhost:8000** in your browser.

### Two Modes

| Mode | Audience | What it does |
|------|----------|-------------|
| **Engineer** | Service technicians | Detailed diagnostics, case references, procedure links, manual citations |
| **Client** | Roaster owners | Simple troubleshooting steps, safety guidance, escalation criteria |

### Tech Stack

- **Backend:** Python + FastAPI
- **AI:** OpenAI GPT API with contextual knowledge retrieval
- **Frontend:** Vanilla HTML/CSS/JS chat interface
- **Knowledge retrieval:** TF-IDF keyword search over 45 markdown documents

### Project Structure (app code)

```
app/
├── main.py          # FastAPI routes + static file serving
├── chat.py          # OpenAI API integration + prompt building
├── knowledge.py     # Knowledge base loader + search engine
└── prompts.py       # System prompts for engineer/client modes
static/
├── index.html       # Chat interface
├── style.css        # Styles
└── app.js           # Client-side logic
```

## Usage (Knowledge Base)

This knowledge base also powers:
1. **AI service chatbot** — symptom → category → solution pipeline
2. **Technician training** — structured onboarding material
3. **Case management** — monthly updates from Monday.com

## Data Sources

- **Monday.com:** ⚙️ Service Tasks (board 1641421174) → "done cases" group
- **Customer Service:** 🛠️ board 1196036912
- **Official manuals:** 14 PDF/DOCX documents
- **Service team:** Alex Savelov, Danil Teterin, Tigran Nersesian, Nikita Vyguzov

## Monthly Update Process

1. Pull new "done" cases from Monday.com
2. Categorize into the 18 troubleshooting categories
3. Add to corresponding file + update model-specific profiles
4. Check for new manual revisions
5. Commit and push

---

> **Typhoon Roasters s.r.o.**  
> Kaprova 42/14, Staré Město, 11000 Praha 1, Czech Republic  
> +420 774 501 511 · ds-sales@typhoon-roaster.com · [typhoon.coffee](http://typhoon.coffee)
