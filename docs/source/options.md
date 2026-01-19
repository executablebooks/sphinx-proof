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

## Title format

By default, the directive titles are formatted as `Name x.y.z (Title)`, where `Name` is the name of the directive (e.g., Proof, Theorem, Definition), `x.y.z` is the numbering of the directive, and `Title` is the optional title provided by the user. If no title is provided, only `Name x.y.z` is displayed. The font weight of the title is set to `--pst-admonition-font-weight-heading` by default, which commonly results in a semi-bold appearance.

You can customize the title format using the `proof_title_format` option. This option allows you to define how the title should be displayed by using `%t` as a placeholder for the user-provided title. The default format is ` (%t)`. A value of an empty string will result in no title being displayed, while ` *%t*` will italicize the title and contain no brackets. Note that the initial part of the title (i.e., `Name x.y.z`) is not customizable and will always be displayed.

The font weight of the title can be adjusted using `proof_number_weight` and the `proof_title_weight` options. Any valid CSS font-weight value can be used, such as `normal`, `bold`, `bolder`, `lighter`, or numeric values like `400`, `700`, etc. The option `proof_number_weight` controls the weight of the initial part of the title (i.e., `Name x.y.z`), while `proof_title_weight` controls the weight of the user-provided title. Default value for both options is `--pst-admonition-font-weight-heading`.

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
