import streamlit as st
import random

# --- 1. THE VERIFIED QUESTION BANK (48 Questions) ---
# Strictly based on your Fall 2025 EMT ARV Study Guide
MASTER_QUESTIONS = [
    # --- ANATOMY & PHYSIOLOGY ---
    {"q": "Which structure is the dividing line between the upper and lower airway?", "options": ["Pharynx", "Larynx", "Trachea", "Carina"], "correct": "Larynx", "rationale": "The larynx (vocal cords) is the transition point. Above is upper, below is lower."},
    {"q": "The phrenic nerve controls the diaphragm. Where does it exit the spine?", "options": ["C1-C2", "C3-C5", "T1-T4", "L1-L2"], "correct": "C3-C5", "rationale": "REMEMBER: 'C3, 4, and 5 keep the diaphragm alive.'"},
    {"q": "What is the leaf-shaped cartilage that prevents aspiration?", "options": ["Cricoid", "Epiglottis", "Carina", "Thyroid"], "correct": "Epiglottis", "rationale": "It covers the glottic opening during swallowing to protect the trachea."},
    {"q": "Where does gas exchange specifically occur?", "options": ["Bronchi", "Alveoli", "Trachea", "Pleura"], "correct": "Alveoli", "rationale": "Diffusion of O2 and CO2 happens at the alveolar-capillary membrane."},
    {"q": "The primary drive to breathe is based on levels of:", "options": ["Oxygen", "Carbon Dioxide", "pH", "Glucose"], "correct": "Carbon Dioxide", "rationale": "The brain monitors CO2 levels in the CSF (Hypercarbic Drive)."},
    {"q": "The 'Hypoxic Drive' is found in late-stage:", "options": ["Asthma", "COPD", "Pneumonia", "CHF"], "correct": "COPD", "rationale": "These patients rely on low oxygen levels to trigger breathing."},
    {"q": "What happens to chest pressure during inhalation?", "options": ["Becomes Positive", "Becomes Negative", "Stays Neutral", "Doubles"], "correct": "Becomes Negative", "rationale": "The diaphragm drops, creating a vacuum (negative pressure) to pull air in."},
    {"q": "What is 'Dead Space'?", "options": ["Air not reaching alveoli", "Air left after exhalation", "Air in a pneumothorax", "BVM volume"], "correct": "Air not reaching alveoli", "rationale": "Air in the trachea/bronchi that does not participate in gas exchange."},
    {"q": "Minute Volume is calculated as:", "options": ["TV + RR", "TV x RR", "TV / RR", "RR - TV"], "correct": "TV x RR", "rationale": "Tidal Volume x Respiratory Rate = Minute Volume."},

    # --- ASSESSMENT & SOUNDS ---
    {"q": "A high-pitched whistling sound on inhalation is:", "options": ["Wheezing", "Stridor", "Rales", "Rhonchi"], "correct": "Stridor", "rationale": "Indicates upper airway obstruction (e.g., croup, foreign body)."},
    {"q": "Wheezing typically indicates:", "options": ["Upper airway obstruction", "Lower airway constriction", "Fluid in lungs", "Tongue blockage"], "correct": "Lower airway constriction", "rationale": "Air whistling through narrowed bronchioles (Asthma/COPD)."},
    {"q": "Gurgling sounds indicate:", "options": ["Fluid in the airway", "Tongue obstruction", "Swelling", "Normal breathing"], "correct": "Fluid in the airway", "rationale": "Immediate need for suctioning."},
    {"q": "Snoring sounds usually indicate:", "options": ["Fluid", "Tongue obstruction", "Bronchospasm", "Infection"], "correct": "Tongue obstruction", "rationale": "The tongue has fallen back against the pharynx."},
    {"q": "Cyanosis (blue skin) is a late sign of:", "options": ["High CO2", "Hypoxia", "Low blood sugar", "Shock"], "correct": "Hypoxia", "rationale": "Significant lack of oxygen in the blood."},

    # --- SUCTIONING & ADJUNCTS ---
    {"q": "Max suction time for an adult:", "options": ["5 sec", "10 sec", "15 sec", "20 sec"], "correct": "15 sec", "rationale": "To prevent hypoxia."},
    {"q": "Max suction time for a child:", "options": ["5 sec", "10 sec", "15 sec", "20 sec"], "correct": "10 sec", "rationale": "Children have less oxygen reserve."},
    {"q": "Max suction time for an infant:", "options": ["5 sec", "10 sec", "15 sec", "20 sec"], "correct": "5 sec", "rationale": "Infants desaturate extremely fast."},
    {"q": "How do you size an OPA?", "options": ["Corner of mouth to angle of the jaw", "Tip of nose to earlobe", "Center of nose to jaw", "Nose to chin"], "correct": "Corner of mouth to angle of the jaw", "rationale": "Or center of mouth to angle of jaw."},
    {"q": "Contraindication for an OPA:", "options": ["Gag reflex", "No teeth", "Skull fracture", "Fluid in airway"], "correct": "Gag reflex", "rationale": "It will cause vomiting and aspiration."},
    {"q": "How do you size an NPA?", "options": ["Corner of mouth to earlobe", "Tip of nose to earlobe", "Center of mouth to jaw", "Nose to chin"], "correct": "Tip of nose to earlobe", "rationale": "Measure from the nostril to the earlobe/angle of jaw."},
    {"q": "Contraindication for an NPA:", "options": ["Gag reflex", "Basilar skull fracture", "Seizure", "Stroke"], "correct": "Basilar skull fracture", "rationale": "Risk of pushing the tube into the brain."},
    {"q": "Suction should be applied:", "options": ["On insertion", "On withdrawal", "Continuously", "Intermittently"], "correct": "On withdrawal", "rationale": "Insert without suction, suction while pulling out."},

    # --- OXYGEN THERAPY ---
    {"q": "FiO2 of Room Air is approx:", "options": ["16%", "21%", "50%", "100%"], "correct": "21%", "rationale": "The atmosphere is ~21% oxygen."},
    {"q": "Nasal Cannula flow range:", "options": ["1-6 LPM", "6-10 LPM", "10-15 LPM", "15-25 LPM"], "correct": "1-6 LPM", "rationale": "Delivers 24-44% oxygen."},
    {"q": "Non-Rebreather (NRB) flow rate:", "options": ["6-10 LPM", "10-15 LPM", "1-6 LPM", "25 LPM"], "correct": "10-15 LPM", "rationale": "Must be high enough to keep the reservoir bag inflated."},
    {"q": "Venturi Mask is best for:", "options": ["Trauma", "COPD", "Cardiac Arrest", "Shock"], "correct": "COPD", "rationale": "It delivers a precise, fixed concentration of oxygen."},
    {"q": "BVM with reservoir delivers approx:", "options": ["21%", "50%", "80%", "Nearly 100%"], "correct": "Nearly 100%", "rationale": "High flow O2 + reservoir bag = max oxygenation."},

    # --- VENTILATION ---
    {"q": "Adult ventilation rate (BVM):", "options": ["Every 3 sec", "Every 5-6 sec", "Every 10 sec", "Every 1 sec"], "correct": "Every 5-6 sec", "rationale": "10-12 breaths per minute."},
    {"q": "Child/Infant ventilation rate (BVM):", "options": ["Every 3-5 sec", "Every 6-8 sec", "Every 10 sec", "Every 2 sec"], "correct": "Every 3-5 sec", "rationale": "12-20 breaths per minute."},
    {"q": "Gastric distension is caused by:", "options": ["Ventilating too fast/hard", "Using an OPA", "Suctioning", "Using a cannula"], "correct": "Ventilating too fast/hard", "rationale": "Air enters the stomach instead of lungs."},
    {"q": "Best indicator of effective ventilation:", "options": ["Chest rise", "SpO2 increases", "Skin color improves", "Normal HR"], "correct": "Chest rise", "rationale": "Visible chest rise is the immediate sign of success."},
    {"q": "Sellick Maneuver (Cricoid Pressure) prevents:", "options": ["Gastric distension", "Vomiting", "Hypoxia", "Aspiration"], "correct": "Gastric distension", "rationale": "Compresses the esophagus (though rarely used now, it's in the curriculum)."},

    # --- CPAP & ADVANCED ---
    {"q": "CPAP stands for:", "options": ["Continuous Positive Airway Pressure", "Constant Pulmonary Airway Pressure", "Cardiopulmonary Airway Pressure", "None of these"], "correct": "Continuous Positive Airway Pressure", "rationale": "Used to keep alveoli open."},
    {"q": "Primary indication for CPAP:", "options": ["Apnea", "Pulmonary Edema/CHF", "Pneumothorax", "Trauma"], "correct": "Pulmonary Edema/CHF", "rationale": "Pushes fluid out of alveoli to improve gas exchange."},
    {"q": "Strict contraindication for CPAP:", "options": ["Hypotension (Low BP)", "Hypertension", "Tachypnea", "Low O2"], "correct": "Hypotension (Low BP)", "rationale": "CPAP increases chest pressure, which drops BP further."},
    {"q": "How do you ventilate a stoma patient?", "options": ["Mask over mouth", "Mask over stoma", "Nasal cannula", "Do not ventilate"], "correct": "Mask over stoma", "rationale": "Use a pediatric mask for a better seal on the neck."},
    {"q": "If air escapes the mouth during stoma ventilation:", "options": ["Seal mouth and nose", "Press harder", "Suction stoma", "Stop"], "correct": "Seal mouth and nose", "rationale": "You must create a closed circuit."},

    # --- DOPE MNEMONIC ---
    {"q": "DOPE: 'D' stands for:", "options": ["Dislodgement", "Death", "Distension", "Drugs"], "correct": "Dislodgement", "rationale": "Tube has moved out of position."},
    {"q": "DOPE: 'O' stands for:", "options": ["Oxygen", "Obstruction", "Overdose", "Output"], "correct": "Obstruction", "rationale": "Mucus/secretions blocking the tube."},
    {"q": "DOPE: 'P' stands for:", "options": ["Pneumonia", "Pneumothorax", "Pulse", "Pain"], "correct": "Pneumothorax", "rationale": "Collapsed lung."},
    {"q": "DOPE: 'E' stands for:", "options": ["Edema", "Embolism", "Equipment", "Energy"], "correct": "Equipment", "rationale": "Check oxygen source and tubing."},
    
    # --- SCENARIOS ---
    {"q": "Patient is breathing 4 times/min. Treatment?", "options": ["NRB", "Cannula", "BVM (Ventilation)", "Monitor"], "correct": "BVM (Ventilation)", "rationale": "Rate of 4 is respiratory failure; they need breathing done for them."},
    {"q": "Patient is gurgling. First step?", "options": ["Ventilate", "Suction", "Oxygen", "CPR"], "correct": "Suction", "rationale": "Clear the airway before anything else."},
    {"q": "Trauma patient airway maneuver?", "options": ["Head-tilt chin-lift", "Jaw-thrust", "Neck lift", "Trendelenburg"], "correct": "Jaw-thrust", "rationale": "Protects the cervical spine."},
    {"q": "Patient with pulmonary edema, conscious, BP 140/90. Device?", "options": ["CPAP", "BVM", "NRB", "Cannula"], "correct": "CPAP", "rationale": "Ideal candidate: awake, fluid in lungs, stable BP."},
    {"q": "The 'E-C' clamp technique is used for:", "options": ["Holding a mask seal", "Checking a pulse", "Sizing an OPA", "Holding a nebulizer"], "correct": "Holding a mask seal", "rationale": "Thumbs/Index (C) on mask, other fingers (E) on jaw."}
]

