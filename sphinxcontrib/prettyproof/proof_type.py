"""
sphinxcontrib.prettyproof.proof_type
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

List of proof-type directives

:copyright: Copyright 2020 by the QuantEcon team, see AUTHORS
:licences: see LICENSE for details
"""

from .directive import ElementDirective


class TheoremDirective(ElementDirective):
    """A custom theorem directive."""

    name = "theorem"


class LemmaDirective(ElementDirective):
    """A custom lemma directive."""

    name = "lemma"


class DefinitionDirective(ElementDirective):
    """A custom definition directive."""

    name = "definition"


class RemarkDirective(ElementDirective):
    """A custom remark directive."""

    name = "remark"


class ConjectureDirective(ElementDirective):
    """A custom conjecture directive."""

    name = "conjecture"


class CorollaryDirective(ElementDirective):
    """A custom corollary directive."""

    name = "corollary"


class AlgorithmDirective(ElementDirective):
    """A custom algorithm directive."""

    name = "algorithm"


class CriteriaDirective(ElementDirective):
    """A custom criteria directive."""

    name = "criteria"


class AxiomDirective(ElementDirective):
    """A custom axiom directive."""

    name = "axiom"


class ExerciseDirective(ElementDirective):
    """A custom exercise directive."""

    name = "exercise"
