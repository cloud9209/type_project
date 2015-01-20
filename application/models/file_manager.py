from google.appengine.api import files

# file overrides built-in function <file>
def save_profile_image(image, image_path):
    path_writable = files.gs.create(image_path, mime_type = image.content_type, acl='public-read')

    with files.open(path_writable, 'ab') as file :
        file.write(image.read())
    files.finalize(path_writable)

def load_profile_image(image_path) :
    with files.open(image_path, 'r') as file :
        data = file.read()
    return data