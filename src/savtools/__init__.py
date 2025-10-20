from .operations import glimpse2

from pathlib import Path
import importlib.util

# Load references/pl.py dynamically
_refs_path = Path(__file__).resolve().parent.parent / "references" / "pl.py"
_spec = importlib.util.spec_from_file_location("pl", _refs_path)
_pl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_pl)  # execute pl.py into _pl

# Export snippet(s)
gb = _pl.gb

__all__ = ["glimpse2", "gb"]
__version__ = "0.1.0"
