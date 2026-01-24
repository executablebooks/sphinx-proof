# -*- coding: utf-8 -*-
"""
sphinx_proof
~~~~~~~~~~~~

A Sphinx extension for producing proofs, theorems, lemmas, etc.
"""
import os
from pathlib import Path
from typing import Any, Dict, Set, Union
from sphinx.config import Config
from sphinx.application import Sphinx
from sphinx.locale import get_translation
from sphinx.environment import BuildEnvironment
from .nodes import visit_enumerable_node, depart_enumerable_node
from .nodes import (
    NODE_TYPES,
    unenumerable_node,
    visit_unenumerable_node,
    depart_unenumerable_node,
)
from .nodes import proof_node, visit_proof_node, depart_proof_node
from .domain import ProofDomain
from .proof_type import PROOF_TYPES
from sphinx.util import logging
from sphinx.util.fileutil import copy_asset

logger = logging.getLogger(__name__)
MESSAGE_CATALOG_NAME = "proof"
_ = get_translation(MESSAGE_CATALOG_NAME)


def purge_proofs(app: Sphinx, env: BuildEnvironment, docname: str) -> None:
    if not hasattr(env, "proof_list"):
        return

    # Override env.proof_list
    env.proof_list = {
        proof: env.proof_list[proof]
        for proof in env.proof_list.keys()
        if env.proof_list[proof]["docname"] != docname
    }


def merge_proofs(
    app: Sphinx, env: BuildEnvironment, docnames: Set[str], other: BuildEnvironment
) -> None:
    if not hasattr(env, "proof_list"):
        env.proof_list = {}

    # Merge env stored data
    if hasattr(other, "proof_list"):
        env.proof_list = {**env.proof_list, **other.proof_list}


def init_numfig(app: Sphinx, config: Config) -> None:
    """Initialize proof numfig format."""
    config["numfig"] = True
    numfig_format = {}
    for typ in NODE_TYPES.keys():
        numfig_format[typ] = typ + " %s"
    numfig_format.update(config.numfig_format)
    config.numfig_format = numfig_format


def copy_asset_files(app: Sphinx, exc: Union[bool, Exception]):

    if app.config["proof_minimal_theme"]:
        static_path = (
            Path(__file__).parent.joinpath("_static", "minimal", "proof.css").absolute()
        )
    else:
        static_path = Path(__file__).parent.joinpath("_static", "proof.css").absolute()
    asset_files = [str(static_path)]

    if exc is None:
        for path in asset_files:
            copy_asset(path, str(Path(app.outdir).joinpath("_static").absolute()))
            # if needed, load css to memory,
            # adjust font-weight according to user's setting in config
            # and write to output static file
            if app.config.proof_number_weight or app.config.proof_title_weight:
                # only if at least one of the two options is set
                path = str(Path(app.outdir).joinpath("_static", "proof.css").absolute())
                with open(path, "r", encoding="utf-8") as f:
                    css_content = f.read()
                if app.config.proof_number_weight:
                    css_content = css_content.replace(
                        "div.proof > p.admonition-title > span.caption-number {\n    font-weight: var(--pst-admonition-font-weight-heading);\n}",  # noqa: E501
                        f"div.proof > p.admonition-title > span.caption-number {{\n    font-weight: {app.config.proof_number_weight};\n}}",  # noqa: E501
                    )
                if app.config.proof_title_weight:
                    css_content = css_content.replace(
                        "div.proof > p.admonition-title {\n    font-weight: var(--pst-admonition-font-weight-heading);\n}",  # noqa: E501
                        f"div.proof > p.admonition-title {{\n    font-weight: {app.config.proof_title_weight};\n}}",  # noqa: E501
                    )
                out_path = Path(app.outdir).joinpath("_static", os.path.basename(path))
                with open(out_path, "w", encoding="utf-8") as f:
                    f.write(css_content)


def setup(app: Sphinx) -> Dict[str, Any]:

    app.add_config_value("proof_minimal_theme", False, "html")
    app.add_config_value("prf_realtyp_to_countertyp", {}, "html")
    app.add_config_value("proof_title_format", " (%t)", "html")
    app.add_config_value("proof_number_weight", "", "html")
    app.add_config_value("proof_title_weight", "", "html")

    app.add_css_file("proof.css")
    app.connect("config-inited", check_config_values)
    app.connect("build-finished", copy_asset_files)
    app.connect("config-inited", init_numfig)
    app.connect("env-purge-doc", purge_proofs)
    app.connect("env-merge-info", merge_proofs)

    # add translations
    package_dir = os.path.abspath(os.path.dirname(__file__))
    locale_dir = os.path.join(package_dir, "translations", "locales")
    app.add_message_catalog(MESSAGE_CATALOG_NAME, locale_dir)

    app.add_domain(ProofDomain)
    app.add_node(
        proof_node,
        html=(visit_proof_node, depart_proof_node),
        latex=(visit_proof_node, depart_proof_node),
    )
    app.add_node(
        unenumerable_node,
        html=(visit_unenumerable_node, depart_unenumerable_node),
        latex=(visit_unenumerable_node, depart_unenumerable_node),
    )
    for node in PROOF_TYPES.keys():
        app.add_enumerable_node(
            NODE_TYPES[node],
            node,
            None,
            html=(visit_enumerable_node, depart_enumerable_node),
            latex=(visit_enumerable_node, depart_enumerable_node),
        )

    return {
        "version": "builtin",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }


def check_config_values(app: Sphinx, config: Config) -> None:
    """Check configuration values."""
    # Check if proof_minimal_theme is boolean
    if not isinstance(config.proof_minimal_theme, bool):
        logger.warning(
            "'proof_minimal_theme' config value must be a boolean. "
            "Using default value False."
        )
        config.proof_minimal_theme = False

    # Check of prf_realtyp_to_countertyp is a dictionary
    if not isinstance(config.prf_realtyp_to_countertyp, dict):
        logger.warning(
            "'prf_realtyp_to_countertyp' config value must be a dictionary. "
            "Using default empty dictionary."
        )
        config.prf_realtyp_to_countertyp = {}
    # Check if each key and each value in prf_realtyp_to_countertyp
    # is a valid proof type
    for key, value in config.prf_realtyp_to_countertyp.items():
        if key not in PROOF_TYPES:
            logger.warning(
                f"Key '{key}' in 'prf_realtyp_to_countertyp' is not "
                "a valid proof type. "
                "It will be removed."
            )
            del config.prf_realtyp_to_countertyp[key]
        elif value not in PROOF_TYPES:
            logger.warning(
                f"Value '{value}' in 'prf_realtyp_to_countertyp' is not "
                "a valid proof type. It will be removed."
            )
            del config.prf_realtyp_to_countertyp[key]
    # Check if proof_title_format is a string
    if not isinstance(config.proof_title_format, str):
        logger.warning(
            "'proof_title_format' config value must be a string."
            "Using default value ' (%t)'."
        )
        config.proof_title_format = " (%t)"
    elif "%t" not in config.proof_title_format:
        logger.warning(
            "'proof_title_format' config value must contain the "
            "substring '%t' to print a title."
        )
    # Check if proof_number_weight is a string
    if not isinstance(config.proof_number_weight, str):
        logger.warning(
            "'proof_number_weight' config value must be a string. "
            "Using default value ''."
        )
        config.proof_number_weight = ""
    # Check if proof_title_weight is a string
    if not isinstance(config.proof_title_weight, str):
        logger.warning(
            "'proof_title_weight' config value must be a string. "
            "Using default value ''."
        )
        config.proof_title_weight = ""
