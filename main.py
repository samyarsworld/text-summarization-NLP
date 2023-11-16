from text_summarizer.config_manager import ConfigManager
from text_summarizer.logging import logger
from text_summarizer.pipeline.data_ingestion import DataIngestionPipeline
from text_summarizer.pipeline.data_validation import DataValidationPipeline
from text_summarizer.pipeline.data_transformation import DataTransformationPipeline
from text_summarizer.pipeline.data_training import DataTrainingPipeline



config = ConfigManager()

# STAGE_NAME = "Data Ingestion"
# try:
#    logger.info(f">>>>>> {STAGE_NAME} stage started <<<<<<") 
#    data_ingestion = DataIngestionPipeline(config)
#    data_ingestion.run()
#    logger.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<")
# except Exception as e:
#     logger.exception(e)
#     raise e


# STAGE_NAME = "Data Validation"
# try:
#    logger.info(f">>>>>> {STAGE_NAME} stage started <<<<<<") 
#    data_validation = DataValidationPipeline(config)
#    data_validation.run()
#    logger.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<")
# except Exception as e:
#     logger.exception(e)
#     raise e


STAGE_NAME = "Data Transformation"
try:
   logger.info(f">>>>>> {STAGE_NAME} stage started <<<<<<") 
   data_transformation = DataTransformationPipeline(config)
   data_transformation.run()
   logger.info(f">>>>>> {STAGE_NAME} stage completed <<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

