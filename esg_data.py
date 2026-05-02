"""
ElectraWireless ESG Data
All metrics derived from the ElectraWireless Pitch Deck (March 2026)
"""

# ── Overall ESG Scores (out of 100) ──────────────────────────────────────────
ESG_SCORES = {
    "ElectraWireless":    {"E": 82, "S": 78, "G": 74, "Total": 78},
    "WiTricity":          {"E": 61, "S": 55, "G": 65, "Total": 60},
    "Ossia":              {"E": 55, "S": 50, "G": 60, "Total": 55},
    "Resonant Link":      {"E": 58, "S": 52, "G": 62, "Total": 57},
    "Traditional Players":{"E": 38, "S": 45, "G": 50, "Total": 44},
}

# ── Score Rationale ───────────────────────────────────────────────────────────
ESG_RATIONALE = {
    "E": (
        "**82/100 — Environmental Leader**\n\n"
        "- Eliminates **10,000 tons** of copper & aluminium cable waste annually\n"
        "- Prevents **77,500 tons of CO₂** emissions (copper 5K t = 17.5K t CO₂ + aluminium 5K t = 60K t CO₂)\n"
        "- AI-driven energy management achieves **>80% WPT efficiency**, reducing grid draw\n"
        "- Targets zero-emission households and EV charging markets aligned with 2035 mandates\n"
        "- Wireless power displaces hazardous cable manufacturing processes\n\n"
        "*Source: Pitch Deck slides 2, 24 & Appendix slide 20*"
    ),
    "S": (
        "**78/100 — Social Advanced**\n\n"
        "- Mission explicitly targets safety: eliminates fire, shock, and short-circuit risks affecting **80% of users**\n"
        "- Elly AI provides free health monitoring (diabetes, blood pressure, mental health) without wearables\n"
        "- **35+ member multinational team** spanning 9+ countries\n"
        "- University partnerships: RMIT Australia, HK Polytechnic University, TALim Belgium\n"
        "- Youth innovation competitions across global education partners\n\n"
        "*Source: Pitch Deck slides 2, 7, 14, 15, 26, 27*"
    ),
    "G": (
        "**74/100 — Governance Developing → Advanced**\n\n"
        "- **US-registered company** with stated regulatory compliance roadmap across all 5 phases\n"
        "- Transparent funding allocation publicly disclosed: 25% / 20% / 20% / 15% / 10% / 10%\n"
        "- IPO planned post-Phase 4 to offer investor liquidity while leadership retains majority control\n"
        "- Elly AI Permissions, Logs & Transparency controls built into the app\n"
        "- **Gap:** Formal GRI/SASB reporting not yet in place (expected for early-stage seed startup)\n\n"
        "*Source: Pitch Deck slides 12, 13, 15, 31*"
    ),
}

# ── ESG Trend Data 2022–2026 ──────────────────────────────────────────────────
YEARS = [2022, 2023, 2024, 2025, 2026]

ESG_TRENDS = {
    "ElectraWireless": {"E": [52, 60, 68, 75, 82], "S": [48, 58, 66, 72, 78], "G": [40, 50, 58, 66, 74]},
    "WiTricity":       {"E": [55, 57, 58, 60, 61], "S": [50, 51, 52, 54, 55], "G": [62, 63, 63, 64, 65]},
    "Ossia":           {"E": [50, 52, 53, 54, 55], "S": [46, 47, 48, 49, 50], "G": [57, 58, 59, 59, 60]},
    "Traditional":     {"E": [42, 40, 39, 38, 38], "S": [47, 46, 46, 45, 45], "G": [52, 51, 51, 50, 50]},
}

# ── Materiality Map ───────────────────────────────────────────────────────────
MATERIALITY = {
    "topic": [
        "Energy Efficiency & WPT", "E-Waste & Metal Conservation", "CO₂ Reduction",
        "Electrical Safety", "Product Safety (FOD)", "Data Privacy (Elly AI)",
        "AI Ethics & Transparency", "Workforce Diversity", "Youth & Education",
        "Supply Chain", "Regulatory Compliance", "Investor Transparency",
        "Community Health (Elly)", "IP & Innovation", "Market Accessibility",
    ],
    "business_impact":    [9.5, 8.8, 8.2, 9.0, 8.5, 7.8, 8.0, 6.5, 6.8, 7.2, 8.5, 8.0, 7.5, 7.0, 7.8],
    "stakeholder_concern":[9.2, 9.5, 9.8, 9.0, 8.8, 9.0, 8.5, 7.5, 7.2, 8.0, 8.8, 8.2, 8.8, 7.0, 8.5],
    "pillar":             ["E","E","E","S","S","G","G","S","S","E","G","G","S","G","S"],
    "bubble_size":        [25, 22, 24, 20, 18, 18, 19, 15, 14, 16, 20, 18, 17, 15, 16],
}

