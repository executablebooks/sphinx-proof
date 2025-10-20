# Internationalization

This package supports **30 languages** for all proof directive types. Translations are specified in `conf.py` using the `language` option.

## Supported Languages

All 15 directive types (Algorithm, Assumption, Axiom, Conjecture, Corollary, Criterion, Definition, Example, Lemma, Notation, Observation, Property, Proposition, Remark, Theorem) have complete translations in the following languages:

| Language | Code | Language | Code |
|----------|------|----------|------|
| Arabic | `ar` | Japanese | `ja` |
| Bulgarian | `bg` | Korean | `ko` |
| Chinese | `zh_CN` | Norwegian | `no` |
| Czech | `cs` | Persian | `fa` |
| Danish | `da` | Polish | `pl` |
| Dutch | `nl` | Portuguese | `pt` |
| Finnish | `fi` | Romanian | `ro` |
| French | `fr` | Russian | `ru` |
| German | `de` | Spanish | `es` |
| Greek | `el` | Swedish | `sv` |
| Hebrew | `he` | Thai | `th` |
| Hindi | `hi` | Turkish | `tr` |
| Hungarian | `hu` | Ukrainian | `uk` |
| Indonesian | `id` | Vietnamese | `vi` |
| Italian | `it` |  |  |

## Usage

To use a specific language, set the `language` option in your Sphinx `conf.py`:

```python
language = 'es'  # For Spanish
```

If no language is specified, **English** (`en`) is used as the default.

All proof directives will automatically use the appropriate translations for the selected language.
