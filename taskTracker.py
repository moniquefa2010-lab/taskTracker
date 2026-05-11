import streamlit as st
import pandas as pd

st.title("Operations Task Tracker")

st.write(
    "An operations dashboard built to manage workflows, task priorities, and team efficiency."
)

csv_url = "https://docs.google.com/spreadsheets/d/1-TJMiKBmXjccU15YGNRnyud9eCNtAnuqyNK_qXbeQ6E/gviz/tq?tqx=out:csv&sheet=Sheet1"

df = pd.read_csv(csv_url)

st.subheader("Task Overview")
st.dataframe(df)

total_tasks = len(df)
completed_tasks = len(df[df["Status"] == "Completed"])
pending_tasks = len(df[df["Status"] == "Pending"])

col1, col2, col3 = st.columns(3)

col1.metric("Total Tasks", total_tasks)
col2.metric("Completed", completed_tasks)
col3.metric("Pending", pending_tasks)

st.subheader("Workload by Department")

df["Hours Needed"] = pd.to_numeric(df["Hours Needed"], errors="coerce")

workload = df.groupby("Department")["Hours Needed"].sum()

st.bar_chart(workload)