<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Supply Chain Optimization Dashboard — Extended Project Explanation (HTML Only)</title>
</head>
<body>

<!-- ========================================================= -->
<!-- Title Page -->
<!-- ========================================================= -->
<h1>Supply Chain Optimization Dashboard — Extended Explanation</h1>
<p>
This document is a <strong>comprehensive, plain-HTML</strong> explanation of the Supply Chain Optimization Dashboard project.
It covers theory, methodology, system architecture, machine learning workflow, data processing, model evaluation, KPI mapping,
business value, case studies, deployment, and troubleshooting. No CSS is used; the focus is clarity and completeness.
</p>

<hr>

<!-- ========================================================= -->
<!-- Abstract -->
<!-- ========================================================= -->
<h2>1. Abstract</h2>
<p>
The Supply Chain Optimization Dashboard is an interactive analytics system built with Streamlit and Plotly that
transforms supply chain data into actionable insights. It evaluates machine learning models, visualizes performance
metrics (Accuracy, Precision, Recall, F1, AUC), and connects technical outputs to business KPIs such as Inventory Turnover,
Order Fulfillment Rate, Lead Time, and Cost Control. The dashboard provides multiple tabs for overview, KPI insights,
comparison across datasets, Python-driven charts, business-domain mapping, a KPI Matrix, and team information. The goal
is to enable faster, informed, and repeatable decision-making for operations, procurement, inventory, and logistics teams.
</p>

<hr>

<!-- ========================================================= -->
<!-- Executive Summary -->
<!-- ========================================================= -->
<h2>2. Executive Summary</h2>
<ul>
  <li><strong>Problem:</strong> Supply chains are complex, data-rich, and time-sensitive. Manual monitoring often results in slow, reactive decisions.</li>
  <li><strong>Solution:</strong> A dashboard that centralizes datasets, evaluates ML model quality, surfaces KPI trends, and translates them into business terms.</li>
  <li><strong>Benefits:</strong> Shorter decision cycles, better forecast alignment, reduced stockouts/overstocks, improved on-time delivery, and cost savings.</li>
  <li><strong>Audience:</strong> Supply chain managers, data analysts, ML engineers, and leadership stakeholders.</li>
</ul>

<hr>

<!-- ========================================================= -->
<!-- Background & Motivation -->
<!-- ========================================================= -->
<h2>3. Background and Motivation</h2>
<p>
Global supply chains face volatility due to fluctuating demand, supplier variability, transportation constraints, and operational inefficiencies.
Traditional dashboards focus on descriptive analytics; this project adds <em>predictive</em> and <em>prescriptive</em> elements via ML metrics and KPI mapping,
bridging the gap between data science outputs and business decisions.
</p>

<hr>

<!-- ========================================================= -->
<!-- Theoretical Foundations -->
<!-- ========================================================= -->
<h2>4. Theoretical Foundations</h2>

<h3>4.1 Supply Chain Concepts</h3>
<ul>
  <li><strong>Inventory Management:</strong> Balancing stock levels to meet demand while minimizing holding costs.</li>
  <li><strong>Procurement & Suppliers:</strong> Evaluating supplier lead times, reliability, and compliance.</li>
  <li><strong>Logistics & Distribution:</strong> Optimizing routing, transportation mode, and delivery performance.</li>
  <li><strong>Demand Forecasting:</strong> Anticipating future demand to align production and inventory.</li>
  <li><strong>Service Level:</strong> Probability that demand is met without stockout during a replenishment cycle.</li>
</ul>

