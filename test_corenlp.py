from nlplogic.corenlp import get_phrases

def test_get_phrases():
    assert 'canada' in get_phrases("Calgary")