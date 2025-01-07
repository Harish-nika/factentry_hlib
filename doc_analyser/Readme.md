doc-analyzer/
├── doc_analyser.py           # Main script with the class and functions
├── requirements.txt          # List of dependencies
├── input/                    # Folder to store input PDFs
│   └── sample1.pdf
│   └── sample2.pdf
├── output/                   # Folder to store results (JSON, Excel)
├── data/                     # Folder for CSV input files
│   └── files.csv
├── README.md                 # Documentation for the project
└── LICENSE                   # License file (if applicable)


# DocAnalyzer - PDF Document Analyzer

DocAnalyzer is a Python-based tool for extracting and analyzing text from PDF documents. It handles both text-based PDFs and image-based PDFs using Optical Character Recognition (OCR). The tool can detect the dominant language in each document, calculate language distributions, and provide insights about the nature of the document (whether it is scanned or not). The results are saved in both JSON and Excel formats for easy access.

## Features

- **Text Extraction**: Extract text from both text-based and image-based PDFs.
- **OCR Support**: Uses Tesseract OCR to extract text from image-based PDFs.
- **Language Detection**: Detect the dominant language and calculate language distributions.
- **Batch Processing**: Analyze multiple PDFs listed in a CSV file.
- **Results Saving**: Saves results in both JSON (per PDF) and Excel (summary of all PDFs).

## Prerequisites

Before running the script, ensure that you have the following installed:

- Python 3.x
- Tesseract OCR (installed locally)
- Required Python packages (listed in `requirements.txt`)

### Tesseract Installation

You need to install Tesseract OCR. You can install it via the following steps:

- **Windows**: Download from [here](https://github.com/UB-Mannheim/tesseract/wiki).
- **macOS**: Use Homebrew:

brew install tesseract

markdown
Copy code
- **Linux**:
sudo apt install tesseract-ocr

bash
Copy code

## Installation

1. Clone the repository:
 ```bash
 git clone https://github.com/your-username/doc-analyzer.git
 cd doc-analyzer
Install the required Python packages:

bash
Copy code
pip install -r requirements.txt
(Optional) Install Tesseract OCR as per the instructions above.

Usage
Analyzing a Single PDF
You can analyze a single PDF document by calling the analyze_pdf method. Here's an example:

python
Copy code
from doc_analyser import DocAnalyzer

# Initialize the analyzer
analyzer = DocAnalyzer(input_folder='path/to/pdf/folder')

# Analyze a single PDF
result = analyzer.analyze_pdf('path/to/pdf/document.pdf')
print(result)
Analyzing Multiple PDFs (Batch Processing)
To analyze multiple PDFs, create a CSV file with the PDF filenames and use the analyze_pdfs method:

Prepare a CSV file (files.csv) with the following structure:

csv
Copy code
filename
document1
document2
Run the batch processing:

python
Copy code
analyzer = DocAnalyzer(input_folder='path/to/pdf/folder', csv_file='files.csv', output_dir='path/to/output')
analyzer.analyze_pdfs()
Results will be saved in the output directory as individual JSON files and an Excel file (checkpoint.xlsx).