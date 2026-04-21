# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['game.py'],
    pathex=[],
    binaries=[],
    datas=[('simkai.ttf', '.'), ('qizi1', 'qizi1'), ('qizi2', 'qizi2'), ('qizi3', 'qizi3'), ('kuang1', 'kuang1'), ('kuang2', 'kuang2'), ('kuang3', 'kuang3'), ('*.mp4', '.'), ('*.mp3', '.'), ('*.wav', '.'), ('*.jpg', '.'), ('*.png', '.')],
    hiddenimports=['pygame', 'cv2'],
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
    name='二字棋',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
