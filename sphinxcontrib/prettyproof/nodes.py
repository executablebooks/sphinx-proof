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
        env = self.builder.env
        exercise_label = node.attributes.get("title", "")
        self.body.append('<p class="admonition-title">')

        # Check to see if exercise label exists
        if exercise_label in env.proof_list.keys():

            # Check to see if exercise has nonumber
            if env.proof_list[exercise_label].get("nonumber", bool):
                # Check if title string in exercise is nonempty
                exercise_title = env.proof_list[exercise_label].get("title", "")
                if exercise_title == "":
                    title = f'<a href="#{exercise_label}">Solution to Exercise</a>'
                    self.body.append(f"<span>{title}</span>")
                else:
                    # Retrieve exercise title
                    atts = {}
                    exercise_title = env.proof_list[exercise_label].get("node")[0]
                    atts["href"] = "#" + exercise_label

                    if len(exercise_title) == 1:
                        # Retreive text item
                        item = exercise_title[0]
                        # Find and remove "(", ")" from title
                        item_txt = item.astext()[
                            item.astext().find("(") + 1 : item.astext().rfind(")")
                        ]
                        # Replace
                        exercise_title.replace(item, nodes.Text(item_txt))
                    else:
                        # Retreive first text item
                        first_item, last_item = exercise_title[0], exercise_title[-1]
                        # Find and remove "(" and ")" from title
                        first_txt = first_item.astext()[
                            first_item.astext().find("(") + 1 :
                        ]
                        last_txt = last_item.astext()[: last_item.rfind(")")]
                        # Replace
                        exercise_title.replace(first_item, nodes.Text(first_txt))
                        exercise_title.replace(last_item, nodes.Text(last_txt))

                    self.body.append(
                        self.starttag(exercise_title, "a", "Solution to ", **atts)
                    )

                    for item in exercise_title:
                        if type(item) == nodes.math:
                            # https://fossies.org/linux/Sphinx/sphinx/ext/mathjax.py
                            self.body.append(
                                self.starttag(
                                    item,
                                    "span",
                                    "",
                                    CLASS="math notranslate nohighlight",
                                )
                            )
                            self.body.append(
                                self.builder.config.mathjax_inline[0]
                                + self.encode(item.astext())
                                + self.builder.config.mathjax_inline[1]
                                + "</span>"
                            )
                        else:
                            self.body.append(item.astext())
                    self.body.append("</a>")
            else:
                # Exercise is an enumerable node
                number = get_node_number(self, exercise_label)
                title = f'<a href="#{exercise_label}">Solution to Exercise {number}</a>'
                self.body.append(f"<span>{title}</span>")
        else:
            # If label of exercise referenced in solution not found
            docpath = env.doc2path(self.builder.current_docname)
            path = docpath[: docpath.rfind(".")]
            msg = f"label '{exercise_label}' not found"
            logger.warning(msg, location=path, color="red")
            title = "Solution to Exercise"
            self.body.append(f"<span>{title}</span>")

        self.body.append("</p>")


def depart_unenumerable_node(self, node: Node) -> None:
    typ = node.attributes.get("type", "")
    idx = len(self.body) - self.body[-1::-1].index('<p class="admonition-title">')

    if typ != "solution":
        element = f"<span>{typ.title()} </span>"
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
