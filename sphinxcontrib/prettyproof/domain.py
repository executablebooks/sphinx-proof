"""
sphinxcontrib.prettyproof.domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A Proof Sphinx Domain

:copyright: Copyright 2020 by the QuantEcon team, see AUTHORS
:licences: see LICENSE for details
"""
from typing import Any, Dict, Tuple, List
from docutils.nodes import Element, Node, document, system_message
from sphinx.environment import BuildEnvironment
from sphinx.addnodes import pending_xref
from sphinx.builders import Builder

from collections import defaultdict
from sphinx.domains import Domain, Index
from sphinx.roles import XRefRole
from sphinx.util.nodes import make_refnode
from sphinx.util import logging
from docutils import nodes
from .directive import ProofDirective
from .proof_type import PROOF_TYPES

logger = logging.getLogger(__name__)


def get_solution_title(env, typ, match):
    # Get exercise label
    exercise_label = match.get("title", "")

    # If exercise label doesn't exist; exception has already been thrown
    try:
        label_match = env.proof_list.get(exercise_label, {})
    except Exception:
        return None

    # Get document name of label match
    docname = label_match.get("docname", "")

    # If exercise directive is enumerable
    if not label_match.get("nonumber", bool):
        _ = env.toc_fignumbers.get(docname, {}).get("proof", {}).get(exercise_label, ())
        number = ".".join(map(str, _))
        title_text = f"{typ.title()} to {label_match.get('type', '').title()} {number}"
        title = nodes.Text(title_text, title_text)
    else:
        # If exercise directive is unenumerable and has no title
        if label_match.get("title", "") == "":
            title_text = f"{typ.title()} to {label_match.get('type', '').title()}"
            title = nodes.Text(title_text, title_text)
        else:
            # If exercise directive is unenumerable but has title
            # Extract title
            exercise_title = env.proof_list[exercise_label].get("node")[0]

            if len(exercise_title) == 1:
                # Retrieve text item
                item = exercise_title[0]
                # Remove parantheses from title
                item_text = (
                    typ.title()
                    + " to "
                    + item.astext()[
                        item.astext().find("(") + 1 : item.astext().rfind(")")
                    ]
                )
                # Create new title as text node
                title = nodes.Text(item_text, item_text)
            else:
                # Retrieve first and last item
                first_item, last_item = exercise_title[0], exercise_title[-1]
                # Remove parantheses from title
                first_text = first_item.astext()[first_item.astext().find("(") + 1 :]
                last_text = last_item.astext()[: last_item.astext().rfind(")")]
                # Replace
                exercise_title.replace(first_item, nodes.Text(first_text))
                exercise_title.replace(last_item, nodes.Text(last_text))
                # Create new title as text node
                title = nodes.inline(text="Solution to ")
                # Loop through elements
                for item in exercise_title:
                    title.append(item)
    return title


class ProofIndex(Index):

    name = "proof"
    localname = "Proof Index"
    shortname = "Proof"

    def generate(self, docnames=None) -> Tuple[Dict[str, Any], bool]:
        content = defaultdict(list)

        if not hasattr(self.domain.env, "proof_list"):
            return content, True

        proofs = self.domain.env.proof_list

        # name, subtype, docname, typ, anchor, extra, qualifier, description
        for anchor, values in proofs.items():
            content[anchor].append(
                (
                    anchor,
                    values["prio"],
                    values["docname"],
                    anchor,
                    values["docname"],
                    "",
                    values["type"],
                )
            )

        content = sorted(content.items())
        return content, True


class ProofXRefRole(XRefRole):
    def result_nodes(
        self, document: document, env: BuildEnvironment, node: Element, is_ref: bool
    ) -> Tuple[List[Node], List[system_message]]:

        node["refdomain"] = "proof"
        return [node], []


class ProofDomain(Domain):

    name = "proof"
    label = "Proof Domain"

    roles = {"ref": ProofXRefRole()}

    indices = {ProofIndex}

    directives = {
        **{"proof": ProofDirective},
        **PROOF_TYPES,
    }

    def resolve_xref(
        self,
        env: BuildEnvironment,
        fromdocname: str,
        builder: Builder,
        typ: str,
        target: str,
        node: pending_xref,
        contnode: Element,
    ) -> Element:

        # If target exists
        try:
            match = env.proof_list[target]
        except Exception:
            docpath = self.env.doc2path(fromdocname)
            path = docpath[: docpath.rfind(".")]
            msg = f"label '{target}' not found"
            logger.warning(msg, location=path, color="red")
            return None

        todocname = match.get("docname", "")
        typ = match.get("type", "")
        text = contnode[0]

        # If label reference with no additional text
        if target in text:
            nonumber = env.proof_list.get(target, {}).get("nonumber", bool)

            # If numbered directive, update title
            if not nonumber:
                _ = (
                    env.toc_fignumbers.get(todocname, {})
                    .get("proof", {})
                    .get(target, ())
                )
                number = ".".join(map(str, _))
                title_text = f"{match.get('type', '').title()} {number}"
                title = nodes.Text(title_text, title_text)

            # If match type is a solution directive
            if typ == "solution":
                title = get_solution_title(env, typ, match)
        else:
            title = nodes.Text(text, text)
        # builder, fromdocname, todocname, targetid, child, title=None
        return make_refnode(builder, fromdocname, todocname, target, title)
