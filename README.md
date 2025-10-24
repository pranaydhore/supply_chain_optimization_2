
<body>
  <div class="container">
    <header class="hero">
      <div class="theme-toggle">
        <span class="tag">Theme</span>
        <div class="switch" id="themeSwitch" title="Toggle light/dark">
          <div class="knob"></div>
        </div>
      </div>
      <span class="pill">Streamlit • Plotly • ML</span>
      <h1>Supply Chain Optimization Dashboard</h1>
      <p class="sub">
        A modern analytics app that transforms raw operational data into actionable insights. 
        Explore model performance (Accuracy, Precision, Recall, F1, AUC), visualize confusion matrices & ROC curves,
        compare experiments, and assess business impact via a dedicated KPI Matrix — all in one place.
      </p>
      <div class="cta">
        <a class="btn" href="#quickstart">🚀 Quickstart</a>
        <a class="btn sec" href="#architecture">📐 Architecture</a>
        <a class="btn sec" href="#kpi-matrix">📊 KPI Matrix</a>
      </div>
      <div class="meta">
        <span class="badge">Python 3.10+</span>
        <span class="badge">Streamlit</span>
        <span class="badge">Plotly</span>
        <span class="badge">scikit-learn</span>
      </div>
    </header>

    <div class="grid cols-2" style="margin-top:22px">
      <aside class="toc card">
        <h3 style="margin:0 0 10px">Table of Contents</h3>
        <a href="#overview">Overview</a>
        <a href="#features">Features by Tab</a>
        <a href="#project-structure">Project Structure</a>
        <a href="#quickstart">Quickstart</a>
        <a href="#configuration">Configuration Paths</a>
        <a href="#architecture">Architecture & Data Flow</a>
        <a href="#visuals">Key Visuals</a>
        <a href="#kpi-matrix">KPI Matrix (New)</a>
        <a href="#usage">Usage Guide</a>
        <a href="#troubleshooting">Troubleshooting</a>
        <a href="#faq">FAQ</a>
        <a href="#team">Team</a>
        <a href="#roadmap">Roadmap</a>
        <a href="#license">License</a>
      </aside>

      <main class="grid" style="gap:18px">
        <section id="overview" class="card">
          <h2>Overview</h2>
          <p>
            This dashboard helps Supply Chain and Data teams evaluate model quality, compare experiments across datasets,
            and translate metrics into business-aligned KPIs. It is built with Streamlit and Plotly, and uses scikit-learn
            for evaluation utilities such as confusion matrix and ROC-AUC.
          </p>
          <div class="callout">
            <strong>Highlights:</strong> unified UI, fast cached data loading, downsampling support for large CSVs,
            and a dedicated <em>KPI Matrix</em> tab for leadership-friendly reporting.
          </div>
        </section>

        <section id="features" class="card">
          <h2>Features by Tab</h2>
          <ul class="list-check">
            <li><strong>Overview</strong> — Confusion Matrix, ROC Curve with live AUC, and model KPIs (top cards).</li>
            <li><strong>KPI Insights</strong> — Average KPI bars, variability box plots, numeric KPI detection.</li>
            <li><strong>Python Charts</strong> — 8+ interactive charts (histogram, bar, box, scatter, line, area, heatmap, bubble) with selectable axes.</li>
            <li><strong>Comparison</strong> — Cross-experiment accuracy comparison from <code>platforms_comparison_metrics.csv</code>.</li>
            <li><strong>Business Domains</strong> — Maps columns to domains (Inventory, Demand, Logistics, etc.) and visualizes domain scores.</li>
            <li><strong>KPI Matrix (New)</strong> — Displays <em>Supply Chain KPI Matrix</em> table, a radar (polar) chart, and a comparison bar chart.</li>
            <li><strong>Team</strong> — Project members and roles.</li>
          </ul>
        </section>

        <section id="project-structure" class="card">
          <h2>Project Structure</h2>
          <pre><code>Project/
