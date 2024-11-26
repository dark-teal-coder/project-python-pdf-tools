
import os
from PyPDF2 import PdfReader, PdfWriter


def merge_pdfs(pdf_files_list, output_folder_name): 
	merger = PdfWriter()
	for pdf in pdf_files_list:
		merger.append(pdf)
	merger.write(f".//{output_folder_name}//Merged PDF.pdf")
	merger.close()

def split_pdf(input_folder_name, output_folder_name, input_file_split): 
	with open(f".//{input_folder_name}//{input_file_split}", 'rb') as infile:
		pdf_reader = PdfReader(infile)
		## Get the total number of pages in the PDF file
		page_total = len(pdf_reader.pages)
		## Remove file extension from file name
		input_file_split_no_ext = os.path.splitext(input_file_split)[0]
		for num in range(page_total):
			pdf_writer = PdfWriter()
			pdf_writer.add_page(pdf_reader.pages[num])
			with open(f".//{output_folder_name}//{input_file_split_no_ext} - page{num+1}.pdf", 'wb') as outfile:
				pdf_writer.write(outfile)

if __name__ == "__main__": 
	## Print menu function options
	menu_message = """What would you like to do with your PDF file(s)? 
	1.) Merge PDF files
	2.) Split a PDF file
	Please input the option number here: """
	option = int(input(menu_message).strip())
	## Create input and output folders if they don't yet exist 
	input_folder_name = "input"
	output_folder_name = "output"
	if not os.path.exists(input_folder_name):
		os.makedirs(input_folder_name)
	if not os.path.exists(output_folder_name):
		os.makedirs(output_folder_name)
	## Function menu
	## Function 1: merge PDF files
	if option == 1: 
		print("Please put all the PDF files in the \"input\" folder.")
		## Get the names of the PDF files to be merged and add the folder name to the front of them  
		input_files_list = os.listdir(f".//{input_folder_name}")
		input_files_list_dir_name = [f".//{input_folder_name}//{input_f}" for input_f in input_files_list]
		merge_pdfs(input_files_list_dir_name, output_folder_name)
	## Function 2: split PDF file
	elif option == 2:
		input_file_split = input("Please enter the PDF file name to split with its extension (e.g., \"file-name.pdf\"): ").strip()
		if not os.path.isfile(f".//{input_folder_name}//{input_file_split}"):
			## Check if the input file exists.
			print(f"The file \"{input_file_split}\" does not exist in the \"input\" folder.")
		else: 
			split_pdf(input_folder_name, output_folder_name, input_file_split)
