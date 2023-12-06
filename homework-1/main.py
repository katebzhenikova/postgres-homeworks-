"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from read_csv import read_csv

csv_file_employees = read_csv('north_data/employees_data.csv')
csv_file_customers = read_csv('north_data/customers_data.csv')
csv_file_orders = read_csv('north_data/orders_data.csv')


# создаем соединение с БД
conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='112233'
)


try:
    with conn:
        with conn.cursor() as cur:
            # выполняем запрос
            cur.executemany('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', csv_file_employees)
            cur.execute('SELECT * FROM employees')

        with conn.cursor() as cur:
            # выполняем запрос
            cur.executemany('INSERT INTO customers VALUES (%s, %s, %s)', csv_file_customers)
            cur.execute('SELECT * FROM customers')

        with conn.cursor() as cur:
            # выполняем запрос
            cur.executemany('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', csv_file_orders)
            cur.execute('SELECT * FROM orders')

finally:
    conn.close()
