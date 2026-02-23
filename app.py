import time
import streamlit.components.v1 as components
import streamlit as st
from datetime import datetime
import time
import streamlit.components.v1 as components
import pandas as pd
# ==============================
# FULL SCREEN SPLASH SCREEN
# ==============================


if "page" not in st.session_state:
    st.session_state.page = "landing"
    
import streamlit.components.v1 as components

if st.session_state.page == "landing":

    landing_html = """
    <html>
    <head>
    <style>
    body {
        margin: 0;
        overflow: hidden;
        background: #000000;
        font-family: Georgia, serif;
    }

    /* PARTICLES BACKGROUND */
    .particles {
        position: absolute;
        width: 100%;
        height: 100%;
        background: radial-gradient(circle, rgba(255,215,0,0.15) 1px, transparent 1px);
        background-size: 50px 50px;
        animation: moveParticles 40s linear infinite;
        z-index: 1;
    }

    @keyframes moveParticles {
        from { background-position: 0 0; }
        to { background-position: 500px 500px; }
    }

    /* CURTAINS */
    .curtain-left, .curtain-right {
        position: absolute;
        top: 0;
        width: 50%;
        height: 100%;
        background: linear-gradient(to bottom, #300000, #100000);
        z-index: 3;
        animation: openCurtain 3s forwards ease-in-out;
    }

    .curtain-left {
        left: 0;
        border-right: 5px solid #D4AF37;
    }

    .curtain-right {
        right: 0;
        border-left: 5px solid #D4AF37;
        animation-delay: 0.2s;
    }

    @keyframes openCurtain {
        to {
            transform: translateX(-100%);
        }
    }

    .curtain-right {
        animation-name: openCurtainRight;
    }

    @keyframes openCurtainRight {
        to {
            transform: translateX(100%);
        }
    }

    /* CENTER CONTENT */
    .content {
        position: relative;
        z-index: 2;
        text-align: center;
        top: 35%;
        color: #D4AF37;
        opacity: 0;
        animation: fadeIn 3s forwards;
        animation-delay: 2s;
    }

    @keyframes fadeIn {
        to { opacity: 1; }
    }

    .title {
        font-size: 4rem;
        text-shadow: 0 0 15px #FFD700;
    }

    .subtitle {
        font-size: 1.5rem;
        margin-top: 20px;
        color: #E6C97F;
    }

    /* PAINT SPLATTER */
    .splash {
        position: absolute;
        width: 200px;
        height: 200px;
        background: radial-gradient(circle, #8B0000 30%, transparent 70%);
        border-radius: 50%;
        top: 20%;
        left: 45%;
        opacity: 0;
        animation: splatter 2s forwards;
        animation-delay: 1s;
        z-index: 2;
    }

    @keyframes splatter {
        0% { transform: scale(0.2); opacity: 0; }
        70% { opacity: 1; }
        100% { transform: scale(1.5); opacity: 0.6; }
    }

    </style>
    </head>

    <body>

        <div class="particles"></div>

        <div class="curtain-left"></div>
        <div class="curtain-right"></div>

        <div class="splash"></div>

        <div class="content">
            <div class="title">Restora A.I</div>
            <div class="subtitle">AI-Powered Cultural Heritage Restoration Assistant</div>
        </div>

    </body>
    </html>
    """

    components.html(landing_html, height=800)
    
    if st.button("Enter the Gallery"):
        st.session_state.page = "dashboard"
        st.rerun()

    st.stop()
