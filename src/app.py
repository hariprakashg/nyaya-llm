import streamlit as st
from src.engine import get_legal_answer

st.set_page_config(page_title="Nyaya-LLM", page_icon="⚖️", layout="centered")

st.title("⚖️ Nyaya-LLM: Offline Legal Assistant")
st.markdown("**Powered by Bhartiya Nyaya Sanhita (BNS) 2023** | 100% Offline & Private")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_query := st.chat_input("Ex: What is the punishment for cyber crime?"):
    
    st.session_state.messages.append({"role": "user", "content": user_query})
    with st.chat_message("user"):
        st.markdown(user_query)

    with st.chat_message("assistant"):
        try:
            stream = get_legal_answer(user_query)
            
            full_response = st.write_stream(stream)
            
            st.session_state.messages.append({"role": "assistant", "content": full_response})
            
        except Exception as e:
            error_msg = f"⚠️ Error generating response: {e}"
            st.error(error_msg)
