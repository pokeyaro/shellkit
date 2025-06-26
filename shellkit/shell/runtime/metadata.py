"""
runtime/metadata.py

Extracts project metadata from pyproject.toml and the build time of syscall syslib.
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
    Returns combined project metadata including name, version, and build time.

    Returns:
        A tuple of (name, version, build_time)
    """
    name, version = get_project_info()
    build_time = get_syslib_build_time()
    return name, version, build_time


def get_project_info() -> tuple[str, str]:
    """
    Returns the project name and version.

    It first tries to read from the installed package metadata.
    If that fails, it attempts to parse pyproject.toml (development mode).

    Returns:
        A tuple of (name, version)
    """
    name = "PYSH"
    version = "MAJOR.MINOR.PATCH"

    try:
        dist = importlib.metadata.distribution("ShellKit")
        name = dist.metadata["Name"] or name
        version = dist.metadata["Version"] or version
    except importlib.metadata.PackageNotFoundError:
        if tomllib:
            pyproject_path = Path(__file__).resolve().parents[3] / "pyproject.toml"
            if pyproject_path.exists():
                try:
                    with pyproject_path.open("rb") as f:
                        data = tomllib.load(f)
                        project = data.get("project", {})
                        name = project.get("name", name)
                        version = project.get("version", version)
                except Exception:
                    pass

    return name, version


def get_syslib_build_time() -> str:
    """
    Returns the build time (ctime) of syslib*.so in the syscall directory.

    Format: 'Jun 2025'. Returns 'MM-YYYY' if not found or on error.

    Returns:
        A formatted build time string
    """
    build_time = "MM-YYYY"

    try:
        base_dir = Path(__file__).resolve().parents[2]
        syscall_dir = base_dir / "syscall"
        candidates = list(syscall_dir.glob("syslib*.so"))
        if candidates:
            ctime = os.path.getctime(candidates[0])
            return time.strftime("%b %Y", time.localtime(ctime))
    except Exception:
        pass

    return build_time
