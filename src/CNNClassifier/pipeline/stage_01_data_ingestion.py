from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.data_ingestion import DataIngestion
from CNNClassifier import logger



STAGE_NAME = "Data Ingestion stage"

class DataIngestionTrainingPipeline:

    def __init__(self):
        pass

    def main(self):

        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config = data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()

    # ConfigurationManager will return the object of the class which have some methods like get_data_ingestion_config which is used to get config object.
    # Data_ingestion_config is obtained by config object method get_data_ingestion_config.


    if __name__ == '__main__':

        try:
            logger.info(f"stage {STAGE_NAME} started")
            obj = DataIngestionTrainingPipeline()
            obj.main()
            logger.info(f"stage {STAGE_NAME} commpleted")
        except Exception as e:
            logger.exception(e)
            raise e


