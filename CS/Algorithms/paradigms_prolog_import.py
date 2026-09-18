"""Import shim: lets paradigms-four-ways.py import the engine from paradigms-prolog.py (a hyphenated filename)."""
import importlib.util, pathlib
_p = pathlib.Path(__file__).with_name("paradigms-prolog.py")
_spec = importlib.util.spec_from_file_location("paradigms_prolog", _p)
_m = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(_m)
KB = _m.KB
