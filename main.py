import streamlit as st
import base64
import codecs

# Set page config for modern look
st.set_page_config(
    page_title="Obfuscation Tool",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded"
)

def rot13(text):
    return codecs.encode(text, 'rot_13')

# Custom CSS for modern dark styling
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    :root {
        --primary-gradient: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        --glass-bg: rgba(255, 255, 255, 0.9);
        --glass-border: rgba(0, 0, 0, 0.1);
        /* Light theme colors for black text readability */
        --text-primary: #000000;
        --text-secondary: #374151;
        --text-muted: #6b7280;
        --text-accent: #667eea;
        --bg-primary: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 50%, #cbd5e1 100%);
    }
    
    * {
        font-family: 'Inter', sans-serif;
    }
    
    .main {
        background: var(--bg-primary);
        min-height: 100vh;
        color: var(--text-secondary);
    }
    
    .main-header {
        background: var(--primary-gradient);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
        text-shadow: 0 4px 8px rgba(0,0,0,0.3);
    }
    
    .tab-content {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 2rem;
        margin-bottom: 1.5rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        border: 1px solid rgba(0, 0, 0, 0.1);
    }
    
    .stButton>button {
        background: var(--primary-gradient);
        color: var(--text-primary);
        border: none;
        border-radius: 12px;
        padding: 1rem 2rem;
        font-size: 1rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.5);
    }
    
    .stTextArea>textarea {
        border-radius: 12px;
        border: 2px solid var(--glass-border);
        background: rgba(255, 255, 255, 0.8);
        color: var(--text-primary);
        backdrop-filter: blur(5px);
        padding: 1rem;
        font-size: 1rem;
    }
    
    .stTextArea>textarea::placeholder {
        color: var(--text-muted);
    }
    
    .stSelectbox > div > div {
        background: rgba(255, 255, 255, 0.8);
        border: 1px solid var(--glass-border);
        border-radius: 12px;
        backdrop-filter: blur(5px);
    }
    
    .stSelectbox > div > div > div > div {
        color: var(--text-primary);
    }
    
    .stSuccess, .stInfo, .stWarning, .stError {
        border-radius: 12px;
        border: none;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
        backdrop-filter: blur(5px);
        color: var(--text-primary) !important;
    }
    
    /* Ensure all text has proper contrast */
    .stMarkdown, .stText, p, span, div {
        color: var(--text-secondary) !important;
    }
    
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: var(--text-primary) !important;
    }
    
    /* Ensure form labels are readable */
    label {
        color: var(--text-secondary) !important;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🔧 Settings")
    st.markdown("---")
    method = st.selectbox(
        "Choose obfuscation method:",
        ["Base64", "ROT13"],
        help="Select the method to use for obfuscation and deobfuscation."
    )
    st.markdown("---")
    st.markdown("**About:**")
    st.markdown("This app helps you obfuscate and deobfuscate text using reversible methods.")

# Main content
st.markdown('<h1 class="main-header">🔒 Obfuscation & Deobfuscation Tool</h1>', unsafe_allow_html=True)
st.markdown("Secure your text with reversible obfuscation methods. Choose your method in the sidebar.")

col1, col2 = st.columns(2)

with col1:
    with st.container():
        st.markdown("### 📝 Obfuscate Text")
        text = st.text_area("Enter the text to obfuscate:", height=200, key="obfuscate_input")
        if st.button("🚀 Obfuscate", key="obfuscate_btn"):
            if text.strip():
                if method == "Base64":
                    obfuscated = base64.b64encode(text.encode('utf-8')).decode('utf-8')
                elif method == "ROT13":
                    obfuscated = rot13(text)
                st.success("Text obfuscated successfully!")
                st.text_area("Obfuscated Text:", value=obfuscated, height=200, key="obfuscate_output")
            else:
                st.warning("⚠️ Please enter some text to obfuscate.")

with col2:
    with st.container():
        st.markdown("### 🔓 Deobfuscate Text")
        obf_text = st.text_area("Enter the obfuscated text to deobfuscate:", height=200, key="deobfuscate_input")
        if st.button("🔄 Deobfuscate", key="deobfuscate_btn"):
            if obf_text.strip():
                try:
                    if method == "Base64":
                        original = base64.b64decode(obf_text).decode('utf-8')
                    elif method == "ROT13":
                        original = rot13(obf_text)
                    st.success("Text deobfuscated successfully!")
                    st.text_area("Original Text:", value=original, height=200, key="deobfuscate_output")
                except Exception as e:
                    st.error(f"❌ Error deobfuscating: {str(e)}. Make sure the input matches the selected method.")
            else:
                st.warning("⚠️ Please enter some obfuscated text to deobfuscate.")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | [GitHub](https://github.com/streamlit/streamlit)")