# --- 2. INITIALIZATION LOGIC (THE FIX) ---
def initialize_quiz():
    # 1. Randomize the ENTIRE list
    full_deck = list(MASTER_QUESTIONS)
    random.shuffle(full_deck)
    
    # 2. Store in session
    st.session_state.master_deck = full_deck
    st.session_state.batch_index = 0
    st.session_state.score = 0
    
    # 3. Pull the first 20 (or less if list is short)
    st.session_state.current_batch = full_deck[:20]
    st.session_state.current_q_index = 0
    st.session_state.show_review = False
    st.session_state.missed_q = []

if 'master_deck' not in st.session_state:
    initialize_quiz()

# --- 3. UI & PROGRESS ---
total_in_deck = len(st.session_state.master_deck)

st.set_page_config(page_title="EMT ARV Review", page_icon="🚑")
st.title("🚑 EMT ARV Module Review")

# Calculate progress
current_q_global = st.session_state.batch_index + st.session_state.current_q_index
st.progress(min(current_q_global / total_in_deck, 1.0))
st.caption(f"Total Progress: {min(current_q_global, total_in_deck)} / {total_in_deck}")

# --- 4. QUESTION DISPLAY ---
batch_q = st.session_state.current_batch
q_idx = st.session_state.current_q_index

if q_idx < len(batch_q):
    item = batch_q[q_idx]
    
    st.subheader(f"Question {q_idx + 1} of {len(batch_q)} (in this batch)")
    st.markdown(f"### {item['q']}")
    
    # Unique key for every single question instance
    choice = st.radio("Select Answer:", item['options'], index=None, key=f"q_{st.session_state.batch_index}_{q_idx}")

    if not st.session_state.show_review:
        if st.button("Submit Answer"):
            if choice:
                st.session_state.show_review = True
                st.rerun()
            else:
                st.warning("Pick an answer!")
    else:
        if choice == item['correct']:
            st.success("**Correct!**")
        else:
            st.error(f"**Incorrect.** The answer is {item['correct']}")
            if item not in st.session_state.missed_q:
                st.session_state.missed_q.append(item)
        
        st.info(f"**Rationale:** {item['rationale']}")
        
        if st.button("Next Question →"):
            if choice == item['correct']:
                st.session_state.score += 1
            st.session_state.current_q_index += 1
            st.session_state.show_review = False
            st.rerun()

