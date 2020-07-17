"""
sphinxcontrib.proof.proof
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
A Proof Sphinx Domain
:copyright: Copyright 2020 by the QuantEcon team, see AUTHORS
:licences: see LICENSE for details
"""

from collections import defaultdict
from sphinx.domains import Domain, Index
from sphinx.roles import XRefRole
from sphinx.util.docutils import SphinxDirective
from sphinx.util.nodes import make_refnode
from docutils import nodes
from docutils.statemachine import ViewList
from docutils.parsers.rst import Directive, directives
from sphinx.util import logging

logger = logging.getLogger(__name__)

import pdb


class proof_node(nodes.Admonition, nodes.Element):
    pass


def visit_proof_node(self, node):
    pass


def depart_proof_node(self, node):
    pass


class ProofDirective(Directive):
    """A custom proof directive."""

    name = "proof"
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "label": directives.unchanged_required,
        "class": directives.class_option,
        "nonumber": directives.flag,
    }

    def run(self):

        domain_name, typ = self.name.split(":")[0], self.name.split(":")[1]
        env = self.state.document.settings.env
        content = ViewList()

        ids, classes = [domain_name], [typ]
        class_name = self.options.get("class")
        # If class in options add to class array
        if class_name:
            classes.extend(class_name)

        section = nodes.admonition(ids=ids, classes=classes)
        emph = nodes.emphasis()

        if self.arguments != []:
            content.append(self.arguments[0], 0)
            self.content.insert(0, content)

        self.content[0] = "Proof. " + self.content[0]
        self.state.nested_parse(self.content, self.content_offset, emph)

        node = proof_node()
        section += emph
        node += section

        # Todo: add QED
        return [node]


class TheoremDirective(Directive):
    """A custom theorem directive."""

    name = "theorem"
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "label": directives.unchanged_required,
        "class": directives.class_option,
        "nonumber": directives.flag,
    }

    def run(self):

        domain_name, typ = self.name.split(":")[0], self.name.split(":")[1]
        env = self.state.document.settings.env

        ids, classes = [domain_name], [typ]
        class_name = self.options.get("class")
        # If class in options add to class array
        if class_name:
            classes.extend(class_name)

        # If label in options
        label = self.options.get("label")
        if label:
            section_id = nodes.make_id(typ + "-" + label)
            ids.append(section_id)
        else:
            label = "{}-{}".format(env.docname, env.new_serialno())
            self.options["noindex"] = True

        # If label, add element
        if "noindex" not in self.options:
            domain = env.get_domain(domain_name)
            domain.add_element(typ, label)

        # If nonumber, add number
        if "nonumber" not in self.options:
            domain = env.get_domain(domain_name)
            domain.add_number(typ, label)
            number = domain.data["obj_options"]["{}-{}".format(typ, label)]

        section = nodes.admonition(ids=ids, classes=classes)

        title = "Theorem "

        if "nonumber" not in self.options:
            title += "{} ".format(number)

        if self.arguments != []:
            title += " (" + self.arguments[0]
            title += ")"

        section += nodes.paragraph(
            text=title, classes=[typ + "-title", domain_name + "-title"]
        )
        self.state.nested_parse(self.content, self.content_offset, section)

        node = proof_node()
        node += section

        return [node]


