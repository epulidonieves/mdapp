# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
import importlib.metadata
sys.path.insert(0, os.path.abspath('../../src/'))

project = 'MdApp'
copyright = '2022, epulidonieves <epulido.nieves@gmail.com>'
author = 'epulidonieves <epulido.nieves@gmail.com>'
release = importlib.metadata.version("mdapp")

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx.ext.autodoc",
    "sphinx_autodoc_typehints",
]

templates_path = ['_templates']
exclude_patterns = []
add_module_names = False

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_show_sourcelink = False
html_static_path = ['_static']
