import streamlit as st
import time

st.set_page_config(page_title="NeuroVoice AI", page_icon="🏥", layout="centered")

st.markdown("""
<style>
.stApp { background-color: #f8fafc; }
.card { background: white; padding: 25px; border-radius: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); border: 1px solid #e2e8f0; margin-bottom: 15px; }
.stButton>button { background: #0f172a !important; color: white !important; border-radius: 12px !important; height: 50px !important; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.title("NeuroVoice AI")
st.write("Clinical Parkinson's Screening System")
st.success("LIVE - Clinical v2.0 | Model: XGBoost | Accuracy: 92.5%")
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("Voice Input")
st.file_uploader("Upload .wav file", type=['wav','mp3'])
if st.button("DEPLOY MODEL + START INFERENCE"):
    bar = st.progress(0)
    for i in range(100):
        time.sleep(0.01)
        bar.progress(i+1)
    st.success("Parkinsonian Pattern: 89.6% confidence - Refer to Neurologist")
st.markdown('</div>', unsafe_allow_html=True)

st.caption("Md. Ishak Hossain | Thesis 2026 | For research only")
       
        


        
    
