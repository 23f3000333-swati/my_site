import streamlit as st

# 1. Page Configuration
st.set_page_config(page_title="Swati Singh | Portfolio", page_icon="📊", layout="wide")

# 2. Sidebar Navigation Setup
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", ["🏠 Home", "🚀 Projects", "🤖 ML Playground"])

# Add a quick contact badge in the sidebar
st.sidebar.markdown("---")
st.sidebar.markdown("### Connect with Me")
st.sidebar.markdown("🔗 [GitHub](https://github.) | 💼 [LinkedIn](https://linkedin.com)")

# ==========================================
# PAGE 1: HOME
# ==========================================
if page == "🏠 Home":
    st.title("👋 Hi, I'm Swati Singh")
    st.subheader("Data Science Student & Applied AI Developer")
    
    st.write(
        "Welcome to my technical portfolio! I specialize in building practical machine learning pipelines, "
        "fine-tuning specialized models, and creating automation scripts to solve real-world problems."
    )
    
    # Let's create two visual columns for your skill layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🛠️ Core Tech Stack")
        st.write("- **Languages:** Python, SQL, Shell Scripting (`bash`, `awk`, `sed`) ")
        st.write("- **Machine Learning / NLP:** Transformers, Ensemble Stacking, Feature Engineering")
        st.write("- **Tools & Platforms:** Git/GitHub, Linux Environments, VS Code, Kaggle")

    with col2:
        st.markdown("### 🎯 Current Focus")
        st.write("- Fine-tuning Multilingual Automatic Speech Recognition (ASR) models.")
        st.write("- Engineering robust ensembling frameworks for predictive performance.")
        st.write("- Streamlining backend data preprocessing and parsing pipelines.")

# ==========================================
# PAGE 2: PROJECTS
# ==========================================
elif page == "🚀 Projects":
    st.title("🚀 Featured Projects & Technical Milestones")
    st.write("Here is a breakdown of the core projects I've engineered:")
    
    # Project 1 Container
    with st.container():
        st.markdown("### 🗣️ Multilingual Speech Recognition (Whisper Fine-Tuning)")
        st.caption("Keywords: NLP | Speech-to-Text | Model Fine-Tuning")
        st.write(
            "Fine-tuned OpenAI's Whisper model for accurate speech transcription in multilingual competitive setups. "
            "Handled complex audio preprocessing pipelines, custom dataset mappings, and resolved intensive training log bottlenecks."
        )
        st.markdown("---")
        
    # Project 2 Container
    with st.container():
        st.markdown("### 📈 Sentiment Analysis via Stacking Ensembles")
        st.caption("Keywords: Machine Learning | Ensemble Methods | Text Classification")
        st.write(
            "Engineered a stacking ensemble model to boost classification metrics for sentiment analysis tasks. "
            "Combined multiple diverse base learners to yield an optimized, robust final metadata predictor."
        )
        st.markdown("---")

    # Project 3 Container
    with st.container():
        st.markdown("### ⚙️ Unix Data Pipeline Utilities")
        st.caption("Keywords: Bash Scripting | DevTools | Data Automation")
        st.write(
            "Designed efficient, lightweight terminal automation workflows using `awk` for fixed-width data parsing "
            "and `sed` for pattern-based transformations. Utilized browser network diagnostics to isolate and fix "
            "unstable data transmission routines."
        )

# ==========================================
# PAGE 3: ML PLAYGROUND
# ==========================================
elif page == "🤖 ML Playground":
    st.title("🤖 Live ML Engine Playground")
    st.write("Interact with live mockups of my machine learning and data engineering workflows.")
    
    # Create two primary tabs for your two major domains
    tab1, tab2 = st.tabs(["🗣️ Whisper Speech Insights", "📈 Stacking Ensemble Simulator"])
    
    # ---------------------------------------------------------
    # TAB 1: WHISPER ASR DEMO
    # ---------------------------------------------------------
    with tab1:
        st.markdown("### Multilingual Audio Transcription Pipeline")
        st.write("Simulate how a fine-tuned Whisper model processes audio across different languages.")
        
        # User Controls
        lang_choice = st.selectbox("Select Target Language:", ["Hindi", "Tamil", "Telugu", "Bengali", "English"])
        beam_size = st.slider("Beam Size (Search Width):", min_value=1, max_value=5, value=3)
        
        st.write(" ")
        if st.button("Simulate Pipeline Execution"):
            with st.spinner("Processing audio chunks, allocating tensor memory..."):
                # Simulating a brief delay like a real model call
                import time
                time.sleep(1) 
                
            st.success("Inference Complete!")
            
            # Dynamic output based on language choice
            transcripts = {
                "Hindi": "डेटा साइंस पोर्टफोलियो में आपका स्वागत है।",
                "Tamil": "தரவு அறிவியல் போர்ட்ஃபோலியோவிற்கு வரவேற்கிறோம்.",
                "Telugu": "డేటా సైన్స్ పోర్ట్‌ఫోలియోకు స్వాగతం.",
                "Bengali": "ডেটা সায়েন্স পোর্টফোলিওতে আপনাকে স্বাগতম।",
                "English": "Welcome to the Data Science Portfolio."
            }
            
            # Display results in structured boxes
            col_a, col_b = st.columns(2)
            with col_a:
                st.info(f"**Predicted Transcription ({lang_choice}):**\n\n {transcripts[lang_choice]}")
            with col_b:
                # Showing performance metrics using Streamlit's built-in metric display
                st.metric(label="WER (Word Error Rate)", value=f"{0.12 - (beam_size * 0.01):.2f}", delta="-2.1% improvement")

    # ---------------------------------------------------------
    # TAB 2: STACKING ENSEMBLE SIMULATOR
    # ---------------------------------------------------------
    with tab2:
        st.markdown("### Sentiment Analysis Stacking Ensemble Optimizer")
        st.write("Adjust the weights of individual base learners to see how it stabilizes the final Meta-Learner prediction accuracy.")
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.markdown("#### Adjust Base Model Weights")
            weight_transformer = st.slider("Transformer Model Weight:", 0.0, 1.0, 0.5)
            weight_logistic = st.slider("Logistic Regression Weight:", 0.0, 1.0, 0.3)
            weight_xgb = st.slider("XGBoost Weight:", 0.0, 1.0, 0.2)
            
            # Normalize weights mathematically
            total_w = weight_transformer + weight_logistic + weight_xgb
            
        with col2:
            st.markdown("#### Live Meta-Learner Performance Summary")
            if total_w == 0:
                st.warning("Please allocate weight to at least one base model.")
            else:
                # Calculate a simulated accuracy based on user choices
                base_accuracy = 0.78
                simulated_acc = base_accuracy + (0.05 * (weight_transformer / total_w)) + (0.03 * (weight_xgb / total_w))
                
                st.metric(label="Calculated Stacking Ensemble Accuracy", value=f"{simulated_acc * 100:.2f}%")
                
                # Create a quick interactive visual bar chart using native Streamlit functions
                chart_data = {
                    "Model Component": ["Transformer", "Logistic Reg", "XGBoost", "Final Ensemble (Combined)"],
                    "Accuracy Score": [0.83, 0.79, 0.81, simulated_acc]
                }
                st.bar_chart(data=chart_data, x="Model Component", y="Accuracy Score")
                st.caption("Visualizing baseline models compared directly with the dynamically weighted Meta-Learner.")