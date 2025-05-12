import os 
import pandas as pd 
from mlProject import logger
from sklearn.model_selection import train_test_split
from mlProject.entity.config_entity import DataTransformationConfig

class DataTransformation: 
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        #You can add all the different transformation techniques needed before spliting the data. 
        
    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)
    #SPlit the data into training and test datasets 
        train, test = train_test_split(data)
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)
        
        logger.info("Splitted data into train and test sets")
        logger.info(train.shape)
        logger.info(test.shape)           