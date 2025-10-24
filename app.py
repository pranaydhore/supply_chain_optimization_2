# import os, json
# from datetime import datetime
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import plotly.graph_objects as go
# import streamlit as st
# from sklearn.metrics import confusion_matrix, roc_curve, auc

# # ========================
# # CONFIGURATION
# # ========================
# NOTEBOOKS_DIR = r"C:\Users\ASUS\OneDrive\Documents\Project\notebooks"
# ARTIFACTS_DIR = r"C:\Users\ASUS\OneDrive\Documents\Project\data\artifacts"
# COMPARISON_DIR = os.path.join(NOTEBOOKS_DIR, "comparison_results")
# COMBINED_DIR = os.path.join(NOTEBOOKS_DIR, "combined_results")
# SUMMARY_CSV = os.path.join(COMPARISON_DIR, "platforms_comparison_metrics.csv")

# # ========================
# # STREAMLIT SETUP
# # ========================
# st.set_page_config(page_title="Supply Chain Optimization Dashboard", layout="wide", page_icon="📦")

# st.markdown("""
# <h1 style='text-align:center;color:#0047AB;'>📦 Supply Chain Optimization Dashboard — AI/ML Insights</h1>
# <p style='text-align:center;color:gray;'>Interactive, professional, and performance-oriented visualization of supply chain analytics.</p>
# """, unsafe_allow_html=True)

# # ========================
# # LOADERS
# # ========================
# @st.cache_data(show_spinner=False)
# def safe_load_csv(path):
#     if not os.path.exists(path): return pd.DataFrame()
#     try: df = pd.read_csv(path)
#     except Exception: df = pd.read_csv(path, engine="python")
#     df = df.loc[:, ~df.columns.duplicated()]
#     return df

# @st.cache_data(show_spinner=False)
# def safe_load_json(path):
#     if not os.path.exists(path): return {}
#     with open(path, "r", encoding="utf-8") as f: return json.load(f)

# def downsample(df, n=5000):
#     return df.sample(n, random_state=42) if not df.empty and len(df) > n else df

# # ========================
# # LOAD DATA
# # ========================
# summary_df = safe_load_csv(SUMMARY_CSV)
# datasets = [d for d in os.listdir(COMPARISON_DIR) if os.path.isdir(os.path.join(COMPARISON_DIR, d))] if os.path.exists(COMPARISON_DIR) else []
# if os.path.exists(COMBINED_DIR): datasets.insert(0, "combined")

# st.sidebar.header("Select Dataset")
# selected = st.sidebar.selectbox("Dataset", ["-- Select --"] + datasets)

# if st.sidebar.button("🔄 Refresh Cache"):
#     st.cache_data.clear()
#     st.experimental_rerun()

# df, metrics = pd.DataFrame(), {}
# if selected != "-- Select --":
#     preds_file = os.path.join(COMBINED_DIR if selected == "combined" else os.path.join(COMPARISON_DIR, selected),
#                               f"{'combined_high_accuracy_predictions' if selected == 'combined' else selected + '_predictions'}.csv")
#     metrics_file = os.path.join(COMBINED_DIR if selected == "combined" else os.path.join(COMPARISON_DIR, selected),
#                                 f"{'combined_high_accuracy_metrics' if selected == 'combined' else selected + '_metrics'}.json")
#     df, metrics = safe_load_csv(preds_file), safe_load_json(metrics_file)
#     df = downsample(df)

# # ========================
# # KPI CARDS
# # ========================
# st.markdown(f"### 🔍 {selected.upper() if selected!='-- Select --' else 'NO DATA SELECTED'} — Model KPIs")

