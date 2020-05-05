from docutils import nodes
from docutils.nodes import field_list
from docutils.parsers.rst import Directive


KNOWN_CATEGORIES = [
    'types', 'keywords', 'languages', 'industries', 'standards', 'companies', 'people'
]


def debug_print(string):
    pass


class MetaInfoNode(nodes.General, nodes.Element):
    meta_information = None

    def __init__(self, meta_information):
        assert meta_information
        super(nodes.General, self).__init__()
        super(nodes.Element, self).__init__()

        self.meta_information = meta_information

        pass

    def get_meta_information(self):
        return self.meta_information


def html_visit_semantics_node(self, node):
    # debug_print(node)

    meta_attrs = {}
    meta_information = node.get_meta_information()
    for field in meta_information:
        meta_attrs[field] = ', '.join(meta_information[field])

    self.body.append(self.starttag(node, 'div', '', CLASS='asc-node', **meta_attrs))


def html_depart_semantics_node(self, node):
    self.body.append('</div>')


class MetaSummaryNode(nodes.General, nodes.Element):
    pass


class MetaSummaryDirective(Directive):
    def run(self):
        return [MetaSummaryNode('')]


class ASCMetaDirective(Directive):
    has_content = True

    def run(self):
        env = self.state.document.settings.env
        if not hasattr(env, 'all_asc_meta'):
            env.all_asc_meta = []

        paragraph_node = nodes.paragraph(text='')

        self.state.nested_parse(self.content, self.content_offset, paragraph_node)

        meta_information = {}

        if not isinstance(paragraph_node.children[0], field_list):
            debug_print("error: Meta information is missing")
            exit(1)

        field_list_node = paragraph_node.children.pop(0)

        debug_print(dir(nodes))

        debug_print(field_list_node.children)
        for field in field_list_node:
            # debug_print(dir(field))
            debug_print("field.tagname: {}".format(field.children))

            field_name_node = field.children[0]
            field_body_node = field.children[1]

            field_name_text_node = field_name_node.children[0]
            field_name_text = field_name_text_node.astext()
            assert isinstance(field_name_text, str)
            assert field_name_text in KNOWN_CATEGORIES

            debug_print("field_name_text: {}".format(field_name_text))

            field_body_paragraph_node = field_body_node.children[0]
            debug_print("field_body_paragraph_node: {}".format(field_body_paragraph_node))

            field_body_paragraph_text_node = field_body_paragraph_node.children[0]
            field_body_paragraph_text = field_body_paragraph_text_node.astext()
            assert isinstance(field_body_paragraph_text, str)

            debug_print("field_body_paragraph_text: {}".format(field_body_paragraph_text))

            if not field_name_text in meta_information:
                meta_information[field_name_text] = []

            values = [v.strip() for v in field_body_paragraph_text.split(',')]
            meta_information[field_name_text].extend(values)

        debug_print("final meta_information: {}".format(meta_information))

        container = MetaInfoNode(meta_information)
        container.append(paragraph_node)

        env.all_asc_meta.append(meta_information)

        return [container]


def process_asc_meta(app, doctree, fromdocname):
    env = app.builder.env
    if not env.all_asc_meta:
        return

    debug_print("process_asc_meta: {}".format(env.all_asc_meta))

    for node in doctree.traverse(MetaSummaryNode):
        content = []

        all_asc_meta = env.all_asc_meta

        all_asc_meta_content = {}
        for asc_meta in all_asc_meta:
            for field in asc_meta:
                if field not in all_asc_meta_content:
                    all_asc_meta_content[field] = set()

                all_asc_meta_content[field].update(asc_meta[field])

        for category in KNOWN_CATEGORIES:
            assert category in all_asc_meta_content

            para = nodes.paragraph()

            # Category
            para += nodes.strong(None, category.capitalize())

            para += nodes.Text(": ", 'ASC-TODO')

            # Values
            value_span_tags = []
            category_values = sorted(all_asc_meta_content[category])

            for value in category_values:
                value_span_tags.append('<span category="{}" class="keyword">{}</span>'.format(category, value))

            values = ' '.join(value_span_tags)

            raw_node = nodes.raw(None, values, format='html')

            para += raw_node

            content.append(para)

        node.replace_self(content)


def setup(app):
    app.add_node(
        MetaInfoNode,
        html=(
            html_visit_semantics_node,
            html_depart_semantics_node
        )
    )
    app.add_directive("asc-meta", ASCMetaDirective)

    app.add_directive('asc-meta-summary', MetaSummaryDirective)
    app.add_node(MetaSummaryNode)

    app.connect('doctree-resolved', process_asc_meta)

    return {
        'version': '0.1',
        'parallel_read_safe': False,
        'parallel_write_safe': False,
    }
