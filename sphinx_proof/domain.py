"""
sphinx_proof.domain
~~~~~~~~~~~~~~~~~~~

A Proof Sphinx Domain

:copyright: Copyright 2020 by the QuantEcon team, see AUTHORS
:licences: see LICENSE for details
"""
from typing import Any, Dict, Tuple, List, Callable
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
from copy import copy

logger = logging.getLogger(__name__)


class ProofIndex(Index):

    name = "prf"
    localname = "Proof Index"
    shortname = "Proof"

    def generate(self, docnames=None) -> Tuple[Dict[str, Any], bool]:
        content = defaultdict(list)

        if not hasattr(self.domain.env, "proof_list"):
            return content, True

        proofs = self.domain.env.proof_list
        # {'theorem-0': {'docname': 'start/overview', 'type': 'theorem', 'ids': ['theorem-0'], 'label': 'theorem-0', 'prio': 0, 'nonumber': False}} # noqa: E501

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

        node["refdomain"] = "prf"
        return [node], []


class ProofDomain(Domain):

    name = "prf"
    label = "Proof Domain"

    roles = {"ref": ProofXRefRole()}  # role name -> role callable

    indices = {ProofIndex}  # a list of index subclasses

    directives = {**{"proof": ProofDirective}, **PROOF_TYPES}  # list of directives

    enumerable_nodes = {}  # type: Dict[[Node], Tuple[str, Callable]]

    def __init__(self, env: "BuildEnvironment") -> None:
        super().__init__(env)

        # set up enumerable nodes
        self.enumerable_nodes = copy(
            self.enumerable_nodes
        )  # create a copy for this instance
        for node, settings in env.app.registry.enumerable_nodes.items():
            self.enumerable_nodes[node] = settings

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
        """
        Resolve the pending_xref node with the given typ and target. This method should
        return a new node, to replace the xref node, containing the contnode which is
        the markup content of the cross-reference. If no resolution can be found, None
        can be returned; the xref node will then given to the missing-reference event,
        and if that yields no resolution, replaced by contnode.The method can also raise
        sphinx.environment.NoUri to suppress the missing-reference event being emitted.
        """
        if node.attributes.get("refdomain", "") == self.name:
            try:
                match = env.proof_list[target]
            except Exception:
                path = self.env.doc2path(fromdocname)[:-3]
                msg = "label '{}' not found.".format(target)
                logger.warning(msg, location=path, color="red")
                return None

            todocname = match["docname"]
            title = contnode[0]

            if target in contnode[0]:
                number = ""
                if not env.proof_list[target]["nonumber"]:
                    typ = env.proof_list[target]["type"]
                    number = ".".join(
                        map(str, env.toc_fignumbers[todocname][typ][target])
                    )
                title = nodes.Text(f"{match['type'].title()} {number}")
            # builder, fromdocname, todocname, targetid, child, title=None
            return make_refnode(builder, fromdocname, todocname, target, title)
        else:
            return None
