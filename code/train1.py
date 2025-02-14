from ultralytics import YOLO
import skimage.io as skio

# Load a model: using model m
model = YOLO("F:/ultralytics_seg/ultralytics/cfg/models/v8/yolov8m-seg.yaml")  # build a new model from YAML


if __name__ == '__main__':
    data_dir = 'F:/ultralytics_seg/dataset/PW_BALFC'
    yaml_name='F:/ultralytics_seg/dataset/PW_BALFC/segment.yaml'
    results = model.train(data=yaml_name, epochs=500, batch=9,
                          imgsz=640, workers=0, multi_scale=False,save_period=1,scale=0.08,hsv_s=0.6,
                          degrees=5,translate=0.2,flipud=0.5,fliplr=0.5,mixup=0.3,copy_paste=0.2)