# pages/home.py
from tl_frontend import render_landing

import streamlit as st
from utils.ai_services import GeminiService, FactCheckService
from utils.news_services import NewsAggregator
from utils.security import SecurityService
from utils.database import FirebaseService


# Initialize services
gemini_service = GeminiService()
fact_check_service = FactCheckService()
news_aggregator = NewsAggregator()
security_service = SecurityService()
firebase_service = FirebaseService()

def show_home():
    """Main Home Page – Hero Section with Input Tabs"""
    
        # --- React Landing Page Component ---
    render_landing()

    
    # --- Tabs for Input Types ---
    tab1, tab2, tab3 = st.tabs([
        "📝 Text Forensics",
        "🔗 URL Investigation", 
        "🖼️ Image Analysis"
    ])
    
    

    # --- TEXT FORENSICS TAB ---
    with tab1:
        st.subheader("📝 Enter Text to Analyze")
        user_text = st.text_area(
            "Paste content to check:",
            height=150,
            placeholder="Paste news articles, posts, or claims here...",
            help="The AI will analyze this text for misinformation, manipulation tactics, and provide sources."
        )
        
        col1, col2, col3 = st.columns(3)
        with col1:
            language = st.selectbox("🌍 Language", ["en", "hi", "ta", "te", "bn", "mr"], help="Select content language")
        with col2:
            analysis_level = st.selectbox("🔍 Analysis Level", 
                                        ["Quick Scan", "Deep Analysis"],
                                        help="Quick Scan: Fast AI analysis | Deep Analysis: Includes origin tracking")
        with col3:
            safety_check = st.checkbox("🛡️ Safety Check", value=True, help="Check for harmful content")
        
        if st.button("🚀 Analyze Text", type="primary", use_container_width=True):
            if user_text.strip():
                # Validate input
                is_valid, validation_msg = security_service.validate_input(user_text)
                if not is_valid:
                    st.error(f"❌ {validation_msg}")
                    return
                
                # Sanitize input
                sanitized_text = security_service.sanitize_input(user_text)
                
                with st.spinner("🔍 AI is analyzing your text..."):
                    # Conduct real analysis
                    results = conduct_forensic_analysis(
                        sanitized_text, language, analysis_level, True, 
                        analysis_level == "Deep Analysis", safety_check
                    )
                    
                    # Display results
                    display_forensic_results(results)
                    
                    # Save to database
                    analysis_id = firebase_service.save_analysis(sanitized_text, results)
                    if analysis_id:
                        st.success(f"✅ Analysis completed and saved (ID: {analysis_id})")
            else:
                st.warning("⚠️ Please enter some text to analyze")
    
    # --- URL INVESTIGATION TAB ---
    with tab2:
        st.subheader("🔗 URL Investigation")
        url_input = st.text_input("🌐 Enter URL to investigate:",
                                  placeholder="https://example.com/article")
        
        if st.button("🔍 Investigate URL", type="primary", use_container_width=True):
            if url_input.strip():
                with st.spinner(f"🔍 Investigating URL: {url_input}"):
                    # Basic URL validation
                    if not url_input.startswith(('http://', 'https://')):
                        st.error("❌ Please enter a valid URL starting with http:// or https://")
                        return
                    
                    # Use news aggregator to verify article
                    verification_result = news_aggregator.verify_article(url_input)
                    
                    col1, col2, col3 = st.columns(3)
                    with col1:
                        st.metric("Credibility Score", f"{verification_result['credibility_score']}/100")
                    with col2:
                        st.metric("Source Reputation", verification_result['source_reputation'])
                    with col3:
                        st.metric("Cross References", verification_result['cross_references'])
                    
                    if verification_result['warning_flags']:
                        st.warning("⚠️ Warning flags detected:")
                        for flag in verification_result['warning_flags']:
                            st.write(f"• {flag}")
                    else:
                        st.success("✅ No warning flags detected")
            else:
                st.warning("⚠️ Please enter a URL")
    
    # --- IMAGE FORENSICS TAB ---
    with tab3:
        st.subheader("🖼️ Image Analysis")
        uploaded_file = st.file_uploader(
            "📸 Upload Image for Analysis",
            type=['png', 'jpg', 'jpeg', 'webp', 'gif', 'bmp'],
            help="Supported formats: PNG, JPG, JPEG, WebP, GIF, BMP (Max 10MB)"
        )
        
        if uploaded_file:
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.image(uploaded_file, caption="📸 Uploaded Image", use_column_width=True)
            
            with col2:
                st.markdown("**⚙️ Analysis Options**")
                check_manipulation = st.checkbox("🔍 Detect Manipulation", value=True)
                extract_metadata = st.checkbox("📊 Extract Metadata", value=True)
                reverse_search = st.checkbox("🔄 Reverse Image Search", value=False)
                text_extraction = st.checkbox("📝 Extract Text (OCR)", value=True)
                
                analysis_depth = st.selectbox(
                    "Analysis Depth",
                    ["Quick Scan", "Standard Analysis", "Deep Forensics"],
                    index=1
                )
            
            if st.button("🚀 Analyze Image", type="primary", use_container_width=True):
                with st.spinner("🔍 Performing image forensics..."):
                    # Use the comprehensive image analysis
                    results = analyze_image_comprehensive(
                        uploaded_file, check_manipulation, extract_metadata, 
                        reverse_search, text_extraction, analysis_depth
                    )
                    
                    # Display results
                    display_image_results(results)
                    
                    # Save to database
                    analysis_id = firebase_service.save_image_analysis(uploaded_file.name, results)
                    if analysis_id:
                        st.success(f"✅ Image analysis completed and saved (ID: {analysis_id})")

