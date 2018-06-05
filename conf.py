from recommonmark.parser import CommonMarkParser
extensions = ['sphinx.ext.mathjax',
    'sphinx.ext.githubpages']
templates_path = ['_templates']
source_suffix = ['.rst', '.md']
source_parsers = {
        '.md': CommonMarkParser,
        }
master_doc = 'index'
project = 'Técnico Integrado em Informática'
copyright = '2018, IFRN'
author = 'IFRN'
version = '2012'
release = '2012'
language = 'pt_BR'
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'alabaster'
html_static_path = ['_static']
htmlhelp_basename = 'TcnicoIntegradoemInformticadoc'
latex_elements = {
}
latex_documents = [
    (master_doc, 'TcnicoIntegradoemInformtica.tex', 'Técnico Integrado em Informática Documentation',
     'IFRN', 'manual'),
]
man_pages = [
    (master_doc, 'tcnicointegradoeminformtica', 'Técnico Integrado em Informática Documentation',
     [author], 1)
]
texinfo_documents = [
    (master_doc, 'TcnicoIntegradoemInformtica', 'Técnico Integrado em Informática Documentation',
     author, 'TcnicoIntegradoemInformtica', 'One line description of project.',
     'Miscellaneous'),
]
