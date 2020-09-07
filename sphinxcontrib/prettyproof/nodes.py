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
    number = get_node_number(self, node, ids)
    idx = self.body.index(f"Proof {number} ")
    self.body[idx] = f"{typ.title()} {number} "
    self.body.append("</div>")


def visit_unenumerable_node(self, node: Node) -> None:
    self.body.append(self.starttag(node, "div", CLASS="admonition"))


def depart_unenumerable_node(self, node: Node) -> None:
    typ = node.attributes.get("type", "")
    title = node.attributes.get("title", "")
    node_id = node.attributes.get("ids", [])[0]

    if typ == "solution":
        idx = [
            ii for ii in range(len(self.body) - 1, -1, -1) if node_id in self.body[ii]
        ][0] + 1
        env = self.builder.env

        if title in env.proof_list.keys():
            # IF NONUMBER? If NONTITLE?
            number = get_node_number(self, node, title)
            title = (
                f'<a href="#{title}">Solution to Exercise {number}</a>'  # add target
            )
        else:
            # If label of exercise referenced in solution not found
            path = env.doc2path(self.builder.current_docname)
            msg = "label '{}' not found.".format(title)
            logger.warning(msg, location=path, color="red")
            title = "Solution to Exercise"

    else:
        title = typ.title()
        if title == "":
            idx = len(self.body) - self.body[-1::-1].index(
                '<p class="admonition-title">'
            )
        else:
            idx = self.body.index(title)

    element = f"<span>{title} </span>"
    self.body.insert(idx, element)
    self.body.append("</div>")


def visit_proof_node(self, node: Node) -> None:
    pass


def depart_proof_node(self, node: Node) -> None:
    pass


def get_node_number(self: HTMLTranslator, node: Node, attr: str) -> str:
    key = "proof"
    number = self.builder.fignumbers.get(key, {}).get(attr, ())
    return ".".join(map(str, number))
