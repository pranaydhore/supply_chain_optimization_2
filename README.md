<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>README — Supply Chain Optimization Dashboard</title>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;800&display=swap" rel="stylesheet">
<meta name="description" content="Streamlit + Plotly Supply Chain Optimization Dashboard README in HTML.">
<style>
  :root{
    --bg:#0b0e13; --panel:#121722; --panel2:#0f141e; --text:#e7eefc; --muted:#9fb0cc;
    --brand:#5b8cff; --accent:#22d3ee; --ok:#22c55e; --warn:#f59e0b; --bad:#ef4444;
    --border:#1b2331; --code:#0d1117; --code-b:#1f2632; --card-r:18px; --shadow:0 10px 26px rgba(0,0,0,.35);
  }
  .light{
    --bg:#f7f9fc; --panel:#ffffff; --panel2:#f6f8fd; --text:#0f1220; --muted:#556482;
    --brand:#3b82f6; --accent:#06b6d4; --border:#e6ecf5; --code:#0f172a; --code-b:#0b1220;
  }
  *{box-sizing:border-box}
  body{margin:0;background:var(--bg);font-family:Inter,system-ui,Segoe UI,Roboto,Arial;color:var(--text);line-height:1.6}
  .wrap{max-width:1040px;margin:0 auto;padding:24px}
  header.hero{position:relative;border:1px solid var(--border);border-radius:22px;padding:42px 28px;
    background:radial-gradient(1200px 400px at -10% -20%, rgba(124,245,255,.16), transparent 55%),
               radial-gradient(1200px 400px at 110% -10%, rgba(91,140,255,.18), transparent 55%),
               linear-gradient(180deg,var(--panel),var(--panel2));
    box-shadow:var(--shadow);overflow:hidden}
  h1{margin:.25rem 0 .35rem;font-size:clamp(28px,4vw,44px)}
  .sub{color:var(--muted);max-width:72ch}
  .row{display:grid;gap:18px}
  @media (min-width:920px){ .row.cols-2{grid-template-columns:1.1fr .9fr} }
  section.card{border:1px solid var(--border);border-radius:18px;padding:20px;background:linear-gradient(180deg,var(--panel),var(--panel2));box-shadow:var(--shadow)}
  h2{margin:.2rem 0 .6rem;font-size:22px}
  h3{margin:1rem 0 .4rem;font-size:18px}
  .toc a{display:block;padding:8px 10px;border-radius:10px;color:var(--muted);text-decoration:none;border:1px dashed transparent}
  .toc a:hover{background:rgba(124,245,255,.06);color:var(--text);border-color:var(--border)}
  .pill{display:inline-flex;gap:8px;align-items:center;background:rgba(124,245,255,.12);border:1px solid rgba(124,245,255,.25);color:#9feaff;padding:6px 10px;border-radius:999px;font-size:12px;font-weight:700}
  .badges{display:flex;gap:10px;flex-wrap:wrap;margin-top:12px}
  .badge{font-size:12px;border:1px solid var(--border);border-radius:999px;padding:3px 8px;color:var(--muted)}
  .btn{display:inline-block;background:linear-gradient(180deg,var(--brand),#355fc7);color:#fff;border:1px solid rgba(255,255,255,.15);padding:10px 14px;border-radius:12px;font-weight:700;text-decoration:none;margin-right:10px}
  .btn.ghost{background:transparent;color:var(--text);border:1px solid var(--border)}
  pre{background:var(--code);color:#e5ecf7;border:1px solid var(--code-b);padding:14px;border-radius:12px;overflow:auto}
  code{font-family:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace}
  table{width:100%;border-collapse:separate;border-spacing:0;border:1px solid var(--border);border-radius:12px;overflow:hidden}
  th,td{padding:10px 12px;border-bottom:1px solid var(--border);text-align:left}
  th{background:rgba(124,245,255,.08)}
  ul.clean{margin:0;padding-left:18px}
  .callout{border-left:4px solid var(--brand);background:rgba(91,140,255,.10);padding:12px 14px;border-radius:8px;margin:12px 0}
  footer{color:var(--muted);text-align:center;margin:28px 0}
  .topbar{position:absolute;top:16px;right:16px;display:flex;gap:10px}
  .switch{width:48px;height:28px;border:1px solid var(--border);border-radius:999px;background:var(--panel2);cursor:pointer;position:relative}
  .knob{position:absolute;top:50%;left:3px;transform:translateY(-50%);width:22px;height:22px;border-radius:50%;background:linear-gradient(180deg,#fff,#cbd5e1)}
  .light .knob{left:23px}
</style>
</head>
<body>
  <div class="wrap">
    <header class="hero">
      <div class="topbar">
        <div class="switch" id="theme"><div class="knob"></div></div>
      </div>
      <span class="pill">README • Streamlit • Plotly • ML</span>
      <h1>Supply Chain Optimization Dashboard</h1>
      <p class="sub">
        A professional Streamlit dashboard powered by Plotly and ML evaluation metrics. It turns raw operational data into actionable insights:
        model KPIs, confusion matrix, ROC, KPI analytics, model comparison, business domain mapping, and a dedicated <strong>KPI Matrix</strong> tab.
      </p>
      <div style="margin-top:14px">
        <a class="btn" href="#quickstart">🚀 Quickstart</a>
        <a class="btn ghost" href="#kpi-matrix">📊 KPI Matrix</a>
        <a class="btn ghost" href="#structure">📁 Structure</a>
      </div>
      <div class="badges">
        <span class="badge">Python 3.10+</span>
        <span class="badge">Streamlit</span>
        <span class="badge">Plotly</span>
        <span class="badge">scikit-learn</span>
      </div>
    </header>

   <div class="row cols-2" style="margin-top:22px">
      <aside class="card toc">
        <h3 style="margin-top:0">Table of Contents</h3>
        <a href="#about">About</a>
        <a href="#features">Features</a>
        <a href="#structure">Project Structure</a>
        <a href="#quickstart">Installation & Quickstart</a>
        <a href="#kpi-matrix">KPI Matrix (New)</a>
        <a href="#visuals">Key Visuals</a>
        <a href="#team">Team</a>
        <a href="#roadmap">Roadmap</a>
        <a href="#contrib">Contribute</a>
        <a href="#license">License</a>
      </aside>

  <main class="row" style="gap:18px">
        <section id="about" class="card">
          <h2>About</h2>
          <p>
            This dashboard helps Supply Chain, Operations, and Data teams evaluate model quality, compare experiments across datasets, and translate metrics
            into business-aligned KPIs. Built with Streamlit + Plotly, and scikit-learn for evaluation utilities.
          </p>
          <div class="callout"><strong>Highlights:</strong> cached loaders, optional downsampling for large CSVs, and a leadership-friendly KPI Matrix.</div>
        </section>

  <section id="features" class="card">
          <h2>Features</h2>
          <table>
            <thead><tr><th>Module</th><th>Description</th></tr></thead>
            <tbody>
              <tr><td><strong>Model KPIs</strong></td><td>Accuracy, Precision, Recall, F1, and ROC-AUC summary cards.</td></tr>
              <tr><td><strong>Confusion Matrix & ROC</strong></td><td>Evaluate classification quality and thresholds.</td></tr>
              <tr><td><strong>KPI Insights</strong></td><td>Average KPI bars and variability box plots.</td></tr>
              <tr><td><strong>Python Charts Lab</strong></td><td>8+ interactive charts (histogram, bar, box, scatter, line, area, heatmap, bubble).</td></tr>
              <tr><td><strong>Comparison</strong></td><td>Cross-experiment accuracy from <code>platforms_comparison_metrics.csv</code>.</td></tr>
              <tr><td><strong>Business Domains</strong></td><td>Maps columns to Inventory, Demand, Logistics, Supplier, etc.</td></tr>
              <tr><td><strong>KPI Matrix</strong></td><td>Table + Radar (polar) + KPI comparison bar chart.</td></tr>
              <tr><td><strong>Team</strong></td><td>Project contributors and roles.</td></tr>
            </tbody>
          </table>
        </section>

   <section id="structure" class="card">
          <h2>Project Structure</h2>
          <pre><code>Project/
│── app.py                       # Streamlit dashboard
│── README.md                    # Documentation (this)
│
│── notebooks/                   # Experiment notebooks
│   ├── comparison_results/      # Per-dataset predictions & metrics
│   └── combined_results/        # Combined high-accuracy outputs
│
│── data/
│   └── artifacts/
│       └── supply_chain_kpi_matrix.csv   # Used by KPI Matrix tab
</code></pre>
        </section>

  <section id="quickstart" class="card">
          <h2>Installation & Quickstart</h2>
          <h3>1) Clone</h3>
          <pre><code>git clone &lt;your-repo-link&gt;
cd &lt;project-folder&gt;</code></pre>
          <h3>2) Virtual Environment</h3>
          <pre><code>python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate  # macOS/Linux</code></pre>
          <h3>3) Install</h3>
          <pre><code>pip install -r requirements.txt
# If missing:
pip install streamlit plotly pandas numpy scikit-learn</code></pre>
          <h3>4) Run</h3>
          <pre><code>streamlit run app.py</code></pre>
        </section>

 <section id="kpi-matrix" class="card">
          <h2>KPI Matrix (New)</h2>
          <p>Place the following CSV before opening the tab:</p>
          <pre><code>data/artifacts/supply_chain_kpi_matrix.csv</code></pre>
          <table>
            <thead><tr><th>Column</th><th>Type</th><th>Description</th></tr></thead>
            <tbody>
              <tr><td><code>KPI</code></td><td>string</td><td>Metric label (e.g., Inventory Turnover, Fill Rate)</td></tr>
              <tr><td><code>Value</code></td><td>number</td><td>Score (normalized 0–1 or scaled 0–100)</td></tr>
            </tbody>
          </table>
          <ul class="clean">
            <li>✅ KPI Data Table</li>
            <li>✅ Radar (Polar) Strength Profile</li>
            <li>✅ KPI Comparison Bar Chart</li>
          </ul>
        </section>

  <section id="visuals" class="card">
          <h2>Key Visuals</h2>
          <table>
            <thead><tr><th>Visualization</th><th>Purpose</th></tr></thead>
            <tbody>
              <tr><td>Confusion Matrix</td><td>Quick view of TP/FP/FN/TN distribution</td></tr>
              <tr><td>ROC Curve + AUC</td><td>Threshold-agnostic probability quality</td></tr>
              <tr><td>Correlation Heatmap</td><td>Feature relationships and dependencies</td></tr>
              <tr><td>Bar / Box / Line / Area / Scatter</td><td>Exploratory KPI analysis and trends</td></tr>
            </tbody>
          </table>
        </section>

   <section id="team" class="card">
          <h2>Team</h2>
          <table>
            <thead><tr><th>Name</th><th>Role</th><th>Focus</th></tr></thead>
            <tbody>
              <tr><td>Pranay Dhore</td><td>Lead Developer / Data Scientist</td><td>Modeling, System Architecture</td></tr>
              <tr><td>Paras Longadge</td><td>Data Analyst / Dashboard Designer</td><td>UI/UX, Visual Analytics</td></tr>
              <tr><td>Sanket Tajne</td><td>ML Engineer</td><td>Feature Engineering, Optimization</td></tr>
              <tr><td>Kunal Gomkar</td><td>Logistics & Integration Specialist</td><td>Process & Ops Integration</td></tr>
            </tbody>
          </table>
        </section>

   <section id="roadmap" class="card">
          <h2>Roadmap</h2>
          <ul class="clean">
            <li>Real-time ERP/WMS/IoT integration</li>
            <li>Demand forecasting & inventory optimization</li>
            <li>Automated retraining pipelines</li>
            <li>Cloud deployment (AWS/GCP/Azure)</li>
            <li>PDF/PPT export of insights</li>
          </ul>
        </section>

  <section id="contrib" class="card">
          <h2>Contribute & Support</h2>
          <p>If this project helps you, please star the repo and open issues/PRs for ideas or fixes.</p>
        </section>

   <section id="license" class="card">
          <h2>License</h2>
          <p>Add your license choice (MIT / Apache-2.0) here.</p>
        </section>
      </main>
    </div>

<footer>
      <p>Built with 💙 for data-informed supply chains • <span id="stamp"></span></p>
    </footer>
  </div>
<script>
  (function(){
    const root=document.documentElement;
    const saved=localStorage.getItem("theme");
    if(saved==="light") root.classList.add("light");
    document.getElementById("theme").addEventListener("click",()=>{
      root.classList.toggle("light");
      localStorage.setItem("theme",root.classList.contains("light")?"light":"dark");
    });
    document.getElementById("stamp").textContent = "Generated: " + new Date().toLocaleString();
  })();
</script>
</body>
</html>
