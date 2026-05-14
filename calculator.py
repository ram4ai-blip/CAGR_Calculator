# To Run Streamlit use this code
# python -m streamlit run app.py

# pip install all the dependencies prior to using the code

import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="CAGR Calculator",
                   page_icon="📈", layout="centered")
st.title("📈 CAGR Calculator")
st.caption("Compound Annual Growth Rate")
st.divider()

col1, col2, col3 = st.columns(3)
with col1:
    start = st.number_input("Beginning Value (₹)",
                            value=100000, min_value=1, step=1000)
with col2:
    end = st.number_input("Ending Value (₹)",
                          value=250000, min_value=1, step=1000)
with col3:
    years = st.number_input("Number of Years", value=7.0,
                            min_value=0.1, step=0.5)

cagr = (end / start) ** (1 / years) - 1
total_growth = ((end - start) / start) * 100
abs_gain = end - start

st.divider()
m1, m2, m3 = st.columns(3)
m1.metric("CAGR",          f"{cagr * 100:.2f}%")
m2.metric("Total Growth",  f"{total_growth:.1f}%")
m3.metric("Absolute Gain", f"₹{abs_gain:,.0f}")
st.divider()

yr_labels = list(range(int(years) + 1))
yr_values = [round(start * (1 + cagr) ** y) for y in yr_labels]

fig = go.Figure()
fig.add_trace(go.Scatter(
    x=yr_labels, y=yr_values,
    mode="lines+markers", fill="tozeroy",
    line=dict(color="#1D9E75", width=2.5),
    marker=dict(size=6, color="#1D9E75"),
    hovertemplate="Year %{x}<br>₹%{y:,.0f}<extra></extra>"
))
fig.update_layout(
    xaxis_title="Year", yaxis_title="Portfolio Value (₹)",
    margin=dict(t=20, b=20),
    plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
    yaxis=dict(gridcolor="rgba(0,0,0,0.07)")
)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Year-by-year breakdown")
rows = []
for y in range(1, int(years) + 1):
    val = start * (1 + cagr) ** y
    prev = start * (1 + cagr) ** (y - 1)
    rows.append({
        "Year": y,
        "Value (₹)":   f"₹{val:,.0f}",
        "Annual Gain": f"₹{val - prev:,.0f}",
        "Growth %":    f"{((val - prev) / prev * 100):.2f}%"
    })
st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)
