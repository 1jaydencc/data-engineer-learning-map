import streamlit as st
import SessionState
import streamlit.components.v1 as components

def render_mermaid_chart(diagram_code):
    with open("mermaid_component/mermaid_component.html", "r") as f:
        html_code = f.read().replace("{{ diagram_code }}", diagram_code)
    components.html(html_code, height=800)

st.title("Learning Path")

learning_path = {
    "Beginner": ["Task 1", "Task 2", "Task 3"],
    "Intermediate": ["Task 4", "Task 5"],
    "Advanced": ["Task 6", "Task 7", "Task 8", "Task 9"],
}

diagram_code = "graph TD\n"
render_mermaid_chart(diagram_code)
prev_level = None

for level, tasks in learning_path.items():
    for i, task in enumerate(tasks):
        checked = st.checkbox(task)
        node_id = f"{level[0]}{i}"
        diagram_code += f'{node_id}["{task} {"(Done)" if checked else ""}"]\n'
        if prev_level:
            diagram_code += f"{prev_level} --> {node_id}\n"
        if i > 0:
            diagram_code += f"{level[0]}{i-1} --> {node_id}\n"
    prev_level = f"{level[0]}{len(tasks)-1}"


