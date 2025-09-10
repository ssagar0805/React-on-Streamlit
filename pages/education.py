# pages/learn.py

import streamlit as st

def show_learn():
    """Learn Page – Educational Resources and Training"""

    st.title("🎓 TruthLens Learning Hub")
    st.markdown("**Learn to identify misinformation and improve digital literacy**")

    # Tabs for learning sections
    tabs = st.tabs([
        "📚 Modules",
        "🧠 Quiz",
        "📊 Case Studies",
        "🎯 Training",
        "📖 Resources"
    ])

    # Module 1: Learning Modules
    with tabs[0]:
        st.subheader("📚 Digital Literacy Learning Modules")
        learning_paths = {
            "🔰 Beginner": "Basic misinformation identification",
            "📈 Intermediate": "Advanced analysis techniques",
            "🎖️ Expert": "Professional investigation methods",
            "👮 Authority": "Law enforcement protocols"
        }
        path = st.selectbox("Select Learning Path", list(learning_paths.keys()))
        st.info(learning_paths[path])

        modules = {
            "🔰 Beginner": [
                "What is Misinformation?",
                "Basic Fact-Checking Techniques",
                "Social Media Literacy",
                "Cognitive Biases and You",
                "Reliable Source Identification"
            ],
            "📈 Intermediate": [
                "Advanced Analysis Methods",
                "Image and Video Verification",
                "Statistical Manipulation Detection",
                "Cross-Platform Investigation",
                "Legal and Ethical Considerations"
            ],
            "🎖️ Expert": [
                "Digital Forensics Techniques",
                "Psychological Warfare Tactics",
                "Geopolitical Context Analysis",
                "AI-Generated Content Detection",
                "Evidence Documentation"
            ],
            "👮 Authority": [
                "Law Enforcement Protocols",
                "Legal Framework and Rights",
                "Emergency Response Procedures",
                "Threat Assessment Methods",
                "Inter-Agency Coordination"
            ]
        }
        for i, m in enumerate(modules[path], 1):
            with st.expander(f"Module {i}: {m}"):
                st.write("• Learning objectives and exercises go here.")
                st.button(f"▶️ Start Module {i}", key=f"start_mod_{i}")

    # Module 2: Interactive Quiz
    with tabs[1]:
        from pages.education import interactive_quiz
        interactive_quiz()

    # Module 3: Case Studies
    with tabs[2]:
        from pages.education import case_studies
        case_studies()

    # Module 4: Training Center
    with tabs[3]:
        from pages.education import training_center
        training_center()

    # Module 5: Resources
    with tabs[4]:
        from pages.education import educational_resources
        educational_resources()