<h3>4.2 KPI Fundamentals</h3>
<table border="1" cellpadding="6">
  <tr><th>KPI</th><th>Definition</th><th>Business Interpretation</th></tr>
  <tr>
    <td>Inventory Turnover</td>
    <td>COGS / Average Inventory</td>
    <td>Higher turnover indicates efficient inventory utilization.</td>
  </tr>
  <tr>
    <td>Order Fulfillment Rate</td>
    <td>Fulfilled Orders / Total Orders</td>
    <td>Direct measure of service performance and reliability.</td>
  </tr>
  <tr>
    <td>Lead Time</td>
    <td>Delivery Date − Order Date</td>
    <td>Lower lead time indicates better responsiveness.</td>
  </tr>
  <tr>
    <td>Fill Rate</td>
    <td>Demand Satisfied from Stock / Total Demand</td>
    <td>Measures availability and customer satisfaction.</td>
  </tr>
  <tr>
    <td>Warehousing Cost</td>
    <td>Storage + Labor + Handling + Shrinkage</td>
    <td>Lower cost at same service level implies higher efficiency.</td>
  </tr>
</table>

<h3>4.3 ML Evaluation Metrics</h3>
<table border="1" cellpadding="6">
  <tr><th>Metric</th><th>Formula</th><th>Meaning</th></tr>
  <tr><td>Accuracy</td><td>(TP + TN) / (TP + TN + FP + FN)</td><td>Overall correctness of predictions.</td></tr>
  <tr><td>Precision</td><td>TP / (TP + FP)</td><td>Fraction of predicted positives that are truly positive.</td></tr>
  <tr><td>Recall (TPR)</td><td>TP / (TP + FN)</td><td>Fraction of actual positives correctly identified.</td></tr>
  <tr><td>F1 Score</td><td>2 × (Precision × Recall) / (Precision + Recall)</td><td>Harmonic mean of precision and recall.</td></tr>
  <tr><td>ROC-AUC</td><td>Area under ROC curve</td><td>Probability model ranks positive higher than negative.</td></tr>
</table>

<hr>

<!-- ========================================================= -->
<!-- System Overview -->
<!-- ========================================================= -->
<h2>5. System Overview</h2>

<h3>5.1 Objectives</h3>
<ul>
  <li>Centralize and visualize model evaluation and KPI insights.</li>
  <li>Enable dataset selection, caching, and fast interaction.</li>
  <li>Map technical results to business domains and KPIs.</li>
  <li>Provide exportable, interpretable visuals for stakeholders.</li>
</ul>

<h3>5.2 High-Level Data Flow</h3>
<pre>[Notebooks/ETL] → CSV/JSON artifacts → [Streamlit Loaders] → Tabs & Visuals → Insights/Decisions</pre>

<hr>

<!-- ========================================================= -->
<!-- Data & File Structure -->
<!-- ========================================================= -->
<h2>6. Data and File Structure</h2>

<h3>6.1 Directories</h3>
<table border="1" cellpadding="6">
  <tr><th>Path</th><th>Purpose</th></tr>
  <tr><td>notebooks/comparison_results/</td><td>Per-dataset predictions and metrics.</td></tr>
  <tr><td>notebooks/combined_results/</td><td>Aggregated “best” predictions and metrics.</td></tr>
  <tr><td>data/artifacts/</td><td>Business-focused files (e.g., KPI matrix CSV).</td></tr>
</table>

<h3>6.2 Required Files</h3>
<ul>
  <li><strong>platforms_comparison_metrics.csv:</strong> Summary of accuracy per dataset/model.</li>
  <li><strong>&lt;dataset&gt;_predictions.csv:</strong> Predictions with true label and probability.</li>
  <li><strong>&lt;dataset&gt;_metrics.json:</strong> Model metrics (accuracy, precision, recall, f1, auc).</li>
  <li><strong>combined_high_accuracy_*.{csv,json}:</strong> Combined results for “combined” selection.</li>
  <li><strong>supply_chain_kpi_matrix.csv:</strong> KPI and Value columns for KPI Matrix tab.</li>
</ul>

<h3>6.3 Example Schema: Predictions CSV</h3>
<table border="1" cellpadding="6">
  <tr><th>Column</th><th>Type</th><th>Description</th></tr>
  <tr><td>efficiency_label</td><td>int/bool</td><td>Ground truth class (e.g., 0/1).</td></tr>
  <tr><td>predicted_efficiency</td><td>int/bool</td><td>Predicted class.</td></tr>
  <tr><td>predicted_probability</td><td>float</td><td>Confidence score (0–1).</td></tr>
  <tr><td>feature_*</td><td>float/int</td><td>Optional input features used by the model.</td></tr>
