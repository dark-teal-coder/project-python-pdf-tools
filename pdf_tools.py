
import os
from PyPDF2 import PdfWriter

def merge_pdfs(pdf_files_list, output_folder_name): 
	merger = PdfWriter()
	for pdf in pdf_files_list:
		merger.append(pdf)
	merger.write(f".//{output_folder_name}//Merged PDF.pdf")
	merger.close()

if __name__ == "__main__": 
	# file_name = input("Enter the name of the PDF file to split: ").strip()
	# pdf_splitter(file_name)
	input_folder_name = "input"
	output_folder_name = "output"
	input_files_list = os.listdir(f".//{input_folder_name}")
	input_files_list_dir_name = [f".//{input_folder_name}//{input_f}" for input_f in input_files_list]
	if not os.path.exists(output_folder_name):
		os.makedirs(output_folder_name)
	merge_pdfs(input_files_list_dir_name, output_folder_name)
