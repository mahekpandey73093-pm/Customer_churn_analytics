import streamlit as st
import pandas as pd
import plotly.express as px
import joblib
import os
# =====================================
# PAGE CONFIG
# =====================================

st.set_page_config(
    page_title="AI Customer Churn Dashboard",
    page_icon="🏦",
    layout="wide"
)

# =====================================
# CUSTOM CSS
# =====================================

st.markdown("""
<style>

/* Main App */
.stApp {
    background-color: #f4f7fb;
}

/* KPI Metric Cards */
div[data-testid="metric-container"] {
    background: linear-gradient(135deg, #4f46e5, #7c3aed);
    padding: 20px;
    border-radius: 18px;
    border: none;
    box-shadow: 0 6px 18px rgba(0,0,0,0.15);
    transition: all 0.3s ease-in-out;
}

div[data-testid="metric-container"]:hover {
    transform: translateY(-5px);
    box-shadow: 0 10px 24px rgba(0,0,0,0.25);
}

/* Metric Value */
div[data-testid="metric-container"] label + div {
    color: #ffffff !important;
    font-size: 30px !important;
    font-weight: 700 !important;
}

/* Metric Label */
div[data-testid="metric-container"] label {
    color: #e5e7eb !important;
    font-size: 15px !important;
    font-weight: 600 !important;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: #ffffff;
    border-right: 1px solid #e5e7eb;
}

/* Buttons */
.stButton > button {
    width: 100%;
    border-radius: 10px;
    border: none;
    font-weight: bold;
    padding: 10px;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.02);
}

/* DataFrames */
div[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 3px 10px rgba(0,0,0,0.1);
}

/* Plotly Charts */
.js-plotly-plot {
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    padding: 15px;
    background: white;
}

/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    gap: 8px;
}

.stTabs [data-baseweb="tab"] {
    background: #f3f4f6;
    border-radius: 10px;
    padding: 8px 16px;
    font-weight: 600;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(90deg, #ec4899, #6366f1);
    color: white;
}

/* Selectbox */
div[data-baseweb="select"] > div {
    border-radius: 10px;
}

/* Slider */
.stSlider {
    padding-top: 10px;
}

/* Markdown Containers */
div.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Scrollbar */
::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-thumb {
    background: #a5b4fc;
    border-radius: 8px;
}

::-webkit-scrollbar-thumb:hover {
    background: #6366f1;
}

</style>
""", unsafe_allow_html=True)
# =====================================
# LOAD DATA
# =====================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(
    BASE_DIR,
    "..",
    "Dataset",
    "European_Bank.csv"
)

df = pd.read_csv(DATA_PATH)

# =====================================
# LOAD MODEL
# =====================================

try:
    MODEL_PATH = os.path.join(
        BASE_DIR,
        "churn_model.pkl"
    )

    model = joblib.load(MODEL_PATH)
    model_loaded = True

except Exception as e:
    st.error(f"Model Error: {e}")
    model_loaded = False

# =====================================
# HEADER
# =====================================

st.markdown("""
<div style="
    background: linear-gradient(90deg,#ec4899,#8b5cf6,#3b82f6);
    padding:15px;
    border-radius:16px;
    text-align:center;
    color:white;
    box-shadow:0 4px 12px rgba(0,0,0,0.1);
">
    <h1>🏦 AI-Powered Customer Churn Intelligence Platform</h1>
    <h4>Customer Segmentation • Churn Prediction • Business Intelligence</h4>
</div>
""", unsafe_allow_html=True)

# =====================================
# SIDEBAR
# =====================================

st.sidebar.title("🔍 Filters")

geo = st.sidebar.selectbox(
    "Geography",
    ["All"] + list(df["Geography"].unique())
)

gender = st.sidebar.selectbox(
    "Gender",
    ["All"] + list(df["Gender"].unique())
)

st.sidebar.success("🚀 Internship Project")
st.sidebar.info("AI Banking Analytics Dashboard")

# =====================================
# FILTER DATA
# =====================================

filtered_df = df.copy()

if geo != "All":
    filtered_df = filtered_df[
        filtered_df["Geography"] == geo
    ]

if gender != "All":
    filtered_df = filtered_df[
        filtered_df["Gender"] == gender
    ]

# =====================================
# KPI SECTION
# =====================================
# =========================
# KPI CALCULATIONS
# =========================

total_customers = len(filtered_df)

churn_rate = round(
    filtered_df["Exited"].mean() * 100,
    2
)

avg_balance = round(
    filtered_df["Balance"].mean(),
    0
)

high_value = len(
    filtered_df[
        filtered_df["Balance"] > 100000
    ]
)

revenue_risk = filtered_df[
    filtered_df["Exited"] == 1
]["Balance"].sum()
st.markdown("## 📊 Executive Dashboard")

col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    st.metric("👥 Customers", f"{total_customers:,}")

with col2:
    st.metric("📉 Churn Rate", f"{churn_rate}%")

with col3:
    st.metric("💰 Avg Balance", f"${avg_balance:,.0f}")

with col4:
    st.metric("💎 High Value", f"{high_value:,}")

with col5:
    st.metric("⚠️ Revenue Risk", f"${revenue_risk:,.0f}")
# =====================================
# TABS
# =====================================

tab1, tab2, tab3 = st.tabs([
    "📊 Dashboard",
    "📈 Analytics",
    "🤖 Prediction"
])

# =====================================
# TAB 1
# =====================================