class LemmaDirective(Directive):
    """A custom lemma directive."""

    name = "lemma"
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "label": directives.unchanged_required,
        "class": directives.class_option,
        "nonumber": directives.flag,
    }

    def run(self):

        domain_name, typ = self.name.split(":")[0], self.name.split(":")[1]
        env = self.state.document.settings.env
        content = ViewList()

        ids, classes = [domain_name], [typ]
        class_name = self.options.get("class")
        # If class in options add to class array
        if class_name:
            classes.extend(class_name)

        # If label in options
        label = self.options.get("label")
        if label:
            section_id = nodes.make_id(typ + "-" + label)
            ids.append(section_id)
        else:
            label = "{}-{}".format(env.docname, env.new_serialno())
            self.options["noindex"] = True

        # If label, add element
        if "noindex" not in self.options:
            domain = env.get_domain(domain_name)
            domain.add_element(typ, label)

        # If nonumber, add number
        if "nonumber" not in self.options:
            domain = env.get_domain(domain_name)
            domain.add_number(typ, label)
            number = domain.data["obj_options"]["{}-{}".format(typ, label)]

        section = nodes.admonition(ids=ids, classes=classes)

        title = "Lemma "
        if "nonumber" not in self.options:
            title += "{} ".format(number)

        section += nodes.paragraph(
            text=title, classes=[typ + "-title", domain_name + "-title"]
        )

        if self.arguments != []:
            content.append(self.arguments[0], 0)
            self.content.insert(0, content)

        self.state.nested_parse(self.content, self.content_offset, section)

        node = proof_node()
        node += section
        return [node]


class DefinitionDirective(Directive):
    """A custom definition directive."""

    name = "definition"
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "label": directives.unchanged_required,
        "class": directives.class_option,
        "nonumber": directives.flag,
    }

    def run(self):

        domain_name, typ = self.name.split(":")[0], self.name.split(":")[1]
        env = self.state.document.settings.env

        ids, classes = [domain_name], [typ]
        class_name = self.options.get("class")
        # If class in options add to class array
        if class_name:
            classes.extend(class_name)

        # If label in options
        label = self.options.get("label")
        if label:
            section_id = nodes.make_id(typ + "-" + label)
            ids.append(section_id)
        else:
            label = "{}-{}".format(env.docname, env.new_serialno())
            self.options["noindex"] = True

        # If label, add element
        if "noindex" not in self.options:
            domain = env.get_domain(domain_name)
            domain.add_element(typ, label)

        # If nonumber, add number
        if "nonumber" not in self.options:
            domain = env.get_domain(domain_name)
            domain.add_number(typ, label)
            number = domain.data["obj_options"]["{}-{}".format(typ, label)]

        section = nodes.admonition(ids=ids, classes=classes)

        title = "Definition "
        if "nonumber" not in self.options:
            title += "{} ".format(number)

        if self.arguments != []:
            title += " (" + self.arguments[0]
            title += ")"

        section += nodes.paragraph(
            text=title, classes=[typ + "-title", domain_name + "-title"]
        )
        self.state.nested_parse(self.content, self.content_offset, section)

        node = proof_node()
        node += section
        return [node]


class RemarkDirective(Directive):
    """A custom remark directive."""

    name = "remark"
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "label": directives.unchanged_required,
        "class": directives.class_option,
        "nonumber": directives.flag,
    }

    def run(self):

        domain_name, typ = self.name.split(":")[0], self.name.split(":")[1]
        env = self.state.document.settings.env

        ids, classes = [domain_name], [typ]
        class_name = self.options.get("class")
        # If class in options add to class array
        if class_name:
            classes.extend(class_name)

        # If label in options
        label = self.options.get("label")
        if label:
            section_id = nodes.make_id(typ + "-" + label)
            ids.append(section_id)
        else:
            label = "{}-{}".format(env.docname, env.new_serialno())
            self.options["noindex"] = True

        # If label, add element
        if "noindex" not in self.options:
            domain = env.get_domain(domain_name)
            domain.add_element(typ, label)

        # If nonumber, add number
        if "nonumber" not in self.options:
            domain = env.get_domain(domain_name)
            domain.add_number(typ, label)
            number = domain.data["obj_options"]["{}-{}".format(typ, label)]

        section = nodes.admonition(ids=ids, classes=classes)

        title = "Remark "
        if "nonumber" not in self.options:
            title += "{} ".format(number)

        if self.arguments != []:
            title += " (" + self.arguments[0]
            title += ")"

        section += nodes.paragraph(
            text=title, classes=[typ + "-title", domain_name + "-title"]
        )
        self.state.nested_parse(self.content, self.content_offset, section)

        node = proof_node()
        node += section
        return [node]


