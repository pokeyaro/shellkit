"""
runtime/metadata.py

Extracts project metadata from pyproject.toml and syscall build time.
"""

import os
import time
import importlib.metadata
from pathlib import Path

# Python 3.10 compatibility
try:
    import tomllib
except ImportError:
    try:
        import tomli as tomllib
    except ImportError:
        tomllib = None


def get_metadata() -> tuple[str, str, str]:
    """
    Reads project name and version from package metadata or pyproject.toml,
    and fetches the build time of syscall/syslib.so (ctime).

    Returns:
        A tuple of (name, version, build_time_str)
    """
    name = "PYSH"
    version = "MAJOR.MINOR.PATCH"
    build_time = "MM-YYYY"

    # Get name and version
    try:
        # Try installed package metadata first
        dist = importlib.metadata.distribution("ShellKit")
        name = dist.metadata["Name"] or name
        version = dist.metadata["Version"] or version
    except importlib.metadata.PackageNotFoundError:
        # Development fallback: try pyproject.toml
        if tomllib:
            pyproject_path = Path(__file__).resolve().parents[2] / "pyproject.toml"
            if pyproject_path.exists():
                try:
                    with pyproject_path.open("rb") as f:
                        data = tomllib.load(f)
                        project = data.get("project", {})
                        name = project.get("name", name)
                        version = project.get("version", version)
                except Exception:
                    pass

    # Get build time from syslib.so
    try:
        # Try to find syslib.so via syscall module
        import syscall
        if hasattr(syscall, "__file__") and syscall.__file__:
            syslib_path = Path(syscall.__file__).parent / "syslib.so"
            if syslib_path.exists():
                ctime = os.path.getctime(syslib_path)
                build_time = time.strftime("%b %Y", time.localtime(ctime))
    except (ImportError, Exception):
        # Fallback: try relative path
        syslib_path = Path(__file__).resolve().parents[2] / "syscall" / "syslib.so"
        if syslib_path.exists():
            try:
                ctime = os.path.getctime(syslib_path)
                build_time = time.strftime("%b %Y", time.localtime(ctime))
            except Exception:
                pass

    return name, version, build_time
