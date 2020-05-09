from docutils.parsers.rst import directives

supported_categories = [
    'types',
    'keywords',
    'languages',
    'industries',
    'standards',
    'companies',
    'people'
]

categories_spec = {
    category: directives.unchanged_required
    for category in supported_categories
}
