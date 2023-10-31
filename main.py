from CNNClassifier import logger
from CNNClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline



STAGE_NAME = "DATA INGESTION STAGE"

try:
    logger.info(f"stage {STAGE_NAME} started")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f"stage {STAGE_NAME} commpleted")
except Exception as e:
    logger.exception(e)
    raise e