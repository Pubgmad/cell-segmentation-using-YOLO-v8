CELL SEGMENTATION USING PRETRAINED MODEL NAMED YOLO-V8:

Cell Segmentation is a fundamental technique in biomedical image processing that involves identifying and separating individual cells from microscopic images. It is widely used in medical research, diagnostics, and drug discovery to analyze cell structures, count cells, and study their morphology and interactions. Accurate segmentation is crucial for tasks like disease detection, tumor analysis, and tracking cell growth over time. Various methods, including traditional image processing techniques and deep learning models, are used to improve segmentation accuracy and efficiency. 🚀


Steps:

    1)create a virtual environment for installing packages
       command:python -m venv yolo_seg
               yolo_seg\scripts\activate

    2) To start the proceedings first create a file named template.py and there u can create the template as you wish.
    3) Create a file named requirements.txt and and add the requirments which is required for the project and install in the environment by the command, 
               command:pip install -r requirements.txt
    
    4) Setup.py is used to create local packages and functions so in that add your name email_id(personal one) and the version 0.0.0 
    5) Utils folder just add the frequent code which you need to implement on a regular basis.

    6) ## Workflows

            1. constants
            2. entity
            3. components
            4. pipelines
            5. app.py

    7) for loading the images we  need to first annotate the image and then only segmentation is possible, so do it using a frame work called robo flow which is available in google.
    