"""
sphinxcontrib.pretty_proof.domain
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A Proof Sphinx Domain
:copyright: Copyright 2020 by the QuantEcon team, see AUTHORS
:licences: see LICENSE for details
"""
from typing import List, Tuple
from docutils.nodes import Element, Node, document, system_message
from sphinx.environment import BuildEnvironment
from collections import defaultdict
from sphinx.domains import Domain, Index
from sphinx.roles import XRefRole
from sphinx.util.nodes import make_refnode
from sphinx.util import logging
from docutils import nodes
from .proof_type import *

logger = logging.getLogger(__name__)

class ProofIndex(Index):

    name = "proof"
    localname = "Proof Index"
    shortname = "Proof"

    def generate(self, docnames=None):
        content = defaultdict(list)


class ProofXRefRole(XRefRole):
    def result_nodes(
        self,
        document: document,
        env: BuildEnvironment,
        node: Element,
        is_ref: bool,
    ) -> Tuple[List[Node], List[system_message]]:

        node["refdomain"] = "proof"
        return [node], []


class ProofDomain(Domain):

    name = "proof"
    label = "Proof Domain"

    roles = {"ref": ProofXRefRole()}

    directives = {
        "proof": ProofDirective,
        "axiom": AxiomDirective,
        "theorem": TheoremDirective,
        "lemma": LemmaDirective,
        "definition": DefinitionDirective,
        "remark": RemarkDirective,
        "conjecture": ConjectureDirective,
        "corollary": CorollaryDirective,
        "algorithm": AlgorithmDirective,
        "criteria": CriteriaDirective,
        "exercise": ExerciseDirective,
    }

    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):

        try:
            match = env.proof_list[target]
        except:
            path = self.env.doc2path(fromdocname)[:-4]
            msg = "label '{}' not found.".format(target)
            logger.warning(msg, location=path, color="red")
            return None

        todocname = match["docname"]
        title = contnode[0]

        if target in contnode[0]:
            number = ""
            if not env.proof_list[target]["nonumber"]:
                number = ".".join(
                    map(str, env.toc_fignumbers[todocname]["proof"][target])
                )
            title = nodes.Text(f"{match['type'].title()} {number}")
        # builder, fromdocname, todocname, targetid, child, title=None
        return make_refnode(builder, fromdocname, todocname, target, title)