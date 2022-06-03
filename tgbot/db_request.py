import sqlite3

def connecting():
    conn = sqlite3.connect('databases/subjects.db')
    cur = conn.cursor()
    return cur, conn

def subject_ball_from_bd(message, year):
    cur,conn = connecting()
    cur.execute(f"SELECT groups.nomer, groups.name, year_{year}.grant, year_{year}.jk, year_{year}.ak FROM groups JOIN year_{year} ON groups.nomer = year_{year}.group_nomer WHERE groups.subject = '{message}' ORDER BY groups.nomer ASC;")
    data_groups = cur.fetchall()
    cur.execute(f"SELECT spec.group_nomer, spec.name FROM spec JOIN groups ON groups.nomer = spec.group_nomer WHERE subject = '{message}' ORDER BY spec.group_nomer ASC;")
    data_spec = cur.fetchall()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name > 'year_';")
    tables = cur.fetchall()
    text = ''
    for group in data_groups:
        group = list(group)
        text = text + f"<{group[1]}>\n"
        for spec in data_spec:
            spec = list(spec)
            if spec[0] == group[0]:
                text = text + "-" + spec[1] + "-\n"  #подумай
        text = text + f"Бакалавриатқа бөлінген грант саны:{group[2]}\nЖалпы конкурс бойынша грантқа түскен минималды балл:{group[3]}\nАуылдық квотамен грантқа түскен минималды балл:{group[4]}\n\n"
    closing(conn)
    return text,tables

def closing(conn):
    conn.close()