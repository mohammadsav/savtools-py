from .operations import glimpse2

from pathlib import Path
import importlib.util

# Point to: src/references/pl.py
_base = Path(__file__).resolve().parent          # src/savtools
_refs_path = _base.parent / "references" / "pl.py"  # src/references/pl.py

_spec = importlib.util.spec_from_file_location("pl", _refs_path)
_pl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_pl)

# Expose snippets
gb = _pl.gb

__all__ = ["glimpse2", "gb"]
__version__ = "0.1.0"