# if df.empty:
#     st.info("Please select a dataset from the sidebar to view details.")
# else:
#     cols = st.columns(5)
#     cols[0].metric("Accuracy", f"{metrics.get('accuracy', 0)*100:.2f}%")
#     cols[1].metric("Precision", f"{metrics.get('precision', 0)*100:.2f}%")
#     cols[2].metric("Recall", f"{metrics.get('recall', 0)*100:.2f}%")
#     cols[3].metric("F1 Score", f"{metrics.get('f1_score', 0)*100:.2f}%")
#     cols[4].metric("AUC", f"{metrics.get('roc_auc', 0):.3f}")

# # ========================
# # MAIN TABS
# # ========================
# tab_overview, tab_kpi, tab_python, tab_compare, tab_domains, tab_team = st.tabs([
#     "📊 Overview", "📈 KPI Insights", "🎨 Python Charts", "🧭 Comparison", "🏢 Business Domains", "👥 Team"
# ])

# # =====================================================
# # OVERVIEW TAB
# # =====================================================
# with tab_overview:
#     if df.empty:
#         st.info("Select a dataset to view Overview.")
#     else:
#         c1, c2 = st.columns(2)
#         if {"efficiency_label", "predicted_efficiency"}.issubset(df.columns):
#             cm = pd.crosstab(df["efficiency_label"], df["predicted_efficiency"])
#             fig_cm = px.imshow(cm, text_auto=True, color_continuous_scale="Tealrose", title="Confusion Matrix")
#             c1.plotly_chart(fig_cm, use_container_width=True)
#         if {"efficiency_label", "predicted_probability"}.issubset(df.columns):
#             d_roc = df.dropna(subset=["efficiency_label", "predicted_probability"])
#             if not d_roc.empty:
#                 fpr, tpr, _ = roc_curve(d_roc["efficiency_label"], d_roc["predicted_probability"])
#                 roc_auc = auc(fpr, tpr)
#                 fig_roc = go.Figure()
#                 fig_roc.add_trace(go.Scatter(x=fpr, y=tpr, mode="lines", line=dict(width=3, color="#1f77b4"),
#                                              name=f"AUC={roc_auc:.3f}"))
#                 fig_roc.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines", line=dict(dash="dash", color="gray")))
#                 fig_roc.update_layout(title="ROC Curve", xaxis_title="False Positive Rate", yaxis_title="True Positive Rate")
#                 c2.plotly_chart(fig_roc, use_container_width=True)

# # =====================================================
# # KPI INSIGHTS TAB
# # =====================================================
# with tab_kpi:
#     if df.empty:
#         st.info("Select a dataset to view KPI insights.")
#     else:
#         st.markdown("### 🎯 KPI Insights — Clear, Colorful & Easy to Interpret")

#         numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
#         if not numeric_cols:
#             st.warning("No numeric columns available for KPI visualization.")
#         else:
#             # KPI Mean Bar Chart
#             kpi_summary = df[numeric_cols].mean().sort_values(ascending=False).reset_index()
#             kpi_summary.columns = ["KPI", "Mean Value"]
#             fig_bar = px.bar(kpi_summary, x="KPI", y="Mean Value", color="Mean Value",
#                              color_continuous_scale="Viridis", text_auto=".2f",
#                              title="Average KPI Scores — Business & Technical Clarity")
#             fig_bar.update_layout(xaxis_tickangle=45, height=500)
#             st.plotly_chart(fig_bar, use_container_width=True)

#             # KPI Variability Boxplot
#             st.markdown("### 📊 KPI Variability Across Dataset")
#             fig_box = px.box(df, y=numeric_cols, color_discrete_sequence=px.colors.qualitative.Set2)
#             fig_box.update_layout(height=600, title="KPI Distribution Range (Performance Spread)")
#             st.plotly_chart(fig_box, use_container_width=True)

# # =====================================================
# # PYTHON CHARTS TAB (8 Reactive Charts)
# # =====================================================
# with tab_python:
#     if df.empty:
#         st.info("Select dataset to generate Python charts.")
#     else:
#         st.markdown("### 🎨 Python Charts — 8 Dynamic Graphs (User Controlled Axes)")
#         num_cols = df.select_dtypes(include=[np.number]).columns.tolist()

