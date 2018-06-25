import sqlite3
from share import begin, end

def main(n=99, init=None):
    conn = sqlite3.connect('frequency.db')
    curs = conn.cursor()

    curs.execute(f'select * from stocks where word0 = "{init if init else begin}" order by random() limit 1')
    [row] = curs.fetchall()
    w0 = row[1]
    w1 = row[2]
    sentence = ""
    if init:
        sentence += init
    sentence += w0 + ("" if w1 == row[2] else w1)

    for i in range(n):
        try:
            curs.execute(f'select * from stocks where word0 = "{w0}" and word1 = "{w1}" order by random() limit 1')
            [row] = curs.fetchall()
            if row[2] == end:
                break
            sentence += row[2]
            w0, w1 = w1, row[2]
        except Exception as e:
            print(e)
            break
    conn.close()

    return sentence

if __name__ == '__main__':
    print(main())