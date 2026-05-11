import streamlit as st
import pandas as pd

st.title("Operations Task Tracker")
st.write("An operations dashboard built to manage workflows, task priorities, and team efficiency.")

# Connects dashboard to live Google Sheets data
csv_url = "https://docs.google.com/spreadsheets/d/1-TJMiKBmXjccU15YGNRnyud9eCNTAnuqyNK_qXbeQ6E/export?format=csv&gid=0"

df = pd.read_csv(csv_url)

st.subheader("Task Overview")
st.dataframe(df)

st.subheader("Key Metrics")

total_tasks = len(df)
completed_tasks = len(df[df["Status"] == "Completed"])
pending_tasks = len(df[df["Status"] == "Pending"])
in_progress_tasks = len(df[df["Status"] == "In Progress"])
high_priority = len(df[df["Priority"] == "High"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Tasks", total_tasks)
col2.metric("Completed", completed_tasks)
col3.metric("Pending", pending_tasks)
col4.metric("High Priority", high_priority)

st.subheader("Filter Tasks")

status_filter = st.selectbox(
    "Filter by Status",
    ["All", "Completed", "Pending", "In Progress"]
)

if status_filter != "All":
    filtered_df = df[df["Status"] == status_filter]
else:
    filtered_df = df

st.dataframe(filtered_df)

st.subheader("Workload by Department")

df["Hours Needed"] = pd.to_numeric(df["Hours Needed"], errors="coerce")
workload = df.groupby("Department")["Hours Needed"].sum()

st.bar_chart(workload)

st.subheader("Operations Insight")

if pending_tasks > completed_tasks:
    st.write("There are more pending tasks than completed tasks. The team may need to prioritize unfinished work.")
else:
    st.write("Task progress looks balanced. Operations are moving efficiently.")