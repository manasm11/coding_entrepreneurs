import os
def add_smiley_to_etc():
    file_path = "/etc/delete_it_as_soon_as_you_see_it"
    with open(file_path, "w") as file:
        file.write("HELLO !!!")
    assert os.path.exists("/etc/delete_it_as_soon_as_you_see_it"), "File not created"
    
