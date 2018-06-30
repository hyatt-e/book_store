import sqlite3
from tkinter import messagebox as tkMessageBox


class Database:

	def __init__(self, db):
		self.conn = sqlite3.connect(db)
		self.cur = self.conn.cursor()
		self.cur.execute('CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)')
		self.conn.commit()
		self.conn.close()


	# pop up confirmation
	def popmessage(self, action):
		#	Pop-up confirmation
		# action will fill Window Title and action-specific message
		answer = tkMessageBox.askyesno("{}".format(action), "Are you sure you want to {} this record?".format(action))
		if answer == True:
			self.conn.commit()
			self.conn.close()
		else:
			pass


	def insert(self, title, author, year, isbn):
		self.conn = sqlite3.connect('books.db')
		self.cur = self.conn.cursor()
		self.cur.execute('INSERT INTO book VALUES (NULL, ?, ?, ?, ?)', (title, author, year, isbn))
		self.popmessage('INSERT')


	def view(self):
		self.conn = sqlite3.connect('books.db')
		self.cur = self.conn.cursor()
		self.cur.execute('SELECT * FROM book')
		rows = self.cur.fetchall()
		self.conn.close()
		return rows


	def search(self, title='', author='', year='', isbn=''):
		self.conn = sqlite3.connect('books.db')
		self.cur = self.conn.cursor()
		self.cur.execute('SELECT * FROM book WHERE title LIKE ?  OR author LIKE ? OR year LIKE ? OR isbn LIKE ?', (title, author, year, isbn))
		rows = self.cur.fetchall()
		self.conn.close()
		return rows


	def delete(self, id):
		self.conn = sqlite3.connect('books.db')
		self.cur = self.conn.cursor()
		self.cur.execute('DELETE FROM book WHERE id=?', (id,))
		self.popmessage('DELETE')


	def update(self, id, title='', author='', year='', isbn=''):
		self.conn = sqlite3.connect('books.db')
		self.cur = self.conn.cursor()
		self.cur.execute('UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?', (title, author, year, isbn, id))
		self.popmessage('UPDATE')


	def __del__(self):
		self.conn.close()


#__init__()

#insert('Goon', 'Fuck', 1976, 173897666)
#delete(2)
#update(4, 'Bitch')
#print(view())
#print(search(author='God'))
