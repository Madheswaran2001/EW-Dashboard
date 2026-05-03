"""
ElectraWireless ESG Dashboard — Streamlit Edition (Fixed)
Deploy via: streamlit run app.py
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np
from esg_data import (
    ESG_SCORES, ESG_RATIONALE, ESG_TRENDS, YEARS,
    MATERIALITY, DISCLOSURE, KPI, COMPETITOR_FEATURES,
    COMP_COLORS, PILLAR_COLORS,
)

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ElectraWireless ESG Dashboard",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #2D0057 0%, #3C3489 100%);
}
[data-testid="stSidebar"] * { color: rgba(255,255,255,0.85) !important; }
div[data-testid="metric-container"] {
    background: #FFFFFF;
    border: 1px solid #EDE9F8;
    border-radius: 12px;
    padding: 16px !important;
    box-shadow: 0 2px 12px rgba(75,0,130,0.06);
}
.hero-banner {
    background: linear-gradient(135deg, #2D0057 0%, #4B0082 60%, #7B2FBE 100%);
    border-radius: 16px;
    padding: 32px 36px;
    color: white;
    margin-bottom: 24px;
}
.highlight-item {
    background: #F8F5FF;
    border-radius: 10px;
    padding: 10px 14px;
    margin-bottom: 8px;
    font-size: 14px;
    border: 1px solid #EDE9F8;
}
.section-title {
    font-size: 20px;
    font-weight: 700;
    color: #4B0082;
    margin-bottom: 4px;
}
.section-sub {
    font-size: 13px;
    color: #6B7280;
    margin-bottom: 16px;
}
</style>
""", unsafe_allow_html=True)

# ── Shared layout helper ──────────────────────────────────────────────────────
# FIX 1: Instead of a dict with a margin key that conflicts when calling
# fig.update_layout(**LAYOUT, margin=...), we use a function that accepts
# overrides — so margin is never duplicated.
def base_layout(**overrides):
    layout = dict(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="sans-serif", color="#1E1B4B"),
        margin=dict(l=60, r=20, t=50, b=60),
    )
    layout.update(overrides)
    return layout

GRID = dict(gridcolor="#F3F0FA", zerolinecolor="#EDE9F8")

