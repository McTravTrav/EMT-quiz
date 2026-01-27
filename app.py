import streamlit as st
import random

# --- 1. THE FULL 70-QUESTION MASTER BANK ---
# Ensure you have your full list of 70 questions here.
MASTER_QUESTIONS = [
    # --- DOPE MNEMONIC BREAKDOWN ---
    {"q": "In the DOPE mnemonic for tracheostomy trouble, what does the 'D' stand for?", "options": ["Dyspnea", "Dislodgement", "Distension", "Diffusion"], "correct": "Dislodgement", "rationale": "D stands for Dislodgement: The tube has come out of the trachea."},
    {"q": "In the DOPE mnemonic for tracheostomy trouble, what does the 'O' stand for?", "options": ["Oxygenation", "Obstruction", "Output", "Over-ventilation"], "correct": "Obstruction", "rationale": "O stands for Obstruction: Often a mucus plug blocking the tube."},
    {"q": "In the DOPE mnemonic for tracheostomy trouble, what does the 'P' stand for?", "options": ["Pneumonia", "Pulse", "Pneumothorax", "Pressure"], "correct": "Pneumothorax", "rationale": "P stands for Pneumothorax: A collapsed lung is a common complication."},
    {"q": "In the DOPE mnemonic for tracheostomy trouble, what does the 'E' stand for?", "options": ["Edema", "Emergency", "Equipment Failure", "Effort"], "correct": "Equipment Failure", "rationale": "E stands for Equipment Failure: Kinked hoses or empty oxygen tanks."},

    # --- ANATOMY & PHYSIOLOGY ---
    {"q": "What structure is the dividing line between the upper and lower airway?", "options": ["Pharynx", "Larynx", "Trachea", "Carina"], "correct": "Larynx", "rationale": "The larynx (vocal cords) is the transition point between upper and lower airways."},
    {"q": "Which nerve innervates the diaphragm?", "options": ["Vagus", "Phrenic", "Glossopharyngeal", "Intercostal"], "correct": "Phrenic", "rationale": "The phrenic nerve (C3-C5) controls the diaphragm."},
    {"q": "What is the primary stimulus for breathing in a healthy patient?", "options": ["Low O2", "High CO2", "Blood pH", "High O2"], "correct": "High CO2", "rationale": "Healthy people breathe based on Carbon Dioxide levels (Hypercarbic Drive)."},
    {"q": "Where does gas exchange specifically occur?", "options": ["Bronchioles", "Trachea", "Alveoli", "Pleura"], "correct": "Alveoli", "rationale": "Exchange occurs at the alveolar-capillary membrane."},
    {"q": "What is the function of the epiglottis?", "options": ["Speech", "Protecting the airway during swallowing", "Coughing", "Filtering"], "correct": "Protecting the airway during swallowing", "rationale": "It prevents food/liquid from entering the trachea."},
    {"q": "What happens to chest pressure during inhalation?", "options": ["Positive", "Negative", "Neutral", "Stays the same"], "correct": "Negative", "rationale": "Chest expansion creates a vacuum (negative pressure) to pull air in."},
    {"q": "What is 'Dead Space'?", "options": ["Air not reaching alveoli", "Air left after max exhalation", "Air in a pneumothorax", "BVM air"], "correct": "Air not reaching alveoli", "rationale": "Dead space is the volume of air that occupies the non-exchange parts of the lungs (trachea/bronchi)."},

    # --- ASSESSMENT & AIRWAY SOUNDS ---
    {"q": "A high-pitched, whistling sound on inhalation is:", "options": ["Wheezing", "Stridor", "Rales", "Rhonchi"], "correct": "Stridor", "rationale": "Stridor indicates a partial upper airway obstruction."},
    {"q": "A 'Gurgling' sound in the airway indicates:", "options": ["Tongue obstruction", "Fluid (blood/vomit)", "Bronchospasm", "Asthma"], "correct": "Fluid (blood/vomit)", "rationale": "Gurgling means liquid is present and requires immediate suctioning."},
    {"q": "Wheezing is associated with:", "options": ["Upper airway obstruction", "Fluid in alveoli", "Lower airway bronchoconstriction", "Aspiration"], "correct": "Lower airway bronchoconstriction", "rationale": "Wheezing is air whistling through narrowed lower bronchioles."},
    {"q": "Rales (crackles) usually indicate:", "options": ["Fluid in the lower airways/alveoli", "Tongue obstruction", "Asthma", "Foreign body"], "correct": "Fluid in the lower airways/alveoli", "rationale": "Crackles are usually heard in patients with CHF or pneumonia."},

    # --- ADJUNCTS & SUCTIONING ---
    {"q": "How do you size an OPA for an adult?", "options": ["Nose to earlobe", "Corner of mouth to earlobe", "Nose to chin", "Corner of mouth to suprasternal notch"], "correct": "Corner of mouth to earlobe", "rationale": "Correct sizing ensures the curve fits the anatomy properly."},
    {"q": "What is the main contraindication for an OPA?", "options": ["Head injury", "Gag reflex", "Facial trauma", "Skull fracture"], "correct": "Gag reflex", "rationale": "An OPA will cause vomiting if the gag reflex is present."},
    {"q": "How do you size an NPA?", "options": ["Mouth to earlobe", "Tip of nose to earlobe", "Nose to chin", "Nose to notch"], "correct": "Tip of nose to earlobe", "rationale": "NPA size is measured from the nares to the earlobe or angle of the jaw."},
    {"q": "Max suction time for an adult is:", "options": ["5 sec", "10 sec", "15 sec", "30 sec"], "correct": "15 sec", "rationale": "Suctioning removes oxygen; limit to 15s to prevent hypoxia."},
    {"q": "Suction is applied only when:", "options": ["Inserting the catheter", "Withdrawing the catheter", "Catheter is stationary", "Continuously"], "correct": "Withdrawing the catheter", "rationale": "Apply suction in a circular motion while withdrawing the tip."},

    # --- OXYGEN & VENTILATION ---
    {"q": "NRB mask flow rate should be:", "options": ["1-6 L/min", "6-10 L/min", "10-15 L/min", "15-25 L/min"], "correct": "10-15 L/min", "rationale": "10-15L keeps the reservoir bag inflated."},
    {"q": "Which mask delivers precise FiO2?", "options": ["NRB", "Nasal Cannula", "Venturi Mask", "Simple Mask"], "correct": "Venturi Mask", "rationale": "Venturi masks allow for precise oxygen percentages for COPD patients."},
    {"q": "What is a danger of CPAP?", "options": ["Hypotension", "Hypertension", "Hyperglycemia", "Bradycardia"], "correct": "Hypotension", "rationale": "Positive pressure can reduce venous return, causing blood pressure to drop."},
    {"q": "One breath every ____ seconds for an adult BVM?", "options": ["2-3", "5-6", "10-12", "15-20"], "correct": "5-6", "rationale": "10-12 breaths per minute is standard for adult rescue breathing."},
    {"q": "The 'E-C' grip is for:", "options": ["Pulse check", "BVM seal", "NPA sizing", "Nasal cannula"], "correct": "BVM seal", "rationale": "The E-C grip ensures a tight mask-to-face seal."},

    # --- SPECIAL SCENARIOS ---
    {"q": "When ventilating a stoma, you should:", "options": ["Use a pediatric mask over the stoma", "Use an adult mask over the mouth", "Use a nasal cannula", "Avoid BVM"], "correct": "Use a pediatric mask over the stoma", "rationale": "A pediatric mask often fits better over the stoma site than an adult mask."},
    {"q": "The 'Hypoxic Drive' is common in:", "options": ["Asthma", "COPD", "Anaphylaxis", "Cardiac arrest"], "correct": "COPD", "rationale": "COPD patients may rely on low oxygen levels to trigger breathing."},
    {"q": "Which maneuver is used for trauma patients?", "options": ["Head-tilt, chin-lift", "Jaw-thrust", "Neck-roll", "Finger-sweep"], "correct": "Jaw-thrust", "rationale": "The jaw-thrust opens the airway without moving the cervical spine."},
    {"q": "A conscious patient with Pulmonary Edema should get:", "options": ["Nasal Cannula", "CPAP", "BVM", "Simple Mask"], "correct": "CPAP", "rationale": "CPAP helps push fluid out of the alveoli in pulmonary edema."},
    {"q": "Minute Volume calculation is:", "options": ["TV x RR", "TV + RR", "TV / RR", "RR - TV"], "correct": "TV x RR", "rationale": "Minute Volume = Tidal Volume x Respiratory Rate."}
]


