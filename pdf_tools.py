
import os
from PyPDF2 import PdfWriter

def merge_pdfs(pdf_files_list, output_folder_name): 
	merger = PdfWriter()
	for pdf in pdf_files_list:
		merger.append(pdf)
	merger.write(f".//{output_folder_name}//Merged PDF.pdf")
	merger.close()

if __name__ == "__main__": 
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
	if option == 1: 
		## Get the names of the PDF files to be merged and add the folder name to the front of them  
		input_files_list = os.listdir(f".//{input_folder_name}")
		input_files_list_dir_name = [f".//{input_folder_name}//{input_f}" for input_f in input_files_list]
		merge_pdfs(input_files_list_dir_name, output_folder_name)
