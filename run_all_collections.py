import os
import subprocess
import sys

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run_collection(collection_folder):
    input_json = os.path.join(BASE_DIR, collection_folder, 'challenge1b_input.json')
    pdf_dir = os.path.join(BASE_DIR, collection_folder, 'PDFs')
    output_json = os.path.join(BASE_DIR, collection_folder, 'challenge1b_output.json')

    print(f"[RUNNING] {collection_folder}")
    try:
        result = subprocess.run(
            [
                sys.executable,  # uses the same python env
                os.path.join(BASE_DIR, 'main.py'),
                '--input_json', input_json,
                '--pdf_dir', pdf_dir,
                '--output_json', output_json
            ],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"[✓] {collection_folder} completed.")
    except subprocess.CalledProcessError as e:
        print(f"[✗] {collection_folder} failed.")
        print("Error output:")
        print(e.stderr)

def main():
    for folder in sorted(os.listdir(BASE_DIR)):
        folder_path = os.path.join(BASE_DIR, folder)
        if os.path.isdir(folder_path) and folder.startswith("Collection"):
            run_collection(folder)

if __name__ == '__main__':
    main()
