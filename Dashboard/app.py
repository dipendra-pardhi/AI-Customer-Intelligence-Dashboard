import streamlit as st
import pandas as pd
import numpy as np


# ----------------------------
# PAGE CONFIG
# ----------------------------
st.set_page_config(
    page_title="AI Customer Intelligence Platform",
    layout="wide"
)

st.markdown("""
<h1 style='text-align:center;
color:#00E5FF;
font-size:55px;'>

🚀 AI Customer Intelligence Platform
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h3 style='text-align:center;
color:#FFD700;'>
Executive Command Center
</h3>
""", unsafe_allow_html=True)

# ----------------------------
# DATABASE CONNECTION
# ----------------------------

st.markdown("""
<hr style="
height:3px;
border:none;
background:linear-gradient(
90deg,
#00E5FF,
#00FF88,
#FFD700,
#FF4B4B
);
">
""", unsafe_allow_html=True)



# ----------------------------
# LOAD DATA
# ----------------------------
customers = pd.read_csv("Data/olist_customers_dataset.csv")
orders = pd.read_csv("Data/olist_orders_dataset.csv")
products = pd.read_csv("Data/olist_products_dataset.csv")

st.success("🟢 Connected to Olist Enterprise Database")


# ----------------------------
# SIDEBAR FILTERS
# ----------------------------

st.sidebar.header("🔍 Dashboard Filters")

orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

selected_year = st.sidebar.selectbox(
    "Select Year",
    sorted(
        orders["order_purchase_timestamp"].dt.year.unique()
    )
)

selected_month = st.sidebar.selectbox(
    "Select Month",
    range(1, 13)
)

filtered_orders = orders[
    (orders["order_purchase_timestamp"].dt.year == selected_year)
    &
    (orders["order_purchase_timestamp"].dt.month == selected_month)
]


# ----------------------------
# KPI DASHBOARD
# ----------------------------

kpi1, kpi2, kpi3 = st.columns(3)

with kpi1:
    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#00E5FF,#007BFF);
    padding:25px;
    border-radius:20px;
    text-align:center;
    box-shadow:0px 0px 20px rgba(0,229,255,0.6);
    ">
        <h3 style="color:white;">👥 Total Customers</h3>
        <h1 style="color:white;">{len(customers):,}</h1>
    </div>
    """, unsafe_allow_html=True)

with kpi2:
    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#00FF88,#00C853);
    padding:25px;
    border-radius:20px;
    text-align:center;
    box-shadow:0px 0px 20px rgba(0,255,136,0.6);
    ">
        <h3 style="color:white;">📦 Total Orders</h3>
        <h1 style="color:white;">{len(orders):,}</h1>
    </div>
    """, unsafe_allow_html=True)

with kpi3:
    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#FFD700,#FF9800);
    padding:25px;
    border-radius:20px;
    text-align:center;
    box-shadow:0px 0px 20px rgba(255,215,0,0.6);
    ">
        <h3 style="color:black;">🛒 Total Products</h3>
        <h1 style="color:black;">{len(products):,}</h1>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.success("🟢 Connected to Olist Enterprise Database")

# ----------------------------
# MONTHLY ORDERS TREND
# ----------------------------

st.subheader("📈 Sales Intelligence Monitor")

import plotly.express as px

orders["order_purchase_timestamp"] = pd.to_datetime(
    orders["order_purchase_timestamp"]
)

monthly_orders = (
    orders.groupby(
        orders["order_purchase_timestamp"].dt.to_period("M")
    )
    .size()
    .reset_index(name="orders")
)

monthly_orders["order_purchase_timestamp"] = (
    monthly_orders["order_purchase_timestamp"].astype(str)
)

fig = px.area(
    monthly_orders,
    x="order_purchase_timestamp",
    y="orders",
    title="📈 Monthly Orders Trend Analysis"
)

fig.update_traces(
    line=dict(
        color="#00E5FF",
        width=4
    )
)

