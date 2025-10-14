# ===============================================================
# 📦 SUPPLY CHAIN OPTIMIZATION DASHBOARD — FINAL VERSION
# ===============================================================

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import os, json, warnings
warnings.filterwarnings("ignore")

# ---------------------------------------------------------------
# 🧭 CONFIGURATION
# ---------------------------------------------------------------
DATA_DIR = r"C:\Users\ASUS\OneDrive\Documents\Project\data"
ARTIFACT_DIR = os.path.join(DATA_DIR, "artifacts")

st.set_page_config(page_title="Supply Chain Analytics Dashboard", layout="wide")
st.title("📊 Supply Chain Optimization Dashboard")
st.markdown("Interactive analytics for Inventory, Demand Forecasting, Logistics, and KPI insights")

# ---------------------------------------------------------------
# 📂 LOAD ORIGINAL DATASETS
# ---------------------------------------------------------------
files = [
    "amazon_products_sales_data_cleaned.csv",
    "Flipkart.csv",
    "Meesho.xlsx",
    "Myntra.csv",
    "Snapdeal.csv",
    "Tata CLiQ.csv"
]

datasets = {}
for f in files:
    path = os.path.join(DATA_DIR, f)
    if os.path.exists(path):
        try:
            if f.endswith(".xlsx"):
                df = pd.read_excel(path)
            else:
                df = pd.read_csv(path)
            datasets[f] = df
            st.sidebar.success(f"✅ Loaded {f} ({df.shape[0]} rows)")
        except Exception as e:
            st.sidebar.error(f"❌ Failed to load {f}: {e}")
    else:
        st.sidebar.warning(f"⚠️ Missing file: {f}")

if not datasets:
    st.error("No datasets found! Please ensure your 6 marketplace files are in the data folder.")
    st.stop()

# ---------------------------------------------------------------
# 🧾 SIDEBAR OPTIONS
# ---------------------------------------------------------------
st.sidebar.header("⚙️ Controls")
selected_dataset = st.sidebar.selectbox("Select Dataset", list(datasets.keys()) + ["Combined (All)"])
st.sidebar.markdown("---")

# ---------------------------------------------------------------
# 🧩 LOAD SELECTED DATASET
# ---------------------------------------------------------------
if selected_dataset == "Combined (All)":
    df = pd.concat(datasets.values(), ignore_index=True, sort=False)
    st.subheader("📘 Combined Dataset (All Marketplaces)")
else:
    df = datasets[selected_dataset]
    st.subheader(f"📘 Dataset: {selected_dataset}")

st.write(f"Shape: {df.shape[0]} rows × {df.shape[1]} columns")
st.dataframe(df.head(10))

# ---------------------------------------------------------------
# 🧩 MISSING VALUE SUMMARY
# ---------------------------------------------------------------
st.subheader("🧩 Missing Value Overview")
missing = (df.isnull().sum() / len(df) * 100).round(2)
missing = missing[missing > 0]
if not missing.empty:
    st.bar_chart(missing)
else:
    st.success("✅ No missing values found!")

# ---------------------------------------------------------------
# 📈 FEATURE DISTRIBUTIONS
# ---------------------------------------------------------------
st.subheader("📈 Feature Distributions")

num_cols = df.select_dtypes(include=["number"]).columns[:5]
cat_cols = df.select_dtypes(include=["object","category","bool"]).columns[:3]

col1, col2 = st.columns(2)

with col1:
    if len(num_cols) > 0:
        sel_num = st.selectbox("Select Numeric Feature", num_cols)
        fig = px.histogram(df, x=sel_num, nbins=40,
                           title=f"Distribution of {sel_num}",
                           color_discrete_sequence=["#4CAF50"])
        st.plotly_chart(fig, use_container_width=True)

with col2:
    if len(cat_cols) > 0:
        sel_cat = st.selectbox("Select Categorical Feature", cat_cols)
        top = df[sel_cat].value_counts().nlargest(15).reset_index()
        top.columns = [sel_cat, "count"]
        fig = px.bar(top, x=sel_cat, y="count",
                     title=f"Top Categories in {sel_cat}",
                     color="count", color_continuous_scale="Viridis")
        st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------------
# 🔗 CORRELATION HEATMAP
# ---------------------------------------------------------------
st.subheader("🔗 Correlation Heatmap")
num_data = df.select_dtypes(include=["number"])
if num_data.shape[1] > 1:
    corr = num_data.corr()
    fig = px.imshow(corr, text_auto=".2f", title="Feature Correlation Matrix", color_continuous_scale="Tealgrn")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.info("Not enough numeric columns for correlation analysis.")

# ---------------------------------------------------------------
# 🔍 BIVARIATE RELATIONSHIPS
# ---------------------------------------------------------------
st.subheader("🔍 Bivariate Relationships")

lower = [c.lower() for c in df.columns]
price_col = next((df.columns[i] for i,v in enumerate(lower) if 'price' in v), None)
rating_col = next((df.columns[i] for i,v in enumerate(lower) if 'rating' in v), None)
sold_col = next((df.columns[i] for i,v in enumerate(lower) if 'sold' in v or 'purchased' in v or 'units' in v), None)

