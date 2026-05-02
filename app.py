"""
ElectraWireless ESG Dashboard — Streamlit Edition
Deploy via: streamlit run app.py
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from esg_data import (
    ESG_SCORES, ESG_RATIONALE, ESG_TRENDS, YEARS,
    MATERIALITY, DISCLOSURE, KPI, COMPETITOR_FEATURES,
    COLORS, COMP_COLORS, PILLAR_COLORS,
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
/* Sidebar */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #2D0057 0%, #3C3489 100%);
}
[data-testid="stSidebar"] * { color: rgba(255,255,255,0.85) !important; }
[data-testid="stSidebar"] .stRadio label { font-size: 14px !important; }

/* Metric cards */
div[data-testid="metric-container"] {
    background: #FFFFFF;
    border: 1px solid #EDE9F8;
    border-radius: 12px;
    padding: 16px !important;
    box-shadow: 0 2px 12px rgba(75,0,130,0.06);
}

/* Score highlight boxes */
.score-box {
    text-align: center;
    padding: 20px;
    border-radius: 16px;
    margin-bottom: 8px;
}
.hero-banner {
    background: linear-gradient(135deg, #2D0057 0%, #4B0082 60%, #7B2FBE 100%);
    border-radius: 16px;
    padding: 32px 36px;
    color: white;
    margin-bottom: 24px;
}
.rationale-card {
    border-radius: 12px;
    padding: 18px;
    margin-bottom: 12px;
    border-left: 4px solid;
}
.highlight-item {
    background: #F8F5FF;
    border-radius: 10px;
    padding: 10px 14px;
    margin-bottom: 8px;
    font-size: 14px;
    border: 1px solid #EDE9F8;
}
/* Data table */
.dataframe { font-size: 12px !important; }
/* Section dividers */
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

# ── Plotly shared layout ──────────────────────────────────────────────────────
LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="sans-serif", color="#1E1B4B"),
    margin=dict(l=10, r=10, t=40, b=10),
)

GRID = dict(gridcolor="#F3F0FA", zerolinecolor="#EDE9F8")


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
# SECTION: OVERVIEW
# ═════════════════════════════════════════════════════════════════════════════
if section == "⚡ Overview":
    ew = ESG_SCORES["ElectraWireless"]

    # Hero banner
    st.markdown(f"""
    <div class="hero-banner">
        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:16px;">
            <div>
                <div style="font-size:13px; opacity:0.7; text-transform:uppercase; letter-spacing:1px; margin-bottom:6px;">
                    AI-Driven Wireless Electricity · Seed Stage
                </div>
                <div style="font-size:42px; font-weight:800; line-height:1;">ElectraWireless</div>
                <div style="font-size:15px; opacity:0.8; margin-top:6px;">
                    ESG Sustainability Dashboard — March 2026
                </div>
            </div>
            <div style="text-align:center;">
                <div style="font-size:12px; opacity:0.7; text-transform:uppercase; letter-spacing:1px;">Overall ESG Score</div>
                <div style="font-size:64px; font-weight:800; line-height:1;">{ew['Total']}</div>
                <div style="font-size:14px; opacity:0.6;">/100</div>
                <div style="background:#22C55E; color:white; border-radius:20px; padding:4px 16px;
                            font-size:13px; font-weight:700; display:inline-block; margin-top:8px;">
                    ● LEADER
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Pillar scores
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("🌿 Environmental", f"{ew['E']} / 100", "+30 pts since 2022")
    with c2:
        st.metric("🤝 Social", f"{ew['S']} / 100", "+30 pts since 2022")
    with c3:
        st.metric("🏛️ Governance", f"{ew['G']} / 100", "+34 pts since 2022")

    st.markdown("---")

    # Gauge charts
    st.markdown('<div class="section-title">Pillar Gauges</div>', unsafe_allow_html=True)

    def gauge(label, value, color):
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=value,
            number={"suffix": "/100", "font": {"size": 22, "color": color}},
            gauge={
                "axis": {"range": [0, 100], "tickcolor": "#ccc"},
                "bar": {"color": color, "thickness": 0.28},
                "bgcolor": "#F3F0FA",
                "borderwidth": 0,
                "steps": [
                    {"range": [0, 40],  "color": "#FECACA"},
                    {"range": [40, 70], "color": "#FEF3C7"},
                    {"range": [70, 100],"color": "#D1FAE5"},
                ],
                "threshold": {"line": {"color": color, "width": 3}, "value": value},
            },
            title={"text": label, "font": {"size": 14, "color": "#4B0082"}},
        ))
        fig.update_layout(**LAYOUT, height=200, margin=dict(l=20, r=20, t=50, b=10))
        return fig

    g1, g2, g3 = st.columns(3)
    with g1:
        st.plotly_chart(gauge("🌿 Environmental", ew["E"], "#22C55E"), use_container_width=True)
    with g2:
        st.plotly_chart(gauge("🤝 Social", ew["S"], "#3B82F6"), use_container_width=True)
    with g3:
        st.plotly_chart(gauge("🏛️ Governance", ew["G"], "#A855F7"), use_container_width=True)

    st.markdown("---")

    # Score rationale
    st.markdown('<div class="section-title">Why These Scores?</div>', unsafe_allow_html=True)
    st.caption("Rationale derived directly from the ElectraWireless Pitch Deck, March 2026")

    with st.expander("🌿 Environmental — 82 / 100  ·  Click to expand rationale", expanded=True):
        st.markdown(ESG_RATIONALE["E"])

    with st.expander("🤝 Social — 78 / 100  ·  Click to expand rationale", expanded=True):
        st.markdown(ESG_RATIONALE["S"])

    with st.expander("🏛️ Governance — 74 / 100  ·  Click to expand rationale", expanded=True):
        st.markdown(ESG_RATIONALE["G"])

    st.markdown("---")

    # Highlights
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
    c_left, c_right = st.columns(2)
    for i, (icon, text) in enumerate(highlights):
        col = c_left if i % 2 == 0 else c_right
        with col:
            st.markdown(
                f'<div class="highlight-item">{icon} &nbsp;{text}</div>',
                unsafe_allow_html=True,
            )


