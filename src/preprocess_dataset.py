import os
import glob
import xml.etree.ElementTree as ET
import re
import json


class MedQuADPreprocessor:
    def __init__(self, input_dir: str, output_path: str):
        """
        This class handles the end-to-end preprocessing of the MedQuAD dataset provided in XML format.
        It loads all XML files from the specified directory, parses them to extract question-answer pairs,
        cleans the text by removing HTML tags and normalizing whitespace, filters out low-quality or too-short
        entries, and formats the data into an instruction-based structure suitable for LLM fine-tuning.

        The resulting data is saved in JSON Lines (.jsonl) format where each line contains a dictionary with:
            {
                "instruction": <question>,
                "response": <answer>
            }

        This output format is ideal for training or fine-tuning instruction-following models such as LLaMA,
        Mistral, or Falcon. The class also provides utilities to visualize or test intermediate steps.
        
        input_dir: path to the root MedQuAD folder containing subfolders with .xml files
        output_path: where to save the preprocessed .jsonl file
        """
        self.input_dir = input_dir
        self.output_path = output_path
        self.xml_files = []       # will store paths to all XML files
        self.qa_pairs = []        # will store extracted and cleaned QA pairs


    def load_xml_files(self):
        """Recursively load all XML file paths from input_dir"""
        pattern = os.path.join(self.input_dir, "**", "*.xml")
        self.xml_files = glob.glob(pattern, recursive=True)
        print(f"Found {len(self.xml_files)} XML files.")


    def parse_xml_file(self, file_path):
        """Parse a single XML file and return a list of (question, answer) pairs."""
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()

            qa_elements = root.findall(".//QAPair") # Find all <QAPair> elements in the XML, regardless of their depth in the hierarchy
            qa_pairs = []

            for qa in qa_elements:
                question = qa.findtext("Question")
                answer = qa.findtext("Answer")

                if question and answer:
                    qa_pairs.append((question.strip(), answer.strip()))

            return qa_pairs if qa_pairs else None

        except ET.ParseError:
            print(f"Failed to parse: {file_path}")
            return None    

    def clean_text(self, text):
        """Remove HTML tags and excessive whitespace from the text."""
        text = re.sub(r"<[^>]+>", "", text)  # remove HTML tags
        text = re.sub(r"\s+", " ", text)     # normalize whitespace
        return text.strip()

    def filter_and_format(self, min_ans_length=20, min_qu_length=10):
        """Filter and format Q&A pairs from all XML files.
        
        Mean lengths for questions and answers help assess the typical size and complexity of the data. 
        This information guides model design decisions (e.g., max input/output lengths) and ensures
        preprocessing steps retain meaningful, informative samples.
        """
        for file_path in self.xml_files:
            qa_list = self.parse_xml_file(file_path)
            if not qa_list:
                continue

            for question, answer in qa_list:
                # Clean both question and answer
                question_clean = self.clean_text(question)
                answer_clean = self.clean_text(answer)

                # Filter: skip too-short entries
                if len(answer_clean) < min_ans_length or len(question_clean) < min_qu_length:
                    continue

                # Format: instruction-based format
                formatted = {
                    "instruction": question_clean,
                    "response": answer_clean
                }
                self.qa_pairs.append(formatted)

        return formatted
   

    def save_to_jsonl(self):
        """Save formatted Q&A pairs to a .jsonl file."""
        with open(self.output_path, "w", encoding="utf-8") as f:
            for pair in self.qa_pairs:
                json.dump(pair, f, ensure_ascii=False)
                f.write("\n")
        print(f"Saved {len(self.qa_pairs)} Q&A pairs to {self.output_path}")


    def run_all(self):
        self.load_xml_files()
        self.filter_and_format()
        self.save_to_jsonl()


if __name__ == "__main__":
    processor = MedQuADPreprocessor(
        input_dir="../data/MedQuAD_XMLs",
        output_path="../data/medquad_preprocessed.jsonl"
    )
    processor.run_all()