with tab1:

    c1, c2 = st.columns(2)

    with c1:

        fig1 = px.pie(
            filtered_df,
            names="Exited",
            title="Customer Churn Distribution",
            color="Exited",
            color_discrete_sequence=[
                "#ff1493",
                "#00e5ff"
            ]
        )

        fig1.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(
            fig1,
            use_container_width=True
        )

    with c2:

        fig2 = px.histogram(
            filtered_df,
            x="Age",
            color="Exited",
            title="Age vs Churn",
            barmode="overlay"
        )

        fig2.update_layout(
            template="plotly_dark",
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)"
        )

        st.plotly_chart(
            fig2,
            use_container_width=True
        )

    geo_churn = (
        filtered_df.groupby("Geography")["Exited"]
        .mean()
        .reset_index()
    )

    fig3 = px.bar(
        geo_churn,
        x="Geography",
        y="Exited",
        color="Geography",
        title="Geography Wise Churn Rate"
    )

    fig3.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

# =====================================
# TAB 2
# =====================================

with tab2:

    fig4 = px.box(
        filtered_df,
        x="Exited",
        y="Balance",
        color="Exited",
        title="Balance vs Churn"
    )

    fig4.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

    fig5 = px.scatter(
        filtered_df,
        x="Age",
        y="Balance",
        color="Exited",
        title="High Value Customer Analysis"
    )

    fig5.update_layout(
        template="plotly_dark",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)"
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

# =====================================
# TAB 3
# =====================================

# =====================================
# TAB 3 - AI PREDICTION
# =====================================

# =====================================
# TAB 3 - AI PREDICTION
# =====================================

with tab3:

    st.subheader("🤖 AI Customer Churn Predictor")

    if model_loaded:

        col1, col2 = st.columns(2)

        with col1:

            credit_score = st.slider(
                "Credit Score",
                300, 900, 650
            )

            age = st.slider(
                "Age",
                18, 90, 35
            )

            tenure = st.slider(
                "Tenure",
                0, 10, 5
            )

            balance = st.number_input(
                "Balance",
                min_value=0.0,
                value=50000.0
            )

        with col2:

            products = st.slider(
                "Number of Products",
                1, 4, 2
            )

            has_card = st.selectbox(
                "Has Credit Card",
                [0, 1]
            )

            active_member = st.selectbox(
                "Is Active Member",
                [0, 1]
            )

            estimated_salary = st.number_input(
                "Estimated Salary",
                min_value=0.0,
                value=50000.0
            )

        if st.button("🚀 Predict Churn"):

            try:

                input_data = pd.DataFrame([[
                    credit_score,
                    age,
                    tenure,
                    balance,
                    products,
                    has_card,
                    active_member,
                    estimated_salary
                ]], columns=[
                    "CreditScore",
                    "Age",
                    "Tenure",
                    "Balance",
                    "NumOfProducts",
                    "HasCrCard",
                    "IsActiveMember",
                    "EstimatedSalary"
                ])

                prediction = model.predict(input_data)[0]

                prob = model.predict_proba(input_data)[0][1]

                st.markdown("---")

                colA, colB = st.columns(2)

                with colA:
                    st.metric(
                        "📊 Churn Probability",
                        f"{prob*100:.2f}%"
                    )

                with colB:
                    st.metric(
                        "🎯 Prediction",
                        "CHURN" if prediction == 1 else "STAY"
                    )

                st.markdown("---")

                if prob >= 0.70:

                    st.error(
                        "🔴 HIGH RISK CUSTOMER"
                    )

                elif prob >= 0.40:

                    st.warning(
                        "🟠 MEDIUM RISK CUSTOMER"
                    )

                else:

                    st.success(
                        "🟢 LOW RISK CUSTOMER"
                    )

                if prediction == 1:

                    st.error(
                        "⚠️ Customer is likely to CHURN"
                    )

                else:

                    st.success(
                        "✅ Customer is likely to STAY"
                    )

                result_df = pd.DataFrame({
                    "Credit Score":[credit_score],
                    "Age":[age],
                    "Balance":[balance],
                    "Prediction":[
                        "CHURN"
                        if prediction == 1
                        else "STAY"
                    ],
                    "Probability (%)":[
                        round(prob*100,2)
                    ]
                })

                st.download_button(
                    "📥 Download Prediction Report",
                    result_df.to_csv(index=False),
                    file_name="prediction_report.csv",
                    mime="text/csv"
                )

            except Exception as e:

                st.error(
                    f"Prediction Error: {e}"
                )

    else:

        st.warning(
            "⚠️ churn_model.pkl not found"
        )
# =====================================
# INSIGHTS
# =====================================

st.markdown("---")

st.markdown("""
## 🎯 Strategic Recommendations

✅ Germany shows higher churn exposure.

✅ Inactive members have greater churn risk.

✅ Senior customers exhibit elevated churn probability.

✅ High-value customers need retention campaigns.

✅ Personalized offers can improve loyalty.

✅ AI monitoring supports proactive retention.
""")

st.success("""
📌 Executive Summary

• Overall churn rate analysis completed.

• Geography significantly impacts churn.

• Customer retention should focus on inactive users.

• High balance customers require special attention.
""")

# =====================================
# FOOTER
# =====================================
st.markdown("""
## 🚀 Project Highlights

✔ Customer Churn Prediction using Machine Learning

✔ Interactive Business Intelligence Dashboard

✔ Customer Segmentation Analysis

✔ Revenue Risk Identification

✔ Streamlit Deployment Ready

✔ Real-Time Prediction Engine
""")
st.markdown("""
---
### 👩‍💻 Developed By Mahek Pandey

BCA with AI | V.T. Poddar College

Skills Used:
Python • Pandas • Plotly • Machine Learning • Streamlit

Project:
AI-Powered Customer Churn Intelligence Platform
""")
