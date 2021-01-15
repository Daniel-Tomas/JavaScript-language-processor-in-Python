# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['PDL-Practica.py'],
             pathex=['C:\\Users\\alesi\\PycharmProjects\\PDL\\src'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

a.datas += [(".\Input.txt", "Input.txt", "DATA")]
a.datas += [(".\Error.txt", "Error.txt", "DATA")]
a.datas += [(".\Parse.txt", "Parse.txt", "DATA")]
a.datas += [(".\Tokens.txt", "Tokens.txt", "DATA")]
a.datas += [(".\TS-Output.txt", "TS-Output.txt", "DATA")]
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='PDL-Practica',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
