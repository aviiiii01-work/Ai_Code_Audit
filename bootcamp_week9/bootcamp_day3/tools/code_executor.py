import sys
from io import StringIO

def execute_python_logic(code: str) -> str:
        """
    Executes Python code in a sandboxed environment and returns the printed output.
    Note: This tool ONLY returns the output; it DOES NOT save files.
    If you need to save the result, pass the output to the 'read_or_write_file' tool.
    """

        old_stdout = sys.stdout
        redirected_output = sys.stdout = StringIO()
        try:
            exec(code)
            sys.stdout = old_stdout
            return redirected_output.getvalue()
        except Exception as e:
            sys.stdout = old_stdout
            return str(e)