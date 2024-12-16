import streamlit as st
# import pandas as pd
# from datetime import datetime
# import requests
from analytics_ui import analytics_tab
from add_update_ui import add_update_tab
# st.title("Expense Managment System")
# expense_dt=st.date_input("Expense Date:")
# if expense_dt:
#     st.write(f"Fetching expenses for {expense_dt}")
#Text elements
# st.header("Strramlit Core Features")
# st.subheader("Text Elements")
# st.text("This is a simple text element.")


# #data display
# st.subheader("Data Display")
# st.write("Here is a simple table:")
# df=pd.DataFrame({
#     "Date":["2024-08-01","2024-08-02","2024-08-03"],
#     "Amount":[250,134,340]
# })
# st.table(df)
# #Charts
# st.subheader("Charts")
# st.line_chart([1,2,3,4])

# #User Input
# st.subheader("User Input")
# value=st.slider("Select a Value",0,100)
# st.write(f"Selected Value:{value}")

# st.title("Interactive Widgets Example")
# #Checkbox
# if st.checkbox("Show/Hide"):
#     st.write("CheckBox Is Checked")

# #selectbox
# option=st.selectbox("Category",["Rent","Food","Groceries"],label_visibility="collapsed")
# st.write(f"You Selected{option}")
# #Multiselect
# options=st.multiselect("Select multiple numbers",[1,2,3])
# st.write(f"You Selected:{options}")

# API_URL="http://localhost:8000"
st.title("Expense tracking System")
tab1,tab2=st.tabs(["Add/Update","Analytics"])

with tab1:
    add_update_tab()
with tab2:
    analytics_tab()
    