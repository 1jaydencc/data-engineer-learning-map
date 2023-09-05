import streamlit as st
import SessionState

def render_mermaid_chart(diagram_code):
    with open("mermaid_component/mermaid_component.html", "r") as f:
        html_code = f.read().replace("{{ diagram_code }}", diagram_code)
    components.html(html_code, height=800)

# Data
milestones = {
    'Milestone 1': {
        'Tasks': {
            'Task 1': ['Course 1', 'Course 2'],
            'Task 2': ['Course 3']
        }
    },
    'Milestone 2': {
        'Tasks': {
            'Task 3': ['Course 4', 'Course 5'],
            'Task 4': []
        }
    }
}

# Create a session state for user's progress
session_state = SessionState.get(progress={})

# Display data
for milestone, details in milestones.items():
    st.markdown(f"### ➡️ {milestone}")
    
    tasks = details['Tasks']
    for task, courses in tasks.items():
        task_status = session_state.progress.get(task, False)
        session_state.progress[task] = st.checkbox(task, value=task_status)
        
        # Display linked courses
        for course in courses:
            course_status = session_state.progress.get(course, False)
            session_state.progress[course] = st.checkbox(course, value=course_status, key=course)
