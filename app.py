import time
import streamlit.components.v1 as components
import streamlit as st
from datetime import datetime
import time
import streamlit.components.v1 as components
import pandas as pd
import matplotlib.pyplot as plt
# ==============================
# FULL SCREEN SPLASH SCREEN
# ==============================

if st.session_state.page == "landing":

    st.markdown("""
    <style>
    .hero-title {
        font-size: 4rem;
        text-align: center;
        color: #D4AF37;
        font-family: 'Georgia', serif;
        animation: glow 2s ease-in-out infinite alternate;
    }

    @keyframes glow {
        from { text-shadow: 0 0 10px #8B6914; }
        to { text-shadow: 0 0 25px #FFD700; }
    }

    .tagline {
        text-align: center;
        font-size: 1.5rem;
        color: #E6C97F;
        margin-bottom: 40px;
    }

    .feature-card {
        background: rgba(20,20,20,0.85);
        padding: 25px;
        border-radius: 15px;
        border: 1px solid #C6A75E;
        text-align: center;
        color: #F5DEB3;
        transition: 0.3s ease;
    }

    .feature-card:hover {
        box-shadow: 0 0 20px #D4AF37;
        transform: translateY(-5px);
    }

    .divider {
        height: 2px;
        background: linear-gradient(to right, transparent, #D4AF37, transparent);
        margin: 50px 0;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="hero-title">Restora A.I</div>', unsafe_allow_html=True)
    st.markdown('<div class="tagline">AI-Powered Cultural Heritage Restoration Assistant</div>', unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="feature-card">
        <h3>🖼 AI Restoration Analysis</h3>
        <p>Generate culturally sensitive, historically accurate restoration strategies using advanced generative AI models.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
        <h3>🏛 Cultural Integrity Protection</h3>
        <p>Preserve authenticity while restoring damaged artwork, monuments, and historical artifacts.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
        <h3>🕓 Restoration Archive</h3>
        <p>Maintain and analyze past restoration records with intelligent tracking and documentation.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    st.markdown(
        "<h2 style='text-align:center; color:#D4AF37;'>Preserve the Past. Restore the Future.</h2>",
        unsafe_allow_html=True
    )

    if st.button("Enter the Gallery"):
        st.session_state.page = "dashboard"
        st.rerun()

    st.stop()
