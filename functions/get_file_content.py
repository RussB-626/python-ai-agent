import os
from config import *

def get_file_content(working_directory, file_path):
  # Build the full path and normalize both paths
  working_abs = os.path.abspath(working_directory)
  target_abs = os.path.abspath(os.path.join(working_directory, file_path))

  if not target_abs.startswith(working_abs):
    return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
  if not os.path.isfile(target_abs):
    return f'Error: File not found or is not a regular file: "{file_path}"'

  try:
    with open(target_abs, "r") as reader:
      file_contents = reader.read(MAX_CHARS)
      if os.path.getsize(target_abs) > MAX_CHARS:
        file_contents += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
    return file_contents  
  except Exception as e:
    return f'Error reading file "${file_path}": {e}'