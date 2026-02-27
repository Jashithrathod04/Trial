# =========================================================
# 🎨 ArtRestorer AI - Smart Assistance for Art Restoration
# Scenario 1 - Generative AI Summative Assessment
# =========================================================

import streamlit as st
import pandas as pd
from datetime import datetime
import time
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="ArtRestorer AI 🎨",
    page_icon="🖌️",
    layout="wide"
)


# ---------------- YELLOW PROMPT BOX STYLE ----------------
st.markdown("""
<style>

.prompt-box {
    background-color: #FBE9A7;  /* keep your yellow */
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.25);
    margin-top: 20px;
}

/* FORCE ALL TEXT INSIDE TO BE BLACK */
.prompt-box * {
    color: black !important;
}

</style>
""", unsafe_allow_html=True)



st.markdown("""
<style>

/* Historic Background Image */
.stApp {
   background-image: url("https://images.pexels.com/photos/15727855/pexels-photo-15727855.jpeg");
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
}

</style>
""", unsafe_allow_html=True)




# ---------------- GLOBAL YELLOW CONTENT CARD ----------------
st.markdown("""
<style>

/* Keep background visible */
.block-container {
    background: transparent;
    padding-top: 2rem;
}

/* Yellow card behind all content */
section.main > div.block-container {
    background-color: #FBE9A7;   /* Soft yellow */
    padding: 35px;
    border-radius: 20px;
    box-shadow: 0px 8px 30px rgba(0,0,0,0.25);
}

/* DO NOT change text colors */
/* We keep default dark text */

</style>
""", unsafe_allow_html=True)





# ---------------- YELLOW BOX STYLE ----------------
st.markdown("""
<style>

/* Yellow Box */
.yellow-box {
    background-color: #FFD54F;  /* Soft museum yellow */
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 25px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.3);
}

/* Text inside yellow box */
.yellow-box h1,
.yellow-box h2,
.yellow-box h3,
.yellow-box h4,
.yellow-box h5,
.yellow-box h6,
.yellow-box p {
    color: #2c2c2c;
}

</style>
""", unsafe_allow_html=True)




# ---------------- YELLOW TABS STYLE (FIXED) ----------------
st.markdown("""
<style>

/* Target the tab buttons container */
div[data-testid="stTabs"] button {
    background-color: #FBE9A7 !important;
    color: black !important;
    border-radius: 12px 12px 0px 0px !important;
    margin-right: 6px !important;
    font-weight: 600 !important;
}

/* Active tab styling */
div[data-testid="stTabs"] button[aria-selected="true"] {
    background-color: #F4C430 !important;
    color: black !important;
    border-bottom: 3px solid black !important;
}

/* Remove grey default highlight */
div[data-testid="stTabs"] button:focus {
    box-shadow: none !important;
}

</style>
""", unsafe_allow_html=True)








# ---------------- GEMINI CLIENT ----------------


# ---------------- SESSION STATE ----------------
if "splash_done" not in st.session_state:
    st.session_state.splash_done = False

if "page" not in st.session_state:
    st.session_state.page = "landing"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ---------------- SPLASH SCREEN ----------------
if not st.session_state.splash_done:

    splash_html = """
    <html>
    <head>
    <style>
    body {
        margin:0;
        background: linear-gradient(180deg,#f3e5f5,#e1bee7,#ce93d8);
        font-family:Segoe UI;
        text-align:center;
        overflow:hidden;
    }
    
    /* Title Styling */
    .title {
        margin-top:180px;
        font-size:60px;
        font-weight:bold;
        color:#4a148c;
        position:relative;
        z-index:2;
    }
    
    .subtitle {
        font-size:22px;
        color:#6a1b9a;
        margin-top:10px;
        position:relative;
        z-index:2;
    }
    
    /* Paint Splashes */
    .splash {
        position:absolute;
        width:120px;
        height:120px;
        border-radius:50%;
        opacity:0.7;
        animation: float 6s infinite ease-in-out alternate;
    }
    
    /* Different colors */
    .s1 { background:#ff5252; top:10%; left:15%; animation-delay:0s; }
    .s2 { background:#ffca28; top:60%; left:70%; animation-delay:1s; }
    .s3 { background:#29b6f6; top:40%; left:30%; animation-delay:2s; }
    .s4 { background:#66bb6a; top:75%; left:20%; animation-delay:3s; }
    .s5 { background:#ab47bc; top:20%; left:80%; animation-delay:4s; }
    
    /* Floating animation */
    @keyframes float {
    0%   { transform: translateY(0px) scale(1); }
    50%  { transform: translateY(-60px) scale(1.15); }
    100% { transform: translateY(0px) scale(1); }
    }
    
    </style>
    </head>
    <body>
    
    <div class="splash s1"></div>
    <div class="splash s2"></div>
    <div class="splash s3"></div>
    <div class="splash s4"></div>
    <div class="splash s5"></div>
    
    <div class="title">🎨 ArtRestorer AI</div>
    <div class="subtitle">Reviving Heritage with Digital Intelligence</div>
    
    </body>
    </html>
    """

    st.components.v1.html(splash_html, height=700)
    time.sleep(6)
    st.session_state.splash_done = True
    st.rerun()

