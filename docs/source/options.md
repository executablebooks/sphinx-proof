# Options

## Minimal color scheme

This package has the option to choose a more **minimal** color scheme.

The aim is to create admonitions that are clearly different to the core text with
colors that do not over emphasises the admonition such as

```{figure} _static/img/definition-minimal.png
```

compared to the current default

```{figure} _static/img/definition.png
```

To enable the `minimal` color scheme you can use the following.

### Jupyter Book Project

Add `proof_minimal_theme = True` to your `_config.yml`

```yaml
sphinx:
  config:
    proof_minimal_theme: true
```

### Sphinx Project

Add `proof_minimal_theme = True` to your `conf.py`


## Shared numbering

By default, each type of theorem has their own numbering and counter.
This can be changed to a common counter by setting the option `proof_uniform_numbering` to true.

### Sphinx Project

Add `proof_uniform_numbering = True` to your `conf.py`


### Jupyter Book Project

Add `proof_uniform_numbering = True` to your `_config.yml` (untested)

```yaml
sphinx:
  config:
    proof_uniform_numbering: true
```
