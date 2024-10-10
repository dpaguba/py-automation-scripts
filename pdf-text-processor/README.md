# 📄 PDF Text Processor

This Python script processes a PDF file by extracting its text content, performing some text modifications, and saving the result to a text file.

## 🛠️ Requirements

- Python 3.x
- pdfplumber library (`pip install pdfplumber`)

## 🚀 Usage

1. Set the `path_to_pdf` variable to the path of your input PDF file.
2. Set the `original_txt` variable to the desired output text file name.
3. (Optional) Add strings to the `strings_to_delete` list if you want to remove specific content from the text.
4. Run the script.

## 🔍 How it works

1. 📂 The script opens the specified PDF file using pdfplumber.
2. 📝 It extracts text from each page of the PDF and writes it to the `original_txt` file.
3. 🔄 The script then reads the `original_txt` file, processes each line by:
   - 🗑️ Removing specified strings (if any)
   - ➕ Adding two newline characters before lines starting with "Frage"
4. 💾 The processed text is written to a temporary file (`temp.txt`).
5. 🔁 Finally, the temporary file replaces the original text file.


Happy PDF processing! 📚✨