"""
sphinx_proof.proof_type
~~~~~~~~~~~~~~~~~~~~~~~

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


class CriterionDirective(ElementDirective):
    """A custom criteria directive."""

    name = "criterion"


class AxiomDirective(ElementDirective):
    """A custom axiom directive."""

    name = "axiom"


class ExampleDirective(ElementDirective):
    """A custom example directive."""

    name = "example"


class PropertyDirective(ElementDirective):
    """A custom property directive."""

    name = "property"


class ObservationDirective(ElementDirective):
    """A custom observation directive."""

    name = "observation"


class PropositionDirective(ElementDirective):
    """A custom proposition directive."""

    name = "proposition"


class AssumptionDirective(ElementDirective):
    """A custom assumption directive."""

    name = "assumption"


PROOF_TYPES = {
    "axiom": AxiomDirective,
    "theorem": TheoremDirective,
    "lemma": LemmaDirective,
    "algorithm": AlgorithmDirective,
    "definition": DefinitionDirective,
    "remark": RemarkDirective,
    "conjecture": ConjectureDirective,
    "corollary": CorollaryDirective,
    "criterion": CriterionDirective,
    "example": ExampleDirective,
    "property": PropertyDirective,
    "observation": ObservationDirective,
    "proposition": PropositionDirective,
    "assumption": AssumptionDirective,
}
