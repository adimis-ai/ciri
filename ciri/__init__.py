try:
    from importlib.metadata import version as get_version
except ImportError:
    from importlib_metadata import version as get_version

try:
    __version__ = get_version("ciri-ai")
except Exception:
    __version__ = "unknown"