else:
    # --- END OF BATCH SCREEN ---
    st.balloons()
    st.header("Batch Complete!")
    st.write(f"Score for this batch: {st.session_state.score} / {len(batch_q)}")
    
    # Check if there are more questions in the master deck
    next_start = st.session_state.batch_index + 20
    
    if next_start < total_in_deck:
        remaining = total_in_deck - next_start
        st.info(f"There are still {remaining} unseen questions in the bank.")
        # Button text changes based on how many are left
        btn_text = f"Load Next {min(remaining, 20)} Questions"
        
        if st.button(btn_text):
            # Move markers forward
            st.session_state.batch_index = next_start
            # Slice the next batch (handles the end of list automatically)
            st.session_state.current_batch = st.session_state.master_deck[next_start : next_start + 20]
            # Reset batch-specific counters
            st.session_state.current_q_index = 0
            st.session_state.score = 0
            st.session_state.show_review = False
            st.rerun()
    else:
        st.success("🎉 You have finished the ENTIRE question bank!")
        
        if st.session_state.missed_q:
            with st.expander("Review Missed Questions"):
                for m in st.session_state.missed_q:
                    st.write(f"- **{m['q']}**")
                    st.write(f"  - Correct: {m['correct']}")
                    st.write(f"  - Note: {m['rationale']}")
                    
        if st.button("Reshuffle & Restart From Beginning"):
            initialize_quiz()

            st.rerun()
