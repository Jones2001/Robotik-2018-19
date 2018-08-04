class Logger:
	def __init__(self, File):
		import xlsxwriter
		workbook = xlsxwriter.Workbook(File)
		worksheet = workbook.add_worksheet()
		self.workbook = workbook
		self.worksheet = worksheet
	def write(self, row, column, content):
		self.worksheet.write(str(row) + str(column), str(content))
	def close(self):
		self.workbook.close()