# FIX 2: Converts a hex colour to a valid rgba() string for fillcolor.
# Plotly rejects hex+2-char-alpha (e.g. "#22C55E18") on newer versions.
def hex_rgba(hex_col, alpha):
    h = hex_col.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{alpha})"


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚡ ElectraWireless")
    st.markdown("**ESG Dashboard · March 2026**")
    st.markdown("---")
    section = st.radio(
        "Navigate",
        options=[
            "⚡ Overview",
            "🗺️ Materiality Map",
            "📈 Trend Lines",
            "📋 Disclosure Analysis",
            "🎯 KPI Performance",
            "🏆 Competitor Comparison",
        ],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.caption("Seed Stage · US Registered")
    st.caption("Data source: Pitch Deck, March 2026")


# ═════════════════════════════════════════════════════════════════════════════
# OVERVIEW
# ═════════════════════════════════════════════════════════════════════════════
if section == "⚡ Overview":
    ew = ESG_SCORES["ElectraWireless"]

    st.markdown(f"""
    <div class="hero-banner">
        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:16px;">
            <div>
                <div style="font-size:13px;opacity:0.7;text-transform:uppercase;letter-spacing:1px;margin-bottom:6px;">
                    AI-Driven Wireless Electricity · Seed Stage
                </div>
                <div style="font-size:42px;font-weight:800;line-height:1;">ElectraWireless</div>
                <div style="font-size:15px;opacity:0.8;margin-top:6px;">
                    ESG Sustainability Dashboard — March 2026
                </div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:12px;opacity:0.7;text-transform:uppercase;letter-spacing:1px;">Overall ESG Score</div>
                <div style="font-size:64px;font-weight:800;line-height:1;">{ew['Total']}</div>
                <div style="font-size:14px;opacity:0.6;">/100</div>
                <div style="background:#22C55E;color:white;border-radius:20px;padding:4px 16px;
                            font-size:13px;font-weight:700;display:inline-block;margin-top:8px;">
                    ● LEADER
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("🌿 Environmental", f"{ew['E']} / 100", "+30 pts since 2022")
    with c2:
        st.metric("🤝 Social", f"{ew['S']} / 100", "+30 pts since 2022")
    with c3:
        st.metric("🏛️ Governance", f"{ew['G']} / 100", "+34 pts since 2022")

    st.markdown("---")
    st.markdown('<div class="section-title">Pillar Gauges</div>', unsafe_allow_html=True)

    # FIX 1 applied: margin is passed as an override inside base_layout(),
    # so there is no duplicate key when calling fig.update_layout().
    def gauge(label, value, color):
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=value,
            number={"suffix": "/100", "font": {"size": 22, "color": color}},
            gauge={
                "axis": {"range": [0, 100], "tickcolor": "#ccc"},
                "bar":  {"color": color, "thickness": 0.28},
                "bgcolor": "#F3F0FA",
                "borderwidth": 0,
                "steps": [
                    {"range": [0,  40], "color": "#FECACA"},
                    {"range": [40, 70], "color": "#FEF3C7"},
                    {"range": [70,100], "color": "#D1FAE5"},
                ],
                "threshold": {"line": {"color": color, "width": 3}, "value": value},
            },
            title={"text": label, "font": {"size": 14, "color": "#4B0082"}},
        ))
        fig.update_layout(**base_layout(height=200, margin=dict(l=20, r=20, t=50, b=10)))
        return fig

    g1, g2, g3 = st.columns(3)
    with g1:
        st.plotly_chart(gauge("🌿 Environmental", ew["E"], "#22C55E"), use_container_width=True)
    with g2:
        st.plotly_chart(gauge("🤝 Social",        ew["S"], "#3B82F6"), use_container_width=True)
    with g3:
        st.plotly_chart(gauge("🏛️ Governance",   ew["G"], "#A855F7"), use_container_width=True)

    st.markdown("---")
    st.markdown('<div class="section-title">Why These Scores?</div>', unsafe_allow_html=True)
    st.caption("Rationale derived directly from the ElectraWireless Pitch Deck, March 2026")

    with st.expander("🌿 Environmental — 82 / 100  ·  Click to expand", expanded=True):
        st.markdown(ESG_RATIONALE["E"])
    with st.expander("🤝 Social — 78 / 100  ·  Click to expand", expanded=True):
        st.markdown(ESG_RATIONALE["S"])
    with st.expander("🏛️ Governance — 74 / 100  ·  Click to expand", expanded=True):
        st.markdown(ESG_RATIONALE["G"])

    st.markdown("---")
    st.markdown('<div class="section-title">Sustainability Highlights</div>', unsafe_allow_html=True)
    highlights = [
        ("🌱", "Eliminates **10,000 tons** of copper & aluminium cable waste **annually**"),
        ("💨", "Prevents **77,500 tons of CO₂** emissions per year"),
        ("⚡", "**>80% wireless power transfer efficiency** — beats all cable-based alternatives"),
        ("🛡️", "Removes fire, shock & short-circuit hazards affecting **80% of households**"),
        ("🤝", "**35+ member multinational team** spanning 9 countries across 4 departments"),
        ("🏛️", "US-registered with **transparent 6-category funding** disclosure & IPO roadmap"),
        ("🎓", "Academic partnerships: **RMIT, HK PolyU, TALim Belgium** + youth competitions"),
        ("🤖", "Elly AI ranked **#4 / 163,000+** applications globally (Kaggle Beta 2025)"),
    ]
    cl, cr = st.columns(2)
    for i, (icon, text) in enumerate(highlights):
        col = cl if i % 2 == 0 else cr
        with col:
            st.markdown(
                f'<div class="highlight-item">{icon} &nbsp;{text}</div>',
                unsafe_allow_html=True,
            )


# ═════════════════════════════════════════════════════════════════════════════
# MATERIALITY MAP
# ═════════════════════════════════════════════════════════════════════════════
elif section == "🗺️ Materiality Map":
    st.markdown('<div class="section-title">Materiality Map</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">ESG topics plotted by Business Impact (x-axis) and Stakeholder Concern (y-axis). '
        'Bubble size reflects priority weight. Top-right quadrant = highest priority.</div>',
        unsafe_allow_html=True,
    )

    df = pd.DataFrame(MATERIALITY)
    df["pillar_label"] = df["pillar"].map({"E": "Environmental", "S": "Social", "G": "Governance"})

    fig = go.Figure()
    for x0, x1, y0, y1, label in [
        (7.5, 10.2, 7.5, 10.2, "HIGH PRIORITY"),
        (5.8, 7.5,  7.5, 10.2, "MONITOR"),
        (7.5, 10.2, 6.5, 7.5,  "ACT"),
        (5.8, 7.5,  6.5, 7.5,  "LOW PRIORITY"),
    ]:
        fig.add_shape(type="rect", x0=x0, x1=x1, y0=y0, y1=y1,
                      fillcolor="rgba(75,0,130,0.04)", line_width=0, layer="below")
        fig.add_annotation(x=(x0+x1)/2, y=(y0+y1)/2, text=f"<b>{label}</b>",
                           showarrow=False, font=dict(size=9, color="#9CA3AF"), opacity=0.7)

    fig.add_shape(type="line", x0=7.5, x1=7.5, y0=6.5, y1=10.2,
                  line=dict(dash="dot", color="#C4B5D8", width=1.5))
    fig.add_shape(type="line", x0=5.8, x1=10.2, y0=7.5, y1=7.5,
                  line=dict(dash="dot", color="#C4B5D8", width=1.5))

    for pillar, pcolor, plabel in [
        ("E", PILLAR_COLORS["E"], "Environmental"),
        ("S", PILLAR_COLORS["S"], "Social"),
        ("G", PILLAR_COLORS["G"], "Governance"),
    ]:
        sub = df[df["pillar"] == pillar]
        fig.add_trace(go.Scatter(
            x=sub["business_impact"], y=sub["stakeholder_concern"],
            mode="markers+text", name=plabel,
            text=sub["topic"], textposition="top center",
            textfont=dict(size=9, color="#374151"),
            marker=dict(size=sub["bubble_size"], color=pcolor, opacity=0.72,
                        line=dict(color="#fff", width=1.5)),
            hovertemplate="<b>%{text}</b><br>Business Impact: %{x}<br>Stakeholder Concern: %{y}<extra></extra>",
        ))

    fig.update_layout(**base_layout(
        height=520, margin=dict(l=20, r=20, t=40, b=60),
        xaxis=dict(title="Business Impact →", range=[5.8, 10.2], **GRID),
        yaxis=dict(title="Stakeholder Concern →", range=[6.5, 10.2], **GRID),
        legend=dict(orientation="h", y=-0.12, font=dict(size=12)),
    ))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 🌿 Top Environmental")
        st.markdown("""
- **CO₂ Footprint Reduction** — highest stakeholder concern (9.8/10)
- **E-Waste & Metal Conservation** — direct product impact (9.5/10)
- **Energy Efficiency & WPT** — core technology differentiator (9.2/10)
        """)
    with c2:
        st.markdown("#### 🤝 Top Social")
        st.markdown("""
- **Electrical Safety** — eliminates 80% of household hazard exposure (9.0/10)
- **Community Health (Elly)** — free AI health monitoring for all users (8.8/10)
- **Market Accessibility** — products for Boomers & Millennials (8.5/10)
        """)
    with c3:
        st.markdown("#### 🏛️ Top Governance")
        st.markdown("""
- **Regulatory Compliance** — phase-by-phase roadmap across 5 phases (8.8/10)
- **Investor Transparency** — full 6-category funding disclosure (8.2/10)
- **AI Ethics & Transparency** — Elly AI logs & permissions controls (8.5/10)
        """)


# ═════════════════════════════════════════════════════════════════════════════
# TREND LINES
# ═════════════════════════════════════════════════════════════════════════════
elif section == "📈 Trend Lines":
    st.markdown('<div class="section-title">ESG Score Trend Lines — 2022 to 2026</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">ElectraWireless shows the steepest improvement trajectory across all three pillars, '
        'driven by product launches, partnership milestones, and growing environmental impact data.</div>',
        unsafe_allow_html=True,
    )

    selected_pillars = st.multiselect(
        "Select pillars to display:",
        options=["Environmental (E)", "Social (S)", "Governance (G)"],
        default=["Environmental (E)", "Social (S)", "Governance (G)"],
    )
    pillar_map   = {"Environmental (E)": "E", "Social (S)": "S", "Governance (G)": "G"}
    selected_keys = [pillar_map[p] for p in selected_pillars]

    fig_combined = go.Figure()
    for p, pcolor, plabel in [
        ("E", "#22C55E", "Environmental"),
        ("S", "#3B82F6", "Social"),
        ("G", "#A855F7", "Governance"),
    ]:
        if p in selected_keys:
            fig_combined.add_trace(go.Scatter(
                x=YEARS, y=ESG_TRENDS["ElectraWireless"][p],
                name=f"EW {plabel}", mode="lines+markers",
                line=dict(color=pcolor, width=3),
                marker=dict(size=9, symbol="circle"),
                fill="tozeroy",
                fillcolor=hex_rgba(pcolor, 0.10),   # FIX 2 applied
            ))

    fig_combined.update_layout(**base_layout(
        height=320, margin=dict(l=20, r=20, t=50, b=60),
        title=dict(text="ElectraWireless — All Pillars Trend", font=dict(size=15, color="#4B0082")),
        xaxis=dict(tickvals=YEARS, **GRID),
        yaxis=dict(range=[0, 100], title="Score /100", **GRID),
        legend=dict(orientation="h", y=-0.22),
    ))
    st.plotly_chart(fig_combined, use_container_width=True)

    st.markdown("---")
    st.markdown("#### Pillar-by-Pillar vs. Competitors")

    tab_e, tab_s, tab_g = st.tabs(["🌿 Environmental", "🤝 Social", "🏛️ Governance"])

    for tab, pillar, pcolor, plabel in [
        (tab_e, "E", "#22C55E", "Environmental"),
        (tab_s, "S", "#3B82F6", "Social"),
        (tab_g, "G", "#A855F7", "Governance"),
    ]:
        with tab:
            fig = go.Figure()
            comp_styles = {
                "ElectraWireless": (pcolor,    3.0, "solid", 8),
                "WiTricity":       ("#0EA5E9", 1.8, "dot",   5),
                "Ossia":           ("#F97316", 1.8, "dot",   5),
                "Traditional":     ("#9CA3AF", 1.8, "dash",  5),
            }
            for comp, (col, lw, dash, ms) in comp_styles.items():
                fig.add_trace(go.Scatter(
                    x=YEARS, y=ESG_TRENDS[comp][pillar],
                    name=comp, mode="lines+markers",
                    line=dict(color=col, width=lw, dash=dash),
                    marker=dict(size=ms),
                ))
            fig.update_layout(**base_layout(
                height=300, margin=dict(l=20, r=20, t=50, b=70),
                title=dict(text=f"{plabel} Score — EW vs. Competitors",
                           font=dict(size=14, color="#4B0082")),
                xaxis=dict(tickvals=YEARS, **GRID),
                yaxis=dict(range=[30, 100], title="Score /100", **GRID),
                legend=dict(orientation="h", y=-0.30, font=dict(size=11)),
            ))
            st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.success("**+30pts Environmental** (52 → 82)\n\nDriven by CO₂ quantification, WPT efficiency milestones, and university partnerships proving real-world impact.")
    with c2:
        st.info("**+30pts Social** (48 → 78)\n\nElly AI health features, 35+ diverse hires, and youth innovation competitions in Belgium, HK, and Australia.")
    with c3:
        st.warning("**+34pts Governance** (40 → 74)\n\nUS company registration, IPO roadmap, AI ethics framework, and transparent seed funding structure.")


# ═════════════════════════════════════════════════════════════════════════════
# DISCLOSURE ANALYSIS
# ═════════════════════════════════════════════════════════════════════════════
elif section == "📋 Disclosure Analysis":
    st.markdown('<div class="section-title">Disclosure Factor Analysis</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">How transparently ElectraWireless reports across ten key ESG disclosure dimensions. '
        'Assessed against pitch deck evidence, public materials, and startup-stage norms.</div>',
        unsafe_allow_html=True,
    )

    df = pd.DataFrame(DISCLOSURE)
    df_sorted = df.sort_values("Score", ascending=True)

    color_map  = {"green": "#22C55E", "yellow": "#F59E0B", "orange": "#F97316", "red": "#EF4444"}
    bar_colors = [color_map[c] for c in df_sorted["Color"]]

    col_bar, col_radar = st.columns([3, 2])

    with col_bar:
        fig_bar = go.Figure(go.Bar(
            x=df_sorted["Score"], y=df_sorted["Factor"],
            orientation="h", marker_color=bar_colors,
            text=[f"{s}/100" for s in df_sorted["Score"]],
            textposition="inside", textfont=dict(color="#fff", size=11),
            hovertemplate="<b>%{y}</b><br>Score: %{x}/100<extra></extra>",
        ))
        fig_bar.update_layout(**base_layout(
            height=400, margin=dict(l=200, r=20, t=50, b=40),
            xaxis=dict(range=[0, 100], title="Score / 100", **GRID),
            yaxis=dict(tickfont=dict(size=11)),
            title=dict(text="Disclosure Scores by Factor", font=dict(size=14, color="#4B0082")),
        ))
        st.plotly_chart(fig_bar, use_container_width=True)

    with col_radar:
        # FIX 3: Full descriptive names on all axes; wide margins prevent clipping
        DISC_LABELS = [
            "Financial Transparency",
            "Environmental Impact Quantification",
            "Product Safety Disclosures",
            "AI Ethics & Data Policy",
            "Social Program Documentation",
            "Governance & Board Structure",
            "Stakeholder Engagement Reports",
            "Supply Chain Transparency",
            "Carbon Accounting & Methodology",
            "GRI / SASB Formal Reporting",
        ]
        scores = df["Score"].tolist()
        fig_radar = go.Figure(go.Scatterpolar(
            r=scores + [scores[0]],
            theta=DISC_LABELS + [DISC_LABELS[0]],
            fill="toself",
            fillcolor="rgba(123,47,190,0.18)",
            line=dict(color="#7B2FBE", width=2.5),
            marker=dict(size=7, color="#4B0082"),
            name="Disclosure Score",
        ))
        fig_radar.update_layout(**base_layout(
            height=460, margin=dict(l=90, r=90, t=70, b=90),
            title=dict(text="Disclosure Radar — All 10 Factors",
                       font=dict(size=14, color="#4B0082")),
            polar=dict(
                radialaxis=dict(
                    range=[0, 100],
                    tickvals=[20, 40, 60, 80, 100],
                    gridcolor="#EDE9F8",
                    tickfont=dict(size=9),
                ),
                angularaxis=dict(
                    tickfont=dict(size=9),
                    rotation=90,
                    direction="clockwise",
                ),
            ),
        ))
        st.plotly_chart(fig_radar, use_container_width=True)

    st.markdown("---")
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown("🟢 **Strong (80–100)** — Disclosed & verified")
    with c2: st.markdown("🟡 **Good (65–79)** — Documented, improving")
    with c3: st.markdown("🟠 **Developing (45–64)** — Partial / early stage")
    with c4: st.markdown("🔴 **Gap (<45)** — Missing or informal")

    st.markdown("---")
    st.markdown("#### Status Detail")
    for _, row in df.iterrows():
        dot   = {"green": "🟢", "yellow": "🟡", "orange": "🟠", "red": "🔴"}[row["Color"]]
        ca, cb, cc = st.columns([3, 1, 6])
        with ca: st.markdown(f"**{row['Factor']}**")
        with cb: st.markdown(f"{dot} **{row['Score']}/100**")
        with cc: st.caption(row["Status"])


# ═════════════════════════════════════════════════════════════════════════════
# KPI PERFORMANCE
# ═════════════════════════════════════════════════════════════════════════════
elif section == "🎯 KPI Performance":
    st.markdown('<div class="section-title">Performance Across KPIs</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">ElectraWireless leads on environmental impact metrics. Social and Governance KPIs '
        'are advancing rapidly for a company at seed stage.</div>',
        unsafe_allow_html=True,
    )

    df = pd.DataFrame(KPI)
    companies = ["ElectraWireless", "WiTricity", "Ossia", "Resonant Link", "Industry Avg"]

    # FIX 4: Clear two-line axis labels so nothing overlaps on the radar
    RADAR_LABELS = [
        "CO₂ Reduction<br>(tons/yr)",
        "E-Waste Prevented<br>(tons/yr)",
        "Energy Efficiency<br>(%)",
        "Safety Incident<br>Reduction (%)",
        "Green Market<br>Coverage (%)",
        "Team Diversity<br>Index (%)",
        "Disclosure<br>Score (/100)",
        "AI Ethics<br>Controls (%)",
        "Community<br>Programs (#)",
    ]

    # Normalise per-KPI row so all companies are on 0-100 scale
    norm_data = {}
    for comp in companies:
        norm_vals = []
        for i in range(len(df)):
            row_vals = [df[c].iloc[i] for c in companies]
            mn, mx   = min(row_vals), max(row_vals)
            v        = df[comp].iloc[i]
            norm_vals.append(round((v - mn) / (mx - mn) * 100) if mx != mn else 50)
        norm_data[comp] = norm_vals

    col_radar, col_bar = st.columns([1, 1])

    with col_radar:
        fig_radar = go.Figure()
        for comp in companies:
            nv    = norm_data[comp]
            is_ew = comp == "ElectraWireless"
            fig_radar.add_trace(go.Scatterpolar(
                r=nv + [nv[0]],
                theta=RADAR_LABELS + [RADAR_LABELS[0]],
                name=comp,
                mode="lines" + ("+markers" if is_ew else ""),
                line=dict(
                    color=COMP_COLORS.get(comp, "#888"),
                    width=3.0 if is_ew else 1.5,
                    dash="solid" if is_ew else "dot",
                ),
                fill="toself"               if is_ew else None,
                fillcolor="rgba(75,0,130,0.10)" if is_ew else None,
                marker=dict(size=7, color=COMP_COLORS.get(comp, "#888")) if is_ew else None,
            ))

        fig_radar.update_layout(**base_layout(
            height=520,
            # Wide margins keep the two-line labels fully visible
            margin=dict(l=110, r=110, t=90, b=110),
            title=dict(text="KPI Radar — Normalised Scores (0–100)",
                       font=dict(size=14, color="#4B0082")),
            polar=dict(
                radialaxis=dict(
                    range=[0, 100],
                    tickvals=[25, 50, 75, 100],
                    gridcolor="#EDE9F8",
                    tickfont=dict(size=8),
                    tickangle=45,
                ),
                angularaxis=dict(
                    tickfont=dict(size=9),
                    rotation=90,
                    direction="clockwise",
                ),
            ),
            legend=dict(
                orientation="h", y=-0.20,
                x=0.5, xanchor="center",
                font=dict(size=10),
            ),
        ))
        st.plotly_chart(fig_radar, use_container_width=True)

    with col_bar:
        bar_kpis = [
            "CO₂ Reduction (tons/yr)",
            "E-Waste Prevented (tons/yr)",
            "Energy Efficiency (%)",
            "Green Market Coverage (%)",
        ]
        fig_bar = go.Figure()
        for comp in ["ElectraWireless", "WiTricity", "Ossia", "Industry Avg"]:
            y_vals = [df[df["KPI"] == k][comp].values[0] for k in bar_kpis]
            fig_bar.add_trace(go.Bar(
                name=comp, x=bar_kpis, y=y_vals,
                marker_color=COMP_COLORS.get(comp, "#888"),
                opacity=0.85,
            ))
        fig_bar.update_layout(**base_layout(
            height=460, margin=dict(l=20, r=20, t=50, b=110),
            barmode="group",
            xaxis=dict(tickangle=-20, tickfont=dict(size=10), automargin=True, **GRID),
            yaxis=dict(**GRID),
            title=dict(text="Key ESG KPIs vs. Competitors", font=dict(size=14, color="#4B0082")),
            legend=dict(orientation="h", y=-0.35, font=dict(size=10)),
        ))
        st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("---")
    st.markdown("#### KPI Detail Table")
    st.caption("All values from pitch deck. Industry averages from comparable wireless power / cleantech startups.")

    display_rows = []
    for _, row in df.iterrows():
        ew_val   = row["ElectraWireless"]
        ind_val  = row["Industry Avg"]
        diff_pct = round(((ew_val - ind_val) / max(ind_val, 1)) * 100)
        arrow    = f"▲ +{diff_pct}%" if diff_pct > 0 else f"▼ {diff_pct}%"
        display_rows.append({
            "KPI":             row["KPI"],
            "ElectraWireless": f"{ew_val:,} {row['Unit']}",
            "Industry Avg":    f"{ind_val:,}",
            "vs. Industry":    arrow,
            "Source":          row["Source"],
        })

    st.dataframe(
        pd.DataFrame(display_rows),
        use_container_width=True,
        hide_index=True,
        column_config={
            "KPI":             st.column_config.TextColumn("KPI",             width="medium"),
            "ElectraWireless": st.column_config.TextColumn("ElectraWireless", width="medium"),
            "vs. Industry":    st.column_config.TextColumn("vs. Industry",    width="small"),
            "Source":          st.column_config.TextColumn("Source",          width="large"),
        },
    )


# ═════════════════════════════════════════════════════════════════════════════
# COMPETITOR COMPARISON
# ═════════════════════════════════════════════════════════════════════════════
elif section == "🏆 Competitor Comparison":
    st.markdown('<div class="section-title">Comparison with Competitors</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">ElectraWireless leads all competitors on Overall ESG score (78/100), '
        'with particular strength in Environmental impact. The only company with all 10 product/sector capabilities.</div>',
        unsafe_allow_html=True,
    )

    companies = list(ESG_SCORES.keys())

    cols = st.columns(len(companies))
    for i, comp in enumerate(companies):
        s = ESG_SCORES[comp]
        rating = ("Leader"    if s["Total"] >= 75 else
                  "Advanced"  if s["Total"] >= 60 else
                  "Developing" if s["Total"] >= 50 else "Lagging")
        rc = ("#3B6D11" if rating == "Leader" else "#185FA5" if rating == "Advanced"
              else "#854F0B" if rating == "Developing" else "#A32D2D")
        is_ew = comp == "ElectraWireless"
        with cols[i]:
            st.markdown(
                f"""<div style="background:{'#F3F0FA' if is_ew else 'white'};
                    border:{'2px solid #4B0082' if is_ew else '1px solid #EDE9F8'};
                    border-radius:12px;padding:14px;text-align:center;margin-bottom:8px;">
                    <div style="font-size:12px;font-weight:{'700' if is_ew else '500'};
                                color:{'#4B0082' if is_ew else '#6B7280'};">{comp}</div>
                    <div style="font-size:30px;font-weight:700;
                                color:{'#4B0082' if is_ew else '#374151'};
                                line-height:1;margin:6px 0;">{s['Total']}</div>
                    <div style="font-size:10px;color:#9CA3AF;margin-bottom:6px;">/100 Overall</div>
                    <div style="font-size:11px;color:#22C55E;">E: {s['E']}</div>
                    <div style="font-size:11px;color:#3B82F6;">S: {s['S']}</div>
                    <div style="font-size:11px;color:#A855F7;">G: {s['G']}</div>
                    <div style="margin-top:6px;font-size:10px;font-weight:600;color:{rc};">{rating.upper()}</div>
                </div>""",
                unsafe_allow_html=True,
            )

    st.markdown("---")
    col_chart, col_table = st.columns([3, 2])
    with col_chart:
        fig_bar = go.Figure()
        for pillar, pcolor, plabel in [
            ("E", "#22C55E", "Environmental"),
            ("S", "#3B82F6", "Social"),
            ("G", "#A855F7", "Governance"),
        ]:
            fig_bar.add_trace(go.Bar(
                name=plabel, x=companies,
                y=[ESG_SCORES[c][pillar] for c in companies],
                marker_color=pcolor, opacity=0.82,
            ))
        fig_bar.update_layout(**base_layout(
            height=360, margin=dict(l=20, r=20, t=50, b=60),
            barmode="group",
            xaxis=dict(tickfont=dict(size=11), **GRID),
            yaxis=dict(range=[0, 100], title="Score /100", **GRID),
            title=dict(text="ESG Pillar Scores — All Companies",
                       font=dict(size=14, color="#4B0082")),
            legend=dict(orientation="h", y=-0.2),
        ))
        st.plotly_chart(fig_bar, use_container_width=True)

    with col_table:
        rating_map = {
            c: ("Leader"    if ESG_SCORES[c]["Total"] >= 75 else
                "Advanced"  if ESG_SCORES[c]["Total"] >= 60 else
                "Developing" if ESG_SCORES[c]["Total"] >= 50 else "Lagging")
            for c in companies
        }
        st.dataframe(
            pd.DataFrame([
                {"Company": c,
                 "E /100":  ESG_SCORES[c]["E"],
                 "S /100":  ESG_SCORES[c]["S"],
                 "G /100":  ESG_SCORES[c]["G"],
                 "Total":   ESG_SCORES[c]["Total"],
                 "Rating":  rating_map[c]}
                for c in companies
            ]),
            use_container_width=True, hide_index=True,
        )

    st.markdown("---")
    st.markdown("#### Capability Coverage Matrix")
    st.caption("From Pitch Deck Slide 7 — ElectraWireless is the only company with all 10 capabilities")

    feat_df      = pd.DataFrame(COMPETITOR_FEATURES)
    feature_cols = [c for c in feat_df.columns if c != "Company"]
    z_t          = [[1 if feat_df[col].iloc[r] else 0 for col in feature_cols]
                    for r in range(len(feat_df))]
    text_labels  = [["✅" if v else "❌" for v in row] for row in z_t]

    fig_heat = go.Figure(go.Heatmap(
        z=z_t, x=feature_cols, y=feat_df["Company"].tolist(),
        colorscale=[[0, "#FECACA"], [1, "#D1FAE5"]],
        showscale=False,
        text=text_labels, texttemplate="%{text}", textfont=dict(size=16),
        hovertemplate="%{y} — %{x}<extra></extra>",
    ))
    fig_heat.update_layout(**base_layout(
        height=260, margin=dict(l=160, r=20, t=60, b=20),
        xaxis=dict(tickangle=-20, tickfont=dict(size=11), side="top"),
        yaxis=dict(tickfont=dict(size=11)),
        title=dict(text="Feature Coverage: ✅ = Supported  ❌ = Not supported",
                   font=dict(size=13, color="#4B0082")),
    ))
    st.plotly_chart(fig_heat, use_container_width=True)

    st.markdown("---")
    st.markdown("#### Competitor ESG Rationale")
    st.caption("Why competitors score lower — derived from pitch deck feature comparison")

    comp_notes = {
        "WiTricity": ("60/100 — Advanced",
            "Wireless power only (no heating or AI optimization). Limited sector coverage "
            "(EV + robotics). No documented social programs or community engagement. "
            "More established governance but narrow ESG scope."),
        "Ossia": ("55/100 — Developing",
            "Wireless power with smart app but no heating capability. Limited environmental "
            "impact quantification. No documented health, safety or community programs. "
            "Basic governance structures with limited public ESG disclosure."),
        "Resonant Link": ("57/100 — Developing",
            "Specialises in medical wireless power — positive health impact but narrow "
            "environmental scope. Medical-grade compliance, but limited transparency and "
            "no broader community or environmental programs."),
        "Traditional Players": ("44/100 — Lagging",
            "Cable-based hardware generates significant copper/aluminium waste, high EMF risk, "
            "and energy loss in transmission. Basic governance but no wireless or AI-driven "
            "innovation toward sustainability goals."),
    }
    c1, c2 = st.columns(2)
    for i, (comp, (rating, note)) in enumerate(comp_notes.items()):
        col = c1 if i % 2 == 0 else c2
        with col:
            color = COMP_COLORS.get(comp, "#888")
            st.markdown(
                f"""<div style="border-left:4px solid {color};border-radius:0 8px 8px 0;
                    padding:12px 14px;background:#F9FAFB;margin-bottom:10px;">
                    <div style="font-weight:700;color:{color};font-size:13px;">{comp}</div>
                    <div style="font-size:11px;color:#6B7280;margin:2px 0 6px;">{rating}</div>
                    <div style="font-size:12px;color:#374151;line-height:1.6;">{note}</div>
                </div>""",
                unsafe_allow_html=True,
            )

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.caption(
    "ElectraWireless ESG Dashboard · March 2026 · "
    "All data sourced from ElectraWireless Pitch Deck · "
    "Built for investor presentation"
)
