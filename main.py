from data_processor import DataProcessor
import config

dp = DataProcessor(data_source = 'alpaca',
                   API_KEY = config.API_KEY,
                   API_SECRET = config.API_SECRET,
                   API_BASE_URL = config.API_BASE_URL,
                   )