</table>

<hr>

<!-- ========================================================= -->
<!-- Data Preparation -->
<!-- ========================================================= -->
<h2>7. Data Preparation</h2>

<h3>7.1 Cleaning</h3>
<ul>
  <li>Removing duplicates and inconsistent records.</li>
  <li>Handling missing values (impute or drop based on logic).</li>
  <li>Standardizing units (e.g., time, currency).</li>
</ul>

<h3>7.2 Feature Engineering</h3>
<ul>
  <li>Lagged demand features for forecasting.</li>
  <li>Supplier-level reliability indices.</li>
  <li>Log-transform skewed cost/time features.</li>
  <li>Creation of composite KPIs (e.g., Service Cost Index).</li>
</ul>

<h3>7.3 Splits</h3>
<ul>
  <li>Train/Validation/Test by time (if temporal) or stratification (if class-imbalance).</li>
  <li>Cross-validation for robust estimation.</li>
</ul>

<hr>

<!-- ========================================================= -->
<!-- ML Pipeline -->
<!-- ========================================================= -->
<h2>8. Machine Learning Pipeline</h2>

<h3>8.1 Modeling Steps</h3>
<ol>
  <li>Define target (e.g., efficient vs. inefficient operation).</li>
  <li>Select algorithms (Logistic Regression, Random Forest, XGBoost, LightGBM).</li>
  <li>Hyperparameter search (Grid/Random/Bayesian).</li>
  <li>Evaluate with metrics and confusion matrix.</li>
  <li>Calibrate probabilities if needed (Platt/Isotonic).</li>
</ol>

<h3>8.2 Confusion Matrix Notation</h3>
<table border="1" cellpadding="6">
  <tr><th></th><th>Predicted Positive</th><th>Predicted Negative</th></tr>
  <tr><td>Actual Positive</td><td>TP</td><td>FN</td></tr>
  <tr><td>Actual Negative</td><td>FP</td><td>TN</td></tr>
</table>

<h3>8.3 Thresholding and Calibration</h3>
<ul>
  <li>Default threshold is 0.5, but adjust per business cost.</li>
  <li>Calibrate to align predicted probabilities with observed frequencies.</li>
</ul>

<hr>

<!-- ========================================================= -->
<!-- Evaluation & Interpretation -->
<!-- ========================================================= -->
<h2>9. Evaluation and Interpretation</h2>

<h3>9.1 Metric Selection Rationale</h3>
<ul>
  <li><strong>Accuracy:</strong> Good for balanced classes; otherwise can be misleading.</li>
  <li><strong>Precision &amp; Recall:</strong> Choose based on tolerance for FP vs FN.</li>
  <li><strong>F1 Score:</strong> Balance metric useful for uneven error costs.</li>
  <li><strong>ROC-AUC:</strong> Threshold-invariant ranking capability.</li>
</ul>

<h3>9.2 Business-Centric Thresholding</h3>
<ul>
  <li>If missing true inefficiencies is costly, increase Recall.</li>
  <li>If unnecessary interventions are costly, increase Precision.</li>
</ul>

<hr>

<!-- ========================================================= -->
<!-- Streamlit Application Architecture -->
<!-- ========================================================= -->
<h2>10. Application Architecture (Streamlit)</h2>

<h3>10.1 Config & Caching</h3>
<ul>
  <li>Path constants: NOTEBOOKS_DIR, ARTIFACTS_DIR, COMPARISON_DIR, COMBINED_DIR.</li>
  <li>@st.cache_data improves load time; “Refresh Cache” clears caches for fresh reads.</li>
</ul>

<h3>10.2 Tabs Overview</h3>
<ol>
  <li><strong>Overview:</strong> Confusion matrix and ROC curve; KPI cards.</li>
  <li><strong>KPI Insights:</strong> Mean KPI bars and variability boxplots.</li>
  <li><strong>Python Charts:</strong> Interactive user-chosen axes for 8 visual types.</li>
  <li><strong>Comparison:</strong> Accuracy comparison across datasets.</li>
  <li><strong>Business Domains:</strong> Domain mapping and colored performance table.</li>
  <li><strong>KPI Matrix:</strong> Table + radar (polar) + bar chart from CSV.</li>
  <li><strong>Team:</strong> Contributors and roles.</li>
