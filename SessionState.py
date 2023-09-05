import streamlit as st

class _SessionState:

    def __init__(self, **kwargs):
        """A new SessionState object."""
        for key, val in kwargs.items():
            setattr(self, key, val)


def get(**kwargs):
    """Gets a SessionState object for the current session. Creates one if necessary."""
    
    # Key we use to store a session state in the current session.
    key = '_session_state'
    
    if not hasattr(st, key):
        st._session_state = _SessionState(**kwargs)
    return st._session_state
