"""
sphinx_proof.nodes
~~~~~~~~~~~~~~~~~~

Enumerable and unenumerable nodes

:copyright: Copyright 2020 by the QuantEcon team, see AUTHORS
:licences: see LICENSE for details
"""
from sphinx.builders.html import HTMLTranslator
from docutils import nodes
from docutils.nodes import Node
from sphinx.writers.latex import LaTeXTranslator

CR = "\n"
latex_admonition_start = CR + "\\begin{sphinxadmonition}{note}"
latex_admonition_end = "\\end{sphinxadmonition}" + CR


class proof_node(nodes.Admonition, nodes.Element):
    pass


class enumerable_node(nodes.Admonition, nodes.Element):
    pass


class unenumerable_node(nodes.Admonition, nodes.Element):
    pass


def visit_enumerable_node(self, node: Node) -> None:
    if isinstance(self, LaTeXTranslator):
        docname = find_parent(self.builder.env, node, "section")
        self.body.append("\\label{" + f"{docname}:{node.attributes['label']}" + "}")
        self.body.append(latex_admonition_start)
    else:
        self.body.append(self.starttag(node, "div", CLASS="admonition"))


def depart_enumerable_node(self, node: Node) -> None:
    typ = node.attributes.get("type", "")
    if isinstance(self, LaTeXTranslator):
        number = get_node_number_latex(self, node)
        idx = list_rindex(self.body, latex_admonition_start) + 2
        self.body.insert(idx, f"{typ.title()} {number}")
        self.body.append(latex_admonition_end)
    else:
        # Find index in list of 'Proof #'
        number = get_node_number(self, node)
        idx = self.body.index(f"Proof {number} ")
        self.body[idx] = f"{typ.title()} {number} "
        self.body.append("</div>")


def visit_unenumerable_node(self, node: Node) -> None:
    if isinstance(self, LaTeXTranslator):
        docname = find_parent(self.builder.env, node, "section")
        self.body.append("\\label{" + f"{docname}:{node.attributes['label']}" + "}")
        self.body.append(latex_admonition_start)
    else:
        self.body.append(self.starttag(node, "div", CLASS="admonition"))


def depart_unenumerable_node(self, node: Node) -> None:
    typ = node.attributes.get("type", "")
    title = node.attributes.get("title", "")
    if isinstance(self, LaTeXTranslator):
        idx = list_rindex(self.body, latex_admonition_start) + 2
        self.body.insert(idx, f"{typ.title()}")
        self.body.append(latex_admonition_end)
    else:
        if title == "":
            idx = list_rindex(self.body, '<p class="admonition-title">') + 1
        else:
            idx = list_rindex(self.body, title)
        element = f"<span>{typ.title()} </span>"
        self.body.insert(idx, element)
        self.body.append("</div>")


def visit_proof_node(self, node: Node) -> None:
    pass


def depart_proof_node(self, node: Node) -> None:
    pass


def find_parent(env, node, parent_tag):
    """Find the nearest parent node with the given tagname."""
    while True:
        node = node.parent
        if node is None:
            return None
        # parent should be a document in toc
        if (
            "docname" in node.attributes
            and env.titles[node.attributes["docname"]].astext().lower()
            in node.attributes["names"]
        ):
            return node.attributes["docname"]

    if node.tagname == parent_tag:
        return node.attributes["docname"]

    return None


def get_node_number(self: HTMLTranslator, node: Node) -> str:
    """Get the number for the directive node for HTML."""
    key = "proof"
    ids = node.attributes.get("ids", [])[0]
    number = self.builder.fignumbers.get(key, {}).get(ids, ())
    return ".".join(map(str, number))


def get_node_number_latex(self: LaTeXTranslator, node: Node) -> str:
    """Get the number for the directive node for LaTeX."""
    key = "proof"
    docname = find_parent(self.builder.env, node, "section")
    ids = node.attributes.get("ids", [])[0]
    fignumbers = self.builder.env.toc_fignumbers.get(
        docname, {}
    )  # Latex does not have builder.fignumbers
    number = fignumbers.get(key, {}).get(ids, ())
    return ".".join(map(str, number))


def list_rindex(li, x) -> int:
    """Getting the last occurence of an item in a list."""
    for i in reversed(range(len(li))):
        if li[i] == x:
            return i
    raise ValueError("{} is not in list".format(x))
