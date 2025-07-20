import unittest
import os
import tempfile
os.sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from preprocess_dataset import MedQuADPreprocessor

class TestMedQuADPreprocessor(unittest.TestCase):

    def test_clean_text_removes_html(self):
        processor = MedQuADPreprocessor("dummy_input", "dummy_output")
        dirty_text = "This is <b>bold</b> and <i>italic</i>."
        expected = "This is bold and italic."
        result = processor.clean_text(dirty_text)
        self.assertEqual(result, expected)

    def test_load_xml_files(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            os.makedirs(os.path.join(tmpdir, "subdir"))
            file_path = os.path.join(tmpdir, "subdir", "sample.xml")
            with open(file_path, "w") as f:
                f.write("<Document></Document>")

            processor = MedQuADPreprocessor(input_dir=tmpdir, output_path="dummy.jsonl")
            processor.load_xml_files()
            self.assertEqual(len(processor.xml_files), 1)
            self.assertTrue(file_path in processor.xml_files)


    def test_filter_and_format(self):
        xml_content = """
        <Document>
            <QAPairs>
                <QAPair>
                    <Question>Short?</Question>
                    <Answer>Too short.</Answer>
                </QAPair>
                <QAPair>
                    <Question>What is a valid question?</Question>
                    <Answer>This is a valid, long enough answer with >20 chars.</Answer>
                </QAPair>
            </QAPairs>
        </Document>
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            xml_path = os.path.join(tmpdir, "test.xml")
            with open(xml_path, "w") as f:
                f.write(xml_content)

            processor = MedQuADPreprocessor(tmpdir, "dummy.jsonl")
            processor.load_xml_files()
            processor.filter_and_format()

            self.assertEqual(len(processor.qa_pairs), 1)
            self.assertEqual(
                processor.qa_pairs[0]["instruction"],
                "What is a valid question?"
            )

    def test_save_to_jsonl(self):
        processor = MedQuADPreprocessor("dummy", "test_output.jsonl")
        processor.qa_pairs = [
            {"instruction": "What is X?", "response": "Answer Y."}
        ]
        processor.save_to_jsonl()

        with open("test_output.jsonl", "r", encoding="utf-8") as f:
            lines = f.readlines()
        self.assertEqual(len(lines), 1)
        self.assertIn("What is X?", lines[0])




if __name__ == '__main__':
    unittest.main()