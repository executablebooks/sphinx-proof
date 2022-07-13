"""
sphinx_proof.directive
~~~~~~~~~~~~~~~~~~~~~~

A custom Sphinx Directive

:copyright: Copyright 2020 by the QuantEcon team, see AUTHORS
:licences: see LICENSE for details
"""
from typing import List
from docutils import nodes
from docutils.nodes import Node
from sphinx.util import logging
from docutils.parsers.rst import directives
from sphinx.util.docutils import SphinxDirective
from .nodes import unenumerable_node, NODE_TYPES
from .nodes import proof_node

logger = logging.getLogger(__name__)


class ElementDirective(SphinxDirective):
    """A custom Sphinx Directive"""

    name = ""
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "label": directives.unchanged_required,
        "class": directives.class_option,
        "nonumber": directives.flag,
    }

    def run(self) -> List[Node]:
        env = self.env
        typ = self.name.split(":")[1]
        serial_no = env.new_serialno()
        if not hasattr(env, "proof_list"):
            env.proof_list = {}

        # If class in options add to class array
        classes, class_name = ["proof", typ], self.options.get("class", [])
        if class_name:
            classes.extend(class_name)

        label = self.options.get("label", "")
        # If label
        if label:
            self.options["noindex"] = False
            node_id = f"{label}"
        else:
            self.options["noindex"] = True
            label = f"{typ}-{serial_no}"
            node_id = f"{typ}-{serial_no}"
        ids = [node_id]

        # Duplicate label warning
        if not label == "" and label in env.proof_list.keys():
            path = env.doc2path(env.docname)[:-3]
            other_path = env.doc2path(env.proof_list[label]["docname"])
            msg = f"duplicate {typ} label '{label}', other instance in {other_path}"
            logger.warning(msg, location=path, color="red")

        title_text = ""
        if self.arguments != []:
            title_text += f" ({self.arguments[0]})"

        textnodes, messages = self.state.inline_text(title_text, self.lineno)

        section = nodes.section(classes=[f"{typ}-content"], ids=["proof-content"])
        self.state.nested_parse(self.content, self.content_offset, section)

        if "nonumber" in self.options:
            node = unenumerable_node()
        else:
            node_type = NODE_TYPES[typ]
            node = node_type()

        node.document = self.state.document
        node += nodes.title(title_text, "", *textnodes)
        node += section

        # Set node attributes
        node["ids"].extend(ids)
        node["classes"].extend(classes)
        node["title"] = title_text
        node["label"] = label
        node["type"] = typ

        env.proof_list[label] = {
            "docname": env.docname,
            "type": typ,
            "ids": ids,
            "label": label,
            "prio": 0,
            "nonumber": True if "nonumber" in self.options else False,
        }

        return [node]


class ProofDirective(SphinxDirective):
    """A custom directive for proofs"""

    name = "proof"
    has_content = True
    required_arguments = 0
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {
        "class": directives.class_option,
    }

    def run(self) -> List[Node]:
        typ = self.name.split(":")[1]

        # If class in options add to class array
        classes, class_name = ["proof", typ], self.options.get("class", [])
        if class_name:
            classes.extend(class_name)

        section = nodes.admonition(classes=classes, ids=[typ])

        self.content[0] = "{}. ".format(typ.title()) + self.content[0]
        self.state.nested_parse(self.content, 0, section)

        node = proof_node()
        node += section

        return [node]
