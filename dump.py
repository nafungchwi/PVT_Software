import sqlite3
con = sqlite3.connect('pseudocomponents.db')

f = open('dump.sql','w')
for line in con.iterdump():
    f.write('%s\n' % line)
f.close()