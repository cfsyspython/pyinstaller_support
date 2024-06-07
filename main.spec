# main.spec
# -*- mode: python ; coding: utf-8 -*-

# Import the PyInstaller modules
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# Define the name of the executable
exe_name = 'my_application'

# Collect additional files or modules
hidden_imports = collect_submodules('some_package')
datas = collect_data_files('some_package')

# Create the Analysis object
a = Analysis(
    ['main.py'],
    pathex=['/path/to/your/project'],
    binaries=[],
    datas=datas,
    hiddenimports=hidden_imports,
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
    noarchive=False,
)

# Define the PyInstaller PYZ object
pyz = PYZ(
    a.pure,
    a.zipped_data,
    cipher=None,
)

# Define the executable
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=exe_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # Set to False for a windowed application
)

# Define the COLLECT object to bundle everything into a single folder
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name=exe_name,
)