# ── Disclosure Factors ────────────────────────────────────────────────────────
DISCLOSURE = {
    "Factor": [
        "Financial Transparency", "Environmental Impact", "Product Safety",
        "AI Ethics & Data Policy", "Social Programs", "Governance & Board",
        "Stakeholder Engagement", "Supply Chain", "Carbon Accounting", "GRI / SASB Reporting",
    ],
    "Score": [85, 82, 80, 75, 70, 68, 60, 55, 45, 30],
    "Status": [
        "Full funding allocation breakdown publicly disclosed (6 categories)",
        "CO₂ & waste data published in pitch materials (slides 2 & 24)",
        "FOD, safety specs documented in technical appendix (slide 20)",
        "Elly AI logs & permissions system active (slide 31)",
        "University & community programs documented (slides 26–27)",
        "US registration & investor roadmap disclosed (slides 13, 15)",
        "Testimonials & partner engagement documented (slide 25)",
        "China hardware sourcing mentioned; limited detail provided",
        "CO₂ numbers stated; methodology not independently verified",
        "No formal GRI/SASB report yet — standard for seed-stage startup",
    ],
    "Color": ["green","green","green","green","yellow","yellow","yellow","orange","orange","red"],
}

# ── KPI Data ──────────────────────────────────────────────────────────────────
KPI = {
    "KPI": [
        "CO₂ Reduction (tons/yr)", "E-Waste Prevented (tons/yr)",
        "Energy Efficiency (%)", "Safety Incident Reduction (%)",
        "Green Market Coverage (%)", "Team Diversity Index (%)",
        "Disclosure Score (/100)", "AI Ethics Controls (%)", "Community Programs (#)",
    ],
    "ElectraWireless": [10000, 10000, 82, 95, 78, 85, 70, 90, 4],
    "WiTricity":       [3200,  2000,  70, 50, 55, 60, 65, 50, 1],
    "Ossia":           [2500,  1500,  65, 40, 45, 55, 55, 60, 1],
    "Resonant Link":   [1800,  800,   72, 60, 40, 50, 60, 45, 0],
    "Industry Avg":    [2000,  1200,  60, 45, 40, 55, 52, 40, 1],
    "Unit":            ["t CO₂","tons","%","%","%","%","/100","%","programs"],
    "Source": [
        "Slides 2 & 24: 5K t copper = 17.5K t CO₂ + 5K t Al = 60K t CO₂",
        "Slides 2 & 24: 10,000 tons metal waste eliminated annually",
        "Appendix slide 20: >80% WPT efficiency stated",
        "Slide 2: Eliminates fire/shock/circuit risk for 80% of users",
        "Slides 7–8: Kitchen, EV, Robotics, IoT, E-bike markets",
        "Slide 15: 9-country team of 35+ members, 4 departments",
        "Slides 12–13: Funding allocation disclosed; no formal ESG report",
        "Slide 31: Elly AI Permissions & Logs controls active",
        "Slides 26–27: RMIT, HK PolyU, TALim Belgium + competitions",
    ],
}

# ── Competitor Feature Matrix (Slide 7) ───────────────────────────────────────
COMPETITOR_FEATURES = {
    "Company":              ["ElectraWireless", "WiTricity", "Ossia", "Resonant Link", "Traditional Players"],
    "Wireless Power":       [True, True, True, True, False],
    "Heating Capability":   [True, False, False, False, True],
    "Smart App & Data":     [True, False, True, False, True],
    "Foreign Object Det.":  [True, False, False, False, False],
    "OEM Customization":    [True, True, True, True, True],
    "Kitchen Appliances":   [True, False, False, False, True],
    "E-Bikes":              [True, False, False, False, True],
    "Robotics":             [True, True, False, False, True],
    "EV Charging":          [True, True, False, False, True],
    "Medical Devices":      [True, False, False, True, False],
}

# ── Colours ───────────────────────────────────────────────────────────────────
COLORS = {
    "EW":          "#4B0082",
    "WiTricity":   "#0EA5E9",
    "Ossia":       "#F97316",
    "Resonant":    "#10B981",
    "Traditional": "#9CA3AF",
    "Industry":    "#6B7280",
    "E":           "#22C55E",
    "S":           "#3B82F6",
    "G":           "#A855F7",
}

COMP_COLORS = {
    "ElectraWireless":    "#4B0082",
    "WiTricity":          "#0EA5E9",
    "Ossia":              "#F97316",
    "Resonant Link":      "#10B981",
    "Traditional Players":"#9CA3AF",
    "Industry Avg":       "#6B7280",
}

PILLAR_COLORS = {"E": "#22C55E", "S": "#3B82F6", "G": "#A855F7"}
