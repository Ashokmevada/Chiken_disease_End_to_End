from CNNClassifier import logger
from CNNClassifier.config.configuration import ConfigurationManager
from CNNClassifier.components.prepare_base_model import PrepareBaseModel


STAGE_NAME = "Prepare Base Model "

class PrepareBaseModelTrainingPipeline:

    def __init__(self):
        pass

    def main(self):

        try:
            config = ConfigurationManager()
            prepare_base_model_config = config.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()

        except Exception as e:

            raise e


    if __name__ == '__main__':

        try:

            logger.info(f"{STAGE_NAME} Started")        
            obj = PrepareBaseModelTrainigPipeline()
            obj.main()
            logger.info(f"{STAGE_NAME} Completed")

        except Exception as e:
            logger.exception(e)
            raise e
