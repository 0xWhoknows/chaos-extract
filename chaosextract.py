import requests
import json
import zipfile
from io import BytesIO
from concurrent.futures import ThreadPoolExecutor
import argparse


def download_and_extract_zip(url: str, output_file: str)-> None :
    try:
        fatch_data = requests.get(url)
        fatch_data.raise_for_status()

        with zipfile.ZipFile(BytesIO(fatch_data.content)) as zip_file:
            for file_info in zip_file.infolist():
                with zip_file.open(file_info) as file_contents:
                    with open(output_file, 'ab') as output:
                        output.write(file_contents.read())

        print(f"Downloaded and extracted {url} to {output_file}")
    except Exception as e:
        print(f"Error downloading and extracting {url}: {e}")

def main() -> None:
    parser = argparse.ArgumentParser(description="Download chaos-data and extract zip files ")
    parser.add_argument("-c", "--concurrency", type=int, default=30, help="The number of concurrent downloads to run")
    parser.add_argument("-o", "--output", default="output.txt", help="The name and location of the output file")
    args = parser.parse_args()

    concurrency : int = args.concurrency
    output_file : str = args.output
    url : str = "https://chaos-data.projectdiscovery.io/index.json"

    fatch_data = requests.get(url)
    fatch_data.raise_for_status()

    data : dict = json.loads(fatch_data.text)

    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        for objdata in data:
            zip_url = objdata["URL"]
            executor.submit(download_and_extract_zip, zip_url, output_file)

    print(f"\tAll downloads completed successfully save in {output_file}")
    

if __name__ == "__main__":
    main()