# --- 2. THE SMART SHUFFLE ENGINE ---
def initialize_quiz():
    full_list = list(MASTER_QUESTIONS)
    random.shuffle(full_list)
    st.session_state.master_pool = full_list
    st.session_state.current_test = full_list[:20]
    st.session_state.remaining_pool = full_list[20:]
    st.session_state.current_index = 0
    st.session_state.score = 0
    st.session_state.show_review = False
    st.session_state.missed_questions = [] # Track wrong answers

if 'master_pool' not in st.session_state:
    initialize_quiz()

# --- 3. UI LAYOUT ---
st.set_page_config(page_title="EMT ARV Master Review", page_icon="🚑")
st.title("🚑 EMT ARV Master Review")
st.sidebar.header("Progress Tracker")
st.sidebar.write(f"Questions left in bank: **{len(st.session_state.remaining_pool)}**")
st.sidebar.write(f"Questions missed so far: **{len(st.session_state.missed_questions)}**")

idx = st.session_state.current_index
total = len(st.session_state.current_test)

if idx < total:
    st.progress(idx / total)
    q_item = st.session_state.current_test[idx]
    
    st.subheader(f"Question {idx + 1} of {total}")
    st.markdown(f"### {q_item['q']}")
    
    user_choice = st.radio("Select the correct answer:", q_item['options'], index=None, key=f"q_{idx}")

    if not st.session_state.get('show_review', False):
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
            # Add to missed list if it's not already there
            if q_item not in st.session_state.missed_questions:
                st.session_state.missed_questions.append(q_item)
        
        st.info(f"**Rationale:** {q_item['rationale']}")
        
        if st.button("Next Question →"):
            if user_choice == q_item['correct']:
                st.session_state.score += 1
            st.session_state.current_index += 1
            st.session_state.show_review = False
            st.rerun()

else:
    # --- END OF SET LOGIC ---
    st.balloons()
    st.header("🏁 Set Complete!")
    st.metric("Set Score", f"{st.session_state.score} / {total}")
    
    # Show missed questions for review
    if st.session_state.missed_questions:
        with st.expander("📝 Review Your Missed Questions"):
            for m in st.session_state.missed_questions:
                st.write(f"**Q:** {m['q']}")
                st.write(f"**Correct Answer:** {m['correct']}")
                st.write(f"**Rationale:** {m['rationale']}")
                st.write("---")

    if len(st.session_state.remaining_pool) > 0:
        next_batch_size = min(len(st.session_state.remaining_pool), 20)
        if st.button(f"Start Next {next_batch_size} Unique Questions"):
            new_pool = st.session_state.remaining_pool
            st.session_state.current_test = new_pool[:next_batch_size]
            st.session_state.remaining_pool = new_pool[next_batch_size:]
            st.session_state.current_index = 0
            st.session_state.score = 0
            st.session_state.show_review = False
            st.rerun()
    else:
        st.success("You have completed the entire question bank!")
        if st.button("Reshuffle and Restart Everything"):
            initialize_quiz()
            st.rerun()