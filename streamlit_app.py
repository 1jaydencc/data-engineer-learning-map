import streamlit as st
import streamlit.components.v1 as components

def render_mermaid_chart(diagram_code):
    with open("mermaid_component/mermaid_component.html", "r") as f:
        html_code = f.read().replace("{{ diagram_code }}", diagram_code)
    components.html(html_code, height=800)

st.title("Learning Path")

sub_items_task1 = ["Architecture overview", "Data engineering life cycle", "Data storage capabilities"]

# Check if state variables are initialized or not
if 'getting_started_checked' not in st.session_state:
    st.session_state.getting_started_checked = False

if 'sub_items_checked' not in st.session_state:
    st.session_state.sub_items_checked = [False] * len(sub_items_task1)

# If "Getting Started" is checked, all sub-items should be checked
if st.session_state.getting_started_checked:
    st.session_state.sub_items_checked = [True] * len(sub_items_task1)

# Checkbox for "Getting Started"
getting_started_checked = st.checkbox("Getting Started", value=st.session_state.getting_started_checked)
if getting_started_checked != st.session_state.getting_started_checked:
    st.session_state.getting_started_checked = getting_started_checked
    if getting_started_checked:
        st.session_state.sub_items_checked = [True] * len(sub_items_task1)

# Checkboxes for sub-items
all_sub_items_checked = True
for i, sub_item in enumerate(sub_items_task1):
    sub_item_checked = st.checkbox(sub_item, value=st.session_state.sub_items_checked[i])
    if sub_item_checked != st.session_state.sub_items_checked[i]:
        st.session_state.sub_items_checked[i] = sub_item_checked
    if not sub_item_checked:
        all_sub_items_checked = False

# If all sub-items are checked, "Getting Started" should be checked
if all_sub_items_checked:
    st.session_state.getting_started_checked = True

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
