import os  # Import the 'os' module to interact with the operating system (e.g., check file/folder existence)
import urllib.request  # Import 'urllib.request' to handle URL operations like downloading files from the internet

if not os.path.exists("the-verdict.txt"):  # Check if the file "the-verdict.txt" does NOT already exist in the current directory
    url = ("https://raw.githubusercontent.com/rasbt/LLMs-from-scratch/main/ch02/01_main-chapter-code/the-verdict.txt")  # Store the URL of the remote text file to be downloaded
    file_path = "the-verdict.txt"  # Define the local filename/path where the downloaded file will be saved
    urllib.request.urlretrieve(url, file_path)  # Download the file from the URL and save it locally at the specified file path

def read_text_file(file_path):  # Define a function to read the contents of a text file given its file path
