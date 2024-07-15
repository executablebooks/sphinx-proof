# Options

This package has the option to choose a more **minimal** color scheme.

The aim is to create admonitions that are clearly different to the core text with
colors that do not over emphasises the admonition such as

```{figure} _static/img/definition-minimal.png
```

compared to the current default

```{figure} _static/img/definition.png
```

To enable the `minimal` color scheme you can use the following.

## Jupyter Book Project

Add `proof_minimal_theme = True` to your `_config.yml`

```yaml
sphinx:
  config:
    proof_minimal_theme: true
```

## Sphinx Project

Add `proof_minimal_theme = True` to your `conf.py`
