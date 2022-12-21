import pytest

from main import TreeStore

items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]
ts = TreeStore(items)


@pytest.mark.parametrize('expected_result', (items,))
def test_getAll(expected_result):
    assert ts.getAll() == expected_result


lst = [None,
       {'id': 1, 'parent': 'root'},
       {'id': 2, 'parent': 1, 'type': 'test'},
       {'id': 3, 'parent': 1, 'type': 'test'},
       {'id': 4, 'parent': 2, 'type': 'test'},
       {'id': 5, 'parent': 2, 'type': 'test'},
       {'id': 6, 'parent': 2, 'type': 'test'},
       {'id': 7, 'parent': 4, 'type': None},
       {'id': 8, 'parent': 4, 'type': None},
       None]
results = zip(range(0, 10), lst)


@pytest.mark.parametrize('i, expected_result', results)
def test_getItem(i, expected_result):
    assert ts.getItem(i) == expected_result


lst = [
    [],
    [{'id': 2, 'parent': 1, 'type': 'test'},
     {'id': 3, 'parent': 1, 'type': 'test'}],
    [{'id': 4, 'parent': 2, 'type': 'test'},
     {'id': 5, 'parent': 2, 'type': 'test'},
     {'id': 6, 'parent': 2, 'type': 'test'}],
    [],
    [{'id': 7, 'parent': 4, 'type': None},
     {'id': 8, 'parent': 4, 'type': None}],
    [],
    [],
    [],
    [],
    []
]
results = zip(range(0, 10), lst)


@pytest.mark.parametrize('i, expected_result', results)
def test_getChildren(i, expected_result):
    assert ts.getChildren(i) == expected_result


lst = [
    [],
    [],
    [{'id': 1, 'parent': 'root'}],
    [{'id': 1, 'parent': 'root'}],
    [{'id': 2, 'parent': 1, 'type': 'test'}, {'id': 1, 'parent': 'root'}],
    [{'id': 2, 'parent': 1, 'type': 'test'}, {'id': 1, 'parent': 'root'}],
    [{'id': 2, 'parent': 1, 'type': 'test'}, {'id': 1, 'parent': 'root'}],
    [{'id': 4, 'parent': 2, 'type': 'test'},
     {'id': 2, 'parent': 1, 'type': 'test'}, {'id': 1, 'parent': 'root'}],
    [{'id': 4, 'parent': 2, 'type': 'test'},
     {'id': 2, 'parent': 1, 'type': 'test'}, {'id': 1, 'parent': 'root'}],
    []
]
results = zip(range(0, 10), lst)


@pytest.mark.parametrize('i, expected_result', results)
def test_getAllParents(i, expected_result):
    assert ts.getAllParents(i) == expected_result


wrong_items = [1, 2, 3]
ts2 = TreeStore(wrong_items)


@pytest.mark.parametrize('i, expected_exception', ([1, AttributeError],))
def test_getItem_exception(i, expected_exception):
    with pytest.raises(expected_exception):
        ts2.getItem(i)


@pytest.mark.parametrize('i, expected_exception', ([1, AttributeError],))
def test_getChildren_exception(i, expected_exception):
    with pytest.raises(expected_exception):
        ts2.getChildren(i)


@pytest.mark.parametrize('i, expected_exception', ([1, AttributeError],))
def test_getAllParents_exception(i, expected_exception):
    with pytest.raises(expected_exception):
        ts2.getAllParents(i)
