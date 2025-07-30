import os

def write_file(working_directory, file_path, content):
  try:
    # Build the full path and normalize both paths
    working_abs = os.path.abspath(working_directory)
    target_abs = os.path.abspath(os.path.join(working_directory, file_path))

    if not target_abs.startswith(working_abs):
      raise Exception(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
    
    dir_path = os.path.dirname(target_abs)
    if not os.path.exists(dir_path):
      os.makedirs(dir_path)

    with open(target_abs, "w") as writer:
      writer.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

  except Exception as e:
    return f"Error writing to file: {e}"