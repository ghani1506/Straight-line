
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------
# Page setup
# -------------------------------------------------------
st.set_page_config(
    page_title="Interactive Straight Line Graph",
    page_icon="📈",
    layout="wide"
)

# -------------------------------------------------------
# Custom CSS: infographic style
# -------------------------------------------------------
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #f7fbff 0%, #eef7ff 45%, #fff8e8 100%);
    }

    .title-box {
        background: linear-gradient(90deg, #0f766e, #2563eb);
        padding: 26px;
        border-radius: 24px;
        color: white;
        text-align: center;
        box-shadow: 0px 8px 25px rgba(0,0,0,0.12);
        margin-bottom: 18px;
    }

    .title-box h1 {
        font-size: 42px;
        margin-bottom: 6px;
    }

    .title-box p {
        font-size: 18px;
        margin: 0;
    }

    .card {
        background-color: white;
        padding: 22px;
        border-radius: 22px;
        box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
        border-left: 8px solid #2563eb;
        margin-bottom: 18px;
    }

    .formula-card {
        background: linear-gradient(135deg, #fff7ed, #ffffff);
        padding: 24px;
        border-radius: 22px;
        box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
        border-left: 8px solid #f97316;
        text-align: center;
    }

    .metric-box {
        background: #ecfeff;
        padding: 18px;
        border-radius: 18px;
        text-align: center;
        border: 2px solid #67e8f9;
    }

    .small-text {
        font-size: 16px;
        color: #334155;
    }

    .success-box {
        background: #f0fdf4;
        padding: 18px;
        border-radius: 18px;
        border-left: 8px solid #22c55e;
        margin-top: 10px;
    }

    .warning-box {
        background: #fff7ed;
        padding: 18px;
        border-radius: 18px;
        border-left: 8px solid #f97316;
        margin-top: 10px;
    }

    .footer {
        text-align: center;
        color: #475569;
        font-size: 14px;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# Header
# -------------------------------------------------------
st.markdown("""
<div class="title-box">
    <h1>📈 Interactive Straight Line Graph</h1>
    <p>Explore how the gradient and y-intercept change the graph of <b>y = mx + c</b></p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# Sidebar controls
# -------------------------------------------------------
st.sidebar.header("🎛️ Graph Control Panel")
st.sidebar.write("Adjust the values below and observe how the line changes.")

m = st.sidebar.slider(
    "Gradient, m",
    min_value=-10.0,
    max_value=10.0,
    value=2.0,
    step=0.5,
    help="The gradient controls the steepness and direction of the line."
)

c = st.sidebar.slider(
    "Y-intercept, c",
    min_value=-10.0,
    max_value=10.0,
    value=1.0,
    step=0.5,
    help="The y-intercept is where the line crosses the y-axis."
)

x_min = st.sidebar.slider("Minimum x-value", -20, 0, -10)
x_max = st.sidebar.slider("Maximum x-value", 1, 20, 10)

show_points = st.sidebar.checkbox("Show sample coordinate points", value=True)
show_grid = st.sidebar.checkbox("Show grid", value=True)
show_intercept = st.sidebar.checkbox("Highlight y-intercept", value=True)

# -------------------------------------------------------
# Main layout
# -------------------------------------------------------
left, right = st.columns([2, 1])

# -------------------------------------------------------
# Graph
# -------------------------------------------------------
with left:
    x = np.linspace(x_min, x_max, 400)
    y = m * x + c

    fig, ax = plt.subplots(figsize=(10, 7))

    ax.plot(x, y, linewidth=4, label=f"y = {m:g}x + {c:g}")

    # Axes
    ax.axhline(0, linewidth=1.5)
    ax.axvline(0, linewidth=1.5)

    # Grid
    if show_grid:
        ax.grid(True, linestyle="--", alpha=0.4)

    # Highlight y-intercept
    if show_intercept:
        ax.scatter([0], [c], s=160, zorder=5)
        ax.annotate(
            f"y-intercept = {c:g}",
            xy=(0, c),
            xytext=(1, c + 2),
            arrowprops=dict(arrowstyle="->", lw=2),
            fontsize=12,
            bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="gray", alpha=0.9)
        )

    # Sample points
    if show_points:
        sample_x = np.array([-2, -1, 0, 1, 2])
        sample_y = m * sample_x + c
        ax.scatter(sample_x, sample_y, s=80, zorder=4)

        for px, py in zip(sample_x, sample_y):
            ax.annotate(
                f"({px:g}, {py:g})",
                (px, py),
                textcoords="offset points",
                xytext=(8, 8),
                fontsize=10
            )

    ax.set_title("Graph of a Straight Line", fontsize=20, fontweight="bold", pad=15)
    ax.set_xlabel("x-axis", fontsize=14)
    ax.set_ylabel("y-axis", fontsize=14)
    ax.legend(fontsize=13, loc="best")

    # Dynamic limits
    y_margin = max(5, (max(y) - min(y)) * 0.1)
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(min(y) - y_margin, max(y) + y_margin)

    st.pyplot(fig)

# -------------------------------------------------------
# Explanation panel
# -------------------------------------------------------
with right:
    st.markdown(f"""
    <div class="formula-card">
        <h2>Current Equation</h2>
        <h1>y = {m:g}x + {c:g}</h1>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        <div class="metric-box">
            <h3>Gradient</h3>
            <h1>{m:g}</h1>
            <p class="small-text">Controls steepness</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="metric-box">
            <h3>Y-intercept</h3>
            <h1>{c:g}</h1>
            <p class="small-text">Crosses y-axis here</p>
        </div>
        """, unsafe_allow_html=True)

    if m > 0:
        gradient_message = "The line rises from left to right because the gradient is positive."
    elif m < 0:
        gradient_message = "The line falls from left to right because the gradient is negative."
    else:
        gradient_message = "The line is horizontal because the gradient is zero."

    st.markdown(f"""
    <div class="success-box">
        <h3>🔍 What is happening?</h3>
        <p>{gradient_message}</p>
        <p>The line crosses the y-axis at <b>{c:g}</b>.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="warning-box">
        <h3>🧠 Remember</h3>
        <p><b>m</b> tells us the steepness.</p>
        <p><b>c</b> tells us where the line cuts the y-axis.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------
# Student learning section
# -------------------------------------------------------
st.markdown("---")

a, b, d = st.columns(3)

with a:
    st.markdown("""
    <div class="card">
        <h3>✅ Step 1: Look at c</h3>
        <p>Find where the line crosses the y-axis. That value is the y-intercept.</p>
    </div>
    """, unsafe_allow_html=True)

with b:
    st.markdown("""
    <div class="card">
        <h3>✅ Step 2: Look at m</h3>
        <p>If m is positive, the line goes up. If m is negative, the line goes down.</p>
    </div>
    """, unsafe_allow_html=True)

with d:
    st.markdown("""
    <div class="card">
        <h3>✅ Step 3: Compare steepness</h3>
        <p>The bigger the size of m, the steeper the line becomes.</p>
    </div>
    """, unsafe_allow_html=True)

# -------------------------------------------------------
# Mini task
# -------------------------------------------------------
st.markdown("""
<div class="card">
    <h2>🎯 Try This</h2>
    <p>Use the sliders to create these graphs:</p>
    <ol>
        <li>A line that rises and crosses the y-axis at 3.</li>
        <li>A line that falls and crosses the y-axis at -2.</li>
        <li>A horizontal line that crosses the y-axis at 5.</li>
    </ol>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    Designed for Mathematics learning: Straight Line Graphs, Gradient and Y-intercept.
</div>
""", unsafe_allow_html=True)
