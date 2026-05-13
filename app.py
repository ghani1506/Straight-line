
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Interactive Straight Line Graph", page_icon="📈", layout="wide")

st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #f0f9ff, #fff7ed);
}
.title-box {
    background: linear-gradient(90deg,#0f766e,#2563eb);
    padding: 25px;
    border-radius: 25px;
    color: white;
    text-align: center;
}
.card {
    background: white;
    padding: 18px;
    border-radius: 18px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="title-box">
<h1>📈 Interactive Straight Line Graph</h1>
<p>Adjust gradient, y-intercept and axis values interactively</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar Controls
# -------------------------------
st.sidebar.header("🎛️ Controls")

m = st.sidebar.slider("Gradient (m)", -10.0, 10.0, 2.0, 0.5)
c = st.sidebar.slider("Y-intercept (c)", -10.0, 10.0, 1.0, 0.5)

st.sidebar.subheader("📏 Adjustable Axis")

x_axis_min = st.sidebar.number_input("X-axis minimum", value=-10)
x_axis_max = st.sidebar.number_input("X-axis maximum", value=10)

y_axis_min = st.sidebar.number_input("Y-axis minimum", value=-10)
y_axis_max = st.sidebar.number_input("Y-axis maximum", value=10)

grid_toggle = st.sidebar.checkbox("Show Grid", value=True)

# Prevent invalid axes
if x_axis_min >= x_axis_max:
    st.error("X-axis minimum must be smaller than maximum.")
    st.stop()

if y_axis_min >= y_axis_max:
    st.error("Y-axis minimum must be smaller than maximum.")
    st.stop()

# -------------------------------
# Graph Data
# -------------------------------
x = np.linspace(x_axis_min, x_axis_max, 400)
y = m * x + c

# -------------------------------
# Layout
# -------------------------------
left, right = st.columns([2,1])

with left:
    fig, ax = plt.subplots(figsize=(10,7))

    ax.plot(x, y, linewidth=4, label=f"y = {m:g}x + {c:g}")

    ax.axhline(0, linewidth=1.5)
    ax.axvline(0, linewidth=1.5)

    if grid_toggle:
        ax.grid(True, linestyle="--", alpha=0.5)

    ax.scatter([0], [c], s=150)
    ax.annotate(
        f"({0}, {c:g})",
        xy=(0,c),
        xytext=(1,c+1),
        arrowprops=dict(arrowstyle="->")
    )

    ax.set_xlim(x_axis_min, x_axis_max)
    ax.set_ylim(y_axis_min, y_axis_max)

    ax.set_title("Straight Line Graph", fontsize=20, fontweight="bold")
    ax.set_xlabel("x-axis")
    ax.set_ylabel("y-axis")

    ax.legend()

    st.pyplot(fig)

with right:
    st.markdown(f"""
    <div class="card">
    <h2>Current Equation</h2>
    <h1>y = {m:g}x + {c:g}</h1>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="card">
    <h3>📌 Gradient</h3>
    <p>{m:g}</p>

    <h3>📌 Y-intercept</h3>
    <p>{c:g}</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="card">
    <h3>📏 Axis Values</h3>
    <p>X-axis: {x_axis_min} to {x_axis_max}</p>
    <p>Y-axis: {y_axis_min} to {y_axis_max}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="card">
<h2>🧠 Learning Notes</h2>
<ul>
<li><b>Gradient (m)</b> controls steepness.</li>
<li><b>Positive gradient</b> rises from left to right.</li>
<li><b>Negative gradient</b> falls from left to right.</li>
<li><b>c</b> is where the line crosses the y-axis.</li>
</ul>
</div>
""", unsafe_allow_html=True)
