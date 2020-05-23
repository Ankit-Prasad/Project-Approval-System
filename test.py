import unittest
import module, services
import sqlite3, os
from flask import session

class TestApp(unittest.TestCase):

	def test_studentlogin(self):
		print('\nTesting "Student Login" module...')
		status = services.student_login('MT2019020', '1234')
		self.assertEqual(status, True)
		status = services.student_login('MT2019020', '12345')
		self.assertEqual(status, False)
		status = services.student_login('MT2019021', '1234')
		self.assertEqual(status, False)
		status = services.student_login('', '')
		self.assertEqual(status, False)
		print('''Passed''')


	def test_studentregister(self):
		print('\nTesting "Student Register" module...')
		status = services.student_register('MT2019000','New User','newuser@iiitb.org','password')
		self.assertEqual(status, True)

		status = services.student_register('MT2019000','New User','newuser@iiitb.org','password')
		self.assertEqual(status, False)
		
		connection = sqlite3.connect('project_approval.db')
		crsr = connection.cursor()
		t = crsr.execute('DELETE FROM Student WHERE Name = ?', ('New User',))
		connection.commit()
		print('''Passed''')


	def test_facultylogin(self):
		print('\nTesting "Faculty Login" module...')
		status = services.faculty_login('1', '1234')
		self.assertEqual(status, True)
		status = services.faculty_login('1', '12345')
		self.assertEqual(status, False)
		status = services.faculty_login('MT2019021', '1234')
		self.assertEqual(status, False)
		status = services.faculty_login('', '')
		self.assertEqual(status, False)
		print('''Passed''')


	def test_facultyregister(self):
		print('\nTesting "Faculty Register" module...')
		status = services.faculty_register('0','New User','newuser0@iiitb.org','password')
		self.assertEqual(status, True)

		status = services.faculty_register('0','New User','newuser0@iiitb.org','password')
		self.assertEqual(status, False)
		
		connection = sqlite3.connect('project_approval.db')
		crsr = connection.cursor()
		t = crsr.execute('DELETE FROM Faculty WHERE F_Id = ?', ('0',))
		connection.commit()
		print('''Passed''')


	def test_talogin(self):
		print('\nTesting "TA Login" module...')
		status = services.ta_login('MT2019020', '1234')
		self.assertEqual(status, True)
		status = services.ta_login('MT2019020', '12345')
		self.assertEqual(status, False)
		status = services.ta_login('MT2019000', '1234')
		self.assertEqual(status, False)
		status = services.ta_login('', '')
		self.assertEqual(status, False)
		print('''Passed''')


if __name__ == '__main__':
    unittest.main()