if price_col and rating_col:
    fig = px.scatter(df, x=price_col, y=rating_col, color=rating_col,
                     title=f"{price_col} vs {rating_col}",
                     color_continuous_scale="Blues")
    st.plotly_chart(fig, use_container_width=True)

if rating_col and sold_col:
    fig = px.scatter(df, x=rating_col, y=sold_col, color=sold_col,
                     title=f"{rating_col} vs {sold_col}",
                     color_continuous_scale="Viridis")
    st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------------
# 🌍 CROSS-DATASET COMPARISONS
# ---------------------------------------------------------------
st.subheader("🌍 Cross-Marketplace Comparison")

compare_stats = []
for name, d in datasets.items():
    lower_cols = [c.lower() for c in d.columns]
    price = next((d.columns[i] for i,v in enumerate(lower_cols) if 'price' in v), None)
    rating = next((d.columns[i] for i,v in enumerate(lower_cols) if 'rating' in v), None)
    sold = next((d.columns[i] for i,v in enumerate(lower_cols) if 'sold' in v or 'purchased' in v or 'units' in v), None)
    compare_stats.append({
        "Marketplace": name.replace(".csv","").replace(".xlsx",""),
        "Avg Price": round(d[price].mean(), 2) if price else np.nan,
        "Avg Rating": round(d[rating].mean(), 2) if rating else np.nan,
        "Total Sold": round(d[sold].sum(), 2) if sold else np.nan,
        "Rows": len(d)
    })

compare_df = pd.DataFrame(compare_stats)
st.dataframe(compare_df)

# Compare visuals
colA, colB = st.columns(2)
with colA:
    fig = px.bar(compare_df, x="Marketplace", y="Avg Price", color="Avg Price", title="Average Price by Marketplace")
    st.plotly_chart(fig, use_container_width=True)
with colB:
    fig = px.bar(compare_df, x="Marketplace", y="Avg Rating", color="Avg Rating", title="Average Rating by Marketplace")
    st.plotly_chart(fig, use_container_width=True)

fig = px.bar(compare_df, x="Marketplace", y="Total Sold", color="Total Sold",
             title="Total Units Sold by Marketplace")
st.plotly_chart(fig, use_container_width=True)

# ---------------------------------------------------------------
# 🤖 MODEL PERFORMANCE (from artifacts)
# ---------------------------------------------------------------
st.subheader("🤖 Model Performance Metrics")
metrics_path = os.path.join(ARTIFACT_DIR, "nn_model_metrics.csv")
if os.path.exists(metrics_path):
    metrics = pd.read_csv(metrics_path)
    st.dataframe(metrics)
    melted = metrics.melt(var_name="Metric", value_name="Score")
    fig = px.bar(melted, x="Metric", y="Score",
                 text_auto=True, color="Metric",
                 title="Model Evaluation Summary")
    st.plotly_chart(fig, use_container_width=True)
else:
    st.warning("⚠️ Model metrics not found in artifacts folder.")

# ---------------------------------------------------------------
# 📊 SUPPLY CHAIN KPI VISUALIZATION
# ---------------------------------------------------------------
st.subheader("📊 Supply Chain KPI Matrix")
kpi_path = os.path.join(ARTIFACT_DIR, "supply_chain_kpi_matrix.csv")
if os.path.exists(kpi_path):
    kpi_df = pd.read_csv(kpi_path)
    st.dataframe(kpi_df)
    radar = px.line_polar(kpi_df, r="Value", theta="KPI", line_close=True,
                          title="Performance Matrix", template="plotly_dark")
    radar.update_traces(fill="toself")
    st.plotly_chart(radar, use_container_width=True)
    st.plotly_chart(px.bar(kpi_df, x="KPI", y="Value", color="Value", title="KPI Comparison"),
                    use_container_width=True)
else:
    st.warning("⚠️ KPI file not found. Run KPI generation notebook first.")

# ---------------------------------------------------------------
# 💡 BUSINESS INSIGHTS (TABLE FORMAT)
# ---------------------------------------------------------------
st.subheader("💡 Business Insights & Recommendations")

insight_path = os.path.join(ARTIFACT_DIR, "supply_chain_insights.json")
if os.path.exists(insight_path):
    with open(insight_path, "r") as f:
        insights = json.load(f)
    
    # Convert JSON to DataFrame
    insights_df = pd.DataFrame(list(insights.items()), columns=["Category", "Insight / Recommendation"])
    
    # Clean formatting
    insights_df["Category"] = insights_df["Category"].str.replace("_", " ").str.title()
    
    # Display in table
    st.dataframe(
        insights_df.style.set_properties(**{
            'background-color': "#000000",
            'border-color': '#DDDDDD',
            'color': "#FFFFFF"
        }),
        use_container_width=True
    )
else:
    st.info("Insights JSON not found in artifacts folder.")


# ---------------------------------------------------------------
# 🏁 FOOTER
# ---------------------------------------------------------------
st.markdown("---")
st.caption("✅ Built with Streamlit | Reads original datasets & artifacts for Supply Chain Analytics")
