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

# Custom CSS for modern styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .tab-content {
        padding: 1rem;
        border-radius: 10px;
        background-color: #f8f9fa;
        margin-bottom: 1rem;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px;
    }
    .stTextArea>textarea {
        border-radius: 5px;
        border: 1px solid #ddd;
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