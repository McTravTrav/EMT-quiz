import streamlit as st
import random

# --- 1. FULL DATA BANK (60+ Questions from your ARV Review) ---
if 'all_q' not in st.session_state:
    st.session_state.all_q = [
        {"q": "What is the leaf-shaped cartilage that prevents aspiration?", "options": ["Cricoid cartilage", "Epiglottis", "Carina", "Thyroid cartilage"], "correct": "Epiglottis", "rationale": "The epiglottis covers the laryngeal inlet during swallowing."},
        {"q": "Which of these is a lower airway structure?", "options": ["Nasopharynx", "Larynx", "Trachea", "Oropharynx"], "correct": "Trachea", "rationale": "The lower airway begins below the larynx and includes the trachea and bronchi."},
        {"q": "The phrenic nerve controls the diaphragm. Where does it exit the spine?", "options": ["C1-C2", "C3-C5", "T1-T4", "L1-L2"], "correct": "C3-C5", "rationale": "C3, 4, and 5 keep the diaphragm alive."},
        {"q": "What is the normal respiratory rate for an adult?", "options": ["8-12 bpm", "12-20 bpm", "20-30 bpm", "10-15 bpm"], "correct": "12-20 bpm", "rationale": "12-20 is the standard range for a healthy adult."},
        {"q": "A high-pitched whistling sound during inhalation is:", "options": ["Wheezing", "Stridor", "Rales", "Rhonchi"], "correct": "Stridor", "rationale": "Stridor indicates a partial upper airway obstruction."},
        {"q": "Minute Volume is calculated as:", "options": ["TV + RR", "TV x RR", "TV / RR", "RR - TV"], "correct": "TV x RR", "rationale": "Minute volume = Tidal Volume multiplied by Respiratory Rate."},
        {"q": "The primary drive to breathe is based on levels of:", "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Glucose"], "correct": "Carbon Dioxide", "rationale": "The brain monitors CO2 and pH in the CSF to regulate breathing."},
        {"q": "Which device is used for a patient with a gag reflex?", "options": ["OPA", "NPA", "King Airway", "LMA"], "correct": "NPA", "rationale": "NPAs are tolerated by patients with an intact gag reflex."},
        {"q": "Max suction time for an adult is:", "options": ["5 sec", "10 sec", "15 sec", "20 sec"], "correct": "15 sec", "rationale": "Limit adult suctioning to 15 seconds to prevent hypoxia."},
        {"q": "The 'O' in the DOPE mnemonic stands for:", "options": ["Oxygen", "Obstruction", "Output", "Over-ventilation"], "correct": "Obstruction", "rationale": "Obstruction (usually mucus) is a common trach tube failure."},
        {"q": "What is the FiO2 of room air?", "options": ["16%", "21%", "44%", "100%"], "correct": "21%", "rationale": "Room air contains approximately 21% oxygen."},
        {"q": "A non-rebreather mask (NRB) should be set to:", "options": ["1-6 L/min", "6-10 L/min", "10-15 L/min", "15-25 L/min"], "correct": "10-15 L/min", "rationale": "This flow rate keeps the reservoir bag inflated."},
        {"q": "Gastric distension is a common complication of:", "options": ["Nasal Cannula", "Over-ventilation with BVM", "Proper OPA insertion", "Suctioning"], "correct": "Over-ventilation with BVM", "rationale": "Excessive pressure forces air into the esophagus."},
        {"q": "Which structure is the site of gas exchange?", "options": ["Bronchi", "Alveoli", "Trachea", "Diaphragm"], "correct": "Alveoli", "rationale": "Gas exchange occurs across the alveolar-capillary membrane."},
        {"q": "The 'Hypoxic Drive' is common in patients with:", "options": ["Asthma", "COPD", "Pneumonia", "CHF"], "correct": "COPD", "rationale": "COPD patients may rely on low O2 levels to trigger breathing."},
        {"q": "Stridor is usually heard during:", "options": ["Inspiration", "Expiration", "Between breaths", "During coughing"], "correct": "Inspiration", "rationale": "Stridor is typically an inspiratory sound from upper airway narrowing."},
        {"q": "What is the first step in opening the airway of a non-trauma patient?", "options": ["Jaw-thrust", "Head-tilt, chin-lift", "OPA insertion", "Suctioning"], "correct": "Head-tilt, chin-lift", "rationale": "This is the standard manual maneuver for medical patients."},
        {"q": "CPAP is primarily used to:", "options": ["Provide high-flow oxygen", "Keep alveoli open with pressure", "Replace the need for a BVM", "Suction the airway"], "correct": "Keep alveoli open with pressure", "rationale": "Continuous Positive Airway Pressure helps move fluid out of alveoli."},
        {"q": "What is the concentration of O2 delivered by a nasal cannula at 4L/min?", "options": ["24%", "36%", "44%", "90%"], "correct": "36%", "rationale": "Oxygen increases by roughly 4% for every 1 L/min above room air (21%)."},
        {"q": "When using a BVM, you should deliver one breath every:", "options": ["2-3 seconds", "5-6 seconds", "10 seconds", "12 seconds"], "correct": "5-6 seconds", "rationale": "This provides a rate of 10-12 breaths per minute for an adult."}
    ]

# --- 2. APP LOGIC ---
st.set_page_config(page_title="EMT ARV Quiz", page_icon="🚑", layout="centered")

if 'test_q' not in st.session_state:
    st.session_state.test_q = random.sample(st.session_state.all_q, 20)
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.show_feedback = False

st.title("🚑 EMT Module: ARV Review")
st.write("20 random questions from your study guide. Good luck!")

# Progress tracking
idx = st.session_state.current_index
total = len(st.session_state.test_q)

if idx < total:
    st.progress(idx / total)
    q_item = st.session_state.test_q[idx]
    
    st.subheader(f"Question {idx + 1}")
    st.markdown(f"### {q_item['q']}")
    
    # Selection
    user_answer = st.radio("Select one:", q_item['options'], index=None, key=f"radio_{idx}")
    
    if not st.session_state.show_feedback:
        if st.button("Submit Answer"):
            if user_answer:
                st.session_state.show_feedback = True
                st.rerun()
            else:
                st.warning("Please select an answer.")
    else:
        if user_answer == q_item['correct']:
            st.success(f"**Correct!**")
        else:
            st.error(f"**Incorrect.** The correct answer was: {q_item['correct']}")
        
        st.info(f"**Rationale:** {q_item['rationale']}")
        
        if st.button("Next Question"):
            if user_answer == q_item['correct']:
                st.session_state.score += 1
            st.session_state.current_index += 1
            st.session_state.show_feedback = False
            st.rerun()
else:
    st.balloons()
    st.header("Test Complete!")
    st.metric("Final Score", f"{st.session_state.score} / {total}")
    if st.button("Start New Random Test"):
        del st.session_state.test_q
        st.rerun()