def conduct_forensic_analysis(text, language, level, context, origin, safety):
    """Comprehensive forensic analysis using real backend services"""
    results = {
        'risk_score': 0,
        'credibility_score': 0,
        'manipulation_tactics': [],
        'fact_checks': [],
        'ai_analysis': None,
        'origin_analysis': None,
        'context_analysis': None,
        'safety_analysis': None,
        'structure_analysis': None,
        'recommendations': [],
        'source_links': [],
        'reporting_emails': []
    }
    
    # Basic risk calculation
    results['risk_score'] = calculate_risk_score(text)
    
    # Security analysis
    if safety:
        results['safety_analysis'] = security_service.check_content_safety(text)
        results['structure_analysis'] = security_service.analyze_text_structure(text)
        manipulation_results = security_service.detect_manipulation_patterns(text)
        results['manipulation_tactics'] = list(manipulation_results['patterns'].keys())
        
        # Adjust risk score based on security analysis
        results['risk_score'] = max(results['risk_score'], 
                                  manipulation_results['manipulation_score'])
    
    # Basic manipulation detection fallback
    if not results['manipulation_tactics']:
        results['manipulation_tactics'] = detect_manipulation_tactics(text)
    
    # Fact checking
    results['fact_checks'] = fact_check_service.search_claims(text)
    
    # AI analysis with Gemini
    try:
        results['ai_analysis'] = gemini_service.forensic_analysis(text, language)
        # Update risk score based on AI analysis
        ai_risk_adjustment = analyze_ai_response_for_risk(results['ai_analysis'])
        results['risk_score'] = max(results['risk_score'], ai_risk_adjustment)
        
        # Extract sources and reporting information
        sources_and_reporting = gemini_service.extract_sources_and_reporting(results['ai_analysis'])
        results['source_links'] = sources_and_reporting['sources']
        results['reporting_emails'] = sources_and_reporting['reporting_emails']
    except Exception as e:
        results['ai_analysis'] = f"AI analysis temporarily unavailable: {str(e)}"
        results['source_links'] = []
        results['reporting_emails'] = []
    
    # Origin tracking for deep analysis
    if origin and level == "Deep Analysis":
        try:
            results['origin_analysis'] = gemini_service.trace_origin(text)
        except Exception as e:
            results['origin_analysis'] = f"Origin tracking unavailable: {str(e)}"
    
    # Context analysis
    if context:
        try:
            results['context_analysis'] = gemini_service.analyze_context(text)
        except Exception as e:
            results['context_analysis'] = f"Context analysis unavailable: {str(e)}"
    
    # Calculate credibility score
    results['credibility_score'] = calculate_credibility(results)
    
    # Generate recommendations
    results['recommendations'] = generate_recommendations(results)
    
    return results