├─ app.py
├─ README.md
├─ notebooks/
│  ├─ comparison_results/          # Per-dataset predictions & metrics
│  └─ combined_results/            # Combined high-accuracy outputs
├─ data/
│  └─ artifacts/
│     └─ supply_chain_kpi_matrix.csv
└─ (optional) requirements.txt
</code></pre>
        </section>

   <section id="quickstart" class="card">
          <h2>Quickstart</h2>
          <h3>1) Create & Activate Virtual Environment</h3>
          <pre><code>python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate</code></pre>

  <h3>2) Install Dependencies</h3>
          <pre><code>pip install streamlit plotly pandas numpy scikit-learn</code></pre>
        <h3>3) Run the App</h3>
          <pre><code>streamlit run app.py</code></pre>
          <p class="muted">Open the provided local URL in your browser to view the dashboard.</p>
        </section>
        
  <section id="configuration" class="card">
          <h2>Configuration Paths</h2>
          <p>The app reads from these base paths (see top of <code>app.py</code>):</p>
          <table class="table">
            <thead><tr><th>Variable</th><th>Purpose</th><th>Default (example)</th></tr></thead>
            <tbody>
              <tr><td><code>NOTEBOOKS_DIR</code></td><td>Jupyter notebooks & experiment outputs</td><td><code>C:\Users\ASUS\OneDrive\Documents\Project\notebooks</code></td></tr>
              <tr><td><code>ARTIFACTS_DIR</code></td><td>Artifacts like KPI matrix CSV</td><td><code>C:\Users\ASUS\OneDrive\Documents\Project\data\artifacts</code></td></tr>
              <tr><td><code>COMPARISON_DIR</code></td><td>Per-dataset results</td><td><code>[NOTEBOOKS_DIR]/comparison_results</code></td></tr>
              <tr><td><code>COMBINED_DIR</code></td><td>Combined high-accuracy results</td><td><code>[NOTEBOOKS_DIR]/combined_results</code></td></tr>
              <tr><td><code>SUMMARY_CSV</code></td><td>Model/platform comparison metrics</td><td><code>[COMPARISON_DIR]/platforms_comparison_metrics.csv</code></td></tr>
            </tbody>
          </table>
          <p>Use the sidebar “🔄 Refresh Cache” button to clear cached CSV/JSON loads.</p>
        </section>

  <section id="architecture" class="card">
          <h2>Architecture & Data Flow</h2>
          <ol>
            <li><strong>Data & Predictions</strong> — CSV predictions and JSON metrics are generated by notebooks into <code>comparison_results/</code> or <code>combined_results/</code>.</li>
            <li><strong>Loaders</strong> — Cached helpers (<code>safe_load_csv</code>, <code>safe_load_json</code>) read and deduplicate columns; optional downsampling keeps UI responsive.</li>
            <li><strong>UI Tabs</strong> — Each tab renders specific visuals based on selected dataset from the sidebar.</li>
            <li><strong>KPI Matrix</strong> — Reads <code>supply_chain_kpi_matrix.csv</code> from <code>ARTIFACTS_DIR</code> for radar/table/bar outputs.</li>
          </ol>
          <pre><code>[Notebooks] → CSV/JSON → [Streamlit Loaders] → [Tabs & Visuals] → Insights</code></pre>
        </section>

  <section id="visuals" class="card">
          <h2>Key Visuals</h2>
          <ul class="list-check">
            <li><strong>Confusion Matrix</strong> — Immediate view of TP/FP/FN/TN.</li>
            <li><strong>ROC Curve + AUC</strong> — Threshold-agnostic probability quality.</li>
            <li><strong>Correlation Heatmap</strong> — Feature dependence analysis.</li>
            <li><strong>Box / Bar / Line / Area / Scatter</strong> — Exploratory data views.</li>
          </ul>
        </section>

  <section id="kpi-matrix" class="card">
          <h2>KPI Matrix (New)</h2>
          <p>
            The KPI Matrix translates technical model outcomes into business language.
            Provide the CSV at: <code>data/artifacts/supply_chain_kpi_matrix.csv</code>. It should minimally contain:
          </p>
          <table class="table">
            <thead><tr><th>Column</th><th>Type</th><th>Description</th></tr></thead>
            <tbody>
              <tr><td><code>KPI</code></td><td>string</td><td>Name of the KPI (e.g., Inventory Turnover, Fill Rate).</td></tr>
              <tr><td><code>Value</code></td><td>numeric</td><td>Score/normalized value (0–1 or 0–100).</td></tr>
            </tbody>
          </table>
          <p>
            In the dashboard, the tab renders:
          </p>
          <ul class="list-check">
            <li>KPI table (<em>sortable in Streamlit</em>).</li>
            <li>Radar (polar) chart for a quick strengths profile.</li>
            <li>Bar chart for side-by-side KPI comparison.</li>
          </ul>
          <p class="callout"><strong>Tip:</strong> Keep KPI names concise; normalize values to a common scale for clear comparisons.</p>
        </section>

  <section id="usage" class="card">
          <h2>Usage Guide</h2>
          <ol>
            <li>Put your experiment outputs in the appropriate <code>comparison_results/&nbsp;/ combined_results/</code> folders.</li>
            <li>Place <code>supply_chain_kpi_matrix.csv</code> in <code>data/artifacts/</code>.</li>
            <li>Run <code>streamlit run app.py</code> and pick a dataset from the sidebar.</li>
            <li>Navigate tabs to analyze performance, explore KPIs, and review business domains.</li>
          </ol>
        </section>

   <section id="troubleshooting" class="card">
          <h2>Troubleshooting</h2>
          <ul class="list-check">
            <li><strong>No datasets in sidebar:</strong> Ensure <code>comparison_results/</code> or <code>combined_results/</code> exists and contains files.</li>
            <li><strong>CSV load errors:</strong> The loader falls back to <code>engine="python"</code>. Validate delimiter & encoding.</li>
            <li><strong>Empty charts:</strong> Check column names (<code>efficiency_label</code>, <code>predicted_efficiency</code>, <code>predicted_probability</code>).</li>
            <li><strong>KPI Matrix warning:</strong> Create the CSV with <code>KPI</code> and <code>Value</code> columns.</li>
            <li><strong>Performance issues:</strong> Use built-in downsampling (defaults to 5,000 rows).</li>
          </ul>
        </section>

  <section id="faq" class="card">
          <h2>FAQ</h2>
          <h3>Can I rename directories?</h3>
          <p>Yes. Update the path constants at the top of <code>app.py</code> to match your structure.</p>
          <h3>What file formats are supported?</h3>
          <p>CSV for predictions; JSON for metrics. The loader handles duplicated columns and common CSV quirks.</p>
          <h3>How do I add a new KPI?</h3>
          <p>Add a row to <code>supply_chain_kpi_matrix.csv</code> and refresh the app cache via the sidebar button.</p>
        </section>

  <section id="team" class="card">
          <h2>Team</h2>
          <table class="table">
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
          <ul class="list-check">
            <li>Real-time ERP/WMS integration</li>
            <li>Demand forecasting and inventory optimization</li>
            <li>Automated retraining pipelines</li>
            <li>Cloud deployment (AWS/GCP/Azure)</li>
            <li>PDF/PPT export of insights</li>
          </ul>
        </section>

   <section id="license" class="card">
          <h2>License</h2>
          <p>Include your preferred license (MIT/Apache-2.0) here.</p>
        </section>
      </main>
    </div>

  <footer>
      <p>Built with ❤️ for data-informed supply chains. • <span id="buildTime"></span></p>
    </footer>
  </div>

<script>
  // Theme toggle with localStorage
  (function(){
    const root = document.documentElement;
    const saved = localStorage.getItem("theme");
    if(saved === "light"){ root.classList.add("light"); }
    const sw = document.getElementById("themeSwitch");
    sw.addEventListener("click", ()=>{
      root.classList.toggle("light");
      localStorage.setItem("theme", root.classList.contains("light") ? "light" : "dark");
    });
    // Build time
    document.getElementById("buildTime").textContent = "Generated: " + new Date().toLocaleString();
  })();
</script>
</body>
</html>