# ---------------- LANDING PAGE ----------------
if st.session_state.page == "landing":

    st.markdown("""
    <div class="yellow-box" style="text-align:center;margin-top:120px;">
        <h1 style="font-size:52px;">AI-Powered Art Restoration Assistant</h1>
        <p style="font-size:20px;">
        Analyze artwork descriptions and generate intelligent restoration suggestions.
        </p>
    </div>
    """, unsafe_allow_html=True)
    

    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        if st.button("🎨 Get Started"):
            st.session_state.page = "profile"
            st.rerun()

# ---------------- PROFILE PAGE ----------------
elif st.session_state.page == "profile":

    st.title("🖌️ Create Your Curator Profile")

    name = st.text_input("👤 Name")
    institution = st.text_input("🏛️ Institution / Museum")
    country = st.text_input("🌍 Country")

    if st.button("Continue to Dashboard"):
        if not name:
            st.warning("Please enter your name.")
        else:
            st.session_state.name = name
            st.session_state.institution = institution
            st.session_state.country = country
            st.session_state.page = "dashboard"
            st.rerun()

# ---------------- DASHBOARD ----------------
elif st.session_state.page == "dashboard":

    # HEADER
    st.markdown(f"""
    <div class="yellow-box" style="text-align:center;">
        <h1>🎨 ArtRestorer AI</h1>
        <p>Welcome {st.session_state.name} | {st.session_state.institution}</p>
    </div>
    """, unsafe_allow_html=True)
    tab_restore, tab_prompts, tab_feedback, tab_usage, tab_settings = st.tabs(
        ["🖌️ Restoration Assistant", 
         "📜 Prompt Library (10+)", 
         "📊 Feedback",
         "📈 Usage",
         "⚙️ Settings"]
    )

    # =====================================================
    # =====================================================
