"""
environs/patches/sysinfo.py

Updates the SYSINFO environment variable by gathering system information.
Supports macOS and Linux. Falls back to "unknown" or 0 if data is unavailable.
"""

import os
import platform
import shutil
import subprocess
from typing import Any

from shellkit.libc import eprintln
from shellkit.shell.environs.accessors import set_sysinfo


def get_arch() -> str:
    """
    Returns the system architecture (e.g., x86_64, arm64).
    """
    return platform.machine()


def get_uname() -> str:
    """
    Returns the system name (e.g., Linux, Darwin).
    """
    return platform.system()


def get_kernel_version() -> str:
    """
    Returns the OS kernel version string (e.g., 5.15.0).
    """
    return platform.release()


def get_os_release() -> str:
    """
    Returns the full OS release string (e.g., macOS-14.4.1-arm64).
    """
    return platform.platform()


def get_cpu_description() -> str:
    """
    Returns a human-readable description of the CPU (e.g., Intel Core i7).
    On macOS, uses sysctl. Falls back to platform.processor().
    """
    system = platform.system().lower()

    if system == "darwin":
        try:
            output = subprocess.check_output(["sysctl", "-n", "machdep.cpu.brand_string"])
            return output.decode().strip()
        except Exception as e:
            eprintln("[warn] get_cpu_description failed: %s", e)

    desc = platform.processor()
    return desc if desc and desc != "i386" else "unknown"


def get_physical_cores() -> int:
    """
    Returns the number of physical CPU cores.
    On Linux, counts unique physical IDs. On macOS, uses sysctl.
    """
    system = platform.system().lower()

    try:
        if system == "linux":
            # Count unique "core id" entries per "physical id"
            physical_ids = set()
            with open("/proc/cpuinfo") as f:
                for line in f:
                    if line.strip().startswith("physical id"):
                        physical_ids.add(line.strip())
            return len(physical_ids) or 0
        elif system == "darwin":
            output = subprocess.check_output(["sysctl", "-n", "hw.physicalcpu_max"])
            return int(output.strip())

    except Exception as e:
        eprintln("[warn] get_physical_cores failed: %s", e)

    return 0


def get_logical_cores() -> int:
    """
    Returns the number of logical CPU cores, falling back to physical cores.
    """
    return os.cpu_count() or get_physical_cores()


def get_hyperthreading() -> bool:
    """
    Determines whether Hyper-Threading is enabled.
    On macOS, parses system profiler output. On Linux, compares core counts.
    """
    system = platform.system().lower()

    if system == "darwin":
        try:
            output = subprocess.check_output(["system_profiler", "SPHardwareDataType"])
            text = output.decode()
            for line in text.splitlines():
                if "Hyper-Threading Technology" in line:
                    status = line.split(":")[1].strip().lower()
                    return status == "enabled"
        except Exception as e:
            eprintln("[warn] get_hyperthreading_enabled(mac) failed: %s", e)
            return False

    elif system == "linux":
        physical = get_physical_cores()
        logical = get_logical_cores()
        return logical > physical if physical else False

    return False


def get_mem_total_bytes() -> int:
    """
    Returns total memory in bytes.
    Reads from /proc/meminfo on Linux or sysctl on macOS.
    """
    system = platform.system().lower()

    try:
        if system == "linux":
            with open("/proc/meminfo") as f:
                for line in f:
                    if line.startswith("MemTotal:"):
                        return int(line.split()[1]) * 1024  # from kB to byte
        elif system == "darwin":
            output = subprocess.check_output(["sysctl", "-n", "hw.memsize"])
            return int(output.strip())

    except Exception as e:
        eprintln("[warn] get_total_memory_bytes failed: %s", e)

    return 0


def get_mem_total_gb() -> str:
    """
    Returns total memory as a rounded GB string (e.g., '16GB').
    """
    total_mem = get_mem_total_bytes()
    return f"{round(total_mem / 1024**3)}GB"


def get_disk_total_bytes() -> int:
    """
    Returns total disk space in bytes (root volume only).
    """
    try:
        total_disk, _, _ = shutil.disk_usage("/")
        return total_disk

    except Exception as e:
        eprintln("[warn] get_disk_total_bytes failed: %s", e)
        return 0


def get_disk_total_gb() -> str:
    """
    Returns total disk space as a rounded GB string (e.g., '512GB').
    """
    total_disk = get_disk_total_bytes()
    return f"{round(total_disk / 1024**3)}GB"