# ═════════════════════════════════════════════════════════════════════════════
# SECTION: MATERIALITY MAP
# ═════════════════════════════════════════════════════════════════════════════
elif section == "🗺️ Materiality Map":
    st.markdown('<div class="section-title">Materiality Map</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">ESG topics plotted by Business Impact (x-axis) and Stakeholder Concern (y-axis). '
        'Bubble size reflects priority weight. Top-right quadrant = highest priority for disclosure and action.</div>',
        unsafe_allow_html=True,
    )

    df = pd.DataFrame(MATERIALITY)
    df["color"] = df["pillar"].map(PILLAR_COLORS)
    df["pillar_label"] = df["pillar"].map({"E": "Environmental", "S": "Social", "G": "Governance"})

    fig = go.Figure()

    # Quadrant backgrounds
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

    # Quadrant lines
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
            x=sub["business_impact"],
            y=sub["stakeholder_concern"],
            mode="markers+text",
            name=plabel,
            text=sub["topic"],
            textposition="top center",
            textfont=dict(size=9, color="#374151"),
            marker=dict(
                size=sub["bubble_size"],
                color=pcolor,
                opacity=0.72,
                line=dict(color="#fff", width=1.5),
            ),
            hovertemplate="<b>%{text}</b><br>Business Impact: %{x}<br>Stakeholder Concern: %{y}<extra></extra>",
        ))

    fig.update_layout(
        **LAYOUT,
        height=520,
        xaxis=dict(title="Business Impact →", range=[5.8, 10.2], **GRID),
        yaxis=dict(title="Stakeholder Concern →", range=[6.5, 10.2], **GRID),
        legend=dict(orientation="h", y=-0.12, font=dict(size=12)),
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 🌿 Top Environmental Topics")
        st.markdown("""
- **CO₂ Footprint Reduction** — highest stakeholder concern (9.8/10)
- **E-Waste & Metal Conservation** — direct product impact (9.5/10)
- **Energy Efficiency & WPT** — core technology differentiator (9.2/10)
        """)
    with c2:
        st.markdown("#### 🤝 Top Social Topics")
        st.markdown("""
- **Electrical Safety** — eliminates 80% of household hazard exposure (9.0/10)
- **Community Health (Elly)** — free AI health monitoring for all users (8.8/10)
- **Market Accessibility** — products for Boomers & Millennials (8.5/10)
        """)
    with c3:
        st.markdown("#### 🏛️ Top Governance Topics")
        st.markdown("""
- **Regulatory Compliance** — phase-by-phase roadmap across 5 phases (8.8/10)
- **Investor Transparency** — full 6-category funding disclosure (8.2/10)
- **AI Ethics & Transparency** — Elly AI logs & permissions controls (8.5/10)
        """)


# ═════════════════════════════════════════════════════════════════════════════
# SECTION: TREND LINES
# ═════════════════════════════════════════════════════════════════════════════
elif section == "📈 Trend Lines":
    st.markdown('<div class="section-title">ESG Score Trend Lines — 2022 to 2026</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">ElectraWireless shows the steepest improvement trajectory across all three pillars, '
        'driven by product launches, partnership milestones, and growing environmental impact data.</div>',
        unsafe_allow_html=True,
    )

    # Pillar selector
    selected_pillars = st.multiselect(
        "Select pillars to display:",
        options=["Environmental (E)", "Social (S)", "Governance (G)"],
        default=["Environmental (E)", "Social (S)", "Governance (G)"],
    )
    pillar_map = {"Environmental (E)": "E", "Social (S)": "S", "Governance (G)": "G"}
    selected_keys = [pillar_map[p] for p in selected_pillars]

    # Combined ElectraWireless trend
    fig_combined = go.Figure()
    for p, pcolor, plabel in [("E","#22C55E","Environmental"), ("S","#3B82F6","Social"), ("G","#A855F7","Governance")]:
        if p in selected_keys:
            fig_combined.add_trace(go.Scatter(
                x=YEARS, y=ESG_TRENDS["ElectraWireless"][p],
                name=f"EW {plabel}", mode="lines+markers",
                line=dict(color=pcolor, width=3),
                marker=dict(size=9, symbol="circle"),
                fill="tozeroy", fillcolor=f"{pcolor}18",
            ))
    fig_combined.update_layout(
        **LAYOUT, height=320,
        title=dict(text="ElectraWireless — All Pillars", font=dict(size=15, color="#4B0082")),
        xaxis=dict(tickvals=YEARS, **GRID),
        yaxis=dict(range=[0, 100], title="Score /100", **GRID),
        legend=dict(orientation="h", y=-0.2),
    )
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
                "ElectraWireless":    (pcolor, 3.0, "solid", 8),
                "WiTricity":          ("#0EA5E9", 1.8, "dot", 5),
                "Ossia":              ("#F97316", 1.8, "dot", 5),
                "Traditional":        ("#9CA3AF", 1.8, "dash", 5),
            }
            for comp, (col, lw, dash, ms) in comp_styles.items():
                fig.add_trace(go.Scatter(
                    x=YEARS, y=ESG_TRENDS[comp][pillar],
                    name=comp, mode="lines+markers",
                    line=dict(color=col, width=lw, dash=dash),
                    marker=dict(size=ms),
                ))
            fig.update_layout(
                **LAYOUT, height=300,
                title=dict(text=f"{plabel} Score — EW vs. Competitors", font=dict(size=14, color="#4B0082")),
                xaxis=dict(tickvals=YEARS, **GRID),
                yaxis=dict(range=[30, 100], title="Score /100", **GRID),
                legend=dict(orientation="h", y=-0.25, font=dict(size=11)),
            )
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
# SECTION: DISCLOSURE ANALYSIS
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

    color_map = {"green": "#22C55E", "yellow": "#F59E0B", "orange": "#F97316", "red": "#EF4444"}
    bar_colors = [color_map[c] for c in df_sorted["Color"]]

    col_bar, col_radar = st.columns([3, 2])
    with col_bar:
        fig_bar = go.Figure(go.Bar(
            x=df_sorted["Score"],
            y=df_sorted["Factor"],
            orientation="h",
            marker_color=bar_colors,
            text=[f"{s}/100" for s in df_sorted["Score"]],
            textposition="inside",
            textfont=dict(color="#fff", size=11),
            hovertemplate="<b>%{y}</b><br>Score: %{x}/100<extra></extra>",
        ))
        fig_bar.update_layout(
            **LAYOUT, height=380,
            xaxis=dict(range=[0, 100], title="Score / 100", **GRID),
            yaxis=dict(tickfont=dict(size=11)),
            title=dict(text="Disclosure Scores by Factor", font=dict(size=14, color="#4B0082")),
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with col_radar:
        fig_radar = go.Figure(go.Scatterpolar(
            r=df["Score"].tolist() + [df["Score"].iloc[0]],
            theta=df["Factor"].tolist() + [df["Factor"].iloc[0]],
            fill="toself",
            fillcolor="rgba(123,47,190,0.18)",
            line=dict(color="#7B2FBE", width=2.5),
            marker=dict(size=6, color="#4B0082"),
        ))
        fig_radar.update_layout(
            **LAYOUT, height=380,
            polar=dict(
                radialaxis=dict(range=[0, 100], gridcolor="#EDE9F8", tickfont=dict(size=9)),
                angularaxis=dict(tickfont=dict(size=9)),
            ),
            title=dict(text="Disclosure Radar", font=dict(size=14, color="#4B0082")),
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    st.markdown("---")

    # Legend
    c1, c2, c3, c4 = st.columns(4)
    with c1: st.markdown("🟢 **Strong (80–100)** — Disclosed & verified")
    with c2: st.markdown("🟡 **Good (65–79)** — Documented, improving")
    with c3: st.markdown("🟠 **Developing (45–64)** — Partial or early stage")
    with c4: st.markdown("🔴 **Gap (<45)** — Missing or informal")

    st.markdown("---")
    st.markdown("#### Status Detail")

    for _, row in df.iterrows():
        dot = {"green": "🟢", "yellow": "🟡", "orange": "🟠", "red": "🔴"}[row["Color"]]
        col_a, col_b, col_c = st.columns([3, 1, 6])
        with col_a:
            st.markdown(f"**{row['Factor']}**")
        with col_b:
            st.markdown(f"{dot} **{row['Score']}/100**")
        with col_c:
            st.caption(row["Status"])


# ═════════════════════════════════════════════════════════════════════════════
# SECTION: KPI PERFORMANCE
# ═════════════════════════════════════════════════════════════════════════════
elif section == "🎯 KPI Performance":
    st.markdown('<div class="section-title">Performance Across KPIs</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">ElectraWireless leads on environmental impact metrics. Social and Governance KPIs are '
        'advancing rapidly for a company at seed stage.</div>',
        unsafe_allow_html=True,
    )

    df = pd.DataFrame(KPI)
    companies = ["ElectraWireless", "WiTricity", "Ossia", "Resonant Link", "Industry Avg"]

    # Normalise for radar
    def normalise(vals):
        mn, mx = min(vals), max(vals)
        if mx == mn:
            return [50] * len(vals)
        return [round((v - mn) / (mx - mn) * 100) for v in vals]

    col_radar, col_bar = st.columns([1, 1])
    with col_radar:
        fig_radar = go.Figure()
        for comp in companies:
            raw = df[comp].tolist()
            norm = normalise([df[c].tolist()[i] for c in companies for i in range(len(raw))
                              if False] + raw)
            # Proper normalise per KPI row
            norm_vals = []
            for i, kpi in enumerate(df["KPI"]):
                row_vals = [df[c].iloc[i] for c in companies]
                mn, mx = min(row_vals), max(row_vals)
                v = df[comp].iloc[i]
                norm_vals.append(round((v - mn) / (mx - mn) * 100) if mx != mn else 50)

            lw = 3 if comp == "ElectraWireless" else 1.5
            fig_radar.add_trace(go.Scatterpolar(
                r=norm_vals + [norm_vals[0]],
                theta=df["KPI"].tolist() + [df["KPI"].iloc[0]],
                name=comp,
                mode="lines" + ("+markers" if comp == "ElectraWireless" else ""),
                line=dict(color=COMP_COLORS.get(comp, "#888"), width=lw,
                          dash="solid" if comp == "ElectraWireless" else "dot"),
                fill="toself" if comp == "ElectraWireless" else None,
                fillcolor="rgba(75,0,130,0.10)" if comp == "ElectraWireless" else None,
            ))
        fig_radar.update_layout(
            **LAYOUT, height=400,
            polar=dict(
                radialaxis=dict(range=[0, 100], gridcolor="#EDE9F8", tickfont=dict(size=8),
                                tickvals=[25, 50, 75, 100]),
                angularaxis=dict(tickfont=dict(size=9)),
            ),
            title=dict(text="KPI Radar — Normalised Scores", font=dict(size=14, color="#4B0082")),
            legend=dict(orientation="v", x=1.05, font=dict(size=10)),
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    with col_bar:
        bar_kpis = ["CO₂ Reduction (tons/yr)", "E-Waste Prevented (tons/yr)",
                    "Energy Efficiency (%)", "Green Market Coverage (%)"]
        fig_bar = go.Figure()
        for comp in ["ElectraWireless", "WiTricity", "Ossia", "Industry Avg"]:
            y_vals = [df[df["KPI"] == k][comp].values[0] for k in bar_kpis]
            fig_bar.add_trace(go.Bar(
                name=comp, x=bar_kpis, y=y_vals,
                marker_color=COMP_COLORS.get(comp, "#888"),
                opacity=0.85,
            ))
        fig_bar.update_layout(
            **LAYOUT, height=400, barmode="group",
            xaxis=dict(tickangle=-15, tickfont=dict(size=10), **GRID),
            yaxis=dict(**GRID),
            title=dict(text="Key ESG KPIs vs. Competitors", font=dict(size=14, color="#4B0082")),
            legend=dict(orientation="h", y=-0.3, font=dict(size=10)),
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    st.markdown("---")
    st.markdown("#### KPI Detail Table")
    st.caption("All values sourced from pitch deck. Industry averages estimated from comparable wireless power / cleantech startups.")

    display_rows = []
    for _, row in df.iterrows():
        ew_val = row["ElectraWireless"]
        ind_val = row["Industry Avg"]
        diff_pct = round(((ew_val - ind_val) / max(ind_val, 1)) * 100)
        arrow = f"▲ +{diff_pct}%" if diff_pct > 0 else f"▼ {diff_pct}%"
        display_rows.append({
            "KPI": row["KPI"],
            "ElectraWireless": f"{ew_val:,} {row['Unit']}",
            "Industry Avg": f"{ind_val:,}",
            "vs. Industry": arrow,
            "Source": row["Source"],
        })

    display_df = pd.DataFrame(display_rows)
    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "KPI": st.column_config.TextColumn("KPI", width="medium"),
            "ElectraWireless": st.column_config.TextColumn("ElectraWireless", width="medium"),
            "vs. Industry": st.column_config.TextColumn("vs. Industry", width="small"),
            "Source": st.column_config.TextColumn("Source", width="large"),
        },
    )


# ═════════════════════════════════════════════════════════════════════════════
# SECTION: COMPETITOR COMPARISON
# ═════════════════════════════════════════════════════════════════════════════
elif section == "🏆 Competitor Comparison":
    st.markdown('<div class="section-title">Comparison with Competitors</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">ElectraWireless leads all competitors on Overall ESG score (78/100), '
        'with particular strength in Environmental impact. The only company with all 10 product/sector capabilities.</div>',
        unsafe_allow_html=True,
    )

    companies = list(ESG_SCORES.keys())

    # Score summary cards
    cols = st.columns(len(companies))
    for i, comp in enumerate(companies):
        s = ESG_SCORES[comp]
        rating = ("Leader" if s["Total"] >= 75 else
                  "Advanced" if s["Total"] >= 60 else
                  "Developing" if s["Total"] >= 50 else "Lagging")
        with cols[i]:
            is_ew = comp == "ElectraWireless"
            st.markdown(
                f"""<div style="background:{'#F3F0FA' if is_ew else 'white'};
                    border:{'2px solid #4B0082' if is_ew else '1px solid #EDE9F8'};
                    border-radius:12px; padding:14px; text-align:center; margin-bottom:8px;">
                    <div style="font-size:12px; font-weight:{'700' if is_ew else '500'};
                                color:{'#4B0082' if is_ew else '#6B7280'};">{comp}</div>
                    <div style="font-size:30px; font-weight:700; color:{'#4B0082' if is_ew else '#374151'};
                                line-height:1; margin:6px 0;">{s['Total']}</div>
                    <div style="font-size:10px; color:#9CA3AF; margin-bottom:6px;">/100 Overall</div>
                    <div style="font-size:11px; color:#22C55E;">E:{s['E']}</div>
                    <div style="font-size:11px; color:#3B82F6;">S:{s['S']}</div>
                    <div style="font-size:11px; color:#A855F7;">G:{s['G']}</div>
                    <div style="margin-top:6px; font-size:10px; font-weight:600;
                                color:{'#3B6D11' if rating=='Leader' else '#185FA5' if rating=='Advanced' else '#854F0B' if rating=='Developing' else '#A32D2D'};">
                        {rating.upper()}
                    </div>
                </div>""",
                unsafe_allow_html=True,
            )

    st.markdown("---")

    # Grouped bar
    col_chart, col_table = st.columns([3, 2])
    with col_chart:
        fig_bar = go.Figure()
        for pillar, pcolor, plabel in [("E","#22C55E","Environmental"), ("S","#3B82F6","Social"), ("G","#A855F7","Governance")]:
            fig_bar.add_trace(go.Bar(
                name=plabel,
                x=companies,
                y=[ESG_SCORES[c][pillar] for c in companies],
                marker_color=pcolor, opacity=0.82,
            ))
        fig_bar.update_layout(
            **LAYOUT, height=360, barmode="group",
            xaxis=dict(tickfont=dict(size=11), **GRID),
            yaxis=dict(range=[0, 100], title="Score /100", **GRID),
            title=dict(text="ESG Pillar Scores — All Companies", font=dict(size=14, color="#4B0082")),
            legend=dict(orientation="h", y=-0.2),
        )
        st.plotly_chart(fig_bar, use_container_width=True)

    with col_table:
        rating_map = {c: ("Leader" if ESG_SCORES[c]["Total"] >= 75 else
                          "Advanced" if ESG_SCORES[c]["Total"] >= 60 else
                          "Developing" if ESG_SCORES[c]["Total"] >= 50 else "Lagging")
                      for c in companies}
        score_df = pd.DataFrame([
            {"Company": c,
             "E /100": ESG_SCORES[c]["E"],
             "S /100": ESG_SCORES[c]["S"],
             "G /100": ESG_SCORES[c]["G"],
             "Total": ESG_SCORES[c]["Total"],
             "Rating": rating_map[c]}
            for c in companies
        ])
        st.dataframe(score_df, use_container_width=True, hide_index=True)

    st.markdown("---")

    # Capability heatmap
    st.markdown("#### Capability Coverage Matrix")
    st.caption("From Pitch Deck Slide 7 — ElectraWireless is the only company with all 10 capabilities")

    feat_df = pd.DataFrame(COMPETITOR_FEATURES)
    feature_cols = [c for c in feat_df.columns if c != "Company"]
    z_numeric = [[1 if v else 0 for v in feat_df[col]] for col in feature_cols]
    z_t = list(map(list, zip(*z_numeric)))

    text_labels = [["✅" if v else "❌" for v in row] for row in z_t]

    fig_heat = go.Figure(go.Heatmap(
        z=z_t,
        x=feature_cols,
        y=feat_df["Company"].tolist(),
        colorscale=[[0, "#FECACA"], [1, "#D1FAE5"]],
        showscale=False,
        text=text_labels,
        texttemplate="%{text}",
        textfont=dict(size=16),
        hovertemplate="%{y} — %{x}<extra></extra>",
    ))
    fig_heat.update_layout(
        **LAYOUT, height=250,
        xaxis=dict(tickangle=-20, tickfont=dict(size=11), side="top"),
        yaxis=dict(tickfont=dict(size=11)),
        title=dict(text="Feature Coverage: ✅ = Supported  ❌ = Not supported",
                   font=dict(size=13, color="#4B0082")),
    )
    st.plotly_chart(fig_heat, use_container_width=True)

    st.markdown("---")
    st.markdown("#### Competitor ESG Rationale")
    st.caption("Why competitors score lower — derived from pitch deck feature comparison")

    comp_notes = {
        "WiTricity":          ("60/100 — Advanced", "Wireless power only (no heating or AI optimization). "
                               "Limited sector coverage (EV + robotics). No documented social programs or community engagement. "
                               "More established governance but narrow ESG scope."),
        "Ossia":              ("55/100 — Developing", "Wireless power with smart app but no heating capability. "
                               "Limited environmental impact quantification. No documented health, safety or community programs. "
                               "Basic governance structures with limited public ESG disclosure."),
        "Resonant Link":      ("57/100 — Developing", "Specialises in medical wireless power — positive health impact "
                               "but narrow environmental scope. Medical-grade regulatory compliance, but limited "
                               "transparency and no broader community or environmental programs."),
        "Traditional Players":("44/100 — Lagging", "Cable-based hardware generates significant copper/aluminium waste, "
                               "high EMF risk, and energy loss in transmission. Larger companies with basic governance "
                               "but no wireless or AI-driven innovation toward sustainability goals."),
    }
    c1, c2 = st.columns(2)
    for i, (comp, (rating, note)) in enumerate(comp_notes.items()):
        col = c1 if i % 2 == 0 else c2
        with col:
            color = COMP_COLORS.get(comp, "#888")
            st.markdown(
                f"""<div style="border-left:4px solid {color}; border-radius:0 8px 8px 0;
                    padding:12px 14px; background:#F9FAFB; margin-bottom:10px;">
                    <div style="font-weight:700; color:{color}; font-size:13px;">{comp}</div>
                    <div style="font-size:11px; color:#6B7280; margin:2px 0 6px;">{rating}</div>
                    <div style="font-size:12px; color:#374151; line-height:1.6;">{note}</div>
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
