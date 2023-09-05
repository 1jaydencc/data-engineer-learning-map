import streamlit as st

class _SessionState:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)


def get(**kwargs):
    """Gets a SessionState object for the current session.
    Creates a new object if necessary."""
    if 'session_state' not in st.session_info:
        st.session_info.session_state = _SessionState(**kwargs)
    return st.session_info.session_state
