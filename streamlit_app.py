import streamlit as st
import streamlit.components.v1 as components

def render_mermaid_chart(diagram_code):
    with open("mermaid_component/mermaid_component.html", "r") as f:
        html_code = f.read().replace("{{ diagram_code }}", diagram_code)
    components.html(html_code, height=800)

st.title("Data Engineering Learning Map")
# Starting point of the diagram_code
diagram_code = "graph TD\n"

# Hardcoded diagram code for "Getting Started"
task1_id = "B0"
sub_items_task1 = ["Architecture overview", "Data engineering life cycle", "Data storage capabilities"]
diagram_code += f'{task1_id}["Getting Started"]\n'

sub_node_prefix = f"{task1_id}S"
for j, sub_item in enumerate(sub_items_task1):
    sub_node_id = f"{sub_node_prefix}{j}"
    diagram_code += f'{sub_node_id}["{sub_item}"]\n'
    diagram_code += f"{task1_id} --> {sub_node_id}\n"

render_mermaid_chart(diagram_code)
