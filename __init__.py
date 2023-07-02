import os

from pathlib import Path

username = 'ubuntu'
project_root = os.path.dirname(__file__)
data_root = os.path.join(project_root, 'data')
print(data_root)
