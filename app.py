"""
Crypto Volatility Visualizer – Mathematics for AI-II
A Streamlit web application for visualizing cryptocurrency price volatility.
Deployment-ready for Streamlit Cloud via GitHub.
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px

# ─── Page Config ───
st.set_page_config(
    page_title="Crypto Volatility Visualizer",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── Custom CSS (Dark Fintech Theme) ───
st.markdown("""
<style>
    .stApp {
        background-color: #0f172a;
        color: #e2e8f0;
    }
    .stSidebar > div {
        background-color: #1e293b;
    }
    .metric-card {
        background: linear-gradient(135deg, #1e293b, #0f172a);
        border: 1px solid #334155;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 0 15px rgba(59, 130, 246, 0.1);
    }
    .metric-value {
        font-size: 28px;
        font-weight: 700;
        color: #60a5fa;
        font-family: 'JetBrains Mono', monospace;
    }
    .metric-label {
        font-size: 12px;
        color: #94a3b8;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .gradient-header {
        background: linear-gradient(135deg, #3b82f6, #8b5cf6, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 36px;
        font-weight: 800;
    }
    h1, h2, h3 { color: #e2e8f0 !important; }
</style>
""", unsafe_allow_html=True)

# ─── Plotly Theme ───
PLOTLY_LAYOUT = dict(
    paper_bgcolor="#0f172a",
    plot_bgcolor="#0f172a",
    font=dict(color="#94a3b8", size=11),
    xaxis=dict(gridcolor="#1e293b", linecolor="#334155"),
    yaxis=dict(gridcolor="#1e293b", linecolor="#334155"),
    margin=dict(l=40, r=20, t=40, b=40),
    hovermode="x unified",
)

# ─── Helper Functions ───
def rolling_std(series, window=7):
    """Calculate rolling standard deviation."""
    return series.rolling(window=window, min_periods=1).std()

def generate_synthetic(amplitude, frequency, drift, n=200):
    """Generate synthetic market data using sine + drift + noise."""
    t = np.arange(n)
    noise = np.random.normal(0, amplitude * 0.3, n)
    price = 100 + amplitude * np.sin(frequency * t * 0.1) + drift * t * 0.1 + noise
    return pd.DataFrame({"t": t, "price": np.maximum(price, 0)})


# ─── Sidebar ───
st.sidebar.markdown('<p class="gradient-header" style="font-size:20px;">📈 Controls</p>', unsafe_allow_html=True)

# File uploader
uploaded_file = st.sidebar.file_uploader("Upload CSV", type=["csv"])

# Time range
time_range = st.sidebar.selectbox("Time Range", ["All Data", "7 Days", "30 Days", "90 Days"])

# Show volatile zones toggle
show_volatile = st.sidebar.toggle("Show Stable vs Volatile Zones", value=False)

# Simulation controls
st.sidebar.markdown("---")
show_sim = st.sidebar.toggle("Simulate Synthetic Market", value=False)

if show_sim:
    amplitude = st.sidebar.slider("Amplitude", 0, 100, 50)
    frequency = st.sidebar.slider("Frequency", 0.1, 5.0, 1.0, step=0.1)
    drift = st.sidebar.slider("Drift", -5.0, 5.0, 0.0, step=0.1)


# ─── Main Panel ───
st.markdown('<p class="gradient-header">Crypto Volatility Visualizer</p>', unsafe_allow_html=True)
st.markdown("*Interactive cryptocurrency analysis • Mathematics for AI-II*")

if uploaded_file is not None:
    # ── Stage 4: Data Preparation ──
    df = pd.read_csv(uploaded_file)
    
    # Normalize column names
    df.columns = [c.strip().lower() for c in df.columns]
    col_map = {}
    for c in df.columns:
        if "timestamp" in c or "date" in c or "time" in c:
            col_map[c] = "timestamp"
        elif c == "open":
            col_map[c] = "open"
        elif c == "high":
            col_map[c] = "high"
        elif c == "low":
            col_map[c] = "low"
        elif c == "close":
            col_map[c] = "close"
        elif "volume" in c or "vol" in c:
            col_map[c] = "volume"
    df.rename(columns=col_map, inplace=True)
    
    # Convert timestamp
    df["timestamp"] = pd.to_datetime(df["timestamp"])
    df.sort_values("timestamp", inplace=True)
    
    # Handle missing values
    df.dropna(subset=["close"], inplace=True)
    df.fillna(method="ffill", inplace=True)
    
    # Filter by time range
    if time_range != "All Data":
        days = int(time_range.split()[0])
        cutoff = df["timestamp"].max() - pd.Timedelta(days=days)
        df = df[df["timestamp"] >= cutoff]
    
    st.markdown(f"**Dataset shape:** `{df.shape[0]} rows × {df.shape[1]} columns`")
    
    # ── KPI Cards ──
    latest_price = df["close"].iloc[-1]
    vol_index = rolling_std(df["close"]).iloc[-1]
    avg_drift = (df["close"].iloc[-1] - df["close"].iloc[0]) / len(df)
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Current Price</div>
            <div class="metric-value">${latest_price:,.2f}</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Volatility Index</div>
            <div class="metric-value">{vol_index:.2f}</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        sign = "+" if avg_drift >= 0 else ""
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">Average Drift</div>
            <div class="metric-value">{sign}{avg_drift:.4f}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("")
    
    # ── Stage 5: Visualization ──
    col_left, col_right = st.columns(2)
    
    with col_left:
        # Close Price Chart
        fig1 = go.Figure()
        fig1.add_trace(go.Scatter(
            x=df["timestamp"], y=df["close"],
            mode="lines", name="Close",
            line=dict(color="#3b82f6", width=2),
            fill="tozeroy", fillcolor="rgba(59,130,246,0.1)"
        ))
        fig1.update_layout(title="Close Price Over Time", **PLOTLY_LAYOUT)
        st.plotly_chart(fig1, use_container_width=True)
    
    with col_right:
        # High vs Low
        fig2 = go.Figure()
        fig2.add_trace(go.Scatter(x=df["timestamp"], y=df["high"], mode="lines", name="High", line=dict(color="#22c55e", width=2)))
        fig2.add_trace(go.Scatter(x=df["timestamp"], y=df["low"], mode="lines", name="Low", line=dict(color="#ef4444", width=2)))
        fig2.update_layout(title="High vs Low Comparison", **PLOTLY_LAYOUT)
        st.plotly_chart(fig2, use_container_width=True)
    
    col_left2, col_right2 = st.columns(2)
    
    with col_left2:
        # Volume Bar Chart
        fig3 = go.Figure()
        fig3.add_trace(go.Bar(x=df["timestamp"], y=df["volume"], name="Volume", marker_color="#8b5cf6", opacity=0.8))
        fig3.update_layout(title="Trading Volume", **PLOTLY_LAYOUT)
        st.plotly_chart(fig3, use_container_width=True)
    
    with col_right2:
        # Volatility Chart
        df["volatility"] = rolling_std(df["close"])
        fig4 = go.Figure()
        fig4.add_trace(go.Scatter(
            x=df["timestamp"], y=df["volatility"],
            mode="lines", name="Volatility",
            line=dict(color="#06b6d4", width=2),
            fill="tozeroy", fillcolor="rgba(6,182,212,0.1)"
        ))
        if show_volatile:
            avg_vol = df["volatility"].mean()
            fig4.add_hline(y=avg_vol * 1.2, line_dash="dash", line_color="#ef4444", annotation_text="Volatile Threshold")
        fig4.update_layout(title="Volatility Index", **PLOTLY_LAYOUT)
        st.plotly_chart(fig4, use_container_width=True)
    
    # Data Preview
    with st.expander("📋 Dataset Preview"):
        st.dataframe(df.head(20), use_container_width=True)

else:
    st.info("👆 Upload a CSV file from the sidebar to get started. Expected columns: Timestamp, Open, High, Low, Close, Volume")

# ── Simulation ──
if show_sim:
    st.markdown("---")
    st.markdown("### 🧮 Synthetic Market Simulation")
    st.markdown(f"`price = {amplitude} × sin({frequency:.1f} × t) + {drift:.1f} × t + noise`")
    
    sim_df = generate_synthetic(amplitude, frequency, drift)
    fig_sim = go.Figure()
    fig_sim.add_trace(go.Scatter(x=sim_df["t"], y=sim_df["price"], mode="lines", name="Synthetic Price", line=dict(color="#8b5cf6", width=2)))
    fig_sim.update_layout(title="Synthetic Market Data", xaxis_title="Time", yaxis_title="Price", **PLOTLY_LAYOUT)
    st.plotly_chart(fig_sim, use_container_width=True)
