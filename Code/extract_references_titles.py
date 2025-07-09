import os
import PyPDF2

def extract_first_four_lines_from_pdf(pdf_path):
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            if reader.pages:
                first_page = reader.pages[0]
                text = first_page.extract_text()
                if text:
                    lines = []
                    for line in text.split('\n'):
                        if line.strip():
                            # Replace spaces with dashes
                            processed_line = line.strip().replace(' ', '-')
                            lines.append(processed_line)
                        if len(lines) == 4:
                            break
                    return lines
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
    return []

def extract_titles_from_folder(folder_path, output_file):
    papers = []
    for filename in os.listdir(folder_path):
        if filename.lower().endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)
            lines = extract_first_four_lines_from_pdf(pdf_path)
            if lines:
                papers.append(lines)
            else:
                print(f"Title not found in {filename}")

    with open(output_file, 'w', encoding='utf-8') as f:
        for idx, lines in enumerate(papers, start=1):
            f.write(f"{idx} ---\n")
            for line in lines:
                f.write(f"{line}\n")
            f.write("\n")  # Add a blank line between papers for readability

    print(f"Extracted {len(papers)} titles to {output_file}")


if __name__ == "__main__":
    # Replace 'path/to/your/pdf/folder' with the actual path to your PDF folder
    # and 'titles.txt' with your desired output file name.
    extract_titles_from_folder(r"C:\Users\dimbe\OneDrive\Desktop\Courses\1학기\Software_Analytics\RAG_FinalProject\Others",
                               r"C:\Users\dimbe\OneDrive\Desktop\LAB\Conferences\Domestic\KCSE_2025\KCSE-project-file\titles.txt")