from PIL import Image
import os


def crop_image(input_path, output_path, crop_size=(400, 400)):
    image = Image.open(input_path)
    width, height = image.size

    # 이미지가 RGBA 형식이면 RGB로 바꾸기
    if image.mode == "RGBA":
        image = image.convert("RGB")

    # 이미지를 400x400 크기로 자르기
    for i in range(0, width, crop_size[0]):
        for j in range(0, height, crop_size[1]):
            #box = (i, j, i+crop_size[0], j+crop_size[1])
            box = (i, j, min(i+crop_size[0], width), min(j+crop_size[1], height))
            cropped_image = image.crop(box)
            cropped_image.save(f"{output_path}_{i}_{j}.jpg")

def combine_images(input_path, output_path, original_size, crop_size=(400, 400)):
    new_image = Image.new('RGB', original_size)
    width, height = original_size

    for i in range(0, width, crop_size[0]):
        for j in range(0, height, crop_size[1]):
            path = f"{input_path}_{i}_{j}.jpg"
            cropped_image = Image.open(path)
            new_image.paste(cropped_image, (i, j))

    new_image.save(output_path)

def main():
    user_input = input("1. crop image\n2. combine image\n3. exit\n")
    if user_input == "1":
        input_image = "../data/input_image"
        output_image = "../data/image_data/allpic"
        images = os.listdir(input_image)
        for image in images:
            crop_image(f"{input_image}/{image}", f"{output_image}/{image[:-4]}")
        return "Done"
    elif user_input == "2":
        input_image = "../data/result_pic/allpic"
        output_image = "../data/final_image"
        images = os.listdir(input_image)
        image = images[0]
        original_size = (3840,2160)
        combine_images(f"{input_image}/{image[:-8]}", f"{output_image}/{image[:-8]}.jpg", original_size)
        return "Done"
    else:
        return "Wrong input"
    
def crop():
    input_image = "../data/input_image"
    output_image = "../data/image_data/allpic"
    images = os.listdir(input_image)
    for image in images:
        crop_image(f"{input_image}/{image}", f"{output_image}/{image[:-4]}")

def combine():
    input_image = "../data/result_pic/allpic"
    output_image = "../data/final_image"
    images = os.listdir(input_image)
    image = images[0]
    original_size = (3840,2160)
    combine_images(f"{input_image}/{image[:-8]}", f"{output_image}/{image[:-8]}.jpg", original_size)