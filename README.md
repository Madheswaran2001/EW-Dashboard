# ⚡ ElectraWireless ESG Dashboard

> AI-Driven Wireless Electricity · Investor ESG Presentation · March 2026

A fully interactive ESG dashboard built with **Streamlit** and **Plotly**, covering all sustainability dimensions of ElectraWireless — derived directly from the March 2026 Pitch Deck.

---

## 📊 Dashboard Sections

| Section | Content |
|---|---|
| ⚡ Overview | ESG score 78/100, pillar gauges, score rationale, sustainability highlights |
| 🗺️ Materiality Map | 15 ESG topics by Business Impact × Stakeholder Concern |
| 📈 Trend Lines | Score progression 2022–2026 vs. WiTricity, Ossia, Traditional Players |
| 📋 Disclosure Analysis | 10 disclosure factors with status & radar chart |
| 🎯 KPI Performance | Radar + bar + full source-cited table |
| 🏆 Competitor Comparison | Score cards, grouped bars, capability heatmap, rationale |

---

## 🚀 Deploy on Streamlit Cloud (5 steps)

1. **Create a GitHub repository** named `EW-Dashboard`
2. **Upload all files** from this folder to the repository root
3. Go to **[share.streamlit.io](https://share.streamlit.io)** and sign in with GitHub
4. Click **"New app"** → select your `EW-Dashboard` repo → set main file to `app.py`
5. Click **"Deploy"** — your link will be:
   ```
   https://[your-username]-ew-dashboard-app-[hash].streamlit.app
   ```

---

## 📁 Files to Upload

```
EW-Dashboard/
├── app.py               ← Main dashboard application
├── esg_data.py          ← All ESG data, scores & rationale
├── requirements.txt     ← Python dependencies
├── .streamlit/
│   └── config.toml      ← ElectraWireless purple theme
└── README.md            ← This file
```

> ⚠️ Make sure to upload the `.streamlit/config.toml` file — it applies the purple brand theme.

---

## 💻 Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
# → Opens at http://localhost:8501
```

---

## 📈 ESG Score Summary

| Company | E | S | G | Total | Rating |
|---|---|---|---|---|---|
| **ElectraWireless** | **82** | **78** | **74** | **78** | **Leader** |
| WiTricity | 61 | 55 | 65 | 60 | Advanced |
| Ossia | 55 | 50 | 60 | 55 | Developing |
| Resonant Link | 58 | 52 | 62 | 57 | Developing |
| Traditional Players | 38 | 45 | 50 | 44 | Lagging |

---

*All data sourced from ElectraWireless Pitch Deck, March 2026*
