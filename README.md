<!DOCTYPE html>
<html>
<head>
  <title>Supply Chain Optimization Dashboard - Documentation</title>
  <meta charset="UTF-8">
</head>
<body>

<h1>📦 Supply Chain Optimization Dashboard</h1>

<p>
This dashboard provides a complete analytical and decision-support interface for evaluating Supply Chain efficiency using Machine Learning models. 
It integrates performance metrics, business KPIs, domain mapping, statistical insights, and visualizations in a structured and easy-to-use UI.
</p>

<hr>

<h2>1. 🎯 Project Objective</h2>
<p>
The goal is to optimize supply chain operations by identifying performance gaps, predicting efficiency categories, and recommending improvements.
The dashboard enables:
</p>
<ul>
  <li>Performance monitoring of supply chain workflows.</li>
  <li>Model-based insights for decision-making.</li>
  <li>Cross-domain evaluation (inventory, logistics, demand, cost, etc.).</li>
</ul>

<hr>

<h2>2. 🧠 Machine Learning Metrics Used</h2>

<table border="1" cellpadding="6">
  <tr><th>Metric</th><th>Meaning</th><th>Importance</th></tr>
  <tr><td>Accuracy</td><td>Percentage of correct predictions.</td><td>General model correctness.</td></tr>
  <tr><td>Precision</td><td>Correct positive predictions out of total predicted positives.</td><td>Useful when false positives matter.</td></tr>
  <tr><td>Recall</td><td>Correct positive predictions out of actual positives.</td><td>Useful when missing true cases is costly.</td></tr>
  <tr><td>F1 Score</td><td>Balance between Precision & Recall.</td><td>Combined performance quality.</td></tr>
  <tr><td>AUC Score</td><td>Probability-based classification strength.</td><td>Shows how well model separates classes.</td></tr>
</table>

<hr>

<h2>3. 📊 KPI Matrix (Business KPI Mapping)</h2>

<p>This matrix connects technical model results to business performance metrics.</p>

<table border="1" cellpadding="6">
  <tr><th>KPI Name</th><th>Explanation</th><th>Impact on Supply Chain</th></tr>
  <tr><td>Inventory Turnover</td><td>How fast inventory is used or sold.</td><td>Higher values = Better warehouse efficiency.</td></tr>
  <tr><td>Order Fulfillment Rate</td><td>Percentage of orders delivered successfully.</td><td>Direct measure of customer satisfaction.</td></tr>
  <tr><td>Lead Time</td><td>Time between order placement and delivery.</td><td>Lower lead time = Faster supply flow.</td></tr>
  <tr><td>Warehouse Cost</td><td>Total cost of storage, labor & handling.</td><td>Lower = Higher operational efficiency.</td></tr>
  <tr><td>Supplier Reliability</td><td>Consistency of supplier delivery.</td><td>Affects overall supply chain stability.</td></tr>
</table>

<p><strong>Dashboard Input File Required:</strong></p>
<pre>data/artifacts/supply_chain_kpi_matrix.csv</pre>

<p><strong>Required Columns:</strong></p>
<table border="1" cellpadding="6">
  <tr><th>Column Name</th><th>Type</th><th>Description</th></tr>
  <tr><td>KPI</td><td>Text</td><td>Name of the performance metric.</td></tr>
  <tr><td>Value</td><td>Numeric</td><td>Score between 0–1 or 0–100.</td></tr>
</table>

<hr>

<h2>4. 🏢 Business Domain Mapping</h2>

<table border="1" cellpadding="6">
  <tr><th>Business Domain</th><th>Example Dataset Attributes</th><th>Insights Provided</th></tr>
  <tr><td>Inventory Management</td><td>stock_level, reorder_point</td><td>Ensures optimal stock control.</td></tr>
  <tr><td>Logistics & Transportation</td><td>delivery_time, route_efficiency</td><td>Improves delivery speed and cost.</td></tr>
  <tr><td>Demand Forecasting</td><td>historic_orders, seasonality</td><td>Prevents understocking/overstocking.</td></tr>
  <tr><td>Supplier Management</td><td>supplier_rating, lead_time</td><td>Enhances procurement stability.</td></tr>
  <tr><td>Cost Optimization</td><td>storage_cost, labor_cost</td><td>Minimizes operational expenditure.</td></tr>
</table>

<hr>

<h2>5. 📁 Dataset & File Requirements</h2>

<p>The dashboard loads prediction and metrics results from structured files:</p>

<table border="1" cellpadding="6">
  <tr><th>Directory</th><th>Description</th></tr>
  <tr><td>notebooks/comparison_results/</td><td>Model-specific predictions and evaluation metrics.</td></tr>
  <tr><td>notebooks/combined_results/</td><td>Aggregated high-performance combined predictions.</td></tr>
  <tr><td>data/artifacts/</td><td>KPI Matrix and business result artifacts.</td></tr>
</table>

<hr>

<h2>6. 🛠 Installation Instructions</h2>

<h3>Step 1 — Clone the repository</h3>
<pre>
git clone &lt;your-repository-link&gt;
cd project-folder
</pre>

<h3>Step 2 — Create Virtual Environment</h3>
<pre>
python -m venv venv
venv\Scripts\activate   (Windows)
</pre>

<h3>Step 3 — Install Dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>Step 4 — Run Dashboard</h3>
<pre>
streamlit run app.py
</pre>

<hr>

<h2>7. 📊 Visual Output Screens in Dashboard</h2>

<ul>
  <li>Model KPI Summary Cards</li>
  <li>Confusion Matrix Heatmap</li>
  <li>ROC Curve & AUC Score</li>
  <li>Interactive Python Graphs (Scatter / Bar / Heatmap)</li>
  <li>Domain-wise KPI Performance Heat Table</li>
  <li>KPI Performance Radar Chart</li>
</ul>

<hr>

<h2>8. 👥 Project Team</h2>

<table border="1" cellpadding="6">
  <tr><th>Name</th><th>Role</th><th>Contribution</th></tr>
  <tr><td><strong>Pranay Dhore</strong></td><td>Lead Developer</td><td>Model training & architecture.</td></tr>
  <tr><td><strong>Paras Longadge</strong></td><td>Data Analyst & UI Designer</td><td>Dashboard design & analysis visuals.</td></tr>
  <tr><td><strong>Sanket Tajne</strong></td><td>ML Engineer</td><td>Feature engineering & tuning.</td></tr>
  <tr><td><strong>Kunal Gomkar</strong></td><td>Supply Chain Specialist</td><td>Operational domain alignment.</td></tr>
</table>

<hr>

<h2>9. 🔮 Future Enhancements</h2>
<ul>
  <li>Deployment to Cloud (AWS, Azure, GCP)</li>
  <li>Real-Time IoT/ERP Data Integration</li>
  <li>Automated Predictive Demand Forecasting</li>
  <li>PDF / PPT auto-report export</li>
</ul>

<hr>

<h2>10. ⭐ Support</h2>
<p>If this project benefits you, please star the repository and share!</p>

<p><strong>Built with ♥ for smart and efficient Supply Chain Systems.</strong></p>

</body>
</html>
