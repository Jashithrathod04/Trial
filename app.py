import time
import streamlit.components.v1 as components

# ==============================
# FULL SCREEN SPLASH SCREEN
# ==============================

splash_html = """
<!DOCTYPE html>
<html>
<head>
<style>

body {
    margin: 0;
    overflow: hidden;
    background: linear-gradient(145deg, #1a120b, #3b2a1a);
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    font-family: Georgia, serif;
}

/* Container */
.splash-container {
    text-align: center;
    color: #C6A75E;
    animation: fadeIn 2s ease forwards;
}

/* Animated Brush Stroke Line */
.brush-line {
    width: 0;
    height: 3px;
    background: linear-gradient(90deg, transparent, #C6A75E, #E0C27B, #C6A75E, transparent);
    margin: 20px auto;
    animation: drawLine 2.5s ease forwards;
}

/* Title */
.title {
    font-size: 3rem;
    letter-spacing: 2px;
    opacity: 0;
    animation: titleReveal 3s ease forwards;
    animation-delay: 1s;
}

/* Subtitle */
.subtitle {
    font-size: 1rem;
    margin-top: 1rem;
    color: #f5e6d3;
    opacity: 0;
    animation: fadeIn 3s ease forwards;
    animation-delay: 2s;
}

/* Animations */

@keyframes drawLine {
    0% { width: 0; }
    100% { width: 60%; }
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes titleReveal {
    0% { opacity: 0; transform: translateY(20px); }
    100% { opacity: 1; transform: translateY(0); }
}

</style>
</head>
<body>

<div class="splash-container">
    <div class="title">🎨 ArtRestorer AI</div>
    <div class="brush-line"></div>
    <div class="subtitle">
        Preserving Cultural Heritage Through Artificial Intelligence
    </div>
</div>

</body>
</html>
"""

# Show splash
components.html(splash_html, height=800)

if "splash_shown" not in st.session_state:
    components.html(splash_html, height=800)
    time.sleep(3)
    st.session_state.splash_shown = True
    st.rerun()

st.empty()
