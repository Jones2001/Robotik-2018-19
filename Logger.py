class Logger:
	def __init__(self, File):
		import xlsxwriter
		workbook = xlsxwriter.Workbook(File)
		worksheet = workbook.add_worksheet()
		self.workbook = workbook
		self.worksheet = worksheet
	def write(self, row, column, content):
		self.worksheet.write(str(row) + str(column), str(content))
	def writeArray(self, row, content):
		for i in range(len(content)):
			self.worksheet.write(str(row) + str(i + 1), content[i])
	def close(self):
		self.workbook.close()