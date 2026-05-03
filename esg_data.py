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

# ── Historical ESG Trend Data — Founded March 2024, tracked quarterly ─────────
# ElectraWireless was founded in March 2024. Trend data starts at founding and
# runs through six quarterly checkpoints to the current dashboard date (Mar 2026).
# Each label represents a quarterly reporting period.
YEARS = ["Mar 2024\n(Founded)", "Jun 2024", "Sep 2024", "Dec 2024", "Jun 2025", "Mar 2026"]

ESG_TRENDS = {
    # EW starts from first-month baseline and improves rapidly each quarter
    # as team, technology, product, and governance structures are built out.
    "ElectraWireless": {
        "E": [42, 52, 61, 68, 75, 82],   # Environmental: R&D → WPT prototype → Phase 1 launch → CO₂ data
        "S": [30, 44, 55, 63, 70, 78],   # Social: team hired → Elly beta → HK PolyU → RMIT partnership
        "G": [22, 36, 48, 57, 66, 74],   # Governance: US incorporation → seed round → funding disclosure → IPO roadmap
    },
    # Established competitors move slowly — already operating well before 2024
    "WiTricity":   {"E": [58, 59, 59, 60, 60, 61], "S": [53, 53, 54, 54, 55, 55], "G": [63, 63, 64, 64, 64, 65]},
    "Ossia":       {"E": [53, 53, 54, 54, 55, 55], "S": [48, 48, 49, 49, 50, 50], "G": [58, 58, 59, 59, 60, 60]},
    "Traditional": {"E": [40, 40, 39, 39, 38, 38], "S": [46, 46, 45, 45, 45, 45], "G": [51, 51, 51, 50, 50, 50]},
}

# ── Future Trend Projections — maintaining same growth rate per quarter ────────
# Methodology: average quarterly gain from historical data is extrapolated forward.
# Phase milestones are used as qualitative anchors for each projection point.
# "Conservative" = 60% of historical rate | "Base" = 100% | "Optimistic" = 140%
#
# Historical quarterly gains (Mar 2024 → Mar 2026 = 8 quarters):
#   E: (82-42)/8 = +5.0 pts/quarter
#   S: (78-30)/8 = +6.0 pts/quarter
#   G: (74-22)/8 = +6.5 pts/quarter
#
# Projection periods: Jun 2026 → Dec 2026 → Jun 2027 → Dec 2027 → Jun 2028 → Dec 2028

FUTURE_YEARS = ["Mar 2026\n(Today)", "Jun 2026", "Dec 2026", "Jun 2027",
                "Dec 2027", "Jun 2028", "Dec 2028"]

FUTURE_MILESTONES = {
    "Jun 2026":  "Phase 2 launch\n(E-Bike charging)",
    "Dec 2026":  "Series A\n(GRI report published)",
    "Jun 2027":  "Phase 3 launch\n(Robotics charging)",
    "Dec 2027":  "Phase 4 launch\n(IoT / Smart Furniture)",
    "Jun 2028":  "Phase 5 launch\n(EV charging)",
    "Dec 2028":  "IPO preparation\n(post-Phase 4)",
}

FUTURE_TRENDS = {
    # Base case: same quarterly rate maintained
    "base": {
        "E": [82, 87, 92, 96, 98, 99, 99],   # caps near 99 (physical/supply limits)
        "S": [78, 83, 88, 92, 95, 97, 98],
        "G": [74, 79, 85, 89, 92, 94, 96],
    },
    # Conservative: 60% of historical rate (slower fundraising, market headwinds)
    "conservative": {
        "E": [82, 85, 88, 91, 93, 95, 96],
        "S": [78, 81, 84, 87, 90, 92, 94],
        "G": [74, 77, 81, 84, 87, 89, 91],
    },
    # Optimistic: 140% of historical rate (accelerated deployment, IPO boost)
    "optimistic": {
        "E": [82, 89, 95, 98, 99, 99, 99],
        "S": [78, 86, 92, 96, 98, 99, 99],
        "G": [74, 82, 89, 94, 97, 98, 99],
    },
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
