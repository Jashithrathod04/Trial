import time
import streamlit.components.v1 as components

# ==============================
# CINEMATIC PAINT SPLASH SCREEN
# ==============================

splash_html = """
<!DOCTYPE html>
<html>
<head>
<style>

body {
    margin: 0;
    overflow: hidden;
    background: radial-gradient(circle at center, #2b1d13, #120b07);
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    font-family: Georgia, serif;
}

/* Splash Container */
.splash-container {
    text-align: center;
    position: relative;
    z-index: 2;
}

/* Paint Stroke */
.paint-stroke {
    position: absolute;
    top: 50%;
    left: -40%;
    width: 80%;
    height: 80px;
    background: linear-gradient(90deg, #C6A75E, #E0C27B, #C6A75E);
    border-radius: 50px;
    filter: blur(2px);
    opacity: 0.85;
    animation: paintSwipe 2.5s ease-out forwards;
}

/* Paint Drip */
.paint-drip {
    position: absolute;
    top: 55%;
    left: 50%;
    width: 8px;
    height: 0;
    background: #C6A75E;
    border-radius: 4px;
    animation: drip 2s ease-in forwards;
    animation-delay: 1.5s;
}

/* Brush */
.brush {
    position: absolute;
    top: 48%;
    left: -15%;
    font-size: 3rem;
    animation: brushMove 2.5s ease-out forwards;
}

/* Title */
.title {
    font-size: 3.2rem;
    letter-spacing: 2px;
    color: #C6A75E;
    opacity: 0;
    margin-top: 2rem;
    animation: titleReveal 2s ease forwards;
    animation-delay: 2s;
}

.subtitle {
    font-size: 1rem;
    color: #f5e6d3;
    opacity: 0;
    margin-top: 1rem;
    animation: fadeIn 2s ease forwards;
    animation-delay: 2.5s;
}

/* Animations */

@keyframes brushMove {
    0% { left: -15%; }
    100% { left: 85%; }
}

@keyframes paintSwipe {
    0% { left: -40%; }
    100% { left: 110%; }
}

@keyframes drip {
    0% { height: 0; opacity: 1; }
    100% { height: 50px; opacity: 0.8; }
}

@keyframes titleReveal {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

</style>
</head>
<body>

<div class="splash-container">
    <div class="paint-stroke"></div>
    <div class="paint-drip"></div>
    <div class="brush">🖌️</div>

    <div class="title">ArtRestorer AI</div>
    <div class="subtitle">
        Restoring Cultural Heritage Through Intelligent Preservation
    </div>
</div>

</body>
</html>
"""


