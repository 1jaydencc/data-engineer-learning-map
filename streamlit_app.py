import streamlit as st
import streamlit.components.v1 as components

def render_mermaid_chart(diagram_code):
    with open("mermaid_component/mermaid_component.html", "r") as f:
        html_code = f.read().replace("{{ diagram_code }}", diagram_code)
    components.html(html_code, height=800)

st.title("Learning Path")

sub_items_task1 = ["Architecture overview", "Data engineering life cycle", "Data storage capabilities"]

# Initial setup for session state variables
if 'getting_started_checked' not in st.session_state:
    st.session_state.getting_started_checked = False

if 'sub_items_checked' not in st.session_state:
    st.session_state.sub_items_checked = [False] * len(sub_items_task1)

# Capture the previous state of "Getting Started"
prev_getting_started_checked = st.session_state.getting_started_checked

# Checkbox for "Getting Started"
getting_started_checked = st.checkbox("Getting Started", value=st.session_state.getting_started_checked)

# Logic for the main task and its sub-items
user_changed_getting_started = prev_getting_started_checked != getting_started_checked

if user_changed_getting_started and getting_started_checked:
    st.session_state.sub_items_checked = [True] * len(sub_items_task1)
elif user_changed_getting_started and not getting_started_checked:
    st.session_state.sub_items_checked = [False] * len(sub_items_task1)

all_sub_items_checked = True
for i, sub_item in enumerate(sub_items_task1):
    # Use Markdown for indented display, and then display the checkbox without the label
    st.markdown(f"   - {sub_item}", unsafe_allow_html=True)  # 3 spaces for indentation
    sub_item_checked = st.checkbox("", key=f"subitem_{i}", value=st.session_state.sub_items_checked[i])

    if sub_item_checked != st.session_state.sub_items_checked[i]:
        st.session_state.sub_items_checked[i] = sub_item_checked

    if not sub_item_checked:
        all_sub_items_checked = False

if all_sub_items_checked and not getting_started_checked:
    getting_started_checked = True

st.session_state.getting_started_checked = getting_started_checked

# Generate the mermaid diagram
diagram_code = "graph TD\n"
task1_id = "B0"
diagram_code += f'{task1_id}["Getting Started {"(Done)" if st.session_state.getting_started_checked else ""}"]\n'

# Nodes for sub-items of "Getting Started"
sub_node_prefix = f"{task1_id}S"
for j, sub_item in enumerate(sub_items_task1):
    sub_node_id = f"{sub_node_prefix}{j}"
    diagram_code += f'{sub_node_id}["{sub_item} {"(Done)" if st.session_state.sub_items_checked[j] else ""}"]\n'
    diagram_code += f"{task1_id} --> {sub_node_id}\n"

render_mermaid_chart(diagram_code)
