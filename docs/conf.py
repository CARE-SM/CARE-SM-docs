import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'CARE Semantic Model'
copyright = ''
author = 'Pablo Alarcon Moreno'

extensions = ['myst_parser']
source_suffix = {
    '.md': 'markdown',
}
master_doc = 'index'

language = 'en'
html_theme = 'sphinx_rtd_theme'
html_static_path = ["_static"]
html_favicon = "_static/favicon.png"