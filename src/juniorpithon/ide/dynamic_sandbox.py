import io
import sys
import logging
from typing import Dict, Any

class JCUIContext:
    """Injected into the user's sandbox to allow Python scripts to build the dashboard."""
    def __init__(self):
        self.ui_state = {}

    def metric(self, label: str, value: Any, color: str = "neutral"):
        self.ui_state[label] = {"type": "metric", "value": value, "color": color}
        
    def log(self, message: str):
        if "logs" not in self.ui_state: self.ui_state["logs"] = []
        self.ui_state["logs"].append(message)

class SovereignSandbox:
    """Executes user Python code securely and captures emitted UI states."""
    def execute_user_script(self, code_str: str) -> Dict[str, Any]:
        ui_ctx = JCUIContext()
        safe_globals = {
            "jc_ui": ui_ctx,
            "__builtins__": __builtins__
        }
        
        captured_output = io.StringIO()
        sys.stdout = captured_output
        try:
            exec(code_str, safe_globals)
            execution_status = "SUCCESS"
        except Exception as e:
            execution_status = f"ERROR: {str(e)}"
        finally:
            sys.stdout = sys.__stdout__

        return {
            "status": execution_status,
            "stdout": captured_output.getvalue(),
            "dynamic_ui": ui_ctx.ui_state
        }
