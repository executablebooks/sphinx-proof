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
from docutils.utils.math import math2html
from sphinx.util import logging
from docutils import nodes
from .directive import ProofDirective
from .proof_type import PROOF_TYPES

logger = logging.getLogger(__name__)


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
            msg = "label '{}' not found.".format(target)
            logger.warning(msg, location=path, color="red")
            return None

        todocname = match.get("docname", "")
        title = contnode[0]

        # If label referenced with no additional text
        if target in contnode[0]:

            number = ""
            nonumber = env.proof_list.get(target, {}).get("nonumber", bool)

            # If numbered directive, update title
            if not nonumber:
                _ = (
                    env.toc_fignumbers.get(todocname, {})
                    .get("proof", {})
                    .get(target, ())
                )
                number = ".".join(map(str, _))
                new_title = match.get("type", "").title()

            # If match type is solution directive
            if match.get("type", "") == "solution":
                ref_label = match.get("title", "")

                # If label of solution's exercise doesn't exist
                try:
                    ref_match = env.proof_list.get(ref_label, {})
                except Exception:
                    return None

                docname = ref_match.get("docname", "")

                # If exercise directive has nonumber
                if not ref_match.get("nonumber", bool):
                    _ = (
                        env.toc_fignumbers.get(docname, {})
                        .get("proof", {})
                        .get(ref_label, ())
                    )
                    number = ".".join(map(str, _))
                    new_title = f"Solution to {ref_match.get('type','').title()}"
                else:
                    if ref_match.get("title", "") == "":
                        new_title = f"Solution to {ref_match.get('type','').title()}"
                    else:
                        # Solution 1 - math2html
                        exercise_node = env.proof_list[ref_label].get("node")
                        exercise_node_title = exercise_node[0]

                        exercise_title = ""
                        for jj in range(len(exercise_node_title)):
                            item = exercise_node_title[jj].astext()
                            if type(exercise_node_title[jj]) == nodes.math:
                                exercise_title += math2html.math2html(item)
                                continue
                            exercise_title += item

                        right_idx, left_idx = (
                            exercise_title.rfind(")"),
                            exercise_title.find("(") + 1,
                        )
                        exercise_title = exercise_title[left_idx:right_idx]
                        new_title = f"Solution to {exercise_title}"

            if number == "":
                title = nodes.Text(f"{new_title}")
            else:
                title = nodes.Text(f"{new_title} {number}")
        # builder, fromdocname, todocname, targetid, child, title=None
        return make_refnode(builder, fromdocname, todocname, target, title)
