import os
import subprocess

def run_python_file(working_directory, file_path, args=None):
  # Build the full path and normalize both paths
  working_abs = os.path.abspath(working_directory)
  target_abs = os.path.abspath(os.path.join(working_directory, file_path))

  if not target_abs.startswith(working_abs):
    f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
  if not os.path.isfile(target_abs):
    f'Error: File "{file_path}" not found.'
  if not file_path.endswith(".py"):
    return f'Error: "{file_path}" is not a Python file.'
    
  try:
    command = ['python', target_abs]
    if args:
      command.extend(args)

    # Run the subprocess
    result = subprocess.run(
        command,
        capture_output=True,
        text=True,
        cwd=working_directory,
        timeout=30
    )

    # Prepare the output
    output = []

    if result.stdout:
      output.append("STDOUT:\n" + result.stdout)
    if result.stderr:
      output.append("STDERR:\n" + result.stderr)

    if result.returncode != 0:
      output.append(f"Process exited with code {result.returncode}")

    return "\n".join(output) if output else "No output produced."

  except Exception as e:
    return f"Error: executing Python file: {e}"