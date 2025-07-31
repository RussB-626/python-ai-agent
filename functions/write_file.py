import os

def write_file(working_directory, file_path, content):
  # Build the full path and normalize both paths
  working_abs = os.path.abspath(working_directory)
  target_abs = os.path.abspath(os.path.join(working_directory, file_path))

  if not target_abs.startswith(working_abs):
    return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
  
  if not os.path.exists(target_abs):
    try:
      os.makedirs(os.path.dirname(target_abs), exist_ok=True)
    except Exception as e:
      return f"Error: creating directory: {e}"
    
  if os.path.exists(target_abs) and os.path.isdir(target_abs):
    return f'Error: "{file_path}" is a directory, not a file'

  try:
    with open(target_abs, "w") as writer:
      writer.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
  except Exception as e:
    return f"Error writing to file: {e}"