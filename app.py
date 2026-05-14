
import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(
    page_title="Interactive Straight Line Graph",
    page_icon="📈",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #f0f9ff, #fff7ed);
}
.block-container {
    padding-top: 1.2rem;
    padding-left: 1.5rem;
    padding-right: 1.5rem;
}
.title-box {
    background: linear-gradient(90deg,#0f766e,#2563eb);
    padding: 20px;
    border-radius: 24px;
    color: white;
    text-align: center;
    margin-bottom: 12px;
}
.title-box h1 {
    font-size: 38px;
    margin-bottom: 3px;
}
.title-box p {
    font-size: 17px;
    margin: 0;
}
.equation-box {
    background: linear-gradient(135deg, #fff7ed, #ffffff);
    padding: 22px;
    border-radius: 22px;
    box-shadow: 0px 5px 18px rgba(0,0,0,0.10);
    border-left: 8px solid #f97316;
    text-align: center;
    margin-bottom: 16px;
}
.equation-line {
    font-size: 34px;
    font-weight: 800;
    color: #0f172a;
    white-space: nowrap;
}
.card {
    background: white;
    padding: 18px;
    border-radius: 20px;
    box-shadow: 0px 5px 18px rgba(0,0,0,0.10);
    margin-bottom: 16px;
}
.small-note {
    font-size: 16px;
    color: #475569;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="title-box">
<h1>📈 Interactive Straight Line Graph</h1>
<p>Move the sliders to see the straight line change instantly</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# Sidebar controls
# -------------------------------------------------------
st.sidebar.header("🎛️ Interactive Controls")

m = st.sidebar.slider(
    "Gradient, m",
    min_value=-10.0,
    max_value=10.0,
    value=2.0,
    step=0.1
)

c = st.sidebar.slider(
    "Y-intercept, c",
    min_value=-10.0,
    max_value=10.0,
    value=1.0,
    step=0.1
)

st.sidebar.subheader("📏 Adjustable Axis")

x_axis_min = st.sidebar.number_input("X-axis minimum", value=-10, step=1)
x_axis_max = st.sidebar.number_input("X-axis maximum", value=10, step=1)

y_axis_min = st.sidebar.number_input("Y-axis minimum", value=-10, step=1)
y_axis_max = st.sidebar.number_input("Y-axis maximum", value=10, step=1)

show_grid = st.sidebar.checkbox("Show grid", value=True)
show_points = st.sidebar.checkbox("Show sample points", value=True)
show_intercept = st.sidebar.checkbox("Show y-intercept", value=True)

if x_axis_min >= x_axis_max:
    st.error("X-axis minimum must be smaller than X-axis maximum.")
    st.stop()

if y_axis_min >= y_axis_max:
    st.error("Y-axis minimum must be smaller than Y-axis maximum.")
    st.stop()

# -------------------------------------------------------
# Data
# -------------------------------------------------------
x = np.linspace(x_axis_min, x_axis_max, 500)
y = m * x + c

if c > 0:
    equation = f"y = {m:g}x + {c:g}"
elif c < 0:
    equation = f"y = {m:g}x - {abs(c):g}"
else:
    equation = f"y = {m:g}x"

# -------------------------------------------------------
# Main layout: bigger graph
# -------------------------------------------------------
left, right = st.columns([3.7, 1])

with left:
    fig = go.Figure()

    fig.add_trace(go.Scatter(
        x=x,
        y=y,
        mode="lines",
        line=dict(width=5),
        name=equation
    ))

    if show_points:
        sample_x = np.array([-2, -1, 0, 1, 2])
        sample_y = m * sample_x + c

        fig.add_trace(go.Scatter(
            x=sample_x,
            y=sample_y,
            mode="markers+text",
            text=[f"({px:g}, {py:g})" for px, py in zip(sample_x, sample_y)],
            textposition="top center",
            marker=dict(size=10),
            name="Sample points"
        ))

    if show_intercept:
        fig.add_trace(go.Scatter(
            x=[0],
            y=[c],
            mode="markers+text",
            text=[f"y-intercept = {c:g}"],
            textposition="top right",
            marker=dict(size=16),
            name="Y-intercept"
        ))

    fig.add_hline(y=0, line_width=2)
    fig.add_vline(x=0, line_width=2)

    fig.update_layout(
        height=760,
        title=dict(
            text="Live Straight Line Graph",
            font=dict(size=26),
            x=0.5
        ),
        xaxis=dict(
            title="x-axis",
            range=[x_axis_min, x_axis_max],
            showgrid=show_grid,
            zeroline=False
        ),
        yaxis=dict(
            title="y-axis",
            range=[y_axis_min, y_axis_max],
            showgrid=show_grid,
            zeroline=False
        ),
        margin=dict(l=40, r=30, t=70, b=40),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        )
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displayModeBar": True,
            "scrollZoom": True
        }
    )

with right:
    st.markdown(f"""
    <div class="equation-box">
        <div class="small-note">Current equation</div>
        <div class="equation-line">{equation}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="card">
        <h3>📌 Values</h3>
        <p><b>Gradient, m:</b> {m:g}</p>
        <p><b>Y-intercept, c:</b> {c:g}</p>
        <p><b>X-axis:</b> {x_axis_min} to {x_axis_max}</p>
        <p><b>Y-axis:</b> {y_axis_min} to {y_axis_max}</p>
    </div>
    """, unsafe_allow_html=True)
