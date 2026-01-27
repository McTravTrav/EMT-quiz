import streamlit as st
import random

# --- 1. THE MASTER QUESTION BANK (70+ QUESTIONS) ---
MASTER_QUESTIONS = [
    # --- ANATOMY & PHYSIOLOGY ---
    {"q": "Which structure is the dividing line between the upper and lower airway?", "options": ["Pharynx", "Larynx", "Trachea", "Carina"], "correct": "Larynx", "rationale": "The larynx (specifically the vocal cords) is the transition point between upper and lower airways."},
    {"q": "What is the primary stimulus for breathing in a healthy patient?", "options": ["Low O2 levels", "High CO2 levels", "Blood pH", "High O2 levels"], "correct": "High CO2 levels", "rationale": "Healthy people breathe based on CO2 levels in the blood/CSF (Hypercarbic Drive)."},
    {"q": "Which nerve innervates the diaphragm?", "options": ["Vagus nerve", "Phrenic nerve", "Sciatic nerve", "Intercostal nerve"], "correct": "Phrenic nerve", "rationale": "The phrenic nerve (C3-C5) controls the diaphragm. Remember: 'C3, 4, 5 keep the diaphragm alive.'"},
    {"q": "Where does gas exchange specifically occur in the lungs?", "options": ["Bronchioles", "Trachea", "Alveoli", "Pleura"], "correct": "Alveoli", "rationale": "Gas exchange occurs at the alveolar-capillary membrane via diffusion."},
    {"q": "What is the function of the epiglottis?", "options": ["Speech production", "Protecting the airway during swallowing", "Triggering coughs", "Filtering air"], "correct": "Protecting the airway during swallowing", "rationale": "It is a leaf-shaped cartilage that covers the glottic opening to prevent aspiration."},
    {"q": "Minute Volume is calculated as:", "options": ["TV + RR", "TV x RR", "TV / RR", "RR - TV"], "correct": "TV x RR", "rationale": "Minute Volume = Tidal Volume multiplied by Respiratory Rate."},
    {"q": "What is 'Dead Space' in the respiratory system?", "options": ["Air that doesn't reach the alveoli", "Air left after max exhalation", "Air in a pneumothorax", "Air inside a BVM"], "correct": "Air that doesn't reach the alveoli", "rationale": "Dead space is air in the trachea/bronchi where no gas exchange occurs."},
    
    # --- ASSESSMENT & SOUNDS ---
    {"q": "A high-pitched, whistling sound heard on inhalation is called:", "options": ["Wheezing", "Rales", "Stridor", "Rhonchi"], "correct": "Stridor", "rationale": "Stridor indicates a partial upper airway obstruction."},
    {"q": "A 'Gurgling' sound in the airway indicates:", "options": ["Tongue obstruction", "Fluid in the airway", "Bronchoconstriction", "Normal breathing"], "correct": "Fluid in the airway", "rationale": "Gurgling is air moving through liquid; it is an immediate indication for suctioning."},
    {"q": "Wheezing is a sound most commonly associated with:", "options": ["Upper airway obstruction", "Fluid in the alveoli", "Lower airway bronchoconstriction", "Aspiration"], "correct": "Lower airway bronchoconstriction", "rationale": "Wheezing is air whistling through narrowed bronchioles (Asthma/COPD)."},
    
    # --- ADJUNCTS & SUCTION ---
    {"q": "To properly size an OPA, you measure from the corner of the mouth to the:", "options": ["Tip of the nose", "Center of the chin", "Angle of the jaw (earlobe)", "Sternal notch"], "correct": "Angle of the jaw (earlobe)", "rationale": "Correct sizing ensures the OPA reaches the pharynx correctly."},
    {"q": "What is the main contraindication for an OPA?", "options": ["Head injury", "Intact gag reflex", "Facial trauma", "Basilar skull fracture"], "correct": "Intact gag reflex", "rationale": "An OPA will cause vomiting and aspiration if a gag reflex is present."},
    {"q": "What is the main contraindication for an NPA?", "options": ["Gag reflex", "Basilar skull fracture", "Unconsciousness", "Asthma"], "correct": "Basilar skull fracture", "rationale": "Risk of intracranial placement through a skull fracture."},
    {"q": "What is the maximum suction time for an adult patient?", "options": ["5 seconds", "10 seconds", "15 seconds", "30 seconds"], "correct": "15 seconds", "rationale": "Suctioning removes oxygen; limiting to 15 seconds prevents severe hypoxia."},
    {"q": "When suctioning a patient, you should only apply suction:", "options": ["On the way in", "On the way out (withdrawing)", "While holding still", "For 30 seconds"], "correct": "On the way out (withdrawing)", "rationale": "This minimizes the time the patient is without oxygen."},
    
    # --- OXYGEN & VENTILATION ---
    {"q": "A non-rebreather mask (NRB) should be set to:", "options": ["1-6 L/min", "6-10 L/min", "10-15 L/min", "15-25 L/min"], "correct": "10-15 L/min", "rationale": "This flow rate keeps the reservoir bag inflated with 100% oxygen."},
    {"q": "Which mask delivers a precise FiO2?", "options": ["NRB", "Nasal Cannula", "Venturi Mask", "Simple Mask"], "correct": "Venturi Mask", "rationale": "The Venturi mask uses adapters to deliver specific, precise oxygen percentages."},
    {"q": "The 'E-C' grip is used for:", "options": ["Holding a nasal cannula", "Checking a pulse", "Maintaining a BVM seal", "Measuring an OPA"], "correct": "Maintaining a BVM seal", "rationale": "The 'E' fingers pull the jaw up, and the 'C' fingers hold the mask down."},
    {"q": "Positive Pressure Ventilation (PPV) can cause:", "options": ["Increased venous return", "Hypotension", "Improved cardiac output", "Decreased gastric pressure"], "correct": "Hypotension", "rationale": "Increased pressure in the chest compresses the vena cava, reducing blood return to the heart."},
    {"q": "The 'O' in DOPE stands for:", "options": ["Oxygen", "Obstruction", "Output", "Over-ventilation"], "correct": "Obstruction", "rationale": "Obstruction (like a mucus plug) is a common failure in tracheostomies."},
    
    # --- CPAP & SCENARIOS ---
    {"q": "What is the primary effect of CPAP?", "options": ["Decrease RR", "Opening collapsed alveoli", "Suctioning mucus", "Increasing pulse"], "correct": "Opening collapsed alveoli", "rationale": "CPAP uses pressure to keep alveoli open at the end of exhalation."},
    {"q": "Which is a strict contraindication for CPAP?", "options": ["Pulmonary edema", "Pneumothorax", "Asthma", "COPD"], "correct": "Pneumothorax", "rationale": "Positive pressure can turn a pneumothorax into a tension pneumothorax."},
    {"q": "When ventilating a stoma patient, air escapes from the mouth. You should:", "options": ["Increase pressure", "Seal the mouth and nose", "Stop ventilating", "Turn them on their side"], "correct": "Seal the mouth and nose", "rationale": "You must seal the upper airway to ensure air goes from the stoma to the lungs."},
    {"q": "A patient is breathing 4 times per minute. You should:", "options": ["Use an NRB", "Use a Nasal Cannula", "Provide BVM ventilation", "Monitor only"], "correct": "Provide BVM ventilation", "rationale": "A rate of 4 is respiratory failure and requires immediate ventilation support."},
    {"q": "What happens to chest pressure during inhalation?", "options": ["Positive", "Negative", "Neutral", "Double"], "correct": "Negative", "rationale": "The chest expands, creating negative pressure (a vacuum) to pull air in."}
]

