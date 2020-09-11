"""
sphinxcontrib.prettyproof.nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enumerable and unenumerable nodes

:copyright: Copyright 2020 by the QuantEcon team, see AUTHORS
:licences: see LICENSE for details
"""
from sphinx.builders.html import HTMLTranslator
from sphinx.util import logging
from docutils import nodes
from docutils.nodes import Node

logger = logging.getLogger(__name__)


class proof_node(nodes.Admonition, nodes.Element):
    pass


class enumerable_node(nodes.Admonition, nodes.Element):
    pass


class unenumerable_node(nodes.Admonition, nodes.Element):
    pass


def visit_enumerable_node(self, node: Node) -> None:
    self.body.append(self.starttag(node, "div", CLASS="admonition"))


def depart_enumerable_node(self, node: Node) -> None:
    typ = node.attributes.get("type", "")
    ids = node.attributes.get("ids", [])[0]

    # Find index in list of 'Proof #'
    number = get_node_number(self, ids)
    idx = self.body.index(f"Proof {number} ")
    self.body[idx] = f"{typ.title()} {number} "
    self.body.append("</div>")


def visit_unenumerable_node(self, node: Node) -> None:
    self.body.append(self.starttag(node, "div", CLASS="admonition"))

    if node.get("type", "") == "solution":
        self.body.append('<p class="admonition-title">')


def depart_unenumerable_node(self, node: Node) -> None:
    typ = node.attributes.get("type", "")
    title = node.attributes.get("title", "")

    idx = len(self.body) - self.body[-1::-1].index('<p class="admonition-title">')

    if typ == "solution":
        exc_label = title
        env = self.builder.env
        if exc_label in env.proof_list.keys():
            # If nonumber check if title
            if env.proof_list[exc_label].get("nonumber", bool):
                node_title = env.proof_list[exc_label].get("title", "")
                if node_title == "":
                    new_title = f'<a href="#{exc_label}">Solution to Exercise</a></p>'
                else:
                    # TODO: if title contains LaTeX
                    new_title = (
                        f'<a href="#{exc_label}">Solution to {node_title}</a></p>'
                    )
            else:
                number = get_node_number(self, title)
                new_title = f'<a href="#{title}">Solution to Exercise {number}</a></p>'
        else:
            # If label of exercise referenced in solution not found
            docpath = env.doc2path(self.builder.current_docname)
            path = docpath[: docpath.rfind(".")]
            msg = "label '{}' not found.".format(title)
            logger.warning(msg, location=path, color="red")
            new_title = "Solution to Exercise"
    else:
        new_title = typ.title()

    element = f"<span>{new_title} </span>"
    self.body.insert(idx, element)
    self.body.append("</div>")


def visit_proof_node(self, node: Node) -> None:
    pass


def depart_proof_node(self, node: Node) -> None:
    pass


def get_node_number(self: HTMLTranslator, attr: str) -> str:
    key = "proof"
    number = self.builder.fignumbers.get(key, {}).get(attr, ())
    return ".".join(map(str, number))
