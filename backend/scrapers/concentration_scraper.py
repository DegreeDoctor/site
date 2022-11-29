from PyPDF2 import PdfReader

reader = PdfReader("../template_files/csci-concentration-courses.pdf")
pages_num = len(reader.pages)

file_text = ""
for pg_num in range(pages_num):
  page = reader.pages[pg_num]
  file_text += page.extract_text().strip()

print(file_text)