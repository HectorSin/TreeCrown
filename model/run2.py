import os
from typing import Any, Dict, List, Optional
import cv2
from _create_xml import create_label_xml

from deepforest import deepforest
import pandas as pd
from pic_crop import crop, combine


SCRIPT_DIR = os.path.abspath(os.getcwd())
IMAGE_DIR_PATH = "../data/image_data"
LABEL_DIR_PATH = "../data/predictions"
MODEL_DIR_PATH = "../data/model_data"

IMAGE_WIDTH = 400
IMAGE_HEIGHT = 400

FILE_NAME = "allpic"

IMAGE_DIR_PATH_READ = f"../data/image_data/{FILE_NAME}"
PREDICT_DIR_PATH = f"../data/result_pic/{FILE_NAME}"
"""
# Get the absolute path of the current script
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Use the absolute path to define the model directory path
IMAGE_DIR_PATH = os.path.join(SCRIPT_DIR, "../data/image_data")
LABEL_DIR_PATH = os.path.join(SCRIPT_DIR, "../data/predictions")
MODEL_DIR_PATH = os.path.join(SCRIPT_DIR, "../data/model_data")
"""

# Load the model
#MODEL_DIR_PATH_JOIN = os.path.join(MODEL_DIR_PATH, "model.h5")
#MODEL_DIR_PATH_JOIN = MODEL_DIR_PATH_JOIN.replace("\\", "/")
print(os.path.join(MODEL_DIR_PATH, "model.h5"))
MODEL = deepforest.deepforest(saved_model=os.path.join(MODEL_DIR_PATH, "model.h5"))
#MODEL = deepforest.deepforest(saved_model=os.path.join(MODEL_DIR_PATH_JOIN))

#MODEL = deepforest.deepforest()
#MODEL.use_release()


def _predict_image(image_path: str) -> Optional[pd.DataFrame]:
    try:
        return MODEL.predict_image(f"{image_path}", show=False, return_plot = False)
    except:
        return None


def _create_label_dir(dir_path: str) -> None:
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    for sub_dir in ["csv", "xml"]:
        sub_dir_path = f"{dir_path}/{sub_dir}"
        if not os.path.exists(sub_dir_path):
            os.makedirs(sub_dir_path)


def _save_csv_prediction(file_path: str, df_prediction: pd.DataFrame) -> None:
    df_prediction.to_csv(file_path, index=False)


def _save_xml_prediction(label_file_path: str, image_folder: str, image_file_name: str, df_prediction: pd.DataFrame) -> None:
    prediction: Dict[str, Any] = {
            "folder": image_folder,
            "filename": image_file_name,
            "path": f"{image_folder}/{image_file_name}",
            "width": IMAGE_WIDTH,
            "height": IMAGE_HEIGHT,
            "label_boxes": []
        }

    for index, row in df_prediction.iterrows():
        '''
        xmin,ymin,xmax,ymax,score,label
        '''
        tmp = {
            "xmin": row["xmin"],
            "ymin": row["ymin"],
            "xmax": row["xmax"],
            "ymax": row["ymax"],
            "label": row["label"],
        }
        prediction["label_boxes"].append(tmp)
    
    xml_file: str = create_label_xml(prediction)
    
    with open(label_file_path, "w") as f:
        f.write(xml_file)


if __name__ == "__main__":
    crop()
    image_dirs = os.listdir(IMAGE_DIR_PATH)
    for image_dir in image_dirs:
        # debug: dir filter
        # if image_dir.find("neustadt_sued") == -1:
        #     continue
        
        current_image_dir_path = f"{IMAGE_DIR_PATH}/{image_dir}"
        #current_image_dir_path = os.path.abspath(f"{IMAGE_DIR_PATH}/{image_dir}")
        #print(f"Current image directory path: {current_image_dir_path}")
        if os.path.isdir(current_image_dir_path) is False:
            continue

        print("학습이 진행되고 있습니다.")

        label_dir = f"{LABEL_DIR_PATH}/{image_dir}"
        _create_label_dir(label_dir)
        
        image_file_names = os.listdir(current_image_dir_path)
        for image_file_name in image_file_names:
            try:
                image_file_path = f"{current_image_dir_path}/{image_file_name}"
                df_prediction = _predict_image(image_file_path)

                #csv_label_path = f"{label_dir}/csv/{image_file_name.replace('.png', '.csv')}"
                csv_label_path = f"{label_dir}/csv/{image_file_name.replace('.jpg', '.csv')}"
                _save_csv_prediction(csv_label_path, df_prediction)

                #xml_label_path = f"{label_dir}/xml/{image_file_name.replace('.png', '.xml')}"
                xml_label_path = f"{label_dir}/xml/{image_file_name.replace('.jpg', '.xml')}"
                _save_xml_prediction(xml_label_path, image_dir, image_file_name, df_prediction)
                print(f"working on {image_file_name}")
            except:
                continue

    #IMAGE_WIDTH = 400
    #IMAGE_HEIGHT = 400
"""
image_dirs = os.listdir(IMAGE_DIR_PATH)
label_dirs = os.listdir(LABEL_DIR_PATH)

SCRIPT_DIR = os.path.abspath(os.getcwd())
IMAGE_DIR_PATH = "../data/image_data"
LABEL_DIR_PATH = "../data/predictions"
MODEL_DIR_PATH = "../data/model_data"

FILE_NAME = "allpic"

IMAGE_DIR_PATH_READ = f"../data/image_data/{FILE_NAME}"
PREDICT_DIR_PATH = f"../data/result_pic/{FILE_NAME}"
"""

if not os.path.exists(PREDICT_DIR_PATH):
    os.makedirs(PREDICT_DIR_PATH)

images = os.listdir(IMAGE_DIR_PATH_READ)

for image_dir in images:
    image_to = f"{IMAGE_DIR_PATH}/{FILE_NAME}/{image_dir}"
    label_to = f"{LABEL_DIR_PATH}/{FILE_NAME}/csv/{image_dir[:-4]}.csv"
    img = cv2.imread(image_to)
    box_info = pd.read_csv(label_to)
    for n in range(len(box_info)):
        x = (box_info.xmin[n]+box_info.xmax[n])/2
        y = (box_info.ymin[n]+box_info.ymax[n])/2
        cv2.circle(img, (int(x), int(y)), 25, (0, 255, 0), 2)
    cv2.putText(img, "TOTAL TREES: " + str(len(box_info)), (3, 14), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255))
    print(f"{PREDICT_DIR_PATH}/{image_dir}")
    cv2.imwrite(f"{PREDICT_DIR_PATH}/{image_dir}", img)

combine()