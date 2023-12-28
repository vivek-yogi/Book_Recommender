from Book_recommend.constants import *
from Book_recommend.utils import create_directories,read_yaml
from pathlib import Path
import os
from Book_recommend.entity import (DataIngestionConfig,DataLoadingConfig)


class ConfigurationManager:
        def __init__(self,config_filepath = CONFIG_FILE_PATH,params_filepath = PARAMS_FILE_PATH):
                
                self.config = read_yaml(config_filepath)
                self.params = read_yaml(params_filepath)
                
        
                create_directories([self.config.artifacts_root]) # creating artifacts

        def get_data_ingestion_config(self) ->DataIngestionConfig: 
                config = self.config.data_ingestion

                create_directories([config.root_dir])
                
                data_ingestion_config  = DataIngestionConfig(
                        root_dir       = config.root_dir,
                        source_URL     = self.config.data_ingestion.source_URL,
                        local_data_file= config.local_data_file,
                        unzip_dir      = config.unzip_dir
                )
                return data_ingestion_config  
        
        
        
       
               
                
