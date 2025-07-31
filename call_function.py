from google.genai import types
from config import *

from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import get_file_content, schema_get_file_content
from functions.run_python import run_python_file, schema_run_python_file
from functions.write_file_content import write_file, schema_write_file

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)


def call_function(function_call_part, verbose=False):
  if verbose:
    print(print(f"Calling function: {function_call_part.name}({function_call_part.args})"))
  else:
    print(f" - Calling function: {function_call_part.name}")

  function_name = function_call_part.name
  function_args = function_call_part.args
  function_args["working_directory"] = WORKING_DIRECTORY

  match function_name:
    case "get_files_info":
      function_result = get_files_info(**function_args)
    case "get_file_content":
      function_result = get_file_content(**function_args)
    case "write_file":
      function_result = write_file(**function_args)
    case "run_python_file":
      function_result = run_python_file(**function_args)
    case _:
      return types.Content(
        role="tool",
        parts=[
          types.Part.from_function_response(
            name=function_name,
            response={"error": f"Unknown function: {function_name}"},
          )
        ],
      )

  return types.Content(
            role="tool",
            parts=[
              types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
              )
            ],
          )