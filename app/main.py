import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from rag.generator import get_qa_chain

# Page config
st.set_page_config(
    page_title="DBMS AI Assistant",
    page_icon="📚",
    layout="wide"
)

# Custom CSS (🔥 makes it sexy)
st.markdown("""
<style>
    .main {
        background-color: #0E1117;
    }
    .stChatMessage {
        border-radius: 10px;
        padding: 10px;
        margin-bottom: 10px;
    }
    .stChatMessage.user {
        background-color: #1f77b4;
    }
    .stChatMessage.assistant {
        background-color: #262730;
    }
</style>
""", unsafe_allow_html=True)

# Title
st.title("📚 DBMS AI Assistant")
st.caption("Your personal AI tutor for Database Management Systems")

# Load model
@st.cache_resource
def load_qa():
    return get_qa_chain()

qa = load_qa()

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input
query = st.chat_input("Ask your DBMS doubt...")

if query:
    # User message
    st.chat_message("user").markdown(query)
    st.session_state.messages.append({"role": "user", "content": query})

    # Loading spinner
    with st.spinner("Thinking... 🤔"):
        result = qa(query)

    answer = result["answer"]
    sources = list(set(result["sources"]))

    # Format response
    formatted_response = answer

    if sources:
        formatted_response += "\n\n---\n📚 **Sources:**\n"
        for src in sources:
            formatted_response += f"- {src}\n"

    # Assistant message
    with st.chat_message("assistant"):
        st.markdown(formatted_response)

    st.session_state.messages.append({
        "role": "assistant",
        "content": formatted_response
    })

with st.sidebar:
    st.title("⚙️ Settings")

    st.markdown("### About")
    st.write("This AI assistant is trained on DBMS course material.")

    st.markdown("### Tips")
    st.write("""
    - Ask specific questions  
    - Mention topic (e.g., indexing, normalization)  
    - Avoid vague queries  
    """)