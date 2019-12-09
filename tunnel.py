# auto login for putty session
import subprocess
import getpass
import sqlite3


conn = sqlite3.connect('database.db')
c = conn.cursor()
c.execute("select count(*) from table1")
n = c.fetchone()[0]
print(n)
choice = 0


def add():
    global n
    d_host = input('host: ')
    d_usr = input('usr: ')
    d_pw = getpass.getpass(prompt='pw: ')
    c.execute(f"insert into table1 values ('{n+1}', '{d_host}', '{d_usr}', '{d_pw}')")
    conn.commit()
    c.execute("select count(*) from table1")
    n = c.fetchone()[0]
    menu()


def remove():
    r_id = input('ID:')
    c.execute(f"delete from table1 where id={r_id}")
    conn.commit()
    menu()


def login():
    for row in c.execute(f"select * from table1 where id={choice}"):
        host = row[1]
        usr = row[2]
        pw = row[3]
        p = subprocess.Popen(f"putty.exe {usr}@{host} -pw {pw}").pid


def menu():
    global choice
    print('Select host or add new one\n')
    c.execute('select * from table1')
    for row in c.execute('select * from table1'):
        print(f'{row[0]}: {row[1]}')

    print(f'A. Add new host')
    print(f'R. Remove host')
    print(f'\n E. Exit')
    choice = input('\nOption: ')
    if choice.isdigit():
        choice = int(choice)
        if 0 < choice <= n:
            login()
    elif choice.lower() == 'a':
        add()
    elif choice.lower() == 'r':
        remove()
    elif choice.lower() == 'e':
        exit()


menu()


#host = input('host: ')
#usr = input('usr: ')
#pw = getpass.getpass(prompt='pw: ')
#pid = subprocess.Popen(f"putty.exe {usr}@{host} -pw {pw}").pid