</ol>

<h3>10.3 Data Downsampling</h3>
<p>
To keep UI responsive with large CSVs, a downsample function limits rows (e.g., 5,000) for quick visuals while preserving distribution.
</p>

<hr>

<!-- ========================================================= -->
<!-- KPI Matrix Design -->
<!-- ========================================================= -->
<h2>11. KPI Matrix Design</h2>

<h3>11.1 Input Format</h3>
<pre>data/artifacts/supply_chain_kpi_matrix.csv</pre>
<table border="1" cellpadding="6">
  <tr><th>Column</th><th>Type</th><th>Notes</th></tr>
  <tr><td>KPI</td><td>string</td><td>Short, clear names (e.g., Lead Time, Fill Rate).</td></tr>
  <tr><td>Value</td><td>float</td><td>Normalized 0–1 or scaled 0–100.</td></tr>
</table>

<h3>11.2 Visualization Choices</h3>
<ul>
  <li><strong>Table:</strong> Inspect actual values by KPI.</li>
  <li><strong>Radar:</strong> “Shape” of strengths and weaknesses across KPIs.</li>
  <li><strong>Bar Chart:</strong> Rank/order KPIs by value importance.</li>
</ul>

<hr>

<!-- ========================================================= -->
<!-- Business Domain Mapping -->
<!-- ========================================================= -->
<h2>12. Business Domain Mapping</h2>

<table border="1" cellpadding="6">
  <tr><th>Domain</th><th>Keyword Examples</th><th>Mapped Columns (examples)</th></tr>
  <tr><td>Inventory Management</td><td>inventory, stock</td><td>inventory_level, stock_out_rate</td></tr>
  <tr><td>Demand Forecasting</td><td>demand</td><td>forecast_error, seasonality_factor</td></tr>
  <tr><td>Logistics Planning</td><td>logistic, lead_time</td><td>delivery_time, route_score</td></tr>
  <tr><td>Supplier Collaboration</td><td>supplier, vendor</td><td>supplier_rating, vendor_lead_time</td></tr>
  <tr><td>Cost Reduction</td><td>cost, profit</td><td>storage_cost, transport_cost</td></tr>
</table>

<hr>

<!-- ========================================================= -->
<!-- Use Cases & Scenarios -->
<!-- ========================================================= -->
<h2>13. Use Cases and Scenarios</h2>

<h3>13.1 Inventory Replenishment</h3>
<ul>
  <li>Use predicted inefficiency + low fill rate → trigger review of reorder points.</li>
  <li>Monitor turnover and carrying cost to balance cash flow.</li>
</ul>

<h3>13.2 Supplier Scorecards</h3>
<ul>
  <li>Combine lead time variability and defect/return rate to rank suppliers.</li>
  <li>Align procurement contracts with reliability targets.</li>
</ul>

<h3>13.3 Logistics Optimization</h3>
<ul>
  <li>Analyze delivery delays and route KPIs to choose modes and carriers.</li>
  <li>Set SLAs based on predicted bottlenecks.</li>
</ul>

<hr>

<!-- ========================================================= -->
<!-- Case Studies -->
<!-- ========================================================= -->
<h2>14. Case Studies</h2>

<h3>14.1 Mid-Size Retailer</h3>
<ul>
  <li>Problem: Stockouts during promotions; high storage cost otherwise.</li>
  <li>Action: Integrate forecast error KPIs; recalibrate reorder models.</li>
  <li>Outcome: 15–25% reduction in stockouts, reduced excess inventory.</li>
</ul>

<h3>14.2 Manufacturing Supplier Network</h3>
<ul>
  <li>Problem: Unpredictable supplier lead time caused production delays.</li>
  <li>Action: Supplier reliability KPI + recall-driven thresholding.</li>
  <li>Outcome: Improved on-time delivery rate and stable production schedule.</li>
