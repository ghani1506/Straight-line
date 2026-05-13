
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------
# Page setup
# -------------------------------------------------------
st.set_page_config(
    page_title="Live Interactive Straight Line Graph",
    page_icon="📈",
    layout="wide"
)

# -------------------------------------------------------
# CSS: infographic style
# -------------------------------------------------------
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #eef7ff 0%, #fff7ed 100%);
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
    margin-bottom: 5px;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 22px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    margin-bottom: 18px;
}

.formula-card {
    background: linear-gradient(135deg, #fff7ed, #ffffff);
    padding: 22px;
    border-radius: 22px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
    border-left: 8px solid #f97316;
    text-align: center;
}

.note-card {
    background: #f0fdf4;
    padding: 18px;
    border-radius: 18px;
    border-left: 8px solid #22c55e;
    margin-bottom: 14px;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# Header
# -------------------------------------------------------
st.markdown("""
<div class="title-box">
    <h1>📈 Live Straight Line Graph</h1>
    <p>Move the gradient and y-intercept sliders. The graph changes instantly.</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# Sidebar controls
# Streamlit automatically reruns the app whenever a widget changes.
# This creates simultaneous/live updates.
# -------------------------------------------------------
st.sidebar.header("🎛️ Live Control Panel")

m = st.sidebar.slider(
    "Gradient, m",
    min_value=-10.0,
    max_value=10.0,
    value=2.0,
    step=0.1,
    help="Change this to make the line steeper, flatter, rising, or falling."
)

c = st.sidebar.slider(
    "Y-intercept, c",
    min_value=-20.0,
    max_value=20.0,
    value=1.0,
    step=0.1,
    help="Change this to move the line up or down."
)

st.sidebar.subheader("📏 Adjustable Axis")

x_axis_min = st.sidebar.number_input("X-axis minimum", value=-10.0, step=1.0)
x_axis_max = st.sidebar.number_input("X-axis maximum", value=10.0, step=1.0)
y_axis_min = st.sidebar.number_input("Y-axis minimum", value=-10.0, step=1.0)
y_axis_max = st.sidebar.number_input("Y-axis maximum", value=10.0, step=1.0)

show_grid = st.sidebar.checkbox("Show grid", value=True)
show_points = st.sidebar.checkbox("Show sample points", value=True)
show_y_intercept = st.sidebar.checkbox("Highlight y-intercept", value=True)

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

# -------------------------------------------------------
# Layout
# -------------------------------------------------------
left, right = st.columns([2.2, 1])

with left:
    graph_placeholder = st.empty()

    with graph_placeholder.container():
        fig, ax = plt.subplots(figsize=(11, 7))

        ax.plot(
            x,
            y,
            linewidth=4,
            label=f"y = {m:.1f}x + {c:.1f}"
        )

        # x-axis and y-axis
        ax.axhline(0, linewidth=1.4)
        ax.axvline(0, linewidth=1.4)

        if show_grid:
            ax.grid(True, linestyle="--", alpha=0.45)

        # y-intercept marker
        if show_y_intercept and y_axis_min <= c <= y_axis_max:
            ax.scatter([0], [c], s=180, zorder=5)
            ax.annotate(
                f"y-intercept = {c:.1f}",
                xy=(0, c),
                xytext=(1, c + 1),
                arrowprops=dict(arrowstyle="->", lw=2),
                fontsize=12,
                bbox=dict(boxstyle="round,pad=0.4", fc="white", ec="gray", alpha=0.9)
            )

        # sample coordinate points
        if show_points:
            sample_x = np.array([-2, -1, 0, 1, 2])
            sample_y = m * sample_x + c

            visible = (
                (sample_x >= x_axis_min) &
                (sample_x <= x_axis_max) &
                (sample_y >= y_axis_min) &
                (sample_y <= y_axis_max)
            )

            ax.scatter(sample_x[visible], sample_y[visible], s=90, zorder=4)

            for px, py in zip(sample_x[visible], sample_y[visible]):
                ax.annotate(
                    f"({px:g}, {py:.1f})",
                    (px, py),
                    textcoords="offset points",
                    xytext=(8, 8),
                    fontsize=10
                )

        ax.set_xlim(x_axis_min, x_axis_max)
        ax.set_ylim(y_axis_min, y_axis_max)

        ax.set_title("Graph of y = mx + c", fontsize=21, fontweight="bold", pad=15)
        ax.set_xlabel("x-axis", fontsize=14)
        ax.set_ylabel("y-axis", fontsize=14)
        ax.legend(fontsize=13, loc="best")

        st.pyplot(fig, clear_figure=True)

with right:
    st.markdown(f"""
    <div class="formula-card">
        <h2>Current Equation</h2>
        <h1>y = {m:.1f}x + {c:.1f}</h1>
    </div>
    """, unsafe_allow_html=True)

    if m > 0:
        gradient_note = "The line rises from left to right."
    elif m < 0:
        gradient_note = "The line falls from left to right."
    else:
        gradient_note = "The line is horizontal."

    st.markdown(f"""
    <div class="note-card">
        <h3>🔍 Live Interpretation</h3>
        <p><b>Gradient:</b> {m:.1f}</p>
        <p>{gradient_note}</p>
        <p><b>Y-intercept:</b> {c:.1f}</p>
        <p>The line crosses the y-axis at <b>{c:.1f}</b>.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="card">
        <h3>📏 Axis Range</h3>
        <p><b>X-axis:</b> {x_axis_min:g} to {x_axis_max:g}</p>
        <p><b>Y-axis:</b> {y_axis_min:g} to {y_axis_max:g}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

st.markdown("""
<div class="card">
    <h2>🎯 Student Challenge</h2>
    <ol>
        <li>Make a line with positive gradient and y-intercept 3.</li>
        <li>Make a line with negative gradient and y-intercept -2.</li>
        <li>Make a horizontal line crossing the y-axis at 5.</li>
        <li>Change only the gradient. What happens to the steepness?</li>
        <li>Change only the y-intercept. What happens to the position of the line?</li>
    </ol>
</div>
""", unsafe_allow_html=True)
