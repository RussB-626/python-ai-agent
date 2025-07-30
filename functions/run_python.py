import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
  try:
    # Build the full path and normalize both paths
    working_abs = os.path.abspath(working_directory)
    target_abs = os.path.abspath(os.path.join(working_directory, file_path))

    if not file_path.endswith(".py"):
      return f'Error: "{file_path}" is not a Python file.'
    if not target_abs.startswith(working_abs):
      raise Exception(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
    if not os.path.isfile(target_abs):
      raise Exception(f'Error: File "{file_path}" not found.')
    
    command = ['python', target_abs] + args

    # Run the subprocess
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        cwd=working_directory,
        timeout=30
    )

    # Prepare the output
    output_lines = []

    if result.stdout:
      output_lines.append("STDOUT:\n" + result.stdout)
    if result.stderr:
      output_lines.append("STDERR:\n" + result.stderr)
    if result.returncode != 0:
      output_lines.append(f"Process exited with code {result.returncode}")
    if not result.stdout and not result.stderr:
      output_lines.append("No output produced.")

    return "\n".join(output_lines)

  except Exception as e:
    return f"Error: executing Python file: {e}"