from setuptools import setup   

APP=['PD_Crack.py']
OPTIONS = {
    'iconfile':'parallels_desktop_macos_bigsur_icon_189848.png',
    'argv_emulation': True,
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app']    
)