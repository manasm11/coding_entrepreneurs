from os import path
import requests
import shutil

def download_file(url, directory, filename=None, replace_existing=False):
    assert isinstance(url, str), "[-] 'url' not a string"
    assert isinstance(directory, str), "'[-] 'directory' not a valid string"
    assert path.exists(directory), f"'[-] path '{directory}' does not exists"
    filename = filename or path.basename(url)
    assert "." in filename, f"[-] {filename} not a valid filename"

    filepath = path.join(directory, filename)
    assert replace_existing or not path.exists(filepath), f"[-] {filepath} already exists"

    # urlretrieve(url=url, filename=filepath)
    with requests.get(url=url, stream=True) as response:
        response.raise_for_status()
        with open(filepath, "wb") as file_obj:
            shutil.copyfileobj(response.raw, file_obj)
    return filepath


download_file(
    url="https://e360.yale.edu/assets/site/Dove-Lake_from_South-2008.jpg",
    directory="downloads"
)
