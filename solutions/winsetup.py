"""
Setup file to generate windows build
"""
import os
import sys
from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": [
        "sklearn",
        "pandas",
        "requests",
    ],
    "excludes": [],
    "includes": [],
    "include_files": [
        "../Images/Scaler_Academy_logo.ico",
    ],
    "include_msvcr": True,
}

shortcut_table = [
    (
        "DesktopShortcut",  # Shortcut
        "DesktopFolder",  # Directory_
        "College Admission Prediction",  # Name
        "TARGETDIR",  # Component_
        "[TARGETDIR]College Admission Prediction.exe",  # Target
        None,  # Arguments
        None,  # Description
        None,  # Hotkey
        None,  # Icon
        None,  # IconIndex
        None,  # ShowCmd
        "TARGETDIR",  # WkDir
    )
]

# Now create the table dictionary
msi_data = {"Shortcut": shortcut_table}

# Change some default MSI options and specify the use of the above defined tables
bdist_msi_options = {"data": msi_data}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
    base = "Win32GUI"
setup(
    name="College Admission Prediction",
    version="1.0.0",
    description="College Admission Prediction",
    options={"build_exe": build_exe_options, "bdist_msi": bdist_msi_options},
    url="https://www.scaler.com",
    executables=[
        Executable(
            script=os.path.join(os.getcwd() + "/main.py"),
            target_name="College Admission Prediction.exe",
            icon="../Images/Scaler_Academy_logo.ico",
            shortcut_name="College Admission Prediction",
            shortcut_dir="DesktopFolder",
            base=base,
        )
    ],
)