</ul>

<hr>

<!-- ========================================================= -->
<!-- Risks & Constraints -->
<!-- ========================================================= -->
<h2>15. Risks and Constraints</h2>
<ul>
  <li>Data quality issues (missing, inconsistent, delayed).</li>
  <li>Concept drift due to seasonality or market shocks.</li>
  <li>Interpretability: Must align model outputs with KPIs.</li>
  <li>Security and access control for sensitive data.</li>
</ul>

<hr>

<!-- ========================================================= -->
<!-- Ethical Considerations -->
<!-- ========================================================= -->
<h2>16. Ethical Considerations</h2>
<ul>
  <li>Use anonymized, aggregated data where possible.</li>
  <li>Prevent biased decisions against particular suppliers or regions without cause.</li>
  <li>Explainability: Provide rationale for thresholds and actions.</li>
</ul>

<hr>

<!-- ========================================================= -->
<!-- Performance & Scaling -->
<!-- ========================================================= -->
<h2>17. Performance and Scaling</h2>
<ul>
  <li>Caching of CSV/JSON reads for responsiveness.</li>
  <li>Downsampling large CSVs for fast charting.</li>
  <li>Optional pre-aggregation for heavy KPI queries.</li>
</ul>

<hr>

<!-- ========================================================= -->
<!-- Deployment Options -->
<!-- ========================================================= -->
<h2>18. Deployment Options</h2>
<ul>
  <li>Local: <code>streamlit run app.py</code></li>
  <li>Streamlit Cloud: Push repo and connect.</li>
  <li>Docker/VPS: Containerize and serve via reverse proxy.</li>
  <li>Enterprise: Kubernetes + CI/CD pipelines for artifacts.</li>
</ul>

<hr>

<!-- ========================================================= -->
<!-- CI/CD and Automation -->
<!-- ========================================================= -->
<h2>19. CI/CD and Automation</h2>
<ul>
  <li>GitHub Actions: test linting and build on push.</li>
  <li>Automated artifact refresh (nightly KPI CSV generation).</li>
  <li>Versioned datasets for reproducibility.</li>
</ul>

<hr>

<!-- ========================================================= -->
<!-- Testing Strategy -->
<!-- ========================================================= -->
<h2>20. Testing Strategy</h2>
<ul>
  <li>Unit tests for loaders and metric calculators.</li>
  <li>Schema validation for input CSV/JSON.</li>
  <li>Golden images (optional) for deterministic charts.</li>
</ul>

<hr>

<!-- ========================================================= -->
<!-- Logging & Monitoring -->
<!-- ========================================================= -->
<h2>21. Logging and Monitoring</h2>
<ul>
  <li>Record load durations and cache hits/misses.</li>
  <li>Track anomalies in KPI values.</li>
  <li>Usage analytics for feature prioritization.</li>
</ul>

<hr>

<!-- ========================================================= -->
<!-- Security & Privacy -->
<!-- ========================================================= -->
<h2>22. Security and Privacy</h2>
<ul>
  <li>Restrict access to artifact directories.</li>
  <li>Avoid storing PII; use aggregated metrics.</li>
  <li>Audit logs for compliance.</li>
</ul>

<hr>

<!-- ========================================================= -->
<!-- Troubleshooting -->
<!-- ========================================================= -->
<h2>23. Troubleshooting</h2>
<table border="1" cellpadding="6">
  <tr><th>Issue</th><th>Possible Cause</th><th>Fix</th></tr>
  <tr><td>No datasets in sidebar</td><td>Empty directories</td><td>Place CSV/JSON into comparison/combined folders.</td></tr>
  <tr><td>Charts empty</td><td>Missing columns</td><td>Ensure efficiency_label/predicted_* columns exist.</td></tr>
  <tr><td>KPI Matrix warning</td><td>CSV missing</td><td>Create supply_chain_kpi_matrix.csv with KPI/Value.</td></tr>
  <tr><td>Slow loading</td><td>Huge CSVs</td><td>Use downsampling or pre-aggregate.</td></tr>
