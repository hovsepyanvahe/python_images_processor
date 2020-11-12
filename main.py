import os
from PIL import Image, ImageDraw


def add_author_names_to_images(images_path):
    if not os.path.exists('./output-images/'):
        os.makedirs('./output-images/')

    for filename in os.listdir(images_path):
        if filename.endswith(".jpg"):
            author_name = filename.replace(".jpg", "")
            image = Image.open('./source-images/' + filename)
            image_editable = ImageDraw.Draw(image)
            width, height = image.size
            author_name_len = len(author_name) * 7
            image_editable.text((width - author_name_len, height - 20), author_name, (237, 230, 211))
            image.save("./output-images/" + author_name + ".jpg")


if __name__ == '__main__':
    add_author_names_to_images("./source-images")
