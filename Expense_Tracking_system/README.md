# Expense Managment System
This Project Is an Expense Managment System That Consists of a Streamlit Application and a FastApi backend Server

## Project Structure
**Frontend**:Contains the Streamlit application code.

**Backend**:Contains the FASTAPI backend server code.
**requirments.txt**:List The requird Python Packages. 

## Setup Instructions
1.**Clone the repository**:
```bash 
git clone https://github.com/TERMINTOR-01/expense-managment-system
cd expense-management-system
```
1. **Install Dependencies:**:
```commandline
pip install -r requirments.txt
```
1.. ** Run The FastApi Server:**:
```commandline
uvicorn server.server:app --reload
```
1. **Run The Stramlit app:**:
```commandline
streamlit run frontend/app.py
```