#         col1, col2 = st.columns(2)
#         x_axis = col1.selectbox("Select X-axis", num_cols, index=0)
#         y_axis = col2.selectbox("Select Y-axis", num_cols, index=1)

#         # Generate charts with consistent layout and vibrant colors
#         charts = [
#             px.histogram(df, x=x_axis, nbins=30, color_discrete_sequence=["#FF6F61"], title="Histogram"),
#             px.bar(df, x=x_axis, y=y_axis, color=y_axis, color_continuous_scale="Sunset", title="Bar Chart"),
#             px.box(df, y=y_axis, color_discrete_sequence=["#6A5ACD"], title="Box Plot"),
#             px.scatter(df, x=x_axis, y=y_axis, color=y_axis, color_continuous_scale="Plasma", title="Scatter Plot"),
#             px.line(df, x=x_axis, y=y_axis, color_discrete_sequence=["#00BFFF"], title="Line Chart"),
#             px.area(df, x=x_axis, y=y_axis, color_discrete_sequence=["#FFD700"], title="Area Chart"),
#             px.imshow(df[num_cols].corr().round(2), text_auto=True, color_continuous_scale="RdYlBu", title="Heatmap"),
#             px.scatter(df, x=x_axis, y=y_axis, size=y_axis, color=y_axis, color_continuous_scale="Rainbow", title="Bubble Chart")
#         ]

#         grid = [st.columns(2), st.columns(2), st.columns(2), st.columns(2)]
#         idx = 0
#         for row in grid:
#             for col in row:
#                 if idx < len(charts):
#                     charts[idx].update_layout(margin=dict(l=20, r=20, t=40, b=20), height=350)
#                     col.plotly_chart(charts[idx], use_container_width=True)
#                     idx += 1

# # =====================================================
# # COMPARISON TAB
# # =====================================================
# with tab_compare:
#     if summary_df.empty:
#         st.warning("No summary data available.")
#     else:
#         st.markdown("### 🧭 Accuracy Comparison Across Datasets")
#         fig = px.bar(summary_df.reset_index(), x="index", y="accuracy", color="accuracy",
#                      color_continuous_scale="Viridis", title="Accuracy Comparison")
#         fig.update_layout(height=500)
#         st.plotly_chart(fig, use_container_width=True)

# # =====================================================
# # BUSINESS DOMAINS TAB
# # =====================================================
# DOMAIN_KEYWORDS = {
#     "Inventory Management": ["inventory"],
#     "Demand Forecasting": ["demand"],
#     "Logistics Planning": ["logistic", "lead_time"],
#     "Supplier Collaboration": ["supplier", "vendor"],
#     # "Artificial Intelligence (AI)": ["ai"],
#     # "Machine Learning (ML)": ["ml"],
#     "Efficiency": ["efficiency"],
#     "Cost Reduction": ["cost", "profit"],
#     "Lead Time": ["lead_time"],
#     "Risk Management": ["risk"],
#     "Performance Matrix": ["performance"]
# }

# with tab_domains:
#     if not datasets:
#         st.warning("No datasets found for domain comparison.")
#     else:
#         st.markdown("### 🏢 Business Domains Summary")
#         domain_data = []
#         for ds in datasets:
#             df_local = safe_load_csv(
#                 os.path.join(COMBINED_DIR if ds == "combined" else os.path.join(COMPARISON_DIR, ds),
#                              f"{'combined_high_accuracy_predictions' if ds == 'combined' else ds + '_predictions'}.csv"))
#             scores = {}
#             for domain, keys in DOMAIN_KEYWORDS.items():
#                 match = [c for c in df_local.columns if any(k in c.lower() for k in keys)]
#                 scores[domain] = np.nanmean(pd.to_numeric(df_local[match[0]], errors="coerce")) if match else 0
#             scores["Dataset"] = ds
#             domain_data.append(scores)

