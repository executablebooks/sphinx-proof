
from pathlib import Path
from typing import Any, Dict
from sphinx.application import Sphinx
from .nodes import enumerable_node, visit_enumerable_node, depart_enumerable_node
from .nodes import unenumerable_node, visit_unenumerable_node, depart_unenumerable_node
from .nodes import proof_node, visit_proof_node, depart_proof_node
from .domain import ProofDomain
from sphinx.util import logging

import pdb
logger = logging.getLogger(__name__)

def purge_proofs(app, env, docname):
    logger.info('=== PURGE PROOFS ===', color='blue')
    if not hasattr(env, 'proofs'):
        return

    env.proofs = [proof for proof in env.proofs
                  if proof['docname'] != docname]


def merge_proofs(app, env, docnames, other):
    logger.info('=== MERGE PROOFS ===', color='blue')
    if not hasattr(env, 'proofs'):
        env.proofs = []

    if hasattr(other, 'proofs'):
        env.proofs.extend(other.proofs)

def init_numfig(app, config):
    """Initialize proof numfig format."""
    config['numfig'] = True

    numfig_format = {
        "proof": "Proof %s",
    }
    numfig_format.update(config.numfig_format)
    config.numfig_format = numfig_format


def get_title(node):
    return node['type']


def setup(app: Sphinx) -> Dict[str, Any]:

    app.connect("config-inited", init_numfig)

    app.add_domain(ProofDomain)
    app.add_node(
        proof_node,
        singlehtml=(visit_proof_node, depart_proof_node),
        html=(visit_proof_node, depart_proof_node)
    )
    app.add_node(
        unenumerable_node,
        singlehtml=(visit_unenumerable_node, depart_unenumerable_node),
        html=(visit_unenumerable_node, depart_unenumerable_node)
    )
    app.add_enumerable_node(
        enumerable_node,
        "proof",
        get_title,
        singlehtml=(visit_enumerable_node, depart_enumerable_node),
        html=(visit_enumerable_node, depart_enumerable_node),
    )

    root_path = Path(__file__).parent.parent.parent
    static_path = root_path.joinpath("_static").absolute()
    app.config.html_static_path.append(str(static_path))
    app.config.html_css_files.append("proof.css")

    return {
        "version": "builtin",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
