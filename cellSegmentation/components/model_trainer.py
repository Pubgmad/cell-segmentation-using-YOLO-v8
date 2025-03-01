import os
import sys
import shutil
import subprocess
import yaml
from cellSegmentation.utils.main_utils import read_yaml_file
from cellSegmentation.logger import logging
from cellSegmentation.exception import AppException
from cellSegmentation.entity.config_entity import ModelTrainerConfig
from cellSegmentation.entity.artifacts_entity import ModelTrainerArtifact


class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig):
        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            logging.info("Unzipping data...")
            # Extract ZIP file using Python
            shutil.unpack_archive("data.zip", extract_dir="data")
            os.remove("data.zip")  # Delete the ZIP file

            logging.info("Starting YOLO training...")
            training_command = (
                f"yolo task=segment mode=train model={self.model_trainer_config.weight_name} "
                f"data=data.yaml epochs={self.model_trainer_config.no_epochs} imgsz=640 save=true"
            )
            # Run the training command and capture output
            result = subprocess.run(
                training_command, shell=True, capture_output=True, text=True
            )
            logging.info(f"Training STDOUT: {result.stdout}")
            logging.info(f"Training STDERR: {result.stderr}")
            if result.returncode != 0:
                raise AppException("YOLO training command failed.", sys)

            # Ensure best.pt exists
            best_model_path = "runs/segment/train/weights/best.pt"
            if not os.path.exists(best_model_path):
                raise AppException(
                    "Training completed but best.pt was not found. Please check the training logs and configuration.",
                    sys,
                )

            # Ensure model trainer directory exists
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)

            # Copy the trained model file
            target_model_path = os.path.join(
                self.model_trainer_config.model_trainer_dir, "best.pt"
            )
            shutil.copy(best_model_path, target_model_path)

            logging.info("Cleaning up unnecessary files and directories...")
            files_to_delete = ["yolov8s-seg.pt", "data.yaml"]
            folders_to_delete = ["train", "valid", "test", "runs"]

            for file in files_to_delete:
                if os.path.exists(file):
                    os.remove(file)

            for folder in folders_to_delete:
                if os.path.exists(folder):
                    shutil.rmtree(folder, ignore_errors=True)

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path=target_model_path,
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact

        except Exception as e:
            logging.error("Error during model training", exc_info=True)
            raise AppException(e, sys)
