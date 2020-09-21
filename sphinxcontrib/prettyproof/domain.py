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


def get_linked_node_title(env, typ, match):
    linked_node_label = match.get("title", "")

    try:
        label_match = env.proof_list.get(linked_node_label, {})
    except Exception:
        return None

    docname = label_match.get("docname", "")

    # If exercise directive is enumerable
    if not label_match.get("nonumber", bool):
        _ = (
            env.toc_fignumbers.get(docname, {})
            .get("proof", {})
            .get(linked_node_label, ())
        )
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
            linked_node_title = env.proof_list[linked_node_label].get("node")[0]

            title = nodes.inline(text=f"{typ.title()} to ")
            items = remove_parantheses(linked_node_title)

            for element in items:
                linked_node_title.replace(element[0], nodes.Text(element[1]))

            for ttl in linked_node_title:
                title.append(ttl)
    return title


def remove_parantheses(title: str) -> List[Tuple[str, str]]:
    updated_items = []
    if len(title) == 1:
        # Retrieve text item
        item = title[0]
        text = item.astext()[item.astext().find("(") + 1 : item.astext().rfind(")")]
        updated_items.append((item, text))
    else:
        # Retrieve first and last test item
        first_item, last_item = title[0], title[-1]
        # Find and remove "(" and ")" from title
        first_text = first_item.astext()[first_item.astext().find("(") + 1 :]
        last_text = last_item.astext()[: last_item.rfind(")")]
        updated_items.append((first_item, first_text))
        updated_items.append((last_item, last_text))
    return updated_items


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

    linked_directives = ("solution",)

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

            # If match type is in linked_directives
            if typ in self.linked_directives:
                title = get_linked_node_title(env, typ, match)
        else:
            title = nodes.Text(text, text)
        # builder, fromdocname, todocname, targetid, child, title=None
        return make_refnode(builder, fromdocname, todocname, target, title)
