import streamlit as st

def display_learning_path():
    st.title("Learning Path for Our Team")

    progress = st.slider("Mark Your Progress:", 0, 100, 0)
    st.progress(progress)

    # Display path based on progress
    if progress < 10:
        st.write("1. Introduction to Topic A")
    if progress < 20:
        st.write("2. Workshop on Topic B")
    # ... and so forth.

if __name__ == "__main__":
    display_learning_path()
