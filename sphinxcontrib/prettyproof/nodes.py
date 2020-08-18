"""
sphinxcontrib.prettyproof.nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enumerable and unenumerable nodes

:copyright: Copyright 2020 by the QuantEcon team, see AUTHORS
:licences: see LICENSE for details
"""
from sphinx.builders.html import HTMLTranslator
from docutils import nodes
from docutils.nodes import Node


class proof_node(nodes.Admonition, nodes.Element):
    pass


class enumerable_node(nodes.Admonition, nodes.Element):
    pass


class unenumerable_node(nodes.Admonition, nodes.Element):
    pass


def visit_enumerable_node(self, node: Node) -> None:
    typ = node.attributes.get("type", "")
    title = node.attributes.get("title", "")
    label = node.attributes.get("label", "")

    self.body.append(self.starttag(node, "div", CLASS="admonition"))
    self.body.append(f'<div class="{typ}-title proof-title">')
    self.add_fignumber(node)
    self.body.append("</div>")

    # Find index in list of 'Proof #'
    number = get_node_number(self, node)
    idx = self.body.index(f"Proof {number} ")
    self.body[idx] = f"{typ.title()} {number} {title}"


def depart_enumerable_node(self, node: Node) -> None:
    self.body.append("</div>")


def visit_unenumerable_node(self, node: Node) -> None:
    typ = node.attributes.get("type", "")
    title = node.attributes.get("title", "")
    label = node.attributes.get("label", "")

    self.body.append(self.starttag(node, "div", CLASS="admonition"))
    self.body.append(f'<div class="{typ}-title  proof-title">')
    self.body.append(f"<span>{typ.title()} {title}</span>")
    self.body.append("</div>")


def depart_unenumerable_node(self, node: Node) -> None:
    self.body.append("</div>")


def visit_proof_node(self, node: Node) -> None:
    pass


def depart_proof_node(self, node: Node) -> None:
    pass


def get_node_number(self: HTMLTranslator, node: Node) -> str:
    key = "proof"
    ids = node.attributes.get("ids", [])[0]
    number = self.builder.fignumbers.get(key, {}).get(ids, ())
    return ".".join(map(str, number))
