from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.statemachine import StringList, ViewList

from sphinx.util.nodes import nested_parse_with_titles

from sphinx.util import logging
log = logging.getLogger(__name__)

try:
    import awesome_meta_conf as aws_config
except ImportError as e:
    log.error("cannot import 'awesome_meta_conf.py'. "
              "make sure you have provided path to it. "
              "Example: add this to the conf.py file: sys.path.insert(0, os.path.abspath('.'))")
    raise SystemExit(1)

VERSION = '0.0.1'


class MetaInfoNode(nodes.General, nodes.Element):
    meta_information = None

    def __init__(self, meta_information):
        assert meta_information
        super(MetaInfoNode, self).__init__()
        self.meta_information = meta_information

    def get_meta_information(self):
        return self.meta_information


def html_visit_semantics_node(self, node):
    meta_attrs = {}
    meta_information = node.get_meta_information()
    for field in meta_information:
        meta_attrs[field] = ', '.join(meta_information[field])

    self.body.append(self.starttag(node, 'div', '', CLASS='aws-node', **meta_attrs))


def html_depart_semantics_node(self, node):
    self.body.append('</div>')


class MetaSummaryNode(nodes.General, nodes.Element):
    pass


class MetaSummaryDirective(Directive):
    def run(self):
        return [MetaSummaryNode('')]


class ASCMetaDirective(Directive):
    has_content = True

    option_spec = aws_config.categories_spec

    def run(self):
        env = self.state.document.settings.env
        if not hasattr(env, 'all_aws_meta'):
            env.all_aws_meta = []

        meta_information = {}

        for option in self.options.keys():
            if option not in meta_information:
                meta_information[option] = []

            values = self.options.get(option, '').split(',')
            values = [v.strip() for v in values]

            meta_information[option].extend(values)

        content_to_rst = StringList()
        for line in self.content:
            content_to_rst.append(line, self.name)
        node_need_content = nodes.paragraph()
        node_need_content.document = self.state.document
        nested_parse_with_titles(self.state, content_to_rst, node_need_content)

        container = MetaInfoNode(meta_information)
        for foo in node_need_content.children:
            container.append(foo)

        env.all_aws_meta.append(meta_information)

        return [container]


def process_aws_meta(app, doctree, fromdocname):
    env = app.builder.env
    supported_categories = aws_config.supported_categories

    if not hasattr(env, 'all_aws_meta'):
        return

    for node in doctree.traverse(MetaSummaryNode):
        content = []

        all_aws_meta = env.all_aws_meta

        all_aws_meta_content = {}
        for aws_meta in all_aws_meta:
            for field in aws_meta:
                if field not in all_aws_meta_content:
                    all_aws_meta_content[field] = set()

                all_aws_meta_content[field].update(aws_meta[field])

        for category in supported_categories:
            if category not in all_aws_meta_content:
                continue

            para = nodes.paragraph()

            # Category
            para += nodes.strong(None, category.capitalize())

            para += nodes.Text(": ", 'AWS-TODO')

            # Values
            value_span_tags = []
            category_values = sorted(all_aws_meta_content[category])

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
    app.add_directive("aws-meta", ASCMetaDirective)

    app.add_directive('aws-meta-summary', MetaSummaryDirective)
    app.add_node(MetaSummaryNode)

    app.connect('doctree-resolved', process_aws_meta)

    app.add_config_value('awesome_meta_config_categories', [], 'html')

    return {
        'version': VERSION,
        'parallel_read_safe': False,
        'parallel_write_safe': False,
    }