# --- 2. INITIALIZATION ---
if 'test_q' not in st.session_state:
    # Shuffle and pick 20
    st.session_state.test_q = random.sample(MASTER_QUESTIONS, min(len(MASTER_QUESTIONS), 20))
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.show_review = False

# --- 3. UI LAYOUT ---
st.set_page_config(page_title="EMT ARV Review", page_icon="🚑")
st.title("🚑 EMT ARV Module Review")
st.write("20 Random Questions • Interactive Study Guide")

idx = st.session_state.current_index
total = len(st.session_state.test_q)

if idx < total:
    st.progress(idx / total)
    q_item = st.session_state.test_q[idx]
    
    st.subheader(f"Question {idx + 1} of {total}")
    st.markdown(f"### {q_item['q']}")
    
    user_choice = st.radio("Select the correct answer:", q_item['options'], index=None, key=f"q_{idx}")

    if not st.session_state.show_review:
        if st.button("Submit Answer"):
            if user_choice:
                st.session_state.show_review = True
                st.rerun()
            else:
                st.warning("Please select an option.")
    else:
        if user_choice == q_item['correct']:
            st.success("**Correct!**")
        else:
            st.error(f"**Incorrect.** The correct answer was: {q_item['correct']}")
        
        st.info(f"**Review/Rationale:** {q_item['rationale']}")
        
        if st.button("Next Question →"):
            if user_choice == q_item['correct']:
                st.session_state.score += 1
            st.session_state.current_index += 1
            st.session_state.show_review = False
            st.rerun()

else:
    st.balloons()
    st.header("🏁 Quiz Complete!")
    score = st.session_state.score
    st.metric("Final Score", f"{score} / {total}", f"{(score/total)*100:.1f}%")
    
    if st.button("Start New Random Test"):
        del st.session_state.test_q
        st.rerun()