# TAB 1 - RESTORATION ASSISTANT
# =====================================================
    with tab_restore:
    
        st.markdown("""
        <div class="prompt-box">
        <h2>Describe the Artwork</h2>
        """, unsafe_allow_html=True)
    
        col1, col2 = st.columns(2)
    
        with col1:
            artwork_type = st.selectbox(
                "Artwork Type",
                ["Oil Painting","Sculpture","Textile","Mural",
                 "Manuscript","Mosaic","Pottery"]
            )
    
            art_period = st.text_input(
                "Art Period / Style (e.g., Renaissance, Mughal, Gothic)"
            )
    
            artist = st.text_input("Artist (if known)")
    
        with col2:
            damage = st.text_area("Damage Description")
    
            output_format = st.selectbox(
                "Desired Output",
                ["Restoration Technique",
                 "Narrative Reconstruction",
                 "Symbol Interpretation",
                 "Complete Analysis"]
            )
    
            temperature = st.slider(
                "Creativity Level (Temperature)",
                0.1, 1.0, 0.6
            )
            uploaded_image = st.file_uploader(
                "Upload Artwork Image (Optional)",
                type=["jpg", "jpeg", "png"]
            )
            if uploaded_image:
                st.image(uploaded_image, caption="Uploaded Artwork", use_container_width=True)

            



        
    
        if st.button("Generate AI Restoration Suggestion"):
    
            prompt = f"""
    You are a senior art restoration expert.
    
    Artwork Type: {artwork_type}
    Period/Style: {art_period}
    Artist: {artist}
    Damage Description: {damage}
    Output Type: {output_format}
    
    Provide:
    1. Restoration Strategy
    2. Implementation Steps
    3. Cultural and Historical Justification
    4. Risk Mitigation Advice
    5. Final Professional Recommendation
    
    Maintain cultural sensitivity and artistic accuracy.
    """
    
            # define once
            model = genai.GenerativeModel("gemini-3-flash-preview")
            
            with st.spinner("Analyzing artwork and generating restoration strategy..."):

                if uploaded_image:
                    response = model.generate_content(
                        [
                            prompt,
                            {
                                "mime_type": uploaded_image.type,
                                "data": uploaded_image.getvalue()
                            }
                        ],
                        generation_config={
                            "temperature": temperature,
                            "max_output_tokens": 2048
                        }
                    )
                else:
                    response = model.generate_content(
                        prompt,
                        generation_config={
                            "temperature": temperature,
                            "max_output_tokens": 2048
                        }
                    )
                st.markdown("### 🎨 AI Restoration Output")
                st.markdown(response.text)
    
            
            
    
        st.markdown("</div>", unsafe_allow_html=True)

    # =====================================================
    # TAB 2 - 10+ PROMPT LIBRARY
    # =====================================================
    with tab_prompts:

        st.markdown("""
        <div class="prompt-box">
        <h2>Compulsory 10 AI Restoration Prompts</h2>
    
        <ol>
            <li>Baroque painting missing upper-left corner — restore dramatic shadows.</li>
            <li>Mughal miniature with faded floral borders — enhance detailing.</li>
            <li>12th century sandstone sculpture with eroded face — reconstruct symmetrically.</li>
            <li>18th century silk tapestry torn near emblem — restore embroidery consistency.</li>
            <li>Abstract Expressionist canvas lost texture — recreate chaotic brushstroke feel.</li>
            <li>Ajanta cave mural with sun fading — digitally revive mineral pigments.</li>
            <li>Mayan glyph carvings partially eroded — reconstruct symbolic inscriptions.</li>
            <li>Japanese Ukiyo-e woodblock faded — enhance wave and ink precision.</li>
            <li>Gothic cathedral mosaic cracked — restore stained glass symmetry.</li>
            <li>Medieval manuscript ink erosion — recreate script and floral margins.</li>
        </ol>
    
        </div>
        """, unsafe_allow_html=True)
        
        

    # =====================================================
    # =====================================================
# TAB 3 - FEEDBACK
# =====================================================
    with tab_feedback:
    
        st.markdown("""
        <div class="prompt-box">
        <h2>AI Output Evaluation</h2>
        """, unsafe_allow_html=True)
    
        with st.form("feedback_form"):
            f1 = st.checkbox("Culturally accurate")
            f2 = st.checkbox("Technically useful")
            f3 = st.checkbox("Historically aligned")
            f4 = st.checkbox("Creative but realistic")
            f5 = st.checkbox("Clear and understandable")
    
            submitted = st.form_submit_button("Submit Feedback")
    
        if submitted:
            score = sum([f1, f2, f3, f4, f5])
            percentage = int((score / 5) * 100)
            st.progress(percentage / 100)
            st.success(f"Quality Score: {percentage}%")
    
        st.markdown("</div>", unsafe_allow_html=True)
        # =====================================================
        # TAB 4 - USAGE
        # =====================================================
        with tab_usage:
    
            usage_data = {
                "Name": st.session_state.name,
                "Institution": st.session_state.institution,
                "Country": st.session_state.country,
                "Time": datetime.now().strftime("%Y-%m-%d %H:%M")
            }
    
            st.dataframe(pd.DataFrame([usage_data]))
    
        # =====================================================
        # =====================================================
        # TAB 5 - SETTINGS
        # =====================================================
        with tab_settings:
        
            st.markdown("""
            <div class="prompt-box">
            <h2>Profile Information</h2>
            """, unsafe_allow_html=True)
        
            st.write(f"Name: {st.session_state.name}")
            st.write(f"Institution: {st.session_state.institution}")
            st.write(f"Country: {st.session_state.country}")
        
            if st.button("Sign Out"):
                st.session_state.page = "landing"
                st.rerun()
        
            st.markdown("</div>", unsafe_allow_html=True)
    
    # ---------------- FOOTER ----------------
    st.markdown("<hr><p style='text-align:center;'>CRS Generative AI | 2026</p>", unsafe_allow_html=True)