#         domain_df = pd.DataFrame(domain_data).set_index("Dataset").fillna(0)
#         st.dataframe(domain_df.style.background_gradient(cmap="Spectral").format("{:.4f}"), use_container_width=True)

#         domain_long = domain_df.reset_index().melt(id_vars="Dataset", var_name="Domain", value_name="Score")
#         fig_domain = px.bar(domain_long, x="Domain", y="Score", color="Dataset",
#                             color_discrete_sequence=px.colors.qualitative.Bold,
#                             title="Domain-Wise Performance Comparison")
#         fig_domain.update_layout(xaxis_tickangle=45, height=600)
#         st.plotly_chart(fig_domain, use_container_width=True)

# # =====================================================
# # TEAM TAB
# # =====================================================
# with tab_team:
#     st.markdown("### 👥 Project Team Members")
#     team = [
#         ("Pranay Dhore", "Lead Developer / Data Scientist"),
#         ("Paras Longadge", "Data Analyst / Dashboard Designer"),
#         ("Sanket Tajne", "ML Engineer / Model Architect"),
#         ("Kunal Gomkar", "Logistics & Integration Specialist")
#     ]

#     cols = st.columns(4)
#     for i, (name, role) in enumerate(team):
#         with cols[i]:
#             st.markdown(f"<h4 style='color:#0073e6; text-align:center;'>{name}</h4>", unsafe_allow_html=True)
#             st.markdown(f"<p style='text-align:center; color:white;'><b>Role:</b> {role}</p>", unsafe_allow_html=True)
#             st.markdown("<hr style='margin:10px 0;'>", unsafe_allow_html=True)

# # =====================================================
# # FOOTER
# # =====================================================
# st.markdown("---")
# st.caption(f"📅 Dashboard generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
# st.caption("⚙️ Built by Team Pranay · Paras · Sanket · Kunal — Supply Chain Optimization using AI/ML")

import os, json
from datetime import datetime
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from sklearn.metrics import confusion_matrix, roc_curve, auc

# ========================
# CONFIGURATION
# ========================
NOTEBOOKS_DIR = r"C:\Users\ASUS\OneDrive\Documents\Project\notebooks"
ARTIFACTS_DIR = r"C:\Users\ASUS\OneDrive\Documents\Project\data\artifacts"
COMPARISON_DIR = os.path.join(NOTEBOOKS_DIR, "comparison_results")
COMBINED_DIR = os.path.join(NOTEBOOKS_DIR, "combined_results")
SUMMARY_CSV = os.path.join(COMPARISON_DIR, "platforms_comparison_metrics.csv")

# ========================
# STREAMLIT SETUP
# ========================
st.set_page_config(page_title="Supply Chain Optimization Dashboard", layout="wide", page_icon="📦")

st.markdown("""
<h1 style='text-align:center;color:#0047AB;'>📦 Supply Chain Optimization Dashboard — AI/ML Insights</h1>
<p style='text-align:center;color:gray;'>Interactive, professional, and performance-oriented visualization of supply chain analytics.</p>
""", unsafe_allow_html=True)

# ========================
# LOADERS
# ========================
@st.cache_data(show_spinner=False)
def safe_load_csv(path):
    if not os.path.exists(path): return pd.DataFrame()
    try: df = pd.read_csv(path)
    except Exception: df = pd.read_csv(path, engine="python")
    df = df.loc[:, ~df.columns.duplicated()]
    return df

@st.cache_data(show_spinner=False)
def safe_load_json(path):
    if not os.path.exists(path): return {}
    with open(path, "r", encoding="utf-8") as f: return json.load(f)

def downsample(df, n=5000):
    return df.sample(n, random_state=42) if not df.empty and len(df) > n else df