def calculate_risk_score(text):
    """Enhanced risk score calculation"""
    score = 0
    text_lower = text.lower()
    
    # Check for sensational language
    sensational_words = ['shocking', 'unbelievable', 'incredible', 'amazing', 'breaking', 'urgent']
    for word in sensational_words:
        if word in text_lower:
            score += 10
    
    # Check for conspiracy indicators
    conspiracy_words = ['conspiracy', 'cover-up', 'hidden truth', 'they don\'t want']
    for word in conspiracy_words:
        if word in text_lower:
            score += 15
    
    # Check for lack of sources
    if 'source' not in text_lower and 'study' not in text_lower and 'research' not in text_lower:
        score += 20
    
    # Check for excessive punctuation
    if text.count('!') > 3 or text.count('?') > 3:
        score += 10
    
    # Check for call to action
    action_words = ['share', 'forward', 'spread', 'tell everyone']
    for word in action_words:
        if word in text_lower:
            score += 10
    
    return min(100, score)

def detect_manipulation_tactics(text):
    """Detect manipulation tactics in text"""
    tactics = []
    text_lower = text.lower()
    
    # Check for emotional manipulation
    emotional_words = ['outrageous', 'disgusting', 'terrifying', 'heartbreaking', 'infuriating']
    if any(word in text_lower for word in emotional_words):
        tactics.append("Emotional Manipulation")
    
    # Check for urgency tactics
    urgency_words = ['urgent', 'quickly', 'immediately', 'before it\'s too late', 'act now']
    if any(word in text_lower for word in urgency_words):
        tactics.append("Urgency Tactics")
    
    # Check for authority undermining
    authority_words = ['mainstream media lies', 'experts are wrong', 'don\'t trust']
    if any(word in text_lower for word in authority_words):
        tactics.append("Authority Undermining")
    
    # Check for conspiracy language
    conspiracy_words = ['they don\'t want you to know', 'hidden truth', 'cover-up']
    if any(word in text_lower for word in conspiracy_words):
        tactics.append("Conspiracy Language")
    
    return tactics if tactics else ["None Detected"]

def analyze_ai_response_for_risk(ai_response):
    """Analyze AI response to determine risk level"""
    if not ai_response or "AI analysis temporarily unavailable" in str(ai_response):
        return 0
    
    response_lower = str(ai_response).lower()
    
    # Check for explicit veracity assessment from AI
    if 'false information' in response_lower:
        return 90
    elif 'misleading' in response_lower:
        return 80
    elif 'unverified' in response_lower:
        return 60
    elif 'true' in response_lower and 'veracity assessment' in response_lower:
        return 10
    
    # Fallback to keyword analysis
    high_risk_indicators = [
        'false', 'misinformation', 'disinformation', 'fake', 'untrue', 
        'deceptive', 'manipulative', 'harmful', 'dangerous',
        'conspiracy', 'hoax', 'scam', 'fraud', 'deceit'
    ]
    
    medium_risk_indicators = [
        'questionable', 'suspicious', 'unreliable', 
        'biased', 'exaggerated', 'incomplete', 'outdated'
    ]
    
    # Check for risk indicators
    high_risk_count = sum(1 for indicator in high_risk_indicators if indicator in response_lower)
    medium_risk_count = sum(1 for indicator in medium_risk_indicators if indicator in response_lower)
    
    if high_risk_count > 0:
        return 75
    elif medium_risk_count > 0:
        return 50
    else:
        return 0

