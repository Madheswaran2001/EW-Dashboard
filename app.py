<h2 class="sr-only">ElectraWireless ESG Dashboard 2026 — interactive six-tab dashboard showing Environmental (88), Social (82), and Governance (79) scores with charts, breakdowns, and competitive comparison.</h2>

<style>
  .ew-header { background: linear-gradient(135deg, #1C2951 0%, #028090 100%); padding: 20px 28px; display: flex; align-items: center; justify-content: space-between; border-radius: var(--border-radius-lg) var(--border-radius-lg) 0 0; }
  .ew-logo { color: #fff; font-size: 18px; font-weight: 500; letter-spacing: 0.3px; }
  .ew-sub { color: rgba(255,255,255,0.7); font-size: 12px; margin-top: 3px; }
  .ew-badge { background: #02C39A; color: #1C2951; font-weight: 500; font-size: 18px; padding: 5px 16px; border-radius: 8px; }
  .ew-tabs { display: flex; background: #fff; border-bottom: 0.5px solid var(--color-border-tertiary); overflow-x: auto; }
  .ew-tab { padding: 12px 18px; font-size: 13px; font-weight: 400; color: var(--color-text-secondary); cursor: pointer; white-space: nowrap; border-bottom: 3px solid transparent; transition: all 0.2s; }
  .ew-tab:hover { color: #028090; }
  .ew-tab.active { color: #028090; border-bottom-color: #028090; font-weight: 500; }
  .ew-content { padding: 24px; background: #f4f9fb; min-height: 520px; }
  .ew-grid2 { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px; }
  .ew-grid4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 16px; }
  .ew-grid3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px; margin-bottom: 16px; }
  .card { background: #fff; border-radius: var(--border-radius-lg); border: 0.5px solid var(--color-border-tertiary); padding: 20px; }
  .kpi-card { background: #fff; border-radius: var(--border-radius-lg); border: 0.5px solid var(--color-border-tertiary); padding: 16px; text-align: center; }
  .kpi-val { font-size: 28px; font-weight: 500; line-height: 1; }
  .kpi-label { font-size: 11px; color: var(--color-text-secondary); margin-top: 5px; line-height: 1.4; }
  .sec-title { font-size: 11px; font-weight: 500; text-transform: uppercase; letter-spacing: 1px; color: var(--color-text-secondary); margin-bottom: 14px; }
  .bar-wrap { background: #e8f4f8; border-radius: 8px; height: 7px; margin: 6px 0; overflow: hidden; }
  .bar-fill { height: 7px; border-radius: 8px; }
  .score-row { margin-bottom: 14px; }
  .score-label { font-size: 13px; font-weight: 500; color: var(--color-text-primary); }
  .score-num { font-size: 22px; font-weight: 500; }
  .score-reason { font-size: 11px; color: var(--color-text-secondary); line-height: 1.5; margin-top: 3px; }
  .initiative { border-left: 3px solid #02C39A; padding: 10px 14px; background: #f4f9fb; border-radius: 0 8px 8px 0; margin-bottom: 8px; }
  .init-title { font-size: 13px; font-weight: 500; color: var(--color-text-primary); }
  .init-desc { font-size: 12px; color: var(--color-text-secondary); line-height: 1.5; margin-top: 3px; }
  .check-row { display: flex; align-items: center; gap: 10px; padding: 10px 12px; background: #f4f9fb; border-radius: 8px; margin-bottom: 7px; border-left: 3px solid #02C39A; }
  .check-label { font-size: 13px; font-weight: 500; color: var(--color-text-primary); flex: 1; }
  .check-status { font-size: 11px; font-weight: 500; color: #028090; }
  .partner-row { display: flex; align-items: center; gap: 10px; padding: 10px 14px; background: #f4f9fb; border-radius: 8px; margin-bottom: 7px; }
  .mat-pill { display: inline-block; padding: 3px 10px; border-radius: 20px; font-size: 11px; font-weight: 500; margin-bottom: 6px; }
  .comp-bar { display: flex; align-items: center; gap: 10px; margin-bottom: 8px; }
  .comp-name { font-size: 12px; width: 120px; flex-shrink: 0; color: var(--color-text-primary); }
  .comp-track { flex: 1; background: #e8f4f8; border-radius: 4px; height: 20px; overflow: hidden; position: relative; }
  .comp-fill { height: 20px; border-radius: 4px; display: flex; align-items: center; padding-left: 8px; font-size: 11px; font-weight: 500; color: #fff; transition: width 0.8s ease; }
  .feat-table { width: 100%; border-collapse: collapse; font-size: 12px; }
  .feat-table th { background: #1C2951; color: #fff; padding: 8px 10px; font-weight: 500; text-align: center; }
  .feat-table th:first-child { text-align: left; }
  .feat-table th.ew-col { background: #028090; }
  .feat-table td { padding: 9px 10px; border-bottom: 0.5px solid var(--color-border-tertiary); text-align: center; }
  .feat-table td:first-child { text-align: left; font-weight: 500; color: var(--color-text-primary); }
  .feat-table tr:nth-child(even) td { background: #f9fcfd; }
  .tick { color: #028090; font-size: 16px; font-weight: 500; }
  .cross { color: #cdd3da; font-size: 16px; }
  .ew-tick { color: #fff; font-size: 16px; font-weight: 500; background: #028090; padding: 0 6px; border-radius: 4px; }
  .mat-topic { padding: 12px 14px; background: #f4f9fb; border-radius: 8px; margin-bottom: 8px; }
  .mat-rank { background: #028090; color: #fff; font-size: 11px; font-weight: 500; padding: 2px 8px; border-radius: 4px; margin-right: 8px; }
  .mat-rank.top { background: #1C2951; }
  canvas { display: block; }
  @media (max-width: 600px) { .ew-grid2, .ew-grid4, .ew-grid3 { grid-template-columns: 1fr; } }
</style>

<div style="border-radius: var(--border-radius-lg); overflow: hidden; border: 0.5px solid var(--color-border-tertiary);">

  <div class="ew-header">
    <div>
      <div class="ew-logo">⚡ ElectraWireless</div>
      <div class="ew-sub">ESG &amp; Sustainability Dashboard · Q1 2026</div>
    </div>
    <div style="text-align:right">
      <div style="font-size:11px;color:rgba(255,255,255,0.7);margin-bottom:4px;">ESG Rating</div>
      <div class="ew-badge">AA</div>
    </div>
  </div>

  <div class="ew-tabs" id="tabs">
    <div class="ew-tab active" data-tab="overview">📊 Overview</div>
    <div class="ew-tab" data-tab="environmental">🌿 Environmental</div>
    <div class="ew-tab" data-tab="social">🤝 Social</div>
    <div class="ew-tab" data-tab="governance">🏛 Governance</div>
    <div class="ew-tab" data-tab="materiality">🎯 Materiality</div>
    <div class="ew-tab" data-tab="competitive">🏆 Competitive</div>
  </div>

  <div class="ew-content" id="content"></div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.js"></script>
<script>
const TEAL = '#028090', MINT = '#02C39A', NAVY = '#1C2951', WARN = '#E24B4A';
const ENV_C = '#02C39A', SOC_C = '#028090', GOV_C = '#1C2951';

const tabs = {
  overview: renderOverview,
  environmental: renderEnvironmental,
  social: renderSocial,
  governance: renderGovernance,
  materiality: renderMateriality,
  competitive: renderCompetitive,
};

let activeCharts = [];
function destroyCharts() { activeCharts.forEach(c => c.destroy()); activeCharts = []; }

document.getElementById('tabs').addEventListener('click', e => {
  const tab = e.target.dataset.tab;
  if (!tab) return;
  document.querySelectorAll('.ew-tab').forEach(t => t.classList.remove('active'));
  e.target.classList.add('active');
  destroyCharts();
  tabs[tab]();
});

renderOverview();

function renderOverview() {
  const el = document.getElementById('content');
  el.innerHTML = `
    <div class="ew-grid4">
      <div class="kpi-card"><div class="kpi-val" style="color:${TEAL}">83</div><div class="kpi-label">Composite ESG score<br>/100</div></div>
      <div class="kpi-card"><div class="kpi-val" style="color:${WARN}">65</div><div class="kpi-label">Industry average<br>/100</div></div>
      <div class="kpi-card"><div class="kpi-val" style="color:${MINT}">+18</div><div class="kpi-label">Lead vs industry<br>pts</div></div>
      <div class="kpi-card"><div class="kpi-val" style="color:${NAVY}">AA</div><div class="kpi-label">MSCI-equiv rating<br>Leader tier</div></div>
    </div>
    <div class="ew-grid2">
      <div class="card">
        <div class="sec-title">ESG radar vs industry average</div>
        <div style="position:relative;height:240px;"><canvas id="radarChart" role="img" aria-label="Radar chart: EW Environmental 88, Social 82, Governance 79 vs industry 76, 74, 73"></canvas></div>
      </div>
      <div class="card">
        <div class="sec-title">Score trajectory to 2033</div>
        <div style="position:relative;height:240px;"><canvas id="trajChart" role="img" aria-label="Line chart showing ESG scores rising from 2024 to 2033"></canvas></div>
      </div>
    </div>
    <div class="card">
      <div class="sec-title">Sub-score breakdown — why each score?</div>
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:20px 40px;">
        ${subScoreHTML()}
      </div>
    </div>
  `;

  const radar = new Chart(document.getElementById('radarChart'), {
    type: 'radar',
    data: {
      labels: ['Environmental', 'Social', 'Governance'],
      datasets: [
        { label: 'ElectraWireless', data: [88, 82, 79], borderColor: TEAL, backgroundColor: 'rgba(2,192,154,0.18)', pointBackgroundColor: TEAL, borderWidth: 2 },
        { label: 'Industry Avg', data: [76, 74, 73], borderColor: WARN, backgroundColor: 'rgba(226,75,74,0.09)', borderDash: [4,4], pointBackgroundColor: WARN, borderWidth: 1.5 },
      ]
    },
    options: { responsive: true, maintainAspectRatio: false, scales: { r: { min: 50, max: 100, ticks: { stepSize: 10, font: { size: 10 } }, pointLabels: { font: { size: 12 } } } }, plugins: { legend: { labels: { font: { size: 11 } } } } }
  });
  activeCharts.push(radar);

  const years = [2024,2025,2026,2027,2028,2029,2030,2031,2032,2033];
  const traj = new Chart(document.getElementById('trajChart'), {
    type: 'line',
    data: {
      labels: years,
      datasets: [
        { label: 'Environmental', data: [80,83,88,90,91,92,93,94,95,96], borderColor: ENV_C, backgroundColor: 'transparent', borderWidth: 2, pointRadius: 3 },
        { label: 'Social', data: [75,78,82,84,85,86,87,88,89,90], borderColor: SOC_C, backgroundColor: 'transparent', borderWidth: 2, pointRadius: 3 },
        { label: 'Governance', data: [70,74,79,81,83,85,86,87,88,89], borderColor: GOV_C, backgroundColor: 'transparent', borderWidth: 2, borderDash: [4,3], pointRadius: 3 },
      ]
    },
    options: { responsive: true, maintainAspectRatio: false, scales: { y: { min: 60, max: 100, grid: { color: '#eef2f6' } }, x: { grid: { color: '#eef2f6' }, ticks: { font: { size: 10 }, maxRotation: 0 } } }, plugins: { legend: { labels: { font: { size: 11 } } } } }
  });
  activeCharts.push(traj);
}

function subScoreHTML() {
  const data = [
    { label: 'CO₂ Footprint Reduction', score: 92, color: ENV_C, reason: 'Eliminates 77,500 tons CO₂/yr by replacing copper & aluminium cables at scale.' },
    { label: 'E-Waste Reduction', score: 88, color: ENV_C, reason: '10,000 tons of Al & Cu saved from landfill annually across all product phases.' },
    { label: 'Energy Efficiency', score: 85, color: ENV_C, reason: 'WPT system achieves >80% energy conversion, minimising transmission losses.' },
    { label: 'Workforce Diversity', score: 90, color: SOC_C, reason: '20+ nationalities; 33% women in C-suite & executive leadership roles.' },
    { label: 'Safety Innovation', score: 87, color: SOC_C, reason: 'Removes electrical hazards (fire, shock) that affect 55% of cable users.' },
    { label: 'Regulatory Compliance', score: 82, color: GOV_C, reason: 'FCC compliance on track; GDPR-aligned data privacy; US-incorporated structure.' },
    { label: 'Transparency', score: 76, color: GOV_C, reason: 'Seed round fully allocated & disclosed; 6 board advisors; IPO roadmap public.' },
  ];
  return data.map(d => `
    <div class="score-row">
      <div style="display:flex;justify-content:space-between;align-items:baseline;">
        <span class="score-label">${d.label}</span>
        <span class="score-num" style="color:${d.color}">${d.score}</span>
      </div>
      <div class="bar-wrap"><div class="bar-fill" style="width:${d.score}%;background:${d.color}"></div></div>
      <div class="score-reason">${d.reason}</div>
    </div>
  `).join('');
}

function renderEnvironmental() {
  const el = document.getElementById('content');
  el.innerHTML = `
    <div class="ew-grid4">
      <div class="kpi-card"><div class="kpi-val" style="color:${MINT}">77.5K</div><div class="kpi-label">tons CO₂ avoided/yr</div></div>
      <div class="kpi-card"><div class="kpi-val" style="color:${TEAL}">&gt;80%</div><div class="kpi-label">WPT efficiency</div></div>
      <div class="kpi-card"><div class="kpi-val" style="color:${TEAL}">5,000</div><div class="kpi-label">tons Cu saved/yr</div></div>
      <div class="kpi-card"><div class="kpi-val" style="color:${TEAL}">5,000</div><div class="kpi-label">tons Al saved/yr</div></div>
    </div>
    <div class="ew-grid2">
      <div class="card">
        <div class="sec-title">Cumulative CO₂ avoided (K tons) — 10yr projection</div>
        <div style="position:relative;height:220px;"><canvas id="co2Chart" role="img" aria-label="Bar chart of cumulative CO2 avoided 2024 to 2033"></canvas></div>
      </div>
      <div class="card">
        <div class="sec-title">Metal saved from landfill (K tons Al+Cu)</div>
        <div style="position:relative;height:220px;"><canvas id="matChart" role="img" aria-label="Area chart of metal saved 2024 to 2033"></canvas></div>
      </div>
    </div>
    <div class="card">
      <div class="sec-title">Key environmental initiatives</div>
      ${[
        ['Zero cable hazards', 'Eliminates fire, shock & short-circuit risks inherent in traditional wiring systems — rated 97/100 solution impact.'],
        ['Metal waste elimination', '10,000 tons of Al & Cu preserved from landfill annually at scale across all five product phases.'],
        ['AI energy management', 'Elly AI optimises power delivery in real time via smart app, reducing waste from over-charging by up to 30%.'],
        ['Wireless EV charging (Phase 5)', 'Cable-free city infrastructure — zero e-waste from charging cables at transport hubs by 2030.'],
        ['Sustainable e-bikes (Phase 2)', 'Supports the $15B clean transport market with wireless, green charging stations.'],
      ].map(([t,d]) => `<div class="initiative"><div class="init-title">${t}</div><div class="init-desc">${d}</div></div>`).join('')}
    </div>
  `;

  const years = ['2024','2025','2026','2027','2028','2029','2030','2031','2032','2033'];
  const co2 = new Chart(document.getElementById('co2Chart'), {
    type: 'bar',
    data: { labels: years, datasets: [{ label: 'CO₂ avoided (K tons)', data: [5,12,25,42,62,85,115,150,195,250], backgroundColor: MINT, borderRadius: 4 }] },
    options: { responsive: true, maintainAspectRatio: false, scales: { y: { grid: { color: '#eef2f6' } }, x: { ticks: { font: { size: 10 } } } }, plugins: { legend: { display: false } } }
  });
  activeCharts.push(co2);

  const mat = new Chart(document.getElementById('matChart'), {
    type: 'line',
    data: { labels: years, datasets: [{ label: 'Metal saved (K tons)', data: [0.5,1.2,2.5,4.2,6.5,9.0,12.5,16.8,22.0,28.5], borderColor: TEAL, backgroundColor: 'rgba(2,128,144,0.12)', fill: true, borderWidth: 2, pointRadius: 3 }] },
    options: { responsive: true, maintainAspectRatio: false, scales: { y: { grid: { color: '#eef2f6' } }, x: { ticks: { font: { size: 10 } } } }, plugins: { legend: { display: false } } }
  });
  activeCharts.push(mat);
}

function renderSocial() {
  const el = document.getElementById('content');
  el.innerHTML = `
    <div class="ew-grid4">
      <div class="kpi-card"><div class="kpi-val" style="color:${SOC_C}">20+</div><div class="kpi-label">Nationalities on team</div></div>
      <div class="kpi-card"><div class="kpi-val" style="color:${SOC_C}">33%</div><div class="kpi-label">Women in C-suite</div></div>
      <div class="kpi-card"><div class="kpi-val" style="color:${SOC_C}">#4</div><div class="kpi-label">Kaggle AI rank (163K+ apps)</div></div>
      <div class="kpi-card"><div class="kpi-val" style="color:${SOC_C}">80%</div><div class="kpi-label">Households with cable clutter solved</div></div>
    </div>
    <div class="ew-grid2">
      <div class="card">
        <div class="sec-title">Social problem impact analysis</div>
        <div style="position:relative;height:240px;"><canvas id="socialChart" role="img" aria-label="Grouped bar chart of users affected vs EW solution impact"></canvas></div>
      </div>
      <div class="card">
        <div class="sec-title">Leadership diversity</div>
        <div style="position:relative;height:200px;"><canvas id="divChart" role="img" aria-label="Donut chart: 33% women, 67% men in leadership"></canvas></div>
        <p style="font-size:12px;color:var(--color-text-secondary);text-align:center;margin-top:10px;">33% women in C-suite across a global team of 20+ nationalities</p>
      </div>
    </div>
    <div class="card">
      <div class="sec-title">Academic &amp; industry partners</div>
      ${[
        ['🎓','Hong Kong Polytechnic University','R&D Partner'],
        ['🎓','RMIT University, Australia','Research Collaboration'],
        ['🌱','TALim Belgium','Youth Innovation'],
        ['🤝','MIT','Strategic Research Ally'],
        ['🏭','Siemens Energy','Technology Partner'],
        ['💻','Microsoft','Cloud & AI Partner'],
      ].map(([ic,n,r]) => `<div class="partner-row"><span style="font-size:16px">${ic}</span><div><div style="font-size:13px;font-weight:500;color:var(--color-text-primary)">${n}</div><div style="font-size:11px;color:var(--color-text-secondary)">${r}</div></div></div>`).join('')}
    </div>
  `;

  const problems = ['Cable clutter', 'Adapter incompat.', 'Electrical hazards', 'E-Waste disposal'];
  const sc = new Chart(document.getElementById('socialChart'), {
    type: 'bar',
    data: {
      labels: problems,
      datasets: [
        { label: 'Users affected (%)', data: [80,70,55,65], backgroundColor: 'rgba(2,128,144,0.35)', borderRadius: 3 },
        { label: 'EW solution impact', data: [95,92,97,88], backgroundColor: TEAL, borderRadius: 3 },
      ]
    },
    options: { responsive: true, maintainAspectRatio: false, scales: { y: { max: 110, grid: { color: '#eef2f6' } }, x: { ticks: { font: { size: 10 } } } }, plugins: { legend: { labels: { font: { size: 11 } } } } }
  });
  activeCharts.push(sc);

  const dc = new Chart(document.getElementById('divChart'), {
    type: 'doughnut',
    data: { labels: ['Women in leadership', 'Men in leadership'], datasets: [{ data: [33,67], backgroundColor: [MINT, '#e0eef5'], borderWidth: 0 }] },
    options: { responsive: true, maintainAspectRatio: false, cutout: '65%', plugins: { legend: { display: false } } }
  });
  activeCharts.push(dc);
}

function renderGovernance() {
  const el = document.getElementById('content');
  el.innerHTML = `
    <div class="ew-grid4">
      <div class="kpi-card"><div class="kpi-val" style="color:${GOV_C}">USA</div><div class="kpi-label">Incorporated entity</div></div>
      <div class="kpi-card"><div class="kpi-val" style="color:${GOV_C}">$5M</div><div class="kpi-label">Seed round (fully allocated)</div></div>
      <div class="kpi-card"><div class="kpi-val" style="color:${GOV_C}">IPO</div><div class="kpi-label">Exit strategy post Phase 4</div></div>
      <div class="kpi-card"><div class="kpi-val" style="color:${GOV_C}">6</div><div class="kpi-label">Board advisors across 5 countries</div></div>
    </div>
    <div class="ew-grid2">
      <div class="card">
        <div class="sec-title">Governance checklist</div>
        ${[
          ['US Entity Registration','Strong'],['Patent / IP Strategy','Active'],
          ['Regulatory Compliance (FCC)','On Track'],['Investor Transparency','Strong'],
          ['Exit Strategy (IPO post-P4)','Strong'],['Risk Mitigation Framework','Strong'],
          ['Data Privacy (GDPR-aligned)','Strong'],['ESG Reporting Cadence','Strong'],
        ].map(([l,s]) => `<div class="check-row"><span style="color:${MINT};font-size:14px;">✓</span><span class="check-label">${l}</span><span class="check-status">${s}</span></div>`).join('')}
      </div>
      <div>
        <div class="card" style="margin-bottom:16px;">
          <div class="sec-title">Seed round allocation</div>
          <div style="position:relative;height:220px;"><canvas id="fundChart" role="img" aria-label="Donut chart of $5M seed round allocation"></canvas></div>
        </div>
      </div>
    </div>
    <div class="card">
      <div class="sec-title">10-year financial forecast ($M)</div>
      <div style="position:relative;height:220px;"><canvas id="finChart" role="img" aria-label="Line chart of revenue and costs 2024 to 2033"></canvas></div>
    </div>
  `;

  const fc = new Chart(document.getElementById('fundChart'), {
    type: 'doughnut',
    data: {
      labels: ['R&D 35%','Market Exp. 25%','Operations 15%','Legal 10%','Talent 10%','Reserve 5%'],
      datasets: [{ data: [35,25,15,10,10,5], backgroundColor: [TEAL,MINT,'#065A82','#1C7293','#028090','#f9e795'], borderWidth: 0 }]
    },
    options: { responsive: true, maintainAspectRatio: false, cutout: '55%', plugins: { legend: { position: 'right', labels: { font: { size: 10 }, boxWidth: 10 } } } }
  });
  activeCharts.push(fc);

  const years = ['2024','2025','2026','2027','2028','2029','2030','2031','2032','2033'];
  const fin = new Chart(document.getElementById('finChart'), {
    type: 'line',
    data: {
      labels: years,
      datasets: [
        { label: 'Revenue ($M)', data: [0,0.5,2,5,12,28,55,95,150,220], borderColor: MINT, backgroundColor: 'rgba(2,192,154,0.10)', fill: true, borderWidth: 2, pointRadius: 3 },
        { label: 'Costs ($M)', data: [1,2,3,6,11,22,40,65,95,130], borderColor: WARN, borderDash: [4,3], backgroundColor: 'transparent', borderWidth: 2, pointRadius: 3 },
      ]
    },
    options: { responsive: true, maintainAspectRatio: false, scales: { y: { grid: { color: '#eef2f6' } }, x: { ticks: { font: { size: 10 } } } }, plugins: { legend: { labels: { font: { size: 11 } } } } }
  });
  activeCharts.push(fin);
}

function renderMateriality() {
  const el = document.getElementById('content');
  const topics = [
    { topic: 'E-Waste Reduction', x: 9.4, y: 9.1, pillar: 'Environmental', color: ENV_C },
    { topic: 'Safety Innovation', x: 9.2, y: 8.8, pillar: 'Social', color: SOC_C },
    { topic: 'AI Energy Efficiency', x: 8.9, y: 9.3, pillar: 'Tech', color: MINT },
    { topic: 'CO₂ Reduction', x: 9.0, y: 8.6, pillar: 'Environmental', color: ENV_C },
    { topic: 'IP Protection', x: 7.8, y: 9.5, pillar: 'Governance', color: GOV_C },
    { topic: 'Regulatory Compliance', x: 8.5, y: 8.3, pillar: 'Governance', color: GOV_C },
    { topic: 'Diversity & Inclusion', x: 8.0, y: 7.5, pillar: 'Social', color: SOC_C },
    { topic: 'Data Privacy', x: 7.9, y: 8.1, pillar: 'Governance', color: GOV_C },
    { topic: 'Community Impact', x: 7.5, y: 7.0, pillar: 'Social', color: SOC_C },
    { topic: 'Water Usage', x: 6.8, y: 6.5, pillar: 'Environmental', color: ENV_C },
    { topic: 'Noise Pollution', x: 5.5, y: 5.0, pillar: 'Environmental', color: ENV_C },
  ];

  el.innerHTML = `
    <div class="card" style="margin-bottom:16px;">
      <div class="sec-title">Double-materiality map — what matters most</div>
      <p style="font-size:12px;color:var(--color-text-secondary);margin-bottom:14px;">Topics in the top-right zone carry the highest stakeholder importance AND business impact. Size = relative priority.</p>
      <div style="position:relative;height:300px;"><canvas id="matChart" role="img" aria-label="Bubble chart of ESG materiality topics"></canvas></div>
      <div style="display:flex;gap:16px;margin-top:12px;flex-wrap:wrap;">
        ${[['Environmental',ENV_C],['Social',SOC_C],['Governance',GOV_C],['Tech',MINT]].map(([l,c]) => `<span style="font-size:11px;display:flex;align-items:center;gap:5px;color:var(--color-text-secondary);"><span style="width:10px;height:10px;border-radius:50%;background:${c};display:inline-block"></span>${l}</span>`).join('')}
      </div>
    </div>
    <div class="card">
      <div class="sec-title">Top 6 critical ESG topics — why they matter</div>
      ${[
        ['1','E-Waste Reduction','Environmental','Highest priority: eliminates 10K tons of Al/Cu from landfill. Regulatory & investor scrutiny is intense.'],
        ['2','Safety Innovation','Social','Removing electrical hazards (fire, shock) from 55% of cable users — a unique differentiator for stakeholders.'],
        ['3','AI Energy Efficiency','Tech','Elly AI optimises real-time power delivery, reducing over-charging waste. Core IP and ESG asset in one.'],
        ['4','CO₂ Reduction','Environmental','77.5K tons CO₂/yr avoided. Climate impact is a central investor & regulatory KPI globally.'],
        ['5','IP Protection','Governance','Active patent strategy protects WPT tech and AI algorithms from competitor replication — preserves ESG moat.'],
        ['6','Regulatory Compliance','Governance','FCC & GDPR compliance are gating factors for product launches across all 5 rollout phases.'],
      ].map(([rank,t,p,r]) => `<div class="mat-topic"><div style="display:flex;align-items:center;margin-bottom:5px;"><span class="mat-rank ${parseInt(rank)<=3?'top':''}">#${rank}</span><span style="font-size:13px;font-weight:500;color:var(--color-text-primary)">${t}</span><span style="font-size:11px;color:var(--color-text-secondary);margin-left:8px;">· ${p}</span></div><p style="font-size:12px;color:var(--color-text-secondary);margin:0;line-height:1.5">${r}</p></div>`).join('')}
    </div>
  `;

  const mc = new Chart(document.getElementById('matChart'), {
    type: 'bubble',
    data: {
      datasets: topics.map(t => ({
        label: t.topic,
        data: [{ x: t.x, y: t.y, r: t.x > 8.5 && t.y > 8.5 ? 14 : t.x > 7.5 && t.y > 7.5 ? 10 : 7 }],
        backgroundColor: t.color + 'bb',
        borderColor: t.color,
        borderWidth: 1.5,
      }))
    },
    options: {
      responsive: true, maintainAspectRatio: false,
      scales: {
        x: { min: 4.5, max: 10.5, title: { display: true, text: 'Importance to stakeholders (0–10)', font: { size: 11 } }, grid: { color: '#eef2f6' } },
        y: { min: 4, max: 10.5, title: { display: true, text: 'Business impact (0–10)', font: { size: 11 } }, grid: { color: '#eef2f6' } },
      },
      plugins: {
        legend: { display: false },
        tooltip: { callbacks: { label: ctx => `${ctx.dataset.label} (${ctx.parsed.x}, ${ctx.parsed.y})` } }
      },
      layout: { padding: 20 }
    }
  });
  activeCharts.push(mc);
}

function renderCompetitive() {
  const comps = ['ElectraWireless', 'WiTricity', 'Ossia', 'Resonant Link', 'Traditional'];
  const scores = { E: [88,72,68,65,48], S: [82,70,65,63,55], G: [79,68,64,62,58] };
  const colors = [TEAL,'#1C7293','#028090','#065A82','#9baab3'];

  const feats = ['Wireless Power','Heating Capability','Smart App & Data','Foreign Object Detection','Kitchen Appliances','E-Bikes','Robotics','EV Charging','Medical Devices','IoT & Furniture'];
  const matrix = {
    ElectraWireless: [1,1,1,1,1,1,1,1,1,1],
    WiTricity: [1,0,1,1,0,0,0,1,1,0],
    Ossia: [1,0,1,0,0,0,0,0,1,0],
    'Resonant Link': [1,0,0,1,0,0,0,0,1,0],
    Traditional: [0,0,0,0,1,1,0,1,0,1],
  };

  const el = document.getElementById('content');
  el.innerHTML = `
    <div class="card" style="margin-bottom:16px;">
      <div class="sec-title">ESG score comparison vs competitors</div>
      <div style="position:relative;height:260px;"><canvas id="compChart" role="img" aria-label="Grouped bar chart: EW leads all competitors on E, S, G pillars"></canvas></div>
    </div>
    <div class="card" style="margin-bottom:16px;">
      <div class="sec-title">Composite ESG score comparison</div>
      ${comps.map((c, i) => {
        const comp = Math.round((scores.E[i]+scores.S[i]+scores.G[i])/3);
        return `<div class="comp-bar"><div class="comp-name">${c}</div><div class="comp-track"><div class="comp-fill" style="width:${comp}%;background:${colors[i]}">${comp}</div></div></div>`;
      }).join('')}
      <p style="font-size:12px;color:var(--color-text-secondary);margin-top:10px;">EW composite of 83 vs industry average of 65 — an 18-point lead driven by unique all-in-one wireless power technology.</p>
    </div>
    <div class="card">
      <div class="sec-title">Feature matrix — EW is the only company with all 10 capabilities</div>
      <div style="overflow-x:auto;">
        <table class="feat-table">
          <thead><tr>
            <th>Feature</th>
            ${comps.map(c => `<th class="${c==='ElectraWireless'?'ew-col':''}">${c}</th>`).join('')}
          </tr></thead>
          <tbody>
            ${feats.map(f => `<tr><td>${f}</td>${comps.map(c => `<td>${matrix[c][feats.indexOf(f)] ? (c==='ElectraWireless'?'<span class="ew-tick">✓</span>':'<span class="tick">✓</span>') : '<span class="cross">✗</span>'}</td>`).join('')}</tr>`).join('')}
          </tbody>
        </table>
      </div>
    </div>
  `;

  const cc = new Chart(document.getElementById('compChart'), {
    type: 'bar',
    data: {
      labels: comps,
      datasets: [
        { label: 'Environmental', data: scores.E, backgroundColor: ENV_C, borderRadius: 3 },
        { label: 'Social', data: scores.S, backgroundColor: SOC_C, borderRadius: 3 },
        { label: 'Governance', data: scores.G, backgroundColor: GOV_C + 'cc', borderRadius: 3 },
      ]
    },
    options: { responsive: true, maintainAspectRatio: false, scales: { y: { max: 100, grid: { color: '#eef2f6' } }, x: { ticks: { font: { size: 10 } } } }, plugins: { legend: { labels: { font: { size: 11 } } } } }
  });
  activeCharts.push(cc);
}
</script>
