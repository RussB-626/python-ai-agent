import os
from config import *
from google import genai
from google.genai import types

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
  
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets a files' contents truncated up to 10000 characters, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to get file contents from, relative to the working directory.",
            ),
        },
    ),
)