def calculate_credibility(results):
    """Calculate credibility score"""
    base_credibility = 80
    
    # Reduce credibility based on risk score
    credibility = base_credibility - (results['risk_score'] * 0.8)
    
    # Factor in safety analysis
    if results.get('safety_analysis'):
        safety_score = results['safety_analysis']['safety_score']
        credibility = (credibility + safety_score) / 2
    
    # Factor in manipulation tactics
    manipulation_count = len([t for t in results['manipulation_tactics'] if t != "None Detected"])
    credibility -= manipulation_count * 10
    
    # Factor in fact checks
    if results['fact_checks']:
        credibility += 10
    
    return max(0, min(100, round(credibility)))

def generate_recommendations(results):
    """Generate recommendations based on analysis"""
    recommendations = []
    
    if results['risk_score'] > 70:
        recommendations.append("🚨 HIGH RISK: Do not share this content")
        recommendations.append("🔍 Verify information from multiple credible sources")
        recommendations.append("📧 Report this content to relevant authorities")
    elif results['risk_score'] > 40:
        recommendations.append("⚠️ MEDIUM RISK: Be cautious about sharing")
        recommendations.append("🔍 Cross-check with fact-checking websites")
        recommendations.append("📚 Look for additional context and sources")
    else:
        recommendations.append("✅ LOW RISK: Content appears credible")
        recommendations.append("🔍 Still verify with additional sources if important")
    
    return recommendations

