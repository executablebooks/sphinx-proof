# Internationalization

This package supports **33 languages** for all proof directive types. Translations are specified in `conf.py` using the `language` option.

## Supported Languages

All 15 directive types (Algorithm, Assumption, Axiom, Conjecture, Corollary, Criterion, Definition, Example, Lemma, Notation, Observation, Property, Proposition, Remark, Theorem) have complete translations in the following languages:

| Language | Code | Language | Code |
|----------|------|----------|------|
| Arabic | `ar` | Bulgarian | `bg` |
| Bengali | `bn` | Chinese | `zh_CN` |
| Czech | `cs` | Danish | `da` |
| Dutch | `nl` | Finnish | `fi` |
| French | `fr` | German | `de` |
| Greek | `el` | Hebrew | `he` |
| Hindi | `hi` | Hungarian | `hu` |
| Indonesian | `id` | Italian | `it` |
| Japanese | `ja` | Korean | `ko` |
| Malay | `ms` | Norwegian | `no` |
| Persian | `fa` | Polish | `pl` |
| Portuguese | `pt` | Romanian | `ro` |
| Russian | `ru` | Spanish | `es` |
| Swedish | `sv` | Thai | `th` |
| Turkish | `tr` | Ukrainian | `uk` |
| Urdu | `ur` | Vietnamese | `vi` |

## Usage

To use a specific language, set the `language` option in your Sphinx `conf.py`:

```python
language = 'es'  # For Spanish
```

If no language is specified, **English** (`en`) is used as the default.

All proof directives will automatically use the appropriate translations for the selected language.