</table>

<hr>

<!-- ========================================================= -->
<!-- FAQs -->
<!-- ========================================================= -->
<h2>24. Frequently Asked Questions</h2>
<h3>Q1: Can I rename folders?</h3>
<p>Yes. Update path constants in <code>app.py</code>.</p>
<h3>Q2: Can I add more KPIs?</h3>
<p>Yes. Add rows to KPI CSV and refresh cache.</p>
<h3>Q3: What if classes are imbalanced?</h3>
<p>Use stratification, resampling, and F1/Recall-driven thresholds.</p>

<hr>

<!-- ========================================================= -->
<!-- Glossary -->
<!-- ========================================================= -->
<h2>25. Glossary</h2>
<ul>
  <li><strong>TP/FP/FN/TN:</strong> True/False Positive/Negative.</li>
  <li><strong>AUC:</strong> Area under ROC curve.</li>
  <li><strong>Lead Time:</strong> Time from order to delivery.</li>
  <li><strong>Fill Rate:</strong> Portion of demand satisfied from stock.</li>
</ul>

<hr>

<!-- ========================================================= -->
<!-- Example Snippets -->
<!-- ========================================================= -->
<h2>26. Example Snippets</h2>

<h3>26.1 Example KPI Matrix CSV</h3>
<pre>KPI,Value
Inventory Turnover,0.78
Order Fulfillment Rate,0.91
Lead Time,0.62
Fill Rate,0.88
Warehouse Operating Cost,0.54
</pre>

<h3>26.2 Example Metric JSON</h3>
<pre>{
  "accuracy": 0.87,
  "precision": 0.83,
  "recall": 0.79,
  "f1_score": 0.81,
  "roc_auc": 0.90
}
</pre>

<h3>26.3 Example Prediction CSV (minimal)</h3>
<pre>efficiency_label,predicted_efficiency,predicted_probability
1,1,0.87
0,0,0.21
1,0,0.48
</pre>

<hr>

<!-- ========================================================= -->
<!-- Governance & Change Management -->
<!-- ========================================================= -->
<h2>27. Governance and Change Management</h2>
<ul>
  <li>Document changes to KPI definitions.</li>
  <li>Version models and artifacts to maintain reproducibility.</li>
  <li>Stakeholder review cycles for threshold updates.</li>
</ul>

<hr>

<!-- ========================================================= -->
<!-- Roadmap -->
<!-- ========================================================= -->
<h2>28. Roadmap</h2>
<ul>
  <li>Advanced feature drift detection.</li>
  <li>What-if simulators (scenario planning).</li>
  <li>Automated SLA breach alerts.</li>
  <li>Role-based dashboards for different teams.</li>
</ul>

<hr>

<!-- ========================================================= -->
<!-- Conclusion -->
<!-- ========================================================= -->
<h2>29. Conclusion</h2>
<p>
The Supply Chain Optimization Dashboard aligns data science with business decision-making by combining ML evaluation,
rich visual analytics, KPI mapping, and domain insights. It reduces the distance between raw data and operational action,
supporting continuous improvement in inventory, logistics, procurement, and customer service.
</p>

<hr>

<!-- ========================================================= -->
<!-- Credits / Team -->
<!-- ========================================================= -->
<h2>30. Credits</h2>
<table border="1" cellpadding="6">
  <tr><th>Name</th><th>Role</th><th>Focus</th></tr>
  <tr><td>Pranay Dhore</td><td>Lead Developer / Data Scientist</td><td>Modeling and Architecture</td></tr>
  <tr><td>Paras Longadge</td><td>Data Analyst / Dashboard Designer</td><td>Visual Analytics and UI</td></tr>
  <tr><td>Sanket Tajne</td><td>ML Engineer</td><td>Feature Engineering and Optimization</td></tr>
  <tr><td>Kunal Gomkar</td><td>Logistics & Integration Specialist</td><td>Domain Integration and Operations</td></tr>
</table>

<p><strong>End of Document.</strong></p>

</body>
</html>