# ========================
# LOAD DATA
# ========================
summary_df = safe_load_csv(SUMMARY_CSV)
datasets = [d for d in os.listdir(COMPARISON_DIR) if os.path.isdir(os.path.join(COMPARISON_DIR, d))] if os.path.exists(COMPARISON_DIR) else []
if os.path.exists(COMBINED_DIR): datasets.insert(0, "combined")

st.sidebar.header("Select Dataset")
selected = st.sidebar.selectbox("Dataset", ["-- Select --"] + datasets)

if st.sidebar.button("🔄 Refresh Cache"):
    st.cache_data.clear()
    st.experimental_rerun()

df, metrics = pd.DataFrame(), {}
if selected != "-- Select --":
    preds_file = os.path.join(COMBINED_DIR if selected == "combined" else os.path.join(COMPARISON_DIR, selected),
                              f"{'combined_high_accuracy_predictions' if selected == 'combined' else selected + '_predictions'}.csv")
    metrics_file = os.path.join(COMBINED_DIR if selected == "combined" else os.path.join(COMPARISON_DIR, selected),
                                f"{'combined_high_accuracy_metrics' if selected == 'combined' else selected + '_metrics'}.json")
    df, metrics = safe_load_csv(preds_file), safe_load_json(metrics_file)
    df = downsample(df)

# ========================
# KPI CARDS
# ========================
st.markdown(f"### 🔍 {selected.upper() if selected!='-- Select --' else 'NO DATA SELECTED'} — Model KPIs")

if df.empty:
    st.info("Please select a dataset from the sidebar to view details.")
else:
    cols = st.columns(5)
    cols[0].metric("Accuracy", f"{metrics.get('accuracy', 0)*100:.2f}%")
    cols[1].metric("Precision", f"{metrics.get('precision', 0)*100:.2f}%")
    cols[2].metric("Recall", f"{metrics.get('recall', 0)*100:.2f}%")
    cols[3].metric("F1 Score", f"{metrics.get('f1_score', 0)*100:.2f}%")
    cols[4].metric("AUC", f"{metrics.get('roc_auc', 0):.3f}")

# ========================
# MAIN TABS
# ========================
tab_overview, tab_kpi, tab_python, tab_compare, tab_domains, tab_kpi_matrix, tab_team = st.tabs([
    "📊 Overview", "📈 KPI Insights", "🎨 Python Charts", "🧭 Comparison", "🏢 Business Domains", "📊 KPI Matrix", "👥 Team"
])

# =====================================================
# OVERVIEW TAB
# =====================================================
with tab_overview:
    if df.empty:
        st.info("Select a dataset to view Overview.")
    else:
        c1, c2 = st.columns(2)
        if {"efficiency_label", "predicted_efficiency"}.issubset(df.columns):
            cm = pd.crosstab(df["efficiency_label"], df["predicted_efficiency"])
            fig_cm = px.imshow(cm, text_auto=True, color_continuous_scale="Tealrose", title="Confusion Matrix")
            c1.plotly_chart(fig_cm, use_container_width=True)
        if {"efficiency_label", "predicted_probability"}.issubset(df.columns):
            d_roc = df.dropna(subset=["efficiency_label", "predicted_probability"])
            if not d_roc.empty:
                fpr, tpr, _ = roc_curve(d_roc["efficiency_label"], d_roc["predicted_probability"])
                roc_auc = auc(fpr, tpr)
                fig_roc = go.Figure()
                fig_roc.add_trace(go.Scatter(x=fpr, y=tpr, mode="lines", line=dict(width=3, color="#1f77b4"),
                                             name=f"AUC={roc_auc:.3f}"))
                fig_roc.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode="lines", line=dict(dash="dash", color="gray")))
                fig_roc.update_layout(title="ROC Curve", xaxis_title="False Positive Rate", yaxis_title="True Positive Rate")
                c2.plotly_chart(fig_roc, use_container_width=True)

