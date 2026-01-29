import streamlit as st
import random

# --- 1. THE CONSOLIDATED MASTER QUESTION BANK (88 QUESTIONS) ---
MASTER_QUESTIONS = [
    # --- ANATOMY & PHYSIOLOGY (FROM STUDY GUIDE) ---
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
    {"q": "How do you size an OPA?", "options": ["Corner of mouth to nose", "Tip of nose to earlobe", "Center of mouth to angle of jaw", "Nose to chin"], "correct": "Corner of mouth to angle of jaw", "rationale": "Or center of mouth to angle of jaw."},
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
    {"q": "Sellick Maneuver (Cricoid Pressure) prevents:", "options": ["Gastric distension", "Vomiting", "Hypoxia", "Aspiration"], "correct": "Gastric distension", "rationale": "Compresses the esophagus."},

    # --- CPAP & STOMA ---
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
    
    # --- SCENARIOS (STUDY GUIDE) ---
    {"q": "Patient is breathing 4 times/min. Treatment?", "options": ["NRB", "Cannula", "BVM (Ventilation)", "Monitor"], "correct": "BVM (Ventilation)", "rationale": "Rate of 4 is respiratory failure; they need breathing done for them."},
    {"q": "Patient is gurgling. First step?", "options": ["Ventilate", "Suction", "Oxygen", "CPR"], "correct": "Suction", "rationale": "Clear the airway before anything else."},
    {"q": "Trauma patient airway maneuver?", "options": ["Head-tilt chin-lift", "Jaw-thrust", "Neck lift", "Trendelenburg"], "correct": "Jaw-thrust", "rationale": "Protects the cervical spine."},
    {"q": "Patient with pulmonary edema, conscious, BP 140/90. Device?", "options": ["CPAP", "BVM", "NRB", "Cannula"], "correct": "CPAP", "rationale": "Ideal candidate: awake, fluid in lungs, stable BP."},
    {"q": "The 'E-C' clamp technique is used for:", "options": ["Holding a mask seal", "Checking a pulse", "Sizing an OPA", "Holding a nebulizer"], "correct": "Holding a mask seal", "rationale": "Thumbs/Index (C) on mask, other fingers (E) on jaw."},

    # --- MED ED PREP BATCH 1 ---
    {"q": "What is a common cause of acute respiratory distress syndrome (ARDS)?", "options": ["Sepsis", "Viral infection", "Chronic obstructive pulmonary disease (COPD)", "Inhalation of toxic chemicals or smoke"], "correct": "Sepsis", "rationale": "ARDS can be triggered by sepsis, trauma, pneumonia, and inhalation injuries."},
    {"q": "How might a swallowed foreign body affect breathing?", "options": ["It may cause difficulty breathing if it obstructs the airway", "It may cause nasal congestion and increased mucus", "It may cause a decrease in lung capacity", "It may cause the voice to become deeper and hoarse"], "correct": "It may cause difficulty breathing if it obstructs the airway", "rationale": "A swallowed foreign body can affect breathing if it obstructs the airway, leading to choking."},
    {"q": "How would you position a patient to manage their airway post-seizure?", "options": ["Recovery position.", "Supine position or Trendelenburg position", "Prone position or lateral recumbent position", "Reverse Trendelenburg position or sitting upright"], "correct": "Recovery position.", "rationale": "Placing a patient on their side (recovery position) allows the tongue and vomit to drain."},
    {"q": "How does cystic fibrosis affect the lungs?", "options": ["It leads to the build-up of thick, sticky mucus", "It leads to the formation of cysts in the lungs", "It causes narrowing and inflammation of the airways", "It impairs the ability of the lungs to expand and contract"], "correct": "It leads to the build-up of thick, sticky mucus", "rationale": "Thick, sticky mucus can block airways and create an environment for infection."},
    {"q": "In a patient with a suspected cervical spine injury, how should the airway be opened?", "options": ["Using a jaw-thrust maneuver without head extension.", "Using a head-tilt, chin-lift maneuver with head extension", "Using a jaw-thrust maneuver with head extension", "Using a jaw-thrust maneuver with head flexion"], "correct": "Using a jaw-thrust maneuver without head extension.", "rationale": "This technique helps protect the spine while opening the airway."},
    {"q": "What is the purpose of a nasopharyngeal airway?", "options": ["Keep the airway patent in a semi-conscious or unconscious patient.", "Provide oxygen to the lungs during CPR", "Facilitate communication during conscious sedation", "Control bleeding in the nasal cavity"], "correct": "Keep the airway patent in a semi-conscious or unconscious patient.", "rationale": "An NPA is designed to keep the airway open in patients who may have an obstruction due to the tongue."},
    {"q": "Which drug class is typically the first-line treatment for COPD?", "options": ["Bronchodilators", "Anticholinergics", "Corticosteroids", "Antihistamines"], "correct": "Bronchodilators", "rationale": "Bronchodilators provide immediate relief by relaxing airway muscles and improving airflow."},
    {"q": "What does stridor suggest about a patient's airway?", "options": ["Upper airway obstruction.", "Lower airway obstruction", "Lower respiratory tract infection", "Allergic reaction"], "correct": "Upper airway obstruction.", "rationale": "Stridor is a high-pitched sound indicating narrowed upper airways."},
    {"q": "What is the primary infectious agent responsible for community-acquired pneumonia?", "options": ["Streptococcus pneumoniae", "Haemophilus influenzae", "Legionella pneumophila", "Staphylococcus aureus"], "correct": "Streptococcus pneumoniae", "rationale": "This bacterium typically causes symptoms such as cough, fever, and chest pain."},
    {"q": "After administering epinephrine for anaphylaxis, the heart rate increases. What is the reason?", "options": ["Epinephrine's beta-adrenergic stimulation", "The anaphylaxis is worsening", "An adverse reaction to the epinephrine", "The medication was improperly administered"], "correct": "Epinephrine's beta-adrenergic stimulation", "rationale": "Epinephrine stimulates beta-adrenergic receptors in the heart, which increases heart rate."},

    # --- MED ED PREP BATCH 2 ---
    {"q": "What condition is characterized by the destruction of the walls of the alveoli, leading to fewer, larger alveoli?", "options": ["Emphysema", "Chronic obstructive pulmonary disease (COPD)", "Bronchiolitis", "Pulmonary fibrosis"], "correct": "Emphysema", "rationale": "Emphysema specifically involves the destruction of alveolar walls, reducing surface area for gas exchange."},
    {"q": "What might cause a sudden decrease in capnography reading during ventilation?", "options": ["Dislodged or blocked airway, pulmonary embolism.", "Increased tidal volume or decreased respiratory rate", "Decreased tidal volume or increased respiratory rate", "Increased end-tidal CO2 or decreased oxygen saturation"], "correct": "Dislodged or blocked airway, pulmonary embolism.", "rationale": "A sudden drop in EtCO2 suggests CO2 is not being produced, transported, or exhaled."},
    {"q": "What is the best patient position for administering intranasal medication?", "options": ["Sitting upright with the head tilted slightly back", "Lying supine on the cot", "Standing with the head down", "Lying in the left lateral recumbent position"], "correct": "Sitting upright with the head tilted slightly back", "rationale": "An upright position with a slight head tilt facilitates optimal airflow and absorption."},
    {"q": "Can the Heimlich maneuver be performed on all patients?", "options": ["No, it is not recommended for infants under 1 year.", "No, it is not recommended for infants under 2 years.", "No, it is not recommended for pregnant women.", "No, it is not recommended for children under 5 years."], "correct": "No, it is not recommended for infants under 1 year.", "rationale": "For infants under 1 year old, back blows and chest thrusts are used instead of abdominal thrusts."},
    {"q": "What is the purpose of administering steroids in asthma?", "options": ["To reduce inflammation", "To relieve bronchospasm", "To increase inflammation", "To prevent allergic reactions"], "correct": "To reduce inflammation", "rationale": "Steroids are a long-term 'controller' medication that reduces airway swelling."},
    {"q": "How does magnesium sulfate work in the treatment of asthma?", "options": ["It’s a bronchial smooth muscle relaxant", "It reduces airway inflammation", "It inhibits the release of histamine", "It increases cardiac output"], "correct": "It’s a bronchial smooth muscle relaxant", "rationale": "Magnesium sulfate relaxes the smooth muscles of the bronchi to improve airflow."},
    {"q": "What might indicate the need for emergency endoscopy after swallowing a foreign body?", "options": ["Signs of obstruction (drooling/inability to swallow) or perforation", "Signs of infection, such as redness and swelling at the site", "Signs of allergic reaction, such as rash or hives", "Signs of gastrointestinal bleeding, such as vomiting blood"], "correct": "Signs of obstruction (drooling/inability to swallow) or perforation", "rationale": "The inability to swallow or handle secretions (drooling) indicates a complete obstruction."},
    {"q": "What is the role of radiographic imaging in managing swallowed foreign bodies?", "options": ["It can help locate the object and assess for complications", "It can provide definitive diagnosis and treatment options", "It can identify the exact location and determine the need for surgery", "It can detect other foreign bodies missed during physical exam"], "correct": "It can help locate the object and assess for complications", "rationale": "X-rays are useful for locating radiopaque objects and checking for complications."},
    {"q": "What is the Heimlich maneuver used for?", "options": ["It is used to dislodge foreign objects from the throat of a choking person", "It is used to perform chest compressions in cardiac arrest patients", "It is used to stabilize the cervical spine in trauma patients", "It is used to administer medications in patients experiencing anaphylaxis"], "correct": "It is used to dislodge foreign objects from the throat of a choking person", "rationale": "It involves delivering abdominal thrusts to force air from the lungs to eject the obstruction."},
    {"q": "How does supplemental oxygen help patients with COPD?", "options": ["It improves oxygenation and reduces the work of breathing", "It reduces airway inflammation", "It enhances mucus clearance", "It stimulates bronchoconstriction"], "correct": "It improves oxygenation and reduces the work of breathing", "rationale": "By increasing inhaled oxygen, we help compensate for diminished lung function."},

    # --- MED ED PREP BATCH 3 ---
    {"q": "What is the primary physiological effect of a Beta-2 agonist like Albuterol?", "options": ["Bronchodilation", "Vasoconstriction", "Decreased heart rate", "Increased mucus production"], "correct": "Bronchodilation", "rationale": "Beta-2 receptors relax the smooth muscles of the bronchi to open the airways."},
    {"q": "What is a common side effect of administering Albuterol?", "options": ["Tachycardia and tremors", "Bradycardia and lethargy", "Hypotension and skin rash", "Nausea and abdominal pain"], "correct": "Tachycardia and tremors", "rationale": "Albuterol is a sympathomimetic and often leads to a fast heart rate and shaky hands."},
    {"q": "Which of the following is an early sign of respiratory distress in a pediatric patient?", "options": ["Nasal flaring and retractions", "Cyanosis and bradycardia", "Altered mental status", "Silent chest"], "correct": "Nasal flaring and retractions", "rationale": "Pediatric patients use accessory muscles like nostrils and intercostal 'pulling' earlier than adults."},
    {"q": "What is the standard adult dose for Epinephrine 1:1,000 via IM injection for anaphylaxis?", "options": ["0.3 mg", "0.15 mg", "1.0 mg", "3.0 mg"], "correct": "0.3 mg", "rationale": "Standard adult dose is 0.3 mg; 0.15 mg is for pediatric patients."},
    {"q": "What is the mechanism of action of Epinephrine in anaphylaxis?", "options": ["Bronchodilation and vasoconstriction", "Bronchoconstriction and vasodilation", "Decreased heart rate and blood pressure", "Inhibition of histamine release only"], "correct": "Bronchodilation and vasoconstriction", "rationale": "Epinephrine opens lungs (Beta-2) and raises blood pressure (Alpha-1)."},
    {"q": "A patient with a history of asthma is 'tri-poding.' What does this indicate?", "options": ["Significant respiratory distress", "A normal resting position for asthma patients", "The patient is recovering from an attack", "The patient is experiencing a cardiac event"], "correct": "Significant respiratory distress", "rationale": "Tripoding allows the patient to use accessory muscles more effectively."},
    {"q": "What is the primary concern when a patient with severe asthma suddenly stops wheezing but remains in distress?", "options": ["'Silent Chest' (minimal air movement)", "The asthma attack has resolved", "The patient is falling asleep", "The bronchodilator has started working"], "correct": "'Silent Chest' (minimal air movement)", "rationale": "No wheezing in a struggling patient means air is no longer moving at all."},
    {"q": "When using a spacers/valved holding chamber with an MDI, what is the benefit?", "options": ["It improves medication delivery to the lower lungs", "It makes the medication act faster", "It prevents the patient from coughing", "It reduces the dose required"], "correct": "It improves medication delivery to the lower lungs", "rationale": "Spacers help the patient breathe in the mist deeply instead of it hitting the back of the throat."},
    {"q": "Which of the following is a symptom of a pleural effusion?", "options": ["Dyspnea and pleuritic chest pain", "Productive cough with yellow sputum", "High fever and night sweats", "Generalized weakness and fatigue"], "correct": "Dyspnea and pleuritic chest pain", "rationale": "Pleural effusion is fluid buildup outside the lung that causes pain during breathing."},
    {"q": "What is the most common cause of bronchiolitis in infants?", "options": ["Respiratory Syncytial Virus (RSV)", "Influenza Virus", "Bacterial infection", "Allergic reaction"], "correct": "Respiratory Syncytial Virus (RSV)", "rationale": "RSV causes inflammation of small airways in children under 2 years old."},

    # --- MED ED PREP BATCH 4 ---
    {"q": "What is the primary risk of providing high-concentration oxygen to a patient with a Paraquat poisoning?", "options": ["It can worsen lung injury and fibrosis", "It can cause immediate cardiac arrest", "It can trigger severe seizures", "It can lead to metabolic acidosis"], "correct": "It can worsen lung injury and fibrosis", "rationale": "Giving high-flow oxygen can accelerate oxidative damage in Paraquat poisoning."},
    {"q": "A patient is coughing up 'rust-colored' sputum. This is a classic sign of:", "options": ["Pneumococcal Pneumonia", "Congestive Heart Failure", "Tuberculosis", "Pulmonary Embolism"], "correct": "Pneumococcal Pneumonia", "rationale": "Rust-colored sputum is a hallmark of Streptococcus pneumoniae infections."},
    {"q": "Which of the following would cause a Pulse Oximeter to give a falsely high reading?", "options": ["Carbon monoxide poisoning", "Hypothermia", "Fingernail polish", "Severe anemia"], "correct": "Carbon monoxide poisoning", "rationale": "Pulse oximeters cannot distinguish between Oxygen and Carbon Monoxide saturation."},
    {"q": "What is the function of the 'Carina' in the respiratory system?", "options": ["The point where the trachea bifurcates into the bronchi", "The cartilage that protects the vocal cords", "The valve between the pharynx and esophagus", "The space between the lungs and the chest wall"], "correct": "The point where the trachea bifurcates into the bronchi", "rationale": "The carina is the point where the trachea splits into two mainstem bronchi."},
    {"q": "A patient has 'Pleuritic' chest pain. What does this mean?", "options": ["Pain that worsens with deep breathing or coughing", "Pain that radiates to the left arm", "Pain that is constant and crushing", "Pain that is relieved by eating"], "correct": "Pain that worsens with deep breathing or coughing", "rationale": "Pleuritic pain occurs when inflamed pleural linings rub together during breathing."},
    {"q": "What is 'Atelectasis'?", "options": ["Collapse of the alveoli", "Fluid in the pleural space", "Infection of the bronchioles", "Spasm of the vocal cords"], "correct": "Collapse of the alveoli", "rationale": "Atelectasis prevents gas exchange in the affected area of the lung."},
    {"q": "Why should we be cautious with oxygen administration in Neonates (premature infants)?", "options": ["It can cause Retinopathy of Prematurity (eye damage)", "It can cause their heart to stop", "It can damage their hearing", "It can cause high blood pressure"], "correct": "It can cause Retinopathy of Prematurity (eye damage)", "rationale": "High oxygen levels in premature infants can cause abnormal vessel growth in the eyes."},
    {"q": "Which respiratory pattern is characterized by increasing, then decreasing, breaths followed by apnea?", "options": ["Cheyne-Stokes", "Kussmaul", "Biot's", "Ataxic"], "correct": "Cheyne-Stokes", "rationale": "Associated with heart failure or central nervous system injuries."},
    {"q": "What is the normal EtCO2 (End-Tidal Carbon Dioxide) range?", "options": ["35-45 mmHg", "25-35 mmHg", "45-55 mmHg", "80-100 mmHg"], "correct": "35-45 mmHg", "rationale": "Represents the normal balance of CO2 production and ventilation."},
    {"q": "What is the primary benefit of the 'sniffing position' in pediatric airway management?", "options": ["It aligns the airway axes for better air flow", "It prevents the patient from vomiting", "It makes it easier to apply a cervical collar", "It reduces the heart rate"], "correct": "It aligns the airway axes for better air flow", "rationale": "Aligning the axes helps overcome the child's naturally large occiput."},

    # --- MISSED QUESTIONS FROM MED ED PREP ---
    {"q": "What is the primary function of the surfactant in the lungs?", "options": ["Reduce surface tension in the alveoli", "Facilitate the exchange of gases", "Lubricate the pleural membranes", "Prevent infection in the lungs"], "correct": "Reduce surface tension in the alveoli", "rationale": "Surfactant prevents the alveoli from collapsing by reducing surface tension."},
    {"q": "How does the body respond to an increase in carbon dioxide levels in the blood?", "options": ["Increasing the respiratory rate and depth", "Decreasing the respiratory rate and depth", "Increasing heart rate and blood pressure", "Decreasing heart rate and blood pressure"], "correct": "Increasing the respiratory rate and depth", "rationale": "The medulla senses high CO2 and signals the body to breathe faster and deeper."},
    {"q": "What is the hallmark sign of a pulmonary embolism?", "options": ["Sudden onset of shortness of breath and chest pain", "Persistent cough with thick, green mucus", "Gradual onset of difficulty breathing and wheezing", "Severe headache and blurred vision"], "correct": "Sudden onset of shortness of breath and chest pain", "rationale": "Sudden onset is the key clinical feature of a PE."},
    {"q": "Which of the following is a symptom of high-altitude pulmonary edema (HAPE)?", "options": ["Coughing up pink, frothy sputum", "Severe headache and dizziness", "Muscle cramps and joint pain", "Swelling of the hands and feet"], "correct": "Coughing up pink, frothy sputum", "rationale": "Pink frothy sputum is a classic sign of pulmonary edema."},
    {"q": "What is the primary goal of oxygen therapy in a patient with COPD?", "options": ["Maintain an oxygen saturation level of 88-92%", "Achieve an oxygen saturation level of 100%", "Decrease the respiratory rate and depth", "Increase the heart rate and blood pressure"], "correct": "Maintain an oxygen saturation level of 88-92%", "rationale": "In COPD, a target of 88-92% prevents suppressing the hypoxic drive."},
    {"q": "In a patient with suspected epiglottitis, what should be avoided?", "options": ["Inspecting the throat with a tongue depressor", "Administering supplemental oxygen", "Keeping the patient in an upright position", "Providing fluids for hydration"], "correct": "Inspecting the throat with a tongue depressor", "rationale": "Aggravating the epiglottis can cause it to spasm and shut the airway entirely."},
    {"q": "Which of the following is a classic sign of tension pneumothorax?", "options": ["Tracheal deviation away from the affected side", "Decreased heart rate and blood pressure", "Increased breath sounds on the affected side", "Dullness to percussion over the affected side"], "correct": "Tracheal deviation away from the affected side", "rationale": "Pressure pushes the trachea toward the 'good' side; this is a life-threatening sign."}
]

