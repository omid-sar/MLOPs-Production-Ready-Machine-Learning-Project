
from us_visa.exception import USvisaException






try:
    print("hello")
    2 / 0  # This will raise a ZeroDivisionError
except Exception as e:
    raise USvisaException(e, context="test")










import os
file_path = os.path.join("artifacts", "file_name.txt")
direct_path = os.path.dirname(file_path)
os.makedirs(direct_path, exist_ok=True)

from us_visa.entity.artifact_entity import DataIngestionArtifact

data_ingestion_artifacts = DataIngestionArtifact(trained_file_path=direct_path, 
                                                 test_file_path=file_path)

