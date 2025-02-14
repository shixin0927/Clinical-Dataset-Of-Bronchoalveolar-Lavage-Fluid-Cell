# Clinical-Dataset-Of-Bronchoalveolar-Lavage-Fluid-Cell 
This dataset comprises BALF cell images stained by Diff-quick staining and Gram staining, from patients who underwent bronchoalveolar lavage  and endotracheal aspirates between 2018 and 2024  at the Chinese PLA General Hospital. The dataset contained 2105 images, with 13,263 annotated cells from  seven typical cell  classes including erythrocyte, ciliated columnar epithelial, squamous epithelial, macrophage, lymphocyte, neutrophil, and eosinophil cells using both contour fine labeling and bounding box labeling. In addition, the  classical YoloV8 deep learning instance segmentation model was used to detect and segment the seven types of BALF cells. As observed, our model demonstrated exceptionally high accuracy. There are four types of the dataset: High Resolution Images, Images, Visualization Images, and Labels, which are helpful to promote the study of automated cell identification in BALF.
## Dataset
https://zenodo.org/uploads/14871206
## Dataset specification
- High Resolution Images: a total of 1903 original images (4,912×3,684 pixels) from clinical samples collected by an ImageView optical microscope (202 images were missed because of the initial anonymous input, but were all included in Images).

- Images: 2105 images from High Resolution Images resampled to the size of 853×640 for bounding box annotation and pixel-level high quality annotation, then applied directedly for network training.

- Visualization Images: images which showed manually labeled contours on each cell.

- Labels: saved in a txt format for direct use of YOLO series models and convenient way to convert to other data formats.
