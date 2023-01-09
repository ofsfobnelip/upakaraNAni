# This file should only be installed in Windows
import shubhlipi as sh
import os
from zipfile import ZipFile

sh.makedir("bin")


def append_var(pth, vl):
    if not sh.IS_WINDOWS:
        return
    from winregistry import WinRegistry
    REG = WinRegistry()
    env = REG.read_entry('HKEY_CURRENT_USER\Environment', pth).value
    if vl not in env:
        sh.cmd(f'setx  {pth} "{env};{vl}"')
        print(f'Appended at {pth} -> {vl}')


opts = [
    "7zip",
    "curl",  # Makinf REST API requests
    # "traefik",  # Reverse Proxy
    "exe_compiler",  # ISCC Compiler
    "signer",  # Microsoft Signer
    "android",  # Android tools to sign and bundle apk
]
for x in sh.argv:
    if x == "7zip":
        with ZipFile('./files/7zip.zip', 'r') as zipObj:
            zipObj.extractall('bin\\7zip')
        print(x, "Installed 7zip")
    elif x == "curl" and sh.IS_WINDOWS:
        lc = './files/curl-7.84.0_6-win64-mingw.7z'
        if os.path.isdir("./bin/curl"):
            sh.delete_folder('./bin/curl')
        sh.extract(lc, './bin/curl')
        append_var('Path', f'{sh.tool}\\curl\\bin')
        print(x, "Installed curl")
    # elif x == "traefik" and sh.IS_WINDOWS:
    #     lc = './files/traefik_v2.8.4_windows_386.7z'
    #     if os.path.isdir("./bin/traefik"):
    #         sh.delete_folder('./bin/traefik')
    #     sh.extract(lc, './bin/traefik')
    #     append_var('Path', f'{sh.tool}/traefik')
    #     print(x, "Installed Traefik")
    elif x == "exe_compiler":
        sh.extract('./files/compiler.7z', './bin/compiler')
        print("Installed Inno Setup Compiler")
    elif x == "signer":
        sh.extract('./files/signer.7z', './bin')
        print(x, "Installed 'signtool' and 'verpatch'")
    elif x == "android":
        sh.extract('./files/android.7z', './bin/android')
        # append_var('Path', f'{sh.tool}\\android')
        print(x, "Installed Android tools")
