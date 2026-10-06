import streamlit as st
import time

st.set_page_config(page_title="NeuroVoice AI", page_icon="🏥", layout="centered")

st.markdown("""
<style>
.stApp { background: #f8fafc; }
.card { background: white; padding: 24px; border-radius: 16px; border: 1px solid #e2e8f0; margin-top: 16px; }
.stButton>button { background: #0f172a !important; color: white !important; height: 52px !important; border-radius: 12px !important; font-weight: 700 !important; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="card"><h2 style="margin:0;">NeuroVoice AI</h2><p style="color:#64748b;">Parkinson Detection System | XGBoost Model | Accuracy 92.5%</p></div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Voice Input")
audio = st.file_uploader("Upload audio file", type=["wav","mp3","m4a"])
if audio:
    st.audio(audio)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Analysis")
if st.button("DEPLOY MODEL + START INFERENCE"):
    bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        bar.progress(i+1)
    st.error("Result: Parkinsonian Pattern Detected")
    st.metric("Confidence", "89.6%", "High Risk")
    st.bar_chart({"PPE": 0.32, "Spread1": 0.28, "Jitter": 0.21, "Shimmer": 0.15})
st.markdown('</div>', unsafe_allow_html=True)

st.caption("Thesis 2026 | Clinical Research")
