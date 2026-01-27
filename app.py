import streamlit as st
import random

# --- 1. THE MASTER QUESTION BANK ---
# Add all 70+ questions into this list.
MASTER_QUESTIONS = [
    {"q": "Which structure is the dividing line between the upper and lower airway?", "options": ["Pharynx", "Larynx", "Trachea", "Carina"], "correct": "Larynx", "rationale": "The larynx (specifically the vocal cords) is the transition point between upper and lower airways."},
    {"q": "What is the primary stimulus for breathing in a healthy patient?", "options": ["Low O2 levels", "High CO2 levels", "Blood pH", "High O2 levels"], "correct": "High CO2 levels", "rationale": "Healthy people breathe based on CO2 levels in the blood/CSF (Hypercarbic Drive)."},
    {"q": "To properly size an OPA, you measure from the corner of the mouth to the:", "options": ["Tip of the nose", "Center of the chin", "Angle of the jaw (earlobe)", "Suprasternal notch"], "correct": "Angle of the jaw (earlobe)", "rationale": "Correct sizing ensures the OPA reaches the pharynx without causing trauma."},
    {"q": "A high-pitched, whistling sound heard on inhalation is called:", "options": ["Wheezing", "Rales", "Stridor", "Rhonchi"], "correct": "Stridor", "rationale": "Stridor indicates a partial upper airway obstruction."},
    {"q": "What is the maximum suction time for an adult patient?", "options": ["5 seconds", "10 seconds", "15 seconds", "30 seconds"], "correct": "15 seconds", "rationale": "Suctioning removes oxygen; limiting to 15 seconds prevents severe hypoxia."},
    {"q": "Which nerve innervates the diaphragm?", "options": ["Vagus nerve", "Phrenic nerve", "Sciatic nerve", "Intercostal nerve"], "correct": "Phrenic nerve", "rationale": "The phrenic nerve (C3-C5) controls the diaphragm."},
    {"q": "What is the site of gas exchange in the lungs?", "options": ["Bronchi", "Bronchioles", "Alveoli", "Pleura"], "correct": "Alveoli", "rationale": "Gas exchange occurs at the alveolar-capillary membrane."},
    {"q": "The 'O' in DOPE stands for:", "options": ["Oxygen", "Obstruction", "Output", "Over-ventilation"], "correct": "Obstruction", "rationale": "Obstruction (like a mucus plug) is a common trach tube failure."},
    {"q": "Minute Volume is calculated as:", "options": ["TV + RR", "TV x RR", "TV / RR", "RR - TV"], "correct": "TV x RR", "rationale": "Minute Volume = Tidal Volume x Respiratory Rate."},
    {"q": "Which mask delivers a precise FiO2?", "options": ["NRB", "Nasal Cannula", "Venturi Mask", "Simple Mask"], "correct": "Venturi Mask", "rationale": "The Venturi mask uses adapters to deliver specific oxygen percentages."},
    # Add your remaining questions here following this same format!
]

# --- 2. INITIALIZATION LOGIC ---
# This block runs only when the app starts or 'test_q' is deleted.
if 'test_q' not in st.session_state:
    # This line handles the "Random 20" requirement
    st.session_state.test_q = random.sample(MASTER_QUESTIONS, min(len(MASTER_QUESTIONS), 20))
    st.session_state.current_idx = 0
    st.session_state.score = 0
    st.session_state.answered = False

# --- 3. APP UI ---
st.set_page_config(page_title="EMT ARV Quiz", page_icon="🚑")
st.title("🚑 EMT ARV Module Review")
st.write("20 Random Questions per test. Immediate review after each answer.")

# Progress 
idx = st.session_state.current_idx
total = len(st.session_state.test_q)

if idx < total:
    st.progress(idx / total)
    q = st.session_state.test_q[idx]
    
    st.subheader(f"Question {idx + 1} of {total}")
    st.markdown(f"### {q['q']}")
    
    # Selection
    user_choice = st.radio("Select the best answer:", q['options'], index=None, key=f"q_{idx}")
    
    # Review Logic
    if not st.session_state.answered:
        if st.button("Submit Answer"):
            if user_choice:
                st.session_state.answered = True
                st.rerun()
            else:
                st.warning("Please select an answer.")
    else:
        # Show Feedback/Review
        if user_choice == q['correct']:
            st.success("**Correct!**")
        else:
            st.error(f"**Incorrect.** The correct answer was: {q['correct']}")
        
        st.info(f"**Review:** {q['rationale']}")
        
        if st.button("Next Question →"):
            if user_choice == q['correct']:
                st.session_state.score += 1
            st.session_state.current_idx += 1
            st.session_state.answered = False
            st.rerun()
else:
    # --- FINAL RESULTS ---
    st.balloons()
    st.header("🏁 Quiz Complete!")
    final_score = st.session_state.score
    st.metric("Your Final Score", f"{final_score} / {total}", f"{(final_score/total)*100:.1f}%")
    
    if st.button("Take a New Random Test"):
        # Clearing state forces the "random.sample" to run again on refresh
        del st.session_state.test_q
        st.rerun()