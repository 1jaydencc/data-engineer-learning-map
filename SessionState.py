class _SessionState:
    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)


def get(**kwargs):
    """Gets a SessionState object for the current session.
    Creates a new object if necessary."""
    if not hasattr(st, '_session_state'):
        st._session_state = _SessionState(**kwargs)
    return st._session_state