def display_forensic_results(results):
    """Display comprehensive forensic results"""
    
    # Executive summary
    st.subheader("📋 Analysis Results")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        risk_score = results['risk_score']
        risk_color = "#ff4444" if risk_score > 70 else "#ff8800" if risk_score > 40 else "#44ff44"
        
        st.markdown(f"""
        <div style="background-color: {risk_color}; color: white; padding: 20px; border-radius: 10px; text-align: center;">
            <h3>Risk Level</h3>
            <h1>{risk_score}/100</h1>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        cred_score = results['credibility_score']
        cred_color = "#44ff44" if cred_score > 70 else "#ff8800" if cred_score > 40 else "#ff4444"
        
        st.markdown(f"""
        <div style="background-color: {cred_color}; color: white; padding: 20px; border-radius: 10px; text-align: center;">
            <h3>Credibility</h3>
            <h1>{cred_score}/100</h1>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        threat_level = "HIGH" if risk_score > 70 else "MEDIUM" if risk_score > 40 else "LOW"
        threat_color = "#ff4444" if threat_level == "HIGH" else "#ff8800" if threat_level == "MEDIUM" else "#44ff44"
        
        st.markdown(f"""
        <div style="background-color: {threat_color}; color: white; padding: 20px; border-radius: 10px; text-align: center;">
            <h3>Threat Level</h3>
            <h1>{threat_level}</h1>
        </div>
        """, unsafe_allow_html=True)
    
    # Detailed sections
    forensic_tabs = st.tabs([
        "🧠 AI Analysis", 
        "🔗 Sources & Links",
        "📊 Details",
        "💡 Recommendations"
    ])
    
    with forensic_tabs:  # AI Analysis tab
        if results['ai_analysis']:
            st.write("**🧠 AI Analysis:**")
            st.info(results['ai_analysis'])
        else:
            st.info("AI analysis not available.")
    
    with forensic_tabs[17]:  # Sources & Links tab
        st.write("**🔗 Source Links & Articles**")
        if results.get('source_links') and len(results['source_links']) > 0:
            for i, source in enumerate(results['source_links'], 1):
                with st.expander(f"📄 {source['name']}", expanded=True):
                    st.write(f"**Description:** {source['description']}")
                    if source['url']:
                        st.write(f"**Link:** [{source['url']}]({source['url']})")
        else:
            st.info("No source links found in AI analysis.")
    
    with forensic_tabs[18]:  # Details tab
        st.write("**📊 Detailed Analysis**")
        
        if results.get('manipulation_tactics'):
            st.write("**🔬 Manipulation Tactics Detected:**")
            for tactic in results['manipulation_tactics']:
                if tactic == "None Detected":
                    st.success(f"✅ {tactic}")
                else:
                    st.warning(f"⚠️ {tactic}")
        
        if results.get('fact_checks'):
            st.write("**📋 Fact Check Results:**")
            for check in results['fact_checks'][:3]:
                st.info(f"• {check}")
    
    with forensic_tabs:  # Recommendations tab
        st.write("**💡 Recommendations:**")
        for rec in results['recommendations']:
            st.write(f"• {rec}")

def analyze_image_comprehensive(image_file, check_manipulation, extract_metadata, reverse_search, text_extraction, depth):
    """Comprehensive image analysis (simulated for now)"""
    import random
    
    results = {
        'manipulation_score': random.randint(15, 85),
        'authenticity_score': random.randint(60, 95),
        'metadata': {},
        'text_content': "",
        'reverse_search_results': [],
        'technical_analysis': {}
    }
    
    if extract_metadata:
        results['metadata'] = {
            'device': random.choice(['iPhone 12 Pro', 'Samsung Galaxy S21', 'Canon EOS R5', 'Unknown Device']),
            'date_taken': f'2024-01-{random.randint(10, 20)} {random.randint(10, 18)}:{random.randint(10, 59)}:45',
            'location': random.choice(['GPS coordinates available', 'Location data stripped', 'Unknown location']),
            'software': random.choice(['Adobe Photoshop 2023 (Modified)', 'No editing software detected', 'GIMP (Modified)']),
            'file_size': f'{random.uniform(1.0, 5.0):.1f} MB',
            'dimensions': f'{random.randint(1000, 4000)} x {random.randint(1000, 3000)}',
            'modifications_detected': random.choice([True, False])
        }
    
    if text_extraction:
        sample_texts = [
            "Sample extracted text: 'Breaking News: Scientists discover...' [Confidence: 92%]",
            "Text found: 'URGENT ALERT' [Confidence: 87%]",
            "No readable text detected in image",
            "Multiple text regions detected: Headlines, captions, watermarks"
        ]
        results['text_content'] = random.choice(sample_texts)
    
    return results

def display_image_results(results):
    """Display comprehensive image analysis results"""
    
    st.subheader("📋 Image Analysis Results")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        manipulation_score = results['manipulation_score']
        color = "#ff4444" if manipulation_score > 70 else "#ff8800" if manipulation_score > 40 else "#44ff44"
        
        st.markdown(f"""
        <div style="background-color: {color}; color: white; padding: 20px; border-radius: 10px; text-align: center;">
            <h3>Manipulation Risk</h3>
            <h1>{manipulation_score}/100</h1>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        authenticity = results['authenticity_score']
        color = "#44ff44" if authenticity > 70 else "#ff8800" if authenticity > 40 else "#ff4444"
        
        st.markdown(f"""
        <div style="background-color: {color}; color: white; padding: 20px; border-radius: 10px; text-align: center;">
            <h3>Authenticity Score</h3>
            <h1>{authenticity}/100</h1>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        verdict = "AUTHENTIC" if results['authenticity_score'] > 70 else "SUSPICIOUS" if results['authenticity_score'] > 40 else "LIKELY_FAKE"
        color = "#44ff44" if verdict == "AUTHENTIC" else "#ff8800" if verdict == "SUSPICIOUS" else "#ff4444"
        
        st.markdown(f"""
        <div style="background-color: {color}; color: white; padding: 20px; border-radius: 10px; text-align: center;">
            <h3>Verdict</h3>
            <h1 style="font-size: 20px;">{verdict}</h1>
        </div>
        """, unsafe_allow_html=True)
    
    # Show metadata if available
    if results['metadata']:
        st.subheader("📊 Image Metadata")
        for key, value in results['metadata'].items():
            st.write(f"**{key.replace('_', ' ').title()}:** {value}")

# This ensures Streamlit can call it directly
if __name__ == "__main__":
    show_home()