# --- 2. LOGIC & INITIALIZATION ---
def initialize_quiz():
    full_deck = list(MASTER_QUESTIONS)
    random.shuffle(full_deck)
    st.session_state.master_deck = full_deck
    st.session_state.batch_index = 0
    st.session_state.score = 0
    st.session_state.current_batch = full_deck[:20]
    st.session_state.current_q_index = 0
    st.session_state.show_review = False
    st.session_state.missed_q = []

if 'master_deck' not in st.session_state:
    initialize_quiz()

# --- 3. UI SETUP ---
st.set_page_config(page_title="EMT ARV Ultimate Review", page_icon="🚑")
st.title("🚑 EMT ARV Ultimate Review Bank")
st.write("Combined Study Guide + Med Ed Prep Missed Questions")

# Global Progress
total_in_deck = len(st.session_state.master_deck)
current_q_global = st.session_state.batch_index + st.session_state.current_q_index
st.progress(min(current_q_global / total_in_deck, 1.0))
st.caption(f"Bank Mastery: {min(current_q_global, total_in_deck)} / {total_in_deck} Questions")

# --- 4. QUESTION HANDLING ---
batch_q = st.session_state.current_batch
q_idx = st.session_state.current_q_index

if q_idx < len(batch_q):
    item = batch_q[q_idx]
    st.subheader(f"Question {q_idx + 1} of {len(batch_q)} (Batch)")
    st.markdown(f"### {item['q']}")
    
    choice = st.radio("Select Answer:", item['options'], index=None, key=f"q_{st.session_state.batch_index}_{q_idx}")

    if not st.session_state.show_review:
        if st.button("Submit Answer"):
            if choice:
                st.session_state.show_review = True
                st.rerun()
            else:
                st.warning("Please select an answer.")
    else:
        if choice == item['correct']:
            st.success("**Correct!**")
        else:
            st.error(f"**Incorrect.** The correct answer is: {item['correct']}")
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
    # --- END OF BATCH LOGIC ---
    st.balloons()
    st.header("Batch Complete!")
    st.write(f"Batch Score: {st.session_state.score} / {len(batch_q)}")
    
    next_start = st.session_state.batch_index + 20
    if next_start < total_in_deck:
        remaining = total_in_deck - next_start
        if st.button(f"Load Next {min(remaining, 20)} Questions"):
            st.session_state.batch_index = next_start
            st.session_state.current_batch = st.session_state.master_deck[next_start : next_start + 20]
            st.session_state.current_q_index = 0
            st.session_state.score = 0
            st.session_state.show_review = False
            st.rerun()
    else:
        st.success("🎉 You've conquered the entire question bank!")
        if st.session_state.missed_q:
            with st.expander("Review My Missed Questions"):
                for m in st.session_state.missed_q:
                    st.write(f"**Q:** {m['q']}")
                    st.write(f"**A:** {m['correct']}")
                    st.write("---")
        
        if st.button("Reshuffle and Restart From Question 1"):
            initialize_quiz()
            st.rerun()