# =====================================================
# KPI INSIGHTS TAB
# =====================================================
with tab_kpi:
    if df.empty:
        st.info("Select a dataset to view KPI insights.")
    else:
        st.markdown("### 🎯 KPI Insights — Clear, Colorful & Easy to Interpret")
        numeric_cols = df.select_dtypes(include=[np.number]).columns.tolist()
        if not numeric_cols:
            st.warning("No numeric columns available for KPI visualization.")
        else:
            kpi_summary = df[numeric_cols].mean().sort_values(ascending=False).reset_index()
            kpi_summary.columns = ["KPI", "Mean Value"]
            fig_bar = px.bar(kpi_summary, x="KPI", y="Mean Value", color="Mean Value",
                             color_continuous_scale="Viridis", text_auto=".2f",
                             title="Average KPI Scores — Business & Technical Clarity")
            fig_bar.update_layout(xaxis_tickangle=45, height=500)
            st.plotly_chart(fig_bar, use_container_width=True)

            st.markdown("### 📊 KPI Variability Across Dataset")
            fig_box = px.box(df, y=numeric_cols, color_discrete_sequence=px.colors.qualitative.Set2)
            fig_box.update_layout(height=600, title="KPI Distribution Range (Performance Spread)")
            st.plotly_chart(fig_box, use_container_width=True)

# =====================================================
# PYTHON CHARTS TAB
# =====================================================
with tab_python:
    if df.empty:
        st.info("Select dataset to generate Python charts.")
    else:
        st.markdown("### 🎨 Python Charts — 8 Dynamic Graphs (User Controlled Axes)")
        num_cols = df.select_dtypes(include=[np.number]).columns.tolist()

        col1, col2 = st.columns(2)
        x_axis = col1.selectbox("Select X-axis", num_cols, index=0)
        y_axis = col2.selectbox("Select Y-axis", num_cols, index=1)

        charts = [
            px.histogram(df, x=x_axis, nbins=30, color_discrete_sequence=["#FF6F61"], title="Histogram"),
            px.bar(df, x=x_axis, y=y_axis, color=y_axis, color_continuous_scale="Sunset", title="Bar Chart"),
            px.box(df, y=y_axis, color_discrete_sequence=["#6A5ACD"], title="Box Plot"),
            px.scatter(df, x=x_axis, y=y_axis, color=y_axis, color_continuous_scale="Plasma", title="Scatter Plot"),
            px.line(df, x=x_axis, y=y_axis, color_discrete_sequence=["#00BFFF"], title="Line Chart"),
            px.area(df, x=x_axis, y=y_axis, color_discrete_sequence=["#FFD700"], title="Area Chart"),
            px.imshow(df[num_cols].corr().round(2), text_auto=True, color_continuous_scale="RdYlBu", title="Heatmap"),
            px.scatter(df, x=x_axis, y=y_axis, size=y_axis, color=y_axis, color_continuous_scale="Rainbow", title="Bubble Chart")
        ]

        grid = [st.columns(2), st.columns(2), st.columns(2), st.columns(2)]
        idx = 0
        for row in grid:
            for col in row:
                if idx < len(charts):
                    charts[idx].update_layout(margin=dict(l=20, r=20, t=40, b=20), height=350)
                    col.plotly_chart(charts[idx], use_container_width=True)
                    idx += 1

# =====================================================
# COMPARISON TAB
# =====================================================
with tab_compare:
    if summary_df.empty:
        st.warning("No summary data available.")
    else:
        st.markdown("### 🧭 Accuracy Comparison Across Datasets")
        fig = px.bar(summary_df.reset_index(), x="index", y="accuracy", color="accuracy",
                     color_continuous_scale="Viridis", title="Accuracy Comparison")
        fig.update_layout(height=500)
        st.plotly_chart(fig, use_container_width=True)

