from pyupgrade._main import main
from pyupgrade._string_helpers import is_codec


def test_keep_encoding(tmpdir):
    f = tmpdir.join('f.py')
    code = '"Björk Guðmundsdóttir".encode("utf-8")'
    f.write(code)
    assert main((f.strpath, '--py3-plus')) == 0
    assert f.read() == code


def test_stop_complaining_about_code_coverage():
    is_codec('foo', 'bar')
