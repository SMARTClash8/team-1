import os
def delete_images(dir):
    for f in os.listdir(dir):
        os.remove(os.path.join(dir, f))