class ConjectureDirective(Directive):
    """A custom conjecture directive."""

    name = "conjecture"
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "label": directives.unchanged_required,
        "class": directives.class_option,
        "nonumber": directives.flag,
    }

    def run(self):

        domain_name, typ = self.name.split(":")[0], self.name.split(":")[1]
        env = self.state.document.settings.env

        ids, classes = [domain_name], [typ]
        class_name = self.options.get("class")
        # If class in options add to class array
        if class_name:
            classes.extend(class_name)

        # If label in options
        label = self.options.get("label")
        if label:
            section_id = nodes.make_id(typ + "-" + label)
            ids.append(section_id)
        else:
            label = "{}-{}".format(env.docname, env.new_serialno())
            self.options["noindex"] = True

        # If label, add element
        if "noindex" not in self.options:
            domain = env.get_domain(domain_name)
            domain.add_element(typ, label)

        # If nonumber, add number
        if "nonumber" not in self.options:
            domain = env.get_domain(domain_name)
            domain.add_number(typ, label)
            number = domain.data["obj_options"]["{}-{}".format(typ, label)]

        section = nodes.admonition(ids=ids, classes=classes)

        title = "Conjecture "
        if "nonumber" not in self.options:
            title += "{} ".format(number)

        if self.arguments != []:
            title += " (" + self.arguments[0]
            title += ")"

        section += nodes.paragraph(
            text=title, classes=[typ + "-title", domain_name + "-title"]
        )
        self.state.nested_parse(self.content, self.content_offset, section)

        node = proof_node()
        node += section
        return [node]


class CorollaryDirective(Directive):
    """A custom corollary directive."""

    name = "corollary"
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "label": directives.unchanged_required,
        "class": directives.class_option,
        "nonumber": directives.flag,
    }

    def run(self):

        domain_name, typ = self.name.split(":")[0], self.name.split(":")[1]
        env = self.state.document.settings.env

        ids, classes = [domain_name], [typ]
        class_name = self.options.get("class")
        # If class in options add to class array
        if class_name:
            classes.extend(class_name)

        # If label in options
        label = self.options.get("label")
        if label:
            section_id = nodes.make_id(typ + "-" + label)
            ids.append(section_id)
        else:
            label = "{}-{}".format(env.docname, env.new_serialno())
            self.options["noindex"] = True

        # If label, add element
        if "noindex" not in self.options:
            domain = env.get_domain(domain_name)
            domain.add_element(typ, label)

        # If nonumber, add number
        if "nonumber" not in self.options:
            domain = env.get_domain(domain_name)
            domain.add_number(typ, label)
            number = domain.data["obj_options"]["{}-{}".format(typ, label)]

        section = nodes.admonition(ids=ids, classes=classes)

        title = "Corollary "
        if "nonumber" not in self.options:
            title += "{} ".format(number)

        if self.arguments != []:
            title += " (" + self.arguments[0]
            title += ")"

        section += nodes.paragraph(
            text=title, classes=[typ + "-title", domain_name + "-title"]
        )
        self.state.nested_parse(self.content, self.content_offset, section)

        node = proof_node()
        node += section
        return [node]


