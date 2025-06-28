# -*- mode: python ; coding: utf-8 -*-


import os

project_dir = os.path.abspath('.')

a = Analysis(
    ['gerlang.py'],
    pathex=[project_dir, 'src'],
    binaries=[],
    datas=[('examples', 'examples'), ('docs', 'docs')],
    hiddenimports=['lexer', 'parser', 'interpreter'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='gerlc',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    version='version.txt',
)
