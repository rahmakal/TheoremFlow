import subprocess
import tempfile
from pathlib import Path


def run_lean_code(lean_code: str):
    # Create a temporary lean file
    with tempfile.NamedTemporaryFile(suffix=".lean", delete=False) as tmp:
        tmp_path = Path(tmp.name)
        tmp.write(lean_code.encode("utf-8"))

    # Run lean on the temporary file
    result = subprocess.run(["lean", str(tmp_path)], capture_output=True, text=True)

    # Collect output
    stdout = result.stdout
    stderr = result.stderr

    # Optional: delete temporary file
    tmp_path.unlink(missing_ok=True)

    return stdout, stderr
