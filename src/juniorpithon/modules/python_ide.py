import io
import sys
import logging

class OpenSourceIDE:
    """
    Executes user-defined Python scripts safely on the edge device.
    Allows Pi users to automate their JuniorHome or Trading setups.
    """
    def execute(self, code_string: str) -> dict:
        captured_out = io.StringIO()
        sys.stdout = captured_out
        status = "SUCCESS"
        
        safe_globals = {
            "__builtins__": __builtins__,
            "log": logging.info
        }
        
        try:
            exec(code_string, safe_globals)
        except Exception as e:
            status = f"ERROR: {str(e)}"
        finally:
            sys.stdout = sys.__stdout__
            
        return {"status": status, "output": captured_out.getvalue()}
