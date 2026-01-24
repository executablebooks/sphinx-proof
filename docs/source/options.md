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

## Title format

By default, the directive titles are formatted as `Name x.y.z (Title)`, where `Name` is the name of the directive (e.g., Proof, Theorem, Definition), `x.y.z` is the numbering of the directive, and `Title` is the optional title provided by the user.

If no title is provided, only `Name x.y.z` is displayed.

The font weight of the entire title (`Name x.y.z (Title)` or `Name x.y.z`) is set to `--pst-admonition-font-weight-heading` by default, which commonly results in a semi-bold appearance.

In the reminder we call the part `Name x.y.z` the "number" and the part `(Title)` the "title".

You can customize the title format using the `proof_title_format` option:

- This option allows you to define how the title should be displayed by using `%t` as a placeholder for the user-provided title.
- The default format is ` (%t)`.
- A value of an empty string will result in no title being displayed.
- A `markdown` string can be used to format the title.
  - For example, ` *%t*` will emphasize the title and contain no brackets.

Note that the initial part of the title (i.e., `Name x.y.z`) is not customizable and will always be displayed.

The font weight of the title can be adjusted using the `proof_title_weight` option:

- Any valid CSS font-weight value can be used, such as `normal`, `bold`, `bolder`, `lighter`, or numeric values like `400`, `700`, etc.
- Default value is `var(--pst-admonition-font-weight-heading)`.

The font weight of the number can be adjusted using the `proof_number_weight` option:
- Any valid CSS font-weight value can be used, such as `normal`, `bold`, `bolder`, `lighter`, or numeric values like `400`, `700`, etc.
- Default value is `var(--pst-admonition-font-weight-heading)`.

### Jupyter Book Project

Add `proof_title_format`, `proof_number_weight` and/or `proof_title_weight` to your `_config.yml`

```yaml
sphinx:
  config:
    proof_title_format: " *%t*"
    proof_number_weight: "bold"
    proof_title_weight: "normal"
```

### Sphinx Project

Add `proof_title_format`, `proof_number_weight` and/or `proof_title_weight` to your `conf.py`

```python
proof_title_format = " *%t*"
proof_number_weight = "bold"
proof_title_weight = "normal"
```
