import os
from google.genai import types

def get_files_info(working_directory, directory="."):
  working_abs = os.path.abspath(working_directory)
  target_abs = os.path.abspath(os.path.join(working_directory, directory))
  
  if not target_abs.startswith(working_abs):
    return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
  if not os.path.isdir(target_abs):
    return f'Error: "{directory}" is not a directory'

  try:
    file_results = []
    for filename in os.listdir(target_abs):
      file_path = os.path.join(target_abs, filename)
      is_dir = os.path.isdir(file_path)
      file_size = os.path.getsize(file_path)

      file_results.append(f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}")
    return "\n".join(file_results)
  except Exception as e:
    return f"Error listing files: {e}"
  
schema_get_files_info = types.FunctionDeclaration(
  name="get_files_info",
  description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
  parameters=types.Schema(
    type=types.Type.OBJECT,
    properties={
      "directory": types.Schema(
        type=types.Type.STRING,
        description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
      ),
    },
    required=["directory"],
  ),
)