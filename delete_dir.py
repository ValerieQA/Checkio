import shutil
import os
database_directory = os.getenv('SURGIMAP_DIR') + '\\SurgimapDatabase\\users\\testWedge@surgimap.com'
print database_directory
shutil.rmtree(database_directory, ignore_errors=True)