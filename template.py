import os
import logging 
from pathlib import Path

project_name='youtube_analyzer'
log_dir='logs'
log_file='project_setup.log'

os.makedirs(log_dir,exist_ok=True)

# loggine setup 
logging.basicConfig(
    filename=os.path.join(log_dir,log_file),
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s - %(message)s"
)
logger=logging.getLogger(__name__)

list_of_files =[
    f"src/{project_name}/__init__.py"
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/entity.py",
    f"src/{project_name}/configuration/__init__.py",
    f"src/{project_name}/configuration/config.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/data_validation.py",
    f"src/{project_name}/components/data_preprocessing.py",
    f"src/{project_name}/components/model_traning.py",
    f"src/{project_name}/components/model_evalution.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/pipeline_01_dataingestion.py",
    f"src/{project_name}/pipeline/pipeline_02_datavalidation.py",
    f"src/{project_name}/pipeline/pipeline_03_datapreprocessing.py",
    f"src/{project_name}/pipeline/pipeline_04_modeltraning.py",
    f"src/{project_name}/pipeline/pipeline_05_modelevalution.py",
    f"src/logger.py",
    'config/config.yaml',
    'params.yaml',
    'main.py',
    'requirements.txt',
    '.gitignore',
    'setup.py',
    'app.py'
]

for file_path in list_of_files:
    file_path=Path(file_path)
    file_dir,file_name=os.path.split(file_path)

    if file_dir:
        os.makedirs(file_dir,exist_ok=True)
        logger.info(f"{file_dir} directory created")

    if not file_path.exists():
        file_path.touch()
        logger.info(f"{file_path} file created ")