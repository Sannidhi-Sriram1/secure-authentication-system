import streamlit as st

def is_authenticated():
    return st.session_state.get("authenticated", False)

def logout():
    st.session_state.authenticated = False
    st.session_state.username = None
