"""
 Francisco Filho
 Faz conexao
 Faz leitura
 Exibe dados em tela caracter (ZIM)
  11.06.2018  18:45 github
"""
import curses
import psycopg2

conn = psycopg2.connect("host=localhost dbname=dbaxxx user=uuuuu password=ppppp")
cur = conn.cursor()
cur.execute('SELECT * FROM numerarec')
umreg = cur.fetchone()
todosreg = cur.fetchall()

# print(one)
# print(all)
# for registro in all:
#     print(registro)

myscreen = curses.initscr()
myscreen.border(2)
myscreen.addstr(2, 20, "Listagem da Tabela NumeraRec")
myscreen.addstr(3, 10, "Loja Seq   Recibo")
myscreen.addstr(3, 40, "Loja Seq   Recibo")

lin = 4
col = 10
for registro in todosreg:
    myscreen.addstr(lin, col, registro[0] + "    " + str(registro[1]) + "    " + str(registro[2]))
    if col == 10:
       col = 40
    else:
       lin = lin + 1
       col = 10

myscreen.addstr(10, 60, "Q Tecla...Para Sair")
myscreen.refresh()
myscreen.getch()
curses.endwin()
conn.close()