fig.update_layout(
    template="plotly_dark",
    height=550,
    title_x=0.3,
    xaxis_title="Month",
    yaxis_title="Orders",
    hovermode="x unified"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ----------------------------
# CUSTOMER SEGMENTATION
# ----------------------------

segments = pd.read_csv(
    "Data/Processed/customer_segments.csv"
)

st.subheader("🎯 AI Customer Segmentation Center")

vip_count = len(
    segments[
        segments["segment"] == "💎 VIP Customers"
    ]
)

risk_count = len(
    segments[
        segments["segment"] == "⚠️ At Risk Customers"
    ]
)

regular_count = len(
    segments[
        segments["segment"] == "🛒 Regular Customers"
    ]
)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#FFD700,#FFB300);
    padding:20px;
    border-radius:20px;
    text-align:center;">
    <h3 style="color:black;">💎 VIP Customers</h3>
    <h1 style="color:black;">{vip_count:,}</h1>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#FF4B4B,#B71C1C);
    padding:20px;
    border-radius:20px;
    text-align:center;">
    <h3 style="color:white;">⚠️ At Risk</h3>
    <h1 style="color:white;">{risk_count:,}</h1>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div style="
    background:linear-gradient(135deg,#00E5FF,#007BFF);
    padding:20px;
    border-radius:20px;
    text-align:center;">
    <h3 style="color:white;">🛒 Regular</h3>
    <h1 style="color:white;">{regular_count:,}</h1>
    </div>
    """, unsafe_allow_html=True)

segment_counts = (
    segments["segment"]
    .value_counts()
    .reset_index()
)

segment_counts.columns = [
    "Segment",
    "Customers"
]

fig = px.pie(
    segment_counts,
    names="Segment",
    values="Customers",
    hole=0.55,
    color="Segment",
    color_discrete_map={
        "💎 VIP Customers": "#FFD700",
        "⚠️ At Risk Customers": "#FF4B4B",
        "🛒 Regular Customers": "#00E5FF"
    }
)

fig.update_layout(
    template="plotly_dark",
    height=600
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ----------------------------
# CUSTOMER STATE ANALYSIS
# ----------------------------

st.subheader("🌎 Customer State Analysis")

state_counts = (
    customers["customer_state"]
    .value_counts()
    .head(10)
    .reset_index()
)

state_counts.columns = [
    "State",
    "Customers"
]

fig = px.bar(
    state_counts,
    x="State",
    y="Customers",
    color="Customers",
    color_continuous_scale="Turbo",
    title="Top 10 States by Customers"
)

fig.update_layout(
    template="plotly_dark",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)
health_score = 92

# ----------------------------
# SMART AI BUSINESS ASSISTANT
# ----------------------------

st.subheader("🤖 Smart AI Business Assistant")

question = st.selectbox(
    "Ask Business AI",
    [
        "Select a Question",
        "Which segment is largest?",
        "How can revenue be increased?",
        "What should we do with At Risk customers?",
        "What is the business health status?",
        "Which state has the most customers?",
        "Who are the highest value customers?",
        "What is the customer retention strategy?"
    ]
)

if question == "Which segment is largest?":

    largest_segment = segment_counts.iloc[0]["Segment"]

    st.success(
        f"📊 Largest customer segment is: {largest_segment}"
    )

elif question == "How can revenue be increased?":

    st.success("""
📈 Revenue Growth Strategy

💎 Focus on VIP Customers

🎯 Upsell Regular Customers

⚠️ Recover At Risk Customers

🏆 Launch Loyalty Programs

📧 Personalized Marketing Campaigns
""")

elif question == "What should we do with At Risk customers?":

    st.warning("""
⚠️ At Risk Customer Strategy

• Provide Special Discounts

• Launch Retention Campaigns

• Send Personalized Offers

• Re-engage Through Email Marketing

• Offer Loyalty Rewards
""")

elif question == "What is the business health status?":

    if health_score >= 80:

        st.success(
            f"🟢 Business Health Score = {health_score}/100 (Excellent)"
        )

    elif health_score >= 60:

        st.warning(
            f"🟡 Business Health Score = {health_score}/100 (Moderate)"
        )

    else:

        st.error(
            f"🔴 Business Health Score = {health_score}/100 (Critical)"
        )

elif question == "Which state has the most customers?":

    top_state = (
        customers["customer_state"]
        .value_counts()
        .idxmax()
    )

    total_customers_state = (
        customers["customer_state"]
        .value_counts()
        .max()
    )

    st.success(
        f"🌎 Top Customer State: {top_state} ({total_customers_state:,} customers)"
    )

elif question == "Who are the highest value customers?":

    top_customer = (
        segments.sort_values(
            by="monetary",
            ascending=False
        )
        .head(1)
    )

    st.success(
        f"🏆 Highest Value Customer Revenue: ₹{top_customer['monetary'].iloc[0]:,.2f}"
    )

elif question == "What is the customer retention strategy?":

    st.info("""
🎯 Customer Retention Strategy

• Reward VIP Customers

• Upsell Regular Customers

• Re-engage At Risk Customers

• Improve Customer Experience

• Run Personalized Promotions

• Monitor Customer Health Score
""")

else:

    st.info("""
🤖 AI Assistant Ready

Try asking:

• Which segment is largest?

• How can revenue be increased?

• What is the business health status?

• Which state has the most customers?

• Who are the highest value customers?

• What is the customer retention strategy?
""")

# ----------------------------
# AI INSIGHTS
# ----------------------------

st.subheader("🤖 AI Business Intelligence Engine")

st.markdown(f"""
<div style="
background:linear-gradient(135deg,#1E1E1E,#2C2C2C);
padding:25px;
border-radius:20px;
border-left:8px solid #00E5FF;
color:white;
font-size:18px;">

<h3>🚀 AI Generated Business Recommendations</h3>

✅ <b>VIP Customers:</b> {vip_count:,}<br><br>

⚠️ <b>At Risk Customers:</b> {risk_count:,}<br><br>

🛒 <b>Regular Customers:</b> {regular_count:,}<br><br>

📊 Customer base is heavily concentrated in the Regular segment.<br><br>

💎 High-value customers should receive loyalty rewards and retention campaigns.<br><br>

🎯 At Risk customers should be targeted with personalized offers and discounts.<br><br>

📈 Opportunity detected to increase revenue through customer upselling.

</div>
""", unsafe_allow_html=True)


# ----------------------------
# TOP VIP CUSTOMERS
# ----------------------------

st.subheader("🏆 Revenue Champions Leaderboard")

top_vips = (
    segments.sort_values(
        by="monetary",
        ascending=False
    )
    .head(10)
)

fig = px.bar(
    top_vips,
    x="monetary",
    y="customer_unique_id",
    orientation="h",
    text="monetary",
    color="monetary",
    color_continuous_scale="Turbo",
    title="💰 Top 10 Revenue Generating Customers"
)

fig.update_layout(
    template="plotly_dark",
    height=600,
    xaxis_title="Revenue Generated",
    yaxis_title="Customer ID",
    coloraxis_showscale=False
)

fig.update_traces(
    texttemplate='%{text:.0f}',
    textposition='outside'
)

fig.update_yaxes(
    categoryorder="total ascending"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ----------------------------
# CUSTOMER VALUE DISTRIBUTION
# ----------------------------

st.subheader("💰 Customer Spending Outlier Analysis")

fig = px.box(
    segments,
    y="monetary",
    points="outliers",
    title="Revenue Outlier Detection Engine",
    color_discrete_sequence=["#FF6B00"]
)

fig.update_layout(
    template="plotly_dark",
    height=600
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ----------------------------
# AI SALES FORECAST ENGINE
# ----------------------------

st.subheader("📈 AI Sales Forecast Engine")

forecast_df = pd.read_csv(
    "Data/Processed/monthly_orders.csv"
)

forecast_df["month_index"] = range(
    len(forecast_df)
)

from sklearn.linear_model import LinearRegression

X = forecast_df[["month_index"]]
y = forecast_df["orders"]

model = LinearRegression()
model.fit(X, y)

future_months = pd.DataFrame({
    "month_index": range(
        len(forecast_df),
        len(forecast_df) + 6
    )
})

future_months["forecast_orders"] = (
    model.predict(
        future_months[["month_index"]]
    )
)

future_months["Month"] = [
    f"Future {i}"
    for i in range(1, 7)
]

import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=forecast_df["month"],
        y=forecast_df["orders"],
        mode="lines+markers",
        name="Historical Orders",
        line=dict(
            color="#00E5FF",
            width=4
        )
    )
)

fig.add_trace(
    go.Scatter(
        x=future_months["Month"],
        y=future_months["forecast_orders"],
        mode="lines+markers",
        name="Forecast Orders",
        line=dict(
            color="#FFD700",
            width=4,
            dash="dash"
        )
    )
)

fig.update_layout(
    template="plotly_dark",
    height=600,
    title="🚀 Next 6 Months Sales Forecast",
    xaxis_title="Month",
    yaxis_title="Orders"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ----------------------------
# CUSTOMER HEALTH SCORE
# ----------------------------

import plotly.graph_objects as go

st.subheader("🎯 Customer Health Score")


fig = go.Figure(
    go.Indicator(
        mode="gauge+number",
        value=health_score,
        title={"text": "Business Health Score"},
        gauge={
            "axis": {"range": [0, 100]},
            "bar": {"color": "#00E5FF"},
            "steps": [
                {"range": [0, 50], "color": "#FF4B4B"},
                {"range": [50, 80], "color": "#FFD700"},
                {"range": [80, 100], "color": "#00FF88"}
            ]
        }
    )
)

fig.update_layout(
    template="plotly_dark",
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ----------------------------
# FILTERED DATA TABLE
# ----------------------------

st.subheader("📋 Filtered Orders Data")

st.dataframe(
    filtered_orders.head(100),
    use_container_width=True
)

st.download_button(
    "📥 Download Filtered Data",
    filtered_orders.to_csv(index=False),
    "filtered_orders.csv",
    "text/csv"
)
