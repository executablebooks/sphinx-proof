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

By default, each type of (prf-)directive has their own numbering and counter. This can be changed by setting the option `prf_realtyp_to_countertyp` to a dictionary associating to a directive which the counter of which directive it should use.

### Sphinx Project

In `conf.py`, e.g. to have a shared counter for all directives:

```
prf_realtyp_to_countertyp = {
    "axiom": "theorem",
    "theorem": "theorem",
    "lemma": "theorem",
    "algorithm": "theorem",
    "definition": "theorem",
    "remark": "theorem",
    "conjecture": "theorem",
    "corollary": "theorem",
    "criterion": "theorem",
    "example": "theorem",
    "property": "theorem",
    "observation": "theorem",
    "proposition": "theorem",
    "assumption": "theorem",
    "notation": "theorem",
}
```

In the following case, the directives `lemma`, `conjecture`, `corollary` and `proposition` will share the counter with `theorem`, while `axiom` and `assumption` will share the counter with `definition`. All other directives would use their original counter.


```
prf_realtyp_to_countertyp = {
    "lemma": "theorem",
    "conjecture": "theorem",
    "corollary": "theorem",
    "proposition": "theorem",
    "axiom": "definition",
    "assumption": "definition",
}
```

````{warning}
The association of a counter to a directive is not transitive: Let us consider the following configuration:

```
prf_realtyp_to_countertyp = {
    "lemma": "theorem",
    "conjecture": "lemma",
}
```

The `lemma` and `theorem` directives share a counter, however the `conjecture` directive has a separate counter (the `lemma` counter which is **not** used by `lemma` directives).
````
