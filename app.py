
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

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
.title-box {
    background: linear-gradient(90deg,#0f766e,#2563eb);
    padding: 24px;
    border-radius: 24px;
    color: white;
    text-align: center;
    margin-bottom: 18px;
}
.card {
    background: white;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 5px 18px rgba(0,0,0,0.10);
    margin-bottom: 16px;
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
.small-note {
    font-size: 16px;
    color: #475569;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="title-box">
<h1>📈 Interactive Straight Line Graph</h1>
<p>Move the controls and watch the graph change instantly</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# Sidebar Controls
# Streamlit reruns automatically whenever these values change.
# This makes the graph move simultaneously with the slider/dial.
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
# Graph data
# -------------------------------------------------------
x = np.linspace(x_axis_min, x_axis_max, 500)
y = m * x + c

# Equation formatting
if c > 0:
    equation = f"y = {m:g}x + {c:g}"
elif c < 0:
    equation = f"y = {m:g}x - {abs(c):g}"
else:
    equation = f"y = {m:g}x"

# -------------------------------------------------------
# Layout
# -------------------------------------------------------
left, right = st.columns([2.25, 1])

with left:
    fig, ax = plt.subplots(figsize=(10, 7))

    ax.plot(x, y, linewidth=4, label=equation)

    ax.axhline(0, linewidth=1.4)
    ax.axvline(0, linewidth=1.4)

    if show_grid:
        ax.grid(True, linestyle="--", alpha=0.45)

    if show_intercept:
        ax.scatter([0], [c], s=160, zorder=5)
        ax.annotate(
            f"y-intercept: {c:g}",
            xy=(0, c),
            xytext=(1, c + 1),
            arrowprops=dict(arrowstyle="->", lw=2),
            fontsize=11,
            bbox=dict(boxstyle="round,pad=0.35", fc="white", ec="gray", alpha=0.9)
        )

    if show_points:
        sample_x = np.array([-2, -1, 0, 1, 2])
        sample_y = m * sample_x + c
        ax.scatter(sample_x, sample_y, s=75, zorder=4)

        for px, py in zip(sample_x, sample_y):
            if y_axis_min <= py <= y_axis_max and x_axis_min <= px <= x_axis_max:
                ax.annotate(
                    f"({px:g}, {py:g})",
                    (px, py),
                    textcoords="offset points",
                    xytext=(8, 8),
                    fontsize=10
                )

    ax.set_xlim(x_axis_min, x_axis_max)
    ax.set_ylim(y_axis_min, y_axis_max)

    ax.set_title("Live Straight Line Graph", fontsize=20, fontweight="bold")
    ax.set_xlabel("x-axis", fontsize=13)
    ax.set_ylabel("y-axis", fontsize=13)
    ax.legend(fontsize=12)

    st.pyplot(fig, clear_figure=True)

with right:
    st.markdown(f"""
    <div class="equation-box">
        <div class="small-note">Current straight line equation</div>
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

    if m > 0:
        direction = "The line rises from left to right."
    elif m < 0:
        direction = "The line falls from left to right."
    else:
        direction = "The line is horizontal."

    st.markdown(f"""
    <div class="card">
        <h3>🧠 What changed?</h3>
        <p>{direction}</p>
        <p>The bigger the size of <b>m</b>, the steeper the line becomes.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>🎯 Student Task</h2>
<p>Adjust the gradient and y-intercept to create:</p>
<ol>
<li>A line that rises and crosses the y-axis at 3.</li>
<li>A line that falls and crosses the y-axis at -2.</li>
<li>A horizontal line that crosses the y-axis at 5.</li>
</ol>
</div>
""", unsafe_allow_html=True)
