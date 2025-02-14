from ultralytics import YOLO
import matplotlib
matplotlib.use('TkAgg')


model=YOLO("F:/ultralytics_seg/runs/segment/PW_BALFC/weights/best.pt")
if __name__ == '__main__':
    data_dir = 'F:/ultralytics_seg/dataset/PW_BALFC'
    yaml_name='F:/ultralytics_seg/dataset/PW_BALFC/segment.yaml'
    # Validate the model
    metrics = model.val(data=yaml_name,iou=0.68,save_txt=True)  # no arguments needed, dataset and settings remembered
    metrics