# =====================================================
# BUSINESS DOMAINS TAB
# =====================================================
DOMAIN_KEYWORDS = {
    "Inventory Management": ["inventory"],
    "Demand Forecasting": ["demand"],
    "Logistics Planning": ["logistic", "lead_time"],
    "Supplier Collaboration": ["supplier", "vendor"],
    "Efficiency": ["efficiency"],
    "Cost Reduction": ["cost", "profit"],
    "Lead Time": ["lead_time"],
    "Risk Management": ["risk"],
    "Performance Matrix": ["performance"]
}

with tab_domains:
    if not datasets:
        st.warning("No datasets found for domain comparison.")
    else:
        st.markdown("### 🏢 Business Domains Summary")
        domain_data = []
        for ds in datasets:
            df_local = safe_load_csv(
                os.path.join(COMBINED_DIR if ds == "combined" else os.path.join(COMPARISON_DIR, ds),
                             f"{'combined_high_accuracy_predictions' if ds == 'combined' else ds + '_predictions'}.csv"))
            scores = {}
            for domain, keys in DOMAIN_KEYWORDS.items():
                match = [c for c in df_local.columns if any(k in c.lower() for k in keys)]
                scores[domain] = np.nanmean(pd.to_numeric(df_local[match[0]], errors="coerce")) if match else 0
            scores["Dataset"] = ds
            domain_data.append(scores)

        domain_df = pd.DataFrame(domain_data).set_index("Dataset").fillna(0)
        st.dataframe(domain_df.style.background_gradient(cmap="Spectral").format("{:.4f}"), use_container_width=True)

        domain_long = domain_df.reset_index().melt(id_vars="Dataset", var_name="Domain", value_name="Score")
        fig_domain = px.bar(domain_long, x="Domain", y="Score", color="Dataset",
                            color_discrete_sequence=px.colors.qualitative.Bold,
                            title="Domain-Wise Performance Comparison")
        fig_domain.update_layout(xaxis_tickangle=45, height=600)
        st.plotly_chart(fig_domain, use_container_width=True)

# =====================================================
# NEW KPI MATRIX TAB
# =====================================================
with tab_kpi_matrix:
    st.subheader("📊 Supply Chain KPI Matrix")

    kpi_path = os.path.join(ARTIFACTS_DIR, "supply_chain_kpi_matrix.csv")

    if os.path.exists(kpi_path):
        kpi_df = pd.read_csv(kpi_path)
        st.dataframe(kpi_df, use_container_width=True)

        radar = px.line_polar(kpi_df, r="Value", theta="KPI", line_close=True,
                              title="Performance Matrix", template="plotly_dark")
        radar.update_traces(fill="toself")
        st.plotly_chart(radar, use_container_width=True)

        fig_bar = px.bar(kpi_df, x="KPI", y="Value", color="Value",
                         color_continuous_scale="Blues", title="KPI Comparison")
        st.plotly_chart(fig_bar, use_container_width=True)

    else:
        st.warning("⚠️ KPI file not found. Run KPI generation notebook first.")

# =====================================================
# TEAM TAB
# =====================================================
with tab_team:
    st.markdown("### 👥 Project Team Members")
    team = [
        ("Pranay Dhore", "Lead Developer / Data Scientist"),
        ("Paras Longadge", "Data Analyst / Dashboard Designer"),
        ("Sanket Tajne", "ML Engineer / Model Architect"),
        ("Kunal Gomkar", "Logistics & Integration Specialist")
    ]

    cols = st.columns(4)
    for i, (name, role) in enumerate(team):
        with cols[i]:
            st.markdown(f"<h4 style='color:#0073e6; text-align:center;'>{name}</h4>", unsafe_allow_html=True)
            st.markdown(f"<p style='text-align:center; color:white;'><b>Role:</b> {role}</p>", unsafe_allow_html=True)
            st.markdown("<hr style='margin:10px 0;'>", unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================
st.markdown("---")
st.caption(f"📅 Dashboard generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
st.caption("⚙️ Built by Team Pranay · Paras · Sanket · Kunal — Supply Chain Optimization using AI/ML")
