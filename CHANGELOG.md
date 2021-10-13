# Changelog

## v0.1.3 (2021-10-14)

### Fixes 🐛

Resolving reference error. See: https://github.com/executablebooks/sphinx-proof/pull/68

## v0.1.2 (2021-10-13)

### Fixes 🐛

Making singlehtml builder error free. See: https://github.com/executablebooks/sphinx-proof/issues/65

## v0.1.1 (2021-08-18)

### Improved 👌

Resetting directive numbering between different directives

## [v0.1.0](https://github.com/executablebooks/sphinx-proof/tree/release-0.1) (2021-07-23)

### NEW ✨

Implemented Latex output of all the directives in this repository.

### Improved 👌

Proper handling of directives which do not have a title specified. For this, added an `enumerable_nodes` dict to ProofDomain.

## [v0.0.3](https://github.com/executablebooks/sphinx-proof/tree/v0.0.3) (2020-10-09)

[Full Changelog](https://github.com/executablebooks/sphinx-proof/compare/v0.0.2...v0.0.3)

### New ✨

We moved away from `sphinxcontrib-prettyproof` and renamed the extension `sphinx-proof`.

### Improved 👌

Among other improvements:

- The proof domain has been renamed "prf" to follow similar naming conventions to other Sphinx domains.
- Introduced the following new directives
	+ example
	+ property
	+ observation
	+ proposition
- Reviewed our test infrastructure to make sure we are following Executable Book Project's contributing guidelines #19 (@AakashGfude).
- Implemented GitHub Actions to build, test, and deploy our code.
- Enhanced the design of the directives per our users' request.


### DEPRECATE 🗑️

`sphinx-exercise` no longer support `exercise` directives. This work has moved to a new extension names `sphinx-exercise`.

### Fixes 🐛

- Fixed math label error in proof directive.
- ReadTheDocs builds documentation use a dev mode environment through the rtd extra.

### Documentation improvements 📚

In addition to other minor documentation improvements, we also introduced high-level description of the API.

**Closed issues:**

- Documentation similarities to / different decisions from sphinxcontrib-proof [\#37](https://github.com/executablebooks/sphinx-proof/issues/37)
- Add a high-level description of the API first on /syntax.html [\#35](https://github.com/executablebooks/sphinx-proof/issues/35)
- \[ENH\] Use upstream flake8 instead of the one provided as pre-commit hook [\#28](https://github.com/executablebooks/sphinx-proof/issues/28)
- Plain background for examples? [\#22](https://github.com/executablebooks/sphinx-proof/issues/22)
- Drop italics in proof body? [\#21](https://github.com/executablebooks/sphinx-proof/issues/21)
- Styling for "proof" too loud? [\#14](https://github.com/executablebooks/sphinx-proof/issues/14)
- \[DISC\] `{proof:proof}` directive has `class` option? [\#9](https://github.com/executablebooks/sphinx-proof/issues/9)
- \[ENH\] Discussion of Syntax Choices [\#6](https://github.com/executablebooks/sphinx-proof/issues/6)
- \[DOC\] Adding documentation for conjectures [\#4](https://github.com/executablebooks/sphinx-proof/issues/4)
- \[BUG\] Math Block `$$ $$` inside proof directive throws error [\#2](https://github.com/executablebooks/sphinx-proof/issues/2)

**Merged pull requests:**

- 👌 IMPROVE: Rename "proof" domain and role to "prf" [\#46](https://github.com/executablebooks/sphinx-proof/pull/46) ([najuzilu](https://github.com/najuzilu))
- ✨ NEW: Migrate to sphinx-proof [\#44](https://github.com/executablebooks/sphinx-proof/pull/44) ([najuzilu](https://github.com/najuzilu))
- 🐛 FIX: RTD fail to install local extension [\#43](https://github.com/executablebooks/sphinx-proof/pull/43) ([najuzilu](https://github.com/najuzilu))
- 🔧 MAINTAIN: Misc edits [\#40](https://github.com/executablebooks/sphinx-proof/pull/40) ([najuzilu](https://github.com/najuzilu))
- 📚 DOCS: Add high-level description of API under syntax [\#39](https://github.com/executablebooks/sphinx-proof/pull/39) ([najuzilu](https://github.com/najuzilu))
- 🗑️ DEPRECATE: Remove exercise directive [\#38](https://github.com/executablebooks/sphinx-proof/pull/38) ([najuzilu](https://github.com/najuzilu))
- 🔧 MAINTAIN: Update links to reflect migration to EBP [\#36](https://github.com/executablebooks/sphinx-proof/pull/36) ([najuzilu](https://github.com/najuzilu))
- 📚 DOCS: Add class option for `proof:proof` [\#34](https://github.com/executablebooks/sphinx-proof/pull/34) ([najuzilu](https://github.com/najuzilu))
- 📚 DOCS: Additional documentation [\#33](https://github.com/executablebooks/sphinx-proof/pull/33) ([najuzilu](https://github.com/najuzilu))
- ✨️ NEW: Add MANIFEST file [\#31](https://github.com/executablebooks/sphinx-proof/pull/31) ([AakashGfude](https://github.com/AakashGfude))
- 👌️ IMPROVE: Update extras [\#30](https://github.com/executablebooks/sphinx-proof/pull/30) ([najuzilu](https://github.com/najuzilu))
- 👌️ IMPROVE: Using upstream flake8 [\#29](https://github.com/executablebooks/sphinx-proof/pull/29) ([AakashGfude](https://github.com/AakashGfude))
- 👌️ IMPROVE: Add tox.ini [\#26](https://github.com/executablebooks/sphinx-proof/pull/26) ([najuzilu](https://github.com/najuzilu))
- \[ENH\] Implement Github workflow [\#25](https://github.com/executablebooks/sphinx-proof/pull/25) ([najuzilu](https://github.com/najuzilu))
- \[STY\] Remove `example` directive background color [\#24](https://github.com/executablebooks/sphinx-proof/pull/24) ([najuzilu](https://github.com/najuzilu))
- \[STY\] Fixes \#21: remove italics from proof [\#23](https://github.com/executablebooks/sphinx-proof/pull/23) ([najuzilu](https://github.com/najuzilu))
- Miscellaneous edits [\#20](https://github.com/executablebooks/sphinx-proof/pull/20) ([najuzilu](https://github.com/najuzilu))
- 👌️ IMPROVE:  Review of test infrastructure [\#19](https://github.com/executablebooks/sphinx-proof/pull/19) ([AakashGfude](https://github.com/AakashGfude))
- \[STY\] Update style of proof directive [\#15](https://github.com/executablebooks/sphinx-proof/pull/15) ([najuzilu](https://github.com/najuzilu))
- \[ENH, DOC\] Add `example`, `property`, `observation` and `proposition` directives [\#12](https://github.com/executablebooks/sphinx-proof/pull/12) ([najuzilu](https://github.com/najuzilu))
- \[FIX,TST\] Fix math label in proof directive [\#11](https://github.com/executablebooks/sphinx-proof/pull/11) ([najuzilu](https://github.com/najuzilu))
- \[DOCS\] add suggested changes for docs [\#5](https://github.com/executablebooks/sphinx-proof/pull/5) ([mmcky](https://github.com/mmcky))

## [v0.0.2](https://github.com/executablebooks/sphinx-proof/tree/v0.0.2) (2020-08-25)

[Full Changelog](https://github.com/executablebooks/sphinx-proof/compare/7977433b6888f1bdbfcda0b41c8cc226d539758e...v0.0.2)



\* *This Changelog was automatically generated by [github_changelog_generator](https://github.com/github-changelog-generator/github-changelog-generator)*