def get_machine_product_name() -> str:
    """
    Returns the hardware model/product name (e.g., MacBook Pro, ThinkPad).
    Uses system_profiler or /sys/class/dmi.
    """
    system = platform.system().lower()

    try:
        if system == "darwin":
            output = subprocess.check_output(
                ["system_profiler", "SPHardwareDataType"], stderr=subprocess.DEVNULL
            )
            for line in output.decode().splitlines():
                if "Model Name" in line:
                    return line.split(":")[1].strip()

        elif system == "linux":
            path = "/sys/class/dmi/id/product_name"
            if os.path.exists(path):
                with open(path) as f:
                    return f.read().strip()

    except Exception as e:
        eprintln("[warn] get_machine_model_name failed: %s", e)

    return "unknown"


def get_machine_serial_number() -> str:
    """
    Returns the serial number of the machine.
    Uses system_profiler or /sys/class/dmi.
    """
    system = platform.system().lower()

    try:
        if system == "darwin":
            output = subprocess.check_output(
                ["system_profiler", "SPHardwareDataType"], stderr=subprocess.DEVNULL
            )
            for line in output.decode().splitlines():
                if "Serial Number" in line:
                    return line.split(":")[1].strip()

        elif system == "linux":
            path = "/sys/class/dmi/id/product_serial"
            if os.path.exists(path):
                with open(path) as f:
                    return f.read().strip()

    except Exception as e:
        eprintln("[warn] get_machine_serial_number failed: %s", e)

    return "unknown"


def get_gpu_info() -> list[dict[str, Any]]:
    """
    Returns a list of GPU info dictionaries on macOS.
    Includes model name, VRAM, and GPU type (discrete/integrated).
    """
    try:
        output = subprocess.check_output(
            ["system_profiler", "SPDisplaysDataType"], text=True, stderr=subprocess.DEVNULL
        )
    except Exception as e:
        eprintln("[warn] get_gpu_info failed: %s", e)
        return []

    gpus: list[dict[str, Any]] = []
    current_gpu: dict[str, Any] = {}
    in_display_section = False

    for line in output.splitlines():
        line = line.strip()

        if not line:
            continue

        if line.startswith("Displays:"):
            in_display_section = True
            continue

        if in_display_section:
            continue

        # GPU name
        if line.startswith("Chipset Model:"):
            if current_gpu:
                gpus.append(current_gpu)
                current_gpu = {}
            current_gpu["name"] = line.split(":", 1)[1].strip()

        # VRAM (Intel/AMD GPUs)
        elif "VRAM" in line:
            current_gpu["vram"] = line.split(":", 1)[1].strip()

        # Apple Silicon: convert core count to VRAM description
        elif line.startswith("Total Number of Cores:"):
            cores = line.split(":", 1)[1].strip()
            current_gpu["vram"] = f"{cores} cores (Apple Silicon Shared)"

        # GPU type: discrete or integrated
        elif line.startswith("Bus:"):
            bus = line.split(":", 1)[1].strip().lower()
            if "pci" in bus:
                current_gpu["type"] = "discrete"
            elif "built-in" in bus:
                current_gpu["type"] = "integrated"
            else:
                current_gpu["type"] = "unknown"

    if current_gpu:
        gpus.append(current_gpu)

    return gpus


def patch_sysinfo() -> None:
    """
    Collects all relevant system information and updates the SYSINFO environment.
    Includes architecture, CPU/memory, disk, hardware model, serial number, and GPU (macOS only).
    """
    info = {
        # Architecture info
        "arch": get_arch(),
        "uname": get_uname(),
        "kernel_version": get_kernel_version(),
        "os_release": get_os_release(),

        # CPU details
        "cpu": get_cpu_description(),
        "cores": get_physical_cores(),
        "logical_cores": get_logical_cores(),
        "hyperthreading": get_hyperthreading(),

        # Memory and disk
        "mem_total": get_mem_total_gb(),
        "disk_total": get_disk_total_gb(),

        # Machine product name
        "product_name": get_machine_product_name(),

        # Hardware sn
        "serial_number": get_machine_serial_number(),
    }

    # Add GPU info (macOS only)
    if platform.system().lower() == "darwin":
        info["gpu"] = get_gpu_info()

    set_sysinfo(info)
