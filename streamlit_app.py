import streamlit as st
import plotly.graph_objects as go

def create_roadmap():
    milestones = ["Start", "Milestone A", "Milestone B", "Milestone C", "Finish"]

    # Construct the figure
    fig = go.Figure()

    # Add a scatter plot for milestones
    fig.add_trace(go.Scatter(
        x=list(range(len(milestones))),
        y=[1] * len(milestones),
        mode="markers+text",
        name="Milestones",
        text=milestones,
        textposition="bottom center"
    ))

    # Customize layout
    fig.update_layout(
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor='white'
    )

    return fig

def display_learning_path():
    st.title("Learning Path Roadmap")

    roadmap_fig = create_roadmap()
    st.plotly_chart(roadmap_fig)

    st.write("## Tasks & Courses per Milestone")
    
    # Example tasks & courses for each milestone
    tasks_courses = {
        "Milestone A": {
            "tasks": ["Task A1", "Task A2"],
            "courses": ["Course A1", "Course A2"]
        },
        "Milestone B": {
            "tasks": ["Task B1"],
            "courses": ["Course B1", "Course B2", "Course B3"]
        },
        # ... add more as needed
    }

    for milestone, data in tasks_courses.items():
        st.write(f"### {milestone}")
        st.write("Tasks:")
        for task in data["tasks"]:
            checkbox_key = f"task_{milestone}_{task}"
            st.checkbox(task, key=checkbox_key)
        st.write("Courses:")
        for course in data["courses"]:
            st.write(f"- {course}")

if __name__ == "__main__":
    display_learning_path()