class AlgorithmDirective(Directive):
    """A custom algorithm directive."""

    name = "algorithm"
    has_content = True
    required_arguments = 0
    optional_arguments = 1
    final_argument_whitespace = True
    option_spec = {
        "label": directives.unchanged_required,
        "class": directives.class_option,
        "nonumber": directives.flag,
    }

    def run(self):

        domain_name, typ = self.name.split(":")[0], self.name.split(":")[1]
        env = self.state.document.settings.env

        ids, classes = [domain_name], [typ]
        class_name = self.options.get("class")
        # If class in options add to class array
        if class_name:
            classes.extend(class_name)

        # If label in options
        label = self.options.get("label")
        if label:
            section_id = nodes.make_id(typ + "-" + label)
            ids.append(section_id)
        else:
            label = "{}-{}".format(env.docname, env.new_serialno())
            self.options["noindex"] = True

        # If label, add element
        if "noindex" not in self.options:
            domain = env.get_domain(domain_name)
            domain.add_element(typ, label)

        # If nonumber, add number
        if "nonumber" not in self.options:
            domain = env.get_domain(domain_name)
            domain.add_number(typ, label)
            number = domain.data["obj_options"]["{}-{}".format(typ, label)]

        section = nodes.admonition(ids=ids, classes=classes)

        title = "Algorithm "
        if "nonumber" not in self.options:
            title += "{} ".format(number)

        if self.arguments != []:
            title += " (" + self.arguments[0]
            title += ")"

        section += nodes.paragraph(
            text=title, classes=[typ + "-title", domain_name + "-title"]
        )
        self.state.nested_parse(self.content, self.content_offset, section)

        node = proof_node()
        node += section
        return [node]


class ProofIndex(Index):

    name = "proof"
    localname = "Proof Index"
    shortname = "Proof"

    def generate(self, docnames=None):

        content = defaultdict(list)

        proofs = self.domain.get_objects()
        proofs = sorted(proofs, key=lambda prf: prf[0])

        # name, subtype, docname, typ, anchor, extra, qualifier, description
        for name, dispname, typ, docname, anchor, _ in proofs:
            content[dispname.lower()].append(
                (dispname, 0, docname, anchor, docname, "", typ)
            )

        content = sorted(content.items())
        return content, True


class ProofXRefRole(XRefRole):
    def result_nodes(self, doc, env, node, is_ref):
        return [node], []


class ProofDomain(Domain):

    name = "proof"
    label = "Proof Sample"

    roles = {"ref": ProofXRefRole()}

    directives = {
        "proof": ProofDirective,
        "theorem": TheoremDirective,
        "lemma": LemmaDirective,
        "definition": DefinitionDirective,
        "remark": RemarkDirective,
        "conjecture": ConjectureDirective,
        "corollary": CorollaryDirective,
        "algorithm": AlgorithmDirective,
    }

    indices = {ProofIndex}

    initial_data = {"objects": {}, "obj_options": {}}

    def get_objects(self):

        for obj in self.data["objects"].values():
            yield (obj)

    def resolve_xref(self, env, fromdocname, builder, typ, target, node, contnode):

        match = [
            (docname, anchor)
            for name, sig, typ, docname, anchor, prio in self.get_objects()
            if sig == target
        ]

        if len(match) > 0:
            todocname = match[0][0]
            targ = match[0][1]

            if target in contnode[0]:
                number = self.data["obj_options"][targ]
                text = targ.split("-")[0].title()
                if number:
                    text += " {}".format(number)
                    title = nodes.Text(text)
                else:
                    title = contnode[0]
            # builder, fromdocname, todocname, targetid, child, title=None
            return make_refnode(builder, fromdocname, todocname, targ, title)
        else:
            # TODO: warning
            return None

    def add_element(self, typ, label):

        name = "{}.{}".format(typ, label)
        anchor = "{}-{}".format(typ, label)

        # If label exists throw warning
        if label in self.data["objects"].keys():
            docname = self.data["objects"][label][3]
            path = self.env.doc2path(docname)
            msg = "duplicate {} label '{}'.".format(typ, label)
            logger.warning(msg, location=path, color="darkred")
        else:
            self.data["objects"][anchor] = (
                name,
                label,
                "Proof",
                self.env.docname,
                anchor,
                0,
            )

    def add_number(self, typ, label):

        anchor = "{}-{}".format(typ, label)
        self.data["obj_options"][anchor] = len(self.data["obj_options"]) + 1
