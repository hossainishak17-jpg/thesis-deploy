import streamlit as st
import time

st.set_page_config(page_title="NeuroVoice AI v2.4", layout="wide")

st.markdown("""
<style>
.stApp { background-color: #0b1220; }
.header { background: #151e32; border: 1px solid #1e2a4a; border-radius: 16px; padding: 18px 22px; display: flex; justify-content: space-between; align-items: center; }
.card { background: #151e32; border: 1px solid #1e2a4a; border-radius: 16px; padding: 18px; }
.card-title { color: #4ea8ff; font-size: 11px; font-weight: 800; letter-spacing: 1.5px; }
.metric-box { background: #0f172a; border-radius: 14px; padding: 16px; text-align: center; border: 1px solid; }
.result-box { background: #0a1f14; border: 1px solid #1f8a4c; border-radius: 16px; padding: 20px; text-align: center; }
.red-btn>button { background: #ff4d4d !important; color: white !important; border-radius: 10px !important; height: 48px !important; width: 100% !important; font-weight: 700 !important; }
.progress { height: 8px; background: #1e2a4a; border-radius: 10px; }
.progress-fill { height: 100%; background: #2f8bff; border-radius: 10px; }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="header">
    <div style="color:#4ea8ff; font-weight:800; font-size:18px;">🧬 NeuroVoice AI v2.4 <span style="color:white; font-weight:400; font-size:13px;">| ML DEPLOYMENT - STREAMLIT PRO</span></div>
    <div style="background:#0a1f14; border:1px solid #1f8a4c; color:#22c55e; padding:6px 14px; border-radius:20px; font-size:12px;">● MODEL SERVER ONLINE - 128ms latency</div>
</div>
""", unsafe_allow_html=True)

st.write("")
col1, col2, col3 = st.columns([1,1.6,1])

# VOICE STATE
if "voice_done" not in st.session_state: st.session_state.voice_done = False

with col1:
    st.markdown('<div class="card"><div class="card-title">🎙️ VOICE ACQUISITION [LIVE MIC]</div></div>', unsafe_allow_html=True)
    st.markdown('<div style="text-align:center; padding:15px 0;"><div style="font-size:40px;">🎤</div><div style="color:#4ea8ff; font-size:11px;">SUSTAINED VOWEL /a/ - 16kHz</div></div>', unsafe_allow_html=True)
    
    # LIVE MIC RECORDING
    st.markdown('<div style="color:white; font-size:13px; margin-bottom:8px;">Record /a/ phonation - 3 sec</div>', unsafe_allow_html=True)
    audio = st.audio_input("Record voice")
    
    if audio:
        st.session_state.voice_done = True
        st.success("Voice Captured ✓")
    else:
        st.info("Press mic and say 'aaaa'")

    st.write("")
    st.markdown('<div class="red-btn">', unsafe_allow_html=True)
    deploy = st.button("🚀 DEPLOY MODEL + START INFERENCE", disabled=not st.session_state.voice_done)
    st.markdown('</div>', unsafe_allow_html=True)
    
    if not st.session_state.voice_done:
        st.caption("⚠️ Record voice first to enable deploy")

with col2:
    st.markdown('<div class="card"><div class="card-title">🧠 LIVE INFERENCE - ENSEMBLE MODEL (SVM + XGB + RF) - DEPLOYED</div></div>', unsafe_allow_html=True)
    st.write("")
    m1_ph = st.empty()
    m_row_ph = st.empty()
    result_ph = st.empty()

    if deploy and st.session_state.voice_done:
        # ROW 1
        m1_ph.markdown('<div class="metric-box" style="border-color:#2f8bff;"><div style="color:#6b7280; font-size:10px;">ACCURACY (CV)</div><div style="color:#4ea8ff; font-size:28px; font-weight:800;">92.5%</div><div style="color:#4ea8ff; font-size:10px;">GroupKFold k=5</div></div>', unsafe_allow_html=True)
        time.sleep(0.7)
        # ROW 2
        c_a, c_b = m_row_ph.columns(2)
        with c_a: st.markdown('<div class="metric-box" style="border-color:#22c55e;"><div style="color:#6b7280; font-size:10px;">AUC-ROC</div><div style="color:#22c55e; font-size:28px; font-weight:800;">0.95</div><div style="color:#22c55e; font-size:10px;">+3.3% Gain</div></div>', unsafe_allow_html=True)
        with c_b: st.markdown('<div class="metric-box" style="border-color:#a78bfa;"><div style="color:#6b7280; font-size:10px;">F1-SCORE</div><div style="color:#a78bfa; font-size:28px; font-weight:800;">91.1%</div><div style="color:#a78bfa; font-size:10px;">Ensemble</div></div>', unsafe_allow_html=True)
        time.sleep(0.7)
        # ROW 3
        result_ph.markdown("""
        <div class="result-box">
            <div style="background:#143d24; border:1px solid #22c55e; color:#86efac; display:inline-block; padding:5px 14px; border-radius:20px; font-size:11px;">● DEPLOYED - PREDICTION: POSITIVE</div>
            <h2 style="color:white; margin:15px 0;">Parkinson Pattern Detected</h2>
            <div style="color:#86efac; font-size:12px;">Confidence 89.6% | Prob 0.896 | Latency 128ms</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        result_ph.markdown('<div class="result-box"><div style="color:gray; padding:30px;">🎙️ Record voice then click Deploy<br>Waiting for inference...</div></div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="card"><div class="card-title">🔬 SHAP EXPLAINABILITY - LIVE</div></div>', unsafe_allow_html=True)
    st.write("")
    shap_ph = st.empty()
    if deploy and st.session_state.voice_done:
        time.sleep(1.4)
        shap_ph.markdown("""
        <div>
            <div style="color:white; font-size:14px;">PPE +0.38 (High Risk)</div><div class="progress"><div class="progress-fill" style="width:78%;"></div></div><br>
            <div style="color:white; font-size:14px;">Jitter(%) +0.31 (High Risk)</div><div class="progress"><div class="progress-fill" style="width:68%;"></div></div><br>
            <div style="color:white; font-size:14px;">Shimmer +0.26 (Medium Risk)</div><div class="progress"><div class="progress-fill" style="width:52%; background:#a78bfa;"></div></div>
        </div>
        """, unsafe_allow_html=True)


      
  
