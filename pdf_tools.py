
import os
from PyPDF2 import PdfWriter, PdfReader, PdfFileMerger, PdfFileReader, PdfFileWriter

def split_pdf():
	if not os.path.isfile(file_name):
		print(f"The file {file_name} does not exist.")
	else:
		inputpdf = PdfReader(open(file_name, "rb"))

		for i in range(0, 6):
			writer = PdfWriter()
			writer.add_page(inputpdf.getPage(i))
			with open("%s-page%s.pdf" % (file_name, i), "wb") as output_pdf:
				writer.write(output_pdf)

		# Merge the split PDF files
		merge_pdf = PdfFileMerger()

		for i in range(0, 6):
			merge_pdf.append(open("%s-page%s.pdf" % (file_name, i), "rb"))

		with open("merged_%s" % file_name, "wb") as output_pdf:
			merge_pdf.write(output_pdf)

def pdf_splitter(path):
	fname = os.path.splitext(os.path.basename(path))[0]
	print()
	pdf = PdfFileReader(path)
	for page in range(pdf.getNumPages()):
		pdf_writer = PdfFileWriter()
		pdf_writer.addPage(pdf.getPage(page))
		output_filename = '{}_page_{}.pdf'.format(
			fname, page+1)
		with open(output_filename, 'wb') as out:
			pdf_writer.write(out)
			print('Created: {}'.format(output_filename))

if __name__ == "__main__": 
	file_name = input("Enter the name of the PDF file to split: ").strip()
	pdf_splitter(file_name)
