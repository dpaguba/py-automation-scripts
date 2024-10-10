import os
import pdfplumber

path_to_pdf = ""
original_txt = ""
temp_txt = "temp.txt"
strings_to_delete = []

with pdfplumber.open(path_to_pdf) as pdf:
    with open(original_txt, "w") as file:
        for page in range(0, len(pdf.pages)):
            data = pdf.pages[page].extract_text()
            file.write(data)
        

with open(original_txt, "r") as input:
    with open(temp_txt, "w") as output:
        for line in input:
            for word in strings_to_delete:
                line = line.replace(word, "")
            if(line.startswith("Frage")):
                line = "\n\n" + line
            output.write(line)


os.replace(temp_txt, original_txt)