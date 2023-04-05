## sql lite
# import sql lite
import sqlite3

# use ':memory:' for temp db in memory or db file name for saved db
conn = sqlite3.connect(':memory:')
# conn = sqlite3.connect('sample_db.db')

# cursor is used to execute sql commands
c = conn.cursor()

# executes sql commands
c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")

def insert_employee(employee):
    # use with to have connection commit automatically
    with conn:
        # can use tuple as second argument for method to specify values
        # c.execute("INSERT INTO employees VALUES (?, ?, ?)", (first_name, last_name, pay_amount))
        # can use object as second argument for for method by sepcifying keys
        c.execute("INSERT INTO employees VALUES (:first, :last, :pay)",
            {'first': employee.first, 'last': employee.last, 'pay': employee.pay})


def get_employee_by_name(last_name):
    with conn:
        c.execute("SELECT * FROM employees WHERE last=:last",
            {'last': last_name})
        return c.fetchall()

def update_pay(employee, pay):
    with conn:
        c.execute("UPDATE employees SET pay=:pay WHERE first=:first AND last=:last",
            {'first': employee.first, 'last': employee.last, 'pay': pay})
        c.execute("SELECT * FROM employees WHERE first=:first, last=:last",
            {'first': employee.first, 'last': employee.last})
        return c.fetchone()

def remove_employee(employee):
    with conn:
        c.execute("SELECT * FROM employees WHERE first=:first, last=:last",
            {'first': employee.first, 'last': employee.last})
        removed = c.fetchone()
        c.execute("DELETE FROM employees WHERE first=:first, last=:last",
            {'first': employee.first, 'last': employee.last})
        return removed


# commits all previous code
# conn.commit()

# closes connection to database
conn.close()