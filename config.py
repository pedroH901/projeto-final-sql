import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Configurações do SQL Server
    DB_SERVER = os.getenv('DB_SERVER', 'localhost')
    DB_DATABASE = os.getenv('DB_DATABASE', 'radar_pet')
    DB_USERNAME = os.getenv('DB_USERNAME', '')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    USE_WINDOWS_AUTH = os.getenv('USE_WINDOWS_AUTH', 'false').lower() == 'true'
    
    # String de conexão baseada no tipo de autenticação
    if USE_WINDOWS_AUTH:
        DB_CONNECTION_STRING = (
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={DB_SERVER};'
            f'DATABASE={DB_DATABASE};'
            f'Trusted_Connection=yes;'
            f'Connection Timeout=30;'
            f'TrustServerCertificate=yes;'
        )
        
        DB_CONNECTION_STRING_NO_DB = (
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={DB_SERVER};'
            f'Trusted_Connection=yes;'
            f'Connection Timeout=30;'
            f'TrustServerCertificate=yes;'
        )
    else:
        DB_CONNECTION_STRING = (
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={DB_SERVER};'
            f'DATABASE={DB_DATABASE};'
            f'UID={DB_USERNAME};'
            f'PWD={DB_PASSWORD};'
            f'Connection Timeout=30;'
            f'TrustServerCertificate=yes;'
        )
        
        DB_CONNECTION_STRING_NO_DB = (
            f'DRIVER={{ODBC Driver 17 for SQL Server}};'
            f'SERVER={DB_SERVER};'
            f'UID={DB_USERNAME};'
            f'PWD={DB_PASSWORD};'
            f'Connection Timeout=30;'
            f'TrustServerCertificate=yes;'
        )