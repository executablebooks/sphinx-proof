from sphinx_proof.translations._convert import convert_json


def test_convert(tmp_path, monkeypatch):
    # Generate folder structures needed
    path_translation = tmp_path / "translations"
    path_jsons = path_translation / "jsons"
    path_compiled = path_translation / "locales"
    path_jsons.mkdir(parents=True)
    (path_jsons / "test.json").write_text(
        '[{"language":"English","symbol":"en","text":"Text"},'
        '{"language":"Other","symbol":"ot","text":"Translate"}]'
    )
    monkeypatch.setattr("subprocess.check_call", lambda args: None)
    convert_json(path_translation)
    assert (path_compiled / "ot").exists()
    path_lc = path_compiled / "ot" / "LC_MESSAGES"
    assert (path_lc / "proof.po").exists()
    assert "Translate" in (path_lc / "proof.po").read_text("utf8")
