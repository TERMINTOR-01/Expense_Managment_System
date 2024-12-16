import mysql.connector
from contextlib import contextmanager
import logging
from logging_setup import setup_logger  
logger=setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit=False):
    connection=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Root",
        database="expense_manager"
    )
    cursor=connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()   #when we add new data
    cursor.close()
    connection.close()

def fetch_all_record():
    with get_db_cursor(commit=False) as cursor:
        cursor.execute("Select * From Expenses")
        expenses=cursor.fetchall()
        for expense in expenses:
            print(expense)

def fetch_expenses_for_the_date(expense_date):
    logger.info(f"fetch expenses_for_date called with {expense_date}")
    with get_db_cursor(commit=False) as cursor:
        cursor.execute("Select * From Expenses where expense_date=%s",(expense_date,))
        expenses=cursor.fetchall()
        return expenses

def insert_expense(expense_date,amount,category,notes):
    logger.info(f"insert_expense called with {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("INSERT INTO expenses (expense_date,amount,category,notes) VALUES (%s,%s,%s,%s)",
                       (expense_date,amount,category,notes))
def delete_expense_for_date(expense_date):
    logger.info(f"delete_expense_for_date called with {expense_date}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("Delete From expenses where expense_date=%s",(expense_date,))

def fetch_expense_summary(start_date,end_date):
    logger.info(f"fetch expense summary called with start:{start_date} end:{end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''SELECT category,sum(amount) as total FROM expenses
            WHERE expense_date BETWEEN %s and %s
           group by category
            
        ''',(start_date,end_date)
        )
        data=cursor.fetchall()
        return data



if __name__=="__main__":
    expenses=fetch_expenses_for_the_date("2024-09-30")
    print(expenses)
    # insert_expense("2024-08-25",40,"Food","Eat Tasty Samosa Chat")
    # expenses=fetch_expenses_for_the_date("2024-08-25")
    # print(expenses)
    # delete_expense_for_date("2024-08-25")
    # expenses=fetch_expenses_for_the_date("2024-08-25")
    # print(expenses)
    summary=fetch_expense_summary("2024-08-01","2024-08-05")
    for record in summary:
        print(record)


