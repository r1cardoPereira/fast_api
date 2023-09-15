import sys
import os
import shutil

# Obter o caminho absoluto dos arquivos de estilo
pygments_css = os.path.abspath('../build/_static/pygments.css')
alabaster_css = os.path.abspath('../build/_static/alabaster.css')
basics_css = os.path.abspath('../build/_static/basic.css')

# Construir o caminho para a pasta _static dentro de build/html
build_static_path = os.path.join(os.path.abspath('../build/html'), '_static')

# Certificar-se de que a pasta build/html/_static existe
os.makedirs(build_static_path, exist_ok=True)

# Copiar os arquivos para a pasta de destino
shutil.copyfile(pygments_css, os.path.join(build_static_path, 'pygments.css'))
shutil.copyfile(alabaster_css, os.path.join(build_static_path, 'alabaster.css'))
shutil.copyfile(basics_css, os.path.join(build_static_path, 'basic.css'))


# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Estudos_FastAPI'
copyright = '2023, Ricardo Pereira'
author = 'Ricardo Pereira'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx_autodoc_typehints'
]


templates_path = ['_templates']
exclude_patterns = []

language = 'pt-br'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
