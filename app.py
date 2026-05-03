"""
ElectraWireless ESG Dashboard — Streamlit Edition (v3 — All fixes applied)
Deploy: streamlit run app.py
"""

import streamlit as st
import plotly.graph_objects as go
import pandas as pd
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

# ── CSS ───────────────────────────────────────────────────────────────────────
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
.section-title { font-size: 20px; font-weight: 700; color: #4B0082; margin-bottom: 4px; }
.section-sub   { font-size: 13px; color: #6B7280; margin-bottom: 16px; }
</style>
""", unsafe_allow_html=True)

# ── Layout helper — no duplicate-key risk ─────────────────────────────────────
def bl(**overrides):
    """Return a Plotly layout dict. Callers override any key without collision."""
    layout = dict(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="sans-serif", color="#1E1B4B"),
        margin=dict(l=60, r=20, t=50, b=60),
    )
    layout.update(overrides)
    return layout

GRID = dict(gridcolor="#F3F0FA", zerolinecolor="#EDE9F8")

def hex_rgba(h, a):
    h = h.lstrip("#")
    r, g, b = int(h[0:2],16), int(h[2:4],16), int(h[4:6],16)
    return f"rgba({r},{g},{b},{a})"

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚡ ElectraWireless")
    st.markdown("**ESG Dashboard · March 2026**")
    st.markdown("---")
    section = st.radio("Navigate", options=[
        "⚡ Overview",
        "🗺️ Materiality Map",
        "📈 Trend Lines",
        "📋 Disclosure Analysis",
        "🎯 KPI Performance",
        "🏆 Competitor Comparison",
    ], label_visibility="collapsed")
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
          <div style="font-size:15px;opacity:0.8;margin-top:6px;">ESG Sustainability Dashboard — March 2026</div>
        </div>
        <div style="text-align:center;">
          <div style="font-size:12px;opacity:0.7;text-transform:uppercase;letter-spacing:1px;">Overall ESG Score</div>
          <div style="font-size:64px;font-weight:800;line-height:1;">{ew['Total']}</div>
          <div style="font-size:14px;opacity:0.6;">/100</div>
          <div style="background:#22C55E;color:white;border-radius:20px;padding:4px 16px;
                      font-size:13px;font-weight:700;display:inline-block;margin-top:8px;">● LEADER</div>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1: st.metric("🌿 Environmental", f"{ew['E']} / 100", "+30 pts since 2022")
    with c2: st.metric("🤝 Social",        f"{ew['S']} / 100", "+30 pts since 2022")
    with c3: st.metric("🏛️ Governance",   f"{ew['G']} / 100", "+34 pts since 2022")

    st.markdown("---")
    st.markdown('<div class="section-title">Pillar Gauges</div>', unsafe_allow_html=True)

    def gauge(label, value, color):
        fig = go.Figure(go.Indicator(
            mode="gauge+number", value=value,
            number={"suffix": "/100", "font": {"size": 22, "color": color}},
            gauge={
                "axis": {"range": [0,100], "tickcolor": "#ccc"},
                "bar":  {"color": color, "thickness": 0.28},
                "bgcolor": "#F3F0FA", "borderwidth": 0,
                "steps": [{"range":[0,40],"color":"#FECACA"},
                           {"range":[40,70],"color":"#FEF3C7"},
                           {"range":[70,100],"color":"#D1FAE5"}],
                "threshold": {"line":{"color":color,"width":3},"value":value},
            },
            title={"text": label, "font": {"size": 14, "color": "#4B0082"}},
        ))
        fig.update_layout(**bl(height=200, margin=dict(l=20,r=20,t=50,b=10)))
        return fig

    g1, g2, g3 = st.columns(3)
    with g1: st.plotly_chart(gauge("🌿 Environmental", ew["E"], "#22C55E"), use_container_width=True)
    with g2: st.plotly_chart(gauge("🤝 Social",        ew["S"], "#3B82F6"), use_container_width=True)
    with g3: st.plotly_chart(gauge("🏛️ Governance",   ew["G"], "#A855F7"), use_container_width=True)

    st.markdown("---")
    st.markdown('<div class="section-title">Why These Scores?</div>', unsafe_allow_html=True)
    st.caption("Rationale derived directly from the ElectraWireless Pitch Deck, March 2026")
    with st.expander("🌿 Environmental — 82 / 100", expanded=True):  st.markdown(ESG_RATIONALE["E"])
    with st.expander("🤝 Social — 78 / 100",        expanded=True):  st.markdown(ESG_RATIONALE["S"])
    with st.expander("🏛️ Governance — 74 / 100",   expanded=True):  st.markdown(ESG_RATIONALE["G"])

    st.markdown("---")
    st.markdown('<div class="section-title">Sustainability Highlights</div>', unsafe_allow_html=True)
    highlights = [
        ("🌱","Eliminates **10,000 tons** of copper & aluminium cable waste **annually**"),
        ("💨","Prevents **77,500 tons of CO₂** emissions per year"),
        ("⚡","**>80% wireless power transfer efficiency** — beats all cable-based alternatives"),
        ("🛡️","Removes fire, shock & short-circuit hazards affecting **80% of households**"),
        ("🤝","**35+ member multinational team** spanning 9 countries across 4 departments"),
        ("🏛️","US-registered with **transparent 6-category funding** disclosure & IPO roadmap"),
        ("🎓","Academic partnerships: **RMIT, HK PolyU, TALim Belgium** + youth competitions"),
        ("🤖","Elly AI ranked **#4 / 163,000+** applications globally (Kaggle Beta 2025)"),
    ]
    cl, cr = st.columns(2)
    for i, (icon, text) in enumerate(highlights):
        with (cl if i % 2 == 0 else cr):
            st.markdown(f'<div class="highlight-item">{icon} &nbsp;{text}</div>', unsafe_allow_html=True)


# ═════════════════════════════════════════════════════════════════════════════
# MATERIALITY MAP
# ═════════════════════════════════════════════════════════════════════════════
elif section == "🗺️ Materiality Map":
    st.markdown('<div class="section-title">Materiality Map</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">ESG topics plotted by Business Impact (x) and Stakeholder Concern (y). '
        'Bubble size reflects priority weight. Top-right = highest priority.</div>',
        unsafe_allow_html=True)

    df = pd.DataFrame(MATERIALITY)
    df["pillar_label"] = df["pillar"].map({"E":"Environmental","S":"Social","G":"Governance"})

    fig = go.Figure()
    for x0,x1,y0,y1,label in [
        (7.5,10.2,7.5,10.2,"HIGH PRIORITY"),(5.8,7.5,7.5,10.2,"MONITOR"),
        (7.5,10.2,6.5,7.5,"ACT"),           (5.8,7.5,6.5,7.5,"LOW PRIORITY"),
    ]:
        fig.add_shape(type="rect",x0=x0,x1=x1,y0=y0,y1=y1,
                      fillcolor="rgba(75,0,130,0.04)",line_width=0,layer="below")
        fig.add_annotation(x=(x0+x1)/2,y=(y0+y1)/2,text=f"<b>{label}</b>",
                           showarrow=False,font=dict(size=9,color="#9CA3AF"),opacity=0.7)
    fig.add_shape(type="line",x0=7.5,x1=7.5,y0=6.5,y1=10.2,
                  line=dict(dash="dot",color="#C4B5D8",width=1.5))
    fig.add_shape(type="line",x0=5.8,x1=10.2,y0=7.5,y1=7.5,
                  line=dict(dash="dot",color="#C4B5D8",width=1.5))
    for pillar, pcolor, plabel in [
        ("E",PILLAR_COLORS["E"],"Environmental"),
        ("S",PILLAR_COLORS["S"],"Social"),
        ("G",PILLAR_COLORS["G"],"Governance"),
    ]:
        sub = df[df["pillar"]==pillar]
        fig.add_trace(go.Scatter(
            x=sub["business_impact"], y=sub["stakeholder_concern"],
            mode="markers+text", name=plabel,
            text=sub["topic"], textposition="top center",
            textfont=dict(size=9,color="#374151"),
            marker=dict(size=sub["bubble_size"],color=pcolor,opacity=0.72,
                        line=dict(color="#fff",width=1.5)),
            hovertemplate="<b>%{text}</b><br>Impact: %{x}<br>Concern: %{y}<extra></extra>",
        ))
    fig.update_layout(**bl(height=520,margin=dict(l=20,r=20,t=40,b=60),
        xaxis=dict(title="Business Impact →",range=[5.8,10.2],**GRID),
        yaxis=dict(title="Stakeholder Concern →",range=[6.5,10.2],**GRID),
        legend=dict(orientation="h",y=-0.12,font=dict(size=12))))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown("#### 🌿 Top Environmental")
        st.markdown("- **CO₂ Footprint Reduction** — highest stakeholder concern (9.8/10)\n"
                    "- **E-Waste & Metal Conservation** — direct product impact (9.5/10)\n"
                    "- **Energy Efficiency & WPT** — core technology differentiator (9.2/10)")
    with c2:
        st.markdown("#### 🤝 Top Social")
        st.markdown("- **Electrical Safety** — eliminates 80% of household hazard exposure (9.0/10)\n"
                    "- **Community Health (Elly)** — free AI health monitoring (8.8/10)\n"
                    "- **Market Accessibility** — products for Boomers & Millennials (8.5/10)")
    with c3:
        st.markdown("#### 🏛️ Top Governance")
        st.markdown("- **Regulatory Compliance** — phase-by-phase roadmap (8.8/10)\n"
                    "- **Investor Transparency** — full 6-category funding disclosure (8.2/10)\n"
                    "- **AI Ethics & Transparency** — Elly AI logs & permissions (8.5/10)")


# ═════════════════════════════════════════════════════════════════════════════
# TREND LINES
# ═════════════════════════════════════════════════════════════════════════════
elif section == "📈 Trend Lines":
    st.markdown('<div class="section-title">ESG Score Trend Lines — 2022 to 2026</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">ElectraWireless shows the steepest improvement trajectory across all three pillars.</div>',
        unsafe_allow_html=True)

    selected_pillars = st.multiselect(
        "Select pillars to display:",
        options=["Environmental (E)","Social (S)","Governance (G)"],
        default=["Environmental (E)","Social (S)","Governance (G)"],
    )
    pillar_map    = {"Environmental (E)":"E","Social (S)":"S","Governance (G)":"G"}
    selected_keys = [pillar_map[p] for p in selected_pillars]

    fig_combined = go.Figure()
    for p, pcolor, plabel in [("E","#22C55E","Environmental"),("S","#3B82F6","Social"),("G","#A855F7","Governance")]:
        if p in selected_keys:
            fig_combined.add_trace(go.Scatter(
                x=YEARS, y=ESG_TRENDS["ElectraWireless"][p],
                name=f"EW {plabel}", mode="lines+markers",
                line=dict(color=pcolor,width=3), marker=dict(size=9),
                fill="tozeroy", fillcolor=hex_rgba(pcolor,0.10),
            ))
    fig_combined.update_layout(**bl(height=320,margin=dict(l=20,r=20,t=50,b=60),
        title=dict(text="ElectraWireless — All Pillars Trend",font=dict(size=15,color="#4B0082")),
        xaxis=dict(tickvals=YEARS,**GRID), yaxis=dict(range=[0,100],title="Score /100",**GRID),
        legend=dict(orientation="h",y=-0.22)))
    st.plotly_chart(fig_combined, use_container_width=True)

    st.markdown("---")
    st.markdown("#### Pillar-by-Pillar vs. Competitors")
    tab_e, tab_s, tab_g = st.tabs(["🌿 Environmental","🤝 Social","🏛️ Governance"])
    for tab, pillar, pcolor, plabel in [
        (tab_e,"E","#22C55E","Environmental"),
        (tab_s,"S","#3B82F6","Social"),
        (tab_g,"G","#A855F7","Governance"),
    ]:
        with tab:
            fig = go.Figure()
            for comp,(col,lw,dash,ms) in {
                "ElectraWireless":(pcolor,3.0,"solid",8),
                "WiTricity":("#0EA5E9",1.8,"dot",5),
                "Ossia":("#F97316",1.8,"dot",5),
                "Traditional":("#9CA3AF",1.8,"dash",5),
            }.items():
                fig.add_trace(go.Scatter(x=YEARS,y=ESG_TRENDS[comp][pillar],name=comp,
                    mode="lines+markers",line=dict(color=col,width=lw,dash=dash),marker=dict(size=ms)))
            fig.update_layout(**bl(height=300,margin=dict(l=20,r=20,t=50,b=70),
                title=dict(text=f"{plabel} Score — EW vs. Competitors",font=dict(size=14,color="#4B0082")),
                xaxis=dict(tickvals=YEARS,**GRID),yaxis=dict(range=[30,100],title="Score /100",**GRID),
                legend=dict(orientation="h",y=-0.30,font=dict(size=11))))
            st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")
    c1, c2, c3 = st.columns(3)
    with c1: st.success("**+30pts Environmental** (52 → 82)\n\nCO₂ quantification, WPT efficiency milestones, university partnerships.")
    with c2: st.info("**+30pts Social** (48 → 78)\n\nElly AI health, 35+ diverse hires, youth competitions in Belgium, HK, Australia.")
    with c3: st.warning("**+34pts Governance** (40 → 74)\n\nUS registration, IPO roadmap, AI ethics framework, transparent seed funding.")


# ═════════════════════════════════════════════════════════════════════════════
# DISCLOSURE ANALYSIS
# ═════════════════════════════════════════════════════════════════════════════
elif section == "📋 Disclosure Analysis":
    st.markdown('<div class="section-title">Disclosure Factor Analysis</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">How transparently ElectraWireless reports across ten key ESG dimensions. '
        'Assessed against pitch deck evidence and startup-stage norms.</div>',
        unsafe_allow_html=True)

    df = pd.DataFrame(DISCLOSURE)
    df_sorted = df.sort_values("Score", ascending=True)
    color_map  = {"green":"#22C55E","yellow":"#F59E0B","orange":"#F97316","red":"#EF4444"}
    bar_colors = [color_map[c] for c in df_sorted["Color"]]

    col_bar, col_radar = st.columns([3, 2])

    with col_bar:
        fig_bar = go.Figure(go.Bar(
            x=df_sorted["Score"], y=df_sorted["Factor"],
            orientation="h", marker_color=bar_colors,
            text=[f"{s}/100" for s in df_sorted["Score"]],
            textposition="inside", textfont=dict(color="#fff",size=11),
            hovertemplate="<b>%{y}</b><br>Score: %{x}/100<extra></extra>",
        ))
        fig_bar.update_layout(**bl(height=400,margin=dict(l=230,r=20,t=50,b=40),
            xaxis=dict(range=[0,100],title="Score / 100",**GRID),
            yaxis=dict(tickfont=dict(size=11)),
            title=dict(text="Disclosure Scores by Factor",font=dict(size=14,color="#4B0082"))))
        st.plotly_chart(fig_bar, use_container_width=True)

    with col_radar:
        # FIX 1 ─ Full unambiguous names, broken into two lines so they fit
        # without truncation on any side of the radar.
        # \n is the Plotly polar axis line-break for angularaxis tick labels.
        DISC_LABELS = [
            "Financial\nTransparency",
            "Environmental Impact\nQuantification",
            "Product Safety\nDisclosures",
            "AI Ethics &\nData Policy",
            "Social Program\nDocumentation",
            "Governance &\nBoard Structure",
            "Stakeholder\nEngagement Reports",
            "Supply Chain\nTransparency",
            "Carbon Accounting\n& Methodology",
            "GRI / SASB\nFormal Reporting",
        ]
        scores = df["Score"].tolist()
        fig_r = go.Figure(go.Scatterpolar(
            r=scores + [scores[0]],
            theta=DISC_LABELS + [DISC_LABELS[0]],
            fill="toself",
            fillcolor="rgba(123,47,190,0.18)",
            line=dict(color="#7B2FBE",width=2.5),
            marker=dict(size=7,color="#4B0082"),
            name="Disclosure Score",
        ))
        fig_r.update_layout(**bl(
            height=460,
            # Extra margin on all sides keeps two-line labels fully visible
            margin=dict(l=100,r=100,t=80,b=100),
            title=dict(text="Disclosure Radar — All 10 Factors",font=dict(size=14,color="#4B0082")),
            polar=dict(
                radialaxis=dict(
                    range=[0,100], tickvals=[20,40,60,80,100],
                    gridcolor="#EDE9F8", tickfont=dict(size=9),
                ),
                angularaxis=dict(
                    tickfont=dict(size=9),
                    rotation=90, direction="clockwise",
                ),
            ),
        ))
        st.plotly_chart(fig_r, use_container_width=True)

    st.markdown("---")
    c1,c2,c3,c4 = st.columns(4)
    with c1: st.markdown("🟢 **Strong (80–100)** — Disclosed & verified")
    with c2: st.markdown("🟡 **Good (65–79)** — Documented, improving")
    with c3: st.markdown("🟠 **Developing (45–64)** — Partial / early stage")
    with c4: st.markdown("🔴 **Gap (<45)** — Missing or informal")

    st.markdown("---")
    st.markdown("#### Status Detail")
    for _, row in df.iterrows():
        dot = {"green":"🟢","yellow":"🟡","orange":"🟠","red":"🔴"}[row["Color"]]
        ca, cb, cc = st.columns([3,1,6])
        with ca: st.markdown(f"**{row['Factor']}**")
        with cb: st.markdown(f"{dot} **{row['Score']}/100**")
        with cc: st.caption(row["Status"])


# ═════════════════════════════════════════════════════════════════════════════
# KPI PERFORMANCE
# ═════════════════════════════════════════════════════════════════════════════
elif section == "🎯 KPI Performance":
    st.markdown('<div class="section-title">Performance Across KPIs</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">ElectraWireless leads on environmental impact metrics. '
        'Social and Governance KPIs advancing rapidly for a seed-stage company.</div>',
        unsafe_allow_html=True)

    df = pd.DataFrame(KPI)
    companies = ["ElectraWireless","WiTricity","Ossia","Resonant Link","Industry Avg"]

    # ── KPI Radar ─────────────────────────────────────────────────────────────
    # HONEST SCORING: each raw value is mapped against a realistic industry
    # CEILING (not against peer-group max) so a company only reaches 100 when
    # it truly achieves best-practice, not merely because it beat this small
    # peer group. ElectraWireless will score high but NOT 100 on every axis,
    # giving stakeholders an accurate and defensible picture.
    #
    # Ceiling rationale (documented for stakeholder Q&A):
    #   CO₂ Reduction       ceiling = 20,000 t  (large industrial WPT target)
    #   E-Waste Prevented   ceiling = 20,000 t  (full cable elimination target)
    #   Energy Efficiency   ceiling = 100 %      (theoretical maximum)
    #   Safety Reduction    ceiling = 100 %      (full hazard elimination)
    #   Green Mkt Coverage  ceiling = 100 %      (all markets green-certified)
    #   Team Diversity      ceiling = 100 %      (fully diverse workforce)
    #   Disclosure Score    ceiling = 100 /100   (full GRI/SASB compliance)
    #   AI Ethics Controls  ceiling = 100 %      (all controls active)
    #   Community Programs  ceiling =   8        (top-tier startup benchmark)

    RADAR_LABELS = [
        "CO₂ Reduction\n(tons/yr)", "E-Waste Prevented\n(tons/yr)",
        "Energy Efficiency\n(%)",   "Safety Incident\nReduction (%)",
        "Green Market\nCoverage (%)","Team Diversity\nIndex (%)",
        "Disclosure\nScore (/100)", "AI Ethics\nControls (%)",
        "Community\nPrograms (#)",
    ]

    # Ceilings aligned to each KPI row order in esg_data.KPI["KPI"]
    CEILINGS = [20000, 20000, 100, 100, 100, 100, 100, 100, 8]

    def absolute_score(raw, ceiling):
        """Map raw value to 0–100 against an absolute ceiling."""
        return round(min(raw / ceiling * 100, 100))

    abs_data = {}
    for comp in companies:
        abs_data[comp] = [
            absolute_score(df[comp].iloc[i], CEILINGS[i])
            for i in range(len(df))
        ]

    fig_radar = go.Figure()
    for comp in companies:
        av = abs_data[comp]; is_ew = comp == "ElectraWireless"
        fig_radar.add_trace(go.Scatterpolar(
            r=av + [av[0]],
            theta=RADAR_LABELS + [RADAR_LABELS[0]],
            name=comp,
            mode="lines" + ("+markers" if is_ew else ""),
            line=dict(color=COMP_COLORS.get(comp, "#888"),
                      width=3.0 if is_ew else 1.5,
                      dash="solid" if is_ew else "dot"),
            fill="toself" if is_ew else None,
            fillcolor="rgba(75,0,130,0.10)" if is_ew else None,
            marker=dict(size=7, color=COMP_COLORS.get(comp, "#888")) if is_ew else None,
            hovertemplate=(
                "<b>" + comp + "</b><br>%{theta}<br>"
                "Score: %{r}/100<extra></extra>"
            ),
        ))

    fig_radar.update_layout(**bl(
        height=520, margin=dict(l=110, r=110, t=100, b=120),
        title=dict(
            text=(
                "KPI Radar — Absolute Performance Score (0–100)<br>"
                "<sup style='font-size:11px;color:#6B7280'>"
                "Each axis scored against an industry best-practice ceiling, "
                "not against peer-group maximum</sup>"
            ),
            font=dict(size=14, color="#4B0082"),
        ),
        polar=dict(
            radialaxis=dict(
                range=[0, 100], tickvals=[25, 50, 75, 100],
                gridcolor="#EDE9F8", tickfont=dict(size=8), tickangle=45,
            ),
            angularaxis=dict(
                tickfont=dict(size=9), rotation=90, direction="clockwise",
            ),
        ),
        legend=dict(orientation="h", y=-0.22, x=0.5, xanchor="center", font=dict(size=10)),
    ))
    st.plotly_chart(fig_radar, use_container_width=True)

    # Scoring methodology callout — so stakeholders understand the chart
    with st.expander("ℹ️ How are radar scores calculated? (click to read methodology)"):
        st.markdown("""
**Each axis uses an absolute ceiling, not peer-group ranking.**

| KPI | ElectraWireless | Ceiling | Score |
|---|---|---|---|
| CO₂ Reduction | 10,000 t/yr | 20,000 t (large WPT target) | **50/100** |
| E-Waste Prevented | 10,000 t/yr | 20,000 t (full cable elimination) | **50/100** |
| Energy Efficiency | 82% | 100% (theoretical max) | **82/100** |
| Safety Incident Reduction | 95% | 100% | **95/100** |
| Green Market Coverage | 78% | 100% | **78/100** |
| Team Diversity Index | 85% | 100% | **85/100** |
| Disclosure Score | 70/100 | 100 (full GRI/SASB) | **70/100** |
| AI Ethics Controls | 90% | 100% | **90/100** |
| Community Programs | 4 | 8 (top-tier startup benchmark) | **50/100** |

> **Why not 100% on every axis?** Because ElectraWireless is a seed-stage startup.
> CO₂ & E-waste savings will scale with each deployment phase. Disclosure will reach
> 100 when formal GRI/SASB reporting is published (planned post-Series A).
> This radar shows honest current performance — strong, but with clear room to grow.
        """)
    st.markdown("---")

    st.markdown("---")

    # FIX 2 ─ Split into TWO separate bar charts so neither scale dominates.
    # Chart A: large-scale metrics (CO₂ reduction & E-waste, units = tons)
    # Chart B: percentage metrics (Energy Efficiency & Green Market Coverage)
    bar_comps = ["ElectraWireless","WiTricity","Ossia","Industry Avg"]

    st.markdown("#### Key ESG KPIs vs. Competitors")
    st.caption("Split into two charts to keep each metric readable at its own scale.")

    col_a, col_b = st.columns(2)

    # ── Chart A: Volume metrics (tons) ───────────────────────────────────────
    with col_a:
        st.markdown("##### 🌿 Volume Impact Metrics (tons/year)")
        vol_kpis = ["CO₂ Reduction (tons/yr)", "E-Waste Prevented (tons/yr)"]
        fig_a = go.Figure()
        for comp in bar_comps:
            y_vals = [df[df["KPI"]==k][comp].values[0] for k in vol_kpis]
            fig_a.add_trace(go.Bar(
                name=comp, x=vol_kpis, y=y_vals,
                marker_color=COMP_COLORS.get(comp,"#888"), opacity=0.88,
                text=[f"{v:,}" for v in y_vals],
                textposition="outside", textfont=dict(size=10),
            ))
        fig_a.update_layout(**bl(height=400,margin=dict(l=20,r=20,t=40,b=80),
            barmode="group",
            xaxis=dict(tickfont=dict(size=11),automargin=True,**GRID),
            yaxis=dict(title="Tons / Year",**GRID),
            title=dict(text="CO₂ Reduction & E-Waste Prevented",font=dict(size=13,color="#4B0082")),
            legend=dict(orientation="h",y=-0.28,font=dict(size=10)),
        ))
        st.plotly_chart(fig_a, use_container_width=True)

    # ── Chart B: Percentage metrics (%) ──────────────────────────────────────
    with col_b:
        st.markdown("##### 📊 Performance Rate Metrics (%)")
        pct_kpis = ["Energy Efficiency (%)", "Green Market Coverage (%)"]
        fig_b = go.Figure()
        for comp in bar_comps:
            y_vals = [df[df["KPI"]==k][comp].values[0] for k in pct_kpis]
            fig_b.add_trace(go.Bar(
                name=comp, x=pct_kpis, y=y_vals,
                marker_color=COMP_COLORS.get(comp,"#888"), opacity=0.88,
                text=[f"{v}%" for v in y_vals],
                textposition="outside", textfont=dict(size=10),
            ))
        fig_b.update_layout(**bl(height=400,margin=dict(l=20,r=20,t=40,b=80),
            barmode="group",
            xaxis=dict(tickfont=dict(size=11),automargin=True,**GRID),
            yaxis=dict(title="%",range=[0,110],**GRID),
            title=dict(text="Energy Efficiency & Green Market Coverage",font=dict(size=13,color="#4B0082")),
            legend=dict(orientation="h",y=-0.28,font=dict(size=10)),
        ))
        st.plotly_chart(fig_b, use_container_width=True)

    st.markdown("---")
    st.markdown("#### KPI Detail Table")
    st.caption("All values from pitch deck. Industry averages from comparable wireless power / cleantech startups.")

    display_rows = []
    for _, row in df.iterrows():
        ew_val, ind_val = row["ElectraWireless"], row["Industry Avg"]
        diff = round(((ew_val-ind_val)/max(ind_val,1))*100)
        display_rows.append({
            "KPI":             row["KPI"],
            "ElectraWireless": f"{ew_val:,} {row['Unit']}",
            "Industry Avg":    f"{ind_val:,}",
            "vs. Industry":    f"▲ +{diff}%" if diff>0 else f"▼ {diff}%",
            "Source":          row["Source"],
        })
    st.dataframe(pd.DataFrame(display_rows), use_container_width=True, hide_index=True,
        column_config={
            "KPI":             st.column_config.TextColumn("KPI",             width="medium"),
            "ElectraWireless": st.column_config.TextColumn("ElectraWireless", width="medium"),
            "vs. Industry":    st.column_config.TextColumn("vs. Industry",    width="small"),
            "Source":          st.column_config.TextColumn("Source",          width="large"),
        })


# ═════════════════════════════════════════════════════════════════════════════
# COMPETITOR COMPARISON
# ═════════════════════════════════════════════════════════════════════════════
elif section == "🏆 Competitor Comparison":
    st.markdown('<div class="section-title">Comparison with Competitors</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-sub">ElectraWireless leads all competitors on Overall ESG score (78/100), '
        'with the only full capability coverage across all 10 product/sector dimensions.</div>',
        unsafe_allow_html=True)

    companies = list(ESG_SCORES.keys())

    # Score cards
    cols = st.columns(len(companies))
    for i, comp in enumerate(companies):
        s = ESG_SCORES[comp]
        rating = ("Leader" if s["Total"]>=75 else "Advanced" if s["Total"]>=60
                  else "Developing" if s["Total"]>=50 else "Lagging")
        rc = ("#3B6D11" if rating=="Leader" else "#185FA5" if rating=="Advanced"
              else "#854F0B" if rating=="Developing" else "#A32D2D")
        is_ew = comp=="ElectraWireless"
        with cols[i]:
            st.markdown(f"""<div style="background:{'#F3F0FA' if is_ew else 'white'};
                border:{'2px solid #4B0082' if is_ew else '1px solid #EDE9F8'};
                border-radius:12px;padding:14px;text-align:center;margin-bottom:8px;">
                <div style="font-size:12px;font-weight:{'700' if is_ew else '500'};
                            color:{'#4B0082' if is_ew else '#6B7280'};">{comp}</div>
                <div style="font-size:30px;font-weight:700;
                            color:{'#4B0082' if is_ew else '#374151'};line-height:1;margin:6px 0;">{s['Total']}</div>
                <div style="font-size:10px;color:#9CA3AF;margin-bottom:6px;">/100 Overall</div>
                <div style="font-size:11px;color:#22C55E;">E: {s['E']}</div>
                <div style="font-size:11px;color:#3B82F6;">S: {s['S']}</div>
                <div style="font-size:11px;color:#A855F7;">G: {s['G']}</div>
                <div style="margin-top:6px;font-size:10px;font-weight:600;color:{rc};">{rating.upper()}</div>
            </div>""", unsafe_allow_html=True)

    st.markdown("---")
    col_chart, col_table = st.columns([3,2])
    with col_chart:
        fig_bar = go.Figure()
        for pillar,pcolor,plabel in [("E","#22C55E","Environmental"),("S","#3B82F6","Social"),("G","#A855F7","Governance")]:
            fig_bar.add_trace(go.Bar(name=plabel, x=companies,
                y=[ESG_SCORES[c][pillar] for c in companies],
                marker_color=pcolor, opacity=0.82))
        fig_bar.update_layout(**bl(height=360,margin=dict(l=20,r=20,t=50,b=60),
            barmode="group",
            xaxis=dict(tickfont=dict(size=11),**GRID),
            yaxis=dict(range=[0,100],title="Score /100",**GRID),
            title=dict(text="ESG Pillar Scores — All Companies",font=dict(size=14,color="#4B0082")),
            legend=dict(orientation="h",y=-0.2)))
        st.plotly_chart(fig_bar, use_container_width=True)
    with col_table:
        rating_map = {c:("Leader" if ESG_SCORES[c]["Total"]>=75 else "Advanced"
                         if ESG_SCORES[c]["Total"]>=60 else "Developing"
                         if ESG_SCORES[c]["Total"]>=50 else "Lagging") for c in companies}
        st.dataframe(pd.DataFrame([
            {"Company":c,"E /100":ESG_SCORES[c]["E"],"S /100":ESG_SCORES[c]["S"],
             "G /100":ESG_SCORES[c]["G"],"Total":ESG_SCORES[c]["Total"],"Rating":rating_map[c]}
            for c in companies]), use_container_width=True, hide_index=True)

    st.markdown("---")
    st.markdown("#### Capability Coverage Matrix")
    st.caption("From Pitch Deck Slide 7 — ElectraWireless is the only company with all 10 capabilities")

    feat_df      = pd.DataFrame(COMPETITOR_FEATURES)
    feature_cols = [c for c in feat_df.columns if c != "Company"]

    # FIX 3 ─ Replace the Plotly heatmap (whose x-axis labels overlap the title)
    # with a native Streamlit dataframe styled as a readable table.
    # The column headers are short (≤14 chars) so they never collide.
    SHORT_LABELS = {
        "Wireless Power":      "Wireless Power",
        "Heating Capability":  "Heating",
        "Smart App & Data":    "Smart App",
        "Foreign Object Det.": "FOD Safety",
        "OEM Customization":   "OEM Custom.",
        "Kitchen Appliances":  "Kitchen",
        "E-Bikes":             "E-Bikes",
        "Robotics":            "Robotics",
        "EV Charging":         "EV Charging",
        "Medical Devices":     "Medical",
    }

    # Build a display dataframe with emoji values
    display_rows = []
    for _, row in feat_df.iterrows():
        d = {"Company": row["Company"]}
        for col in feature_cols:
            d[SHORT_LABELS.get(col, col)] = "✅" if row[col] else "❌"
        display_rows.append(d)

    matrix_df = pd.DataFrame(display_rows)

    # Colour the rows: ElectraWireless row gets a light purple tint
    def style_row(row):
        if row["Company"] == "ElectraWireless":
            return ["background-color:#EDE9F8;font-weight:bold"] * len(row)
        return [""] * len(row)

    styled = matrix_df.style.apply(style_row, axis=1)
    st.dataframe(styled, use_container_width=True, hide_index=True)

    # Legend below the table
    st.markdown(
        "<span style='font-size:13px;'>✅ = Capability supported &nbsp;&nbsp; "
        "❌ = Not supported &nbsp;&nbsp; "
        "<b style='color:#4B0082'>Purple row = ElectraWireless</b></span>",
        unsafe_allow_html=True,
    )

    st.markdown("---")
    st.markdown("#### Competitor ESG Rationale")
    st.caption("Why competitors score lower — derived from pitch deck feature comparison")

    comp_notes = {
        "WiTricity":("60/100 — Advanced",
            "Wireless power only (no heating or AI optimization). Limited sector coverage "
            "(EV + robotics only). No documented social programs or community engagement. "
            "More established governance but a narrow ESG scope overall."),
        "Ossia":("55/100 — Developing",
            "Wireless power with smart app but no heating capability. Limited environmental "
            "impact quantification published. No documented health, safety or community "
            "programs. Basic governance with limited public ESG disclosure."),
        "Resonant Link":("57/100 — Developing",
            "Specialises in medical wireless power — positive health impact but narrow "
            "environmental scope. Medical-grade regulatory compliance, yet limited "
            "transparency and no broader community or environmental programs."),
        "Traditional Players":("44/100 — Lagging",
            "Cable-based hardware generates significant copper/aluminium waste, high EMF "
            "risk, and energy loss in transmission. Basic governance but no wireless or "
            "AI-driven innovation toward sustainability goals."),
    }
    c1, c2 = st.columns(2)
    for i,(comp,(rating,note)) in enumerate(comp_notes.items()):
        col = c1 if i%2==0 else c2
        with col:
            color = COMP_COLORS.get(comp,"#888")
            st.markdown(
                f"""<div style="border-left:4px solid {color};border-radius:0 8px 8px 0;
                    padding:12px 14px;background:#F9FAFB;margin-bottom:10px;">
                    <div style="font-weight:700;color:{color};font-size:13px;">{comp}</div>
                    <div style="font-size:11px;color:#6B7280;margin:2px 0 6px;">{rating}</div>
                    <div style="font-size:12px;color:#374151;line-height:1.6;">{note}</div>
                </div>""", unsafe_allow_html=True)


# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.caption(
    "ElectraWireless ESG Dashboard · March 2026 · "
    "All data sourced from ElectraWireless Pitch Deck · Built for investor presentation"
)
