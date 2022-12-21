from typing import List, Union


class TreeStore:

    def __init__(self, items: List[dict[str, Union[int, str, None]]]):
        """
        Get an array of objects.
        Objects (dict) have the fields 'id' and 'parent'.
        Example items:
        items = [{'id': 1, 'parent': 'root'},
         {'id': 2, 'parent': 1, 'type': 'test'},
         {'id': 3, 'parent': 1, 'type': 'test'},
         {'id': 4, 'parent': 2, 'type': 'test'},
         {'id': 5, 'parent': 2, 'type': 'test'},
         {'id': 6, 'parent': 2, 'type': 'test'},
         {'id': 7, 'parent': 4, 'type': None},
         {'id': 8, 'parent': 4, 'type': None}]
        :param items: array of objects
        """
        self.items = items

    def getAll(self) -> List[dict[str, Union[int, str, None]]]:
        """
        Method returns incoming items array
        :return: incoming items array
        """
        return self.items

    def getItem(self, idx: int) -> Union[
        dict[str, Union[int, str, None]], None
    ]:
        """
        Method returns item where 'id'=idx
        :param idx: item id
        :return: item or None
        """
        try:
            return tuple(filter(lambda x: x.get('id') == idx, self.items))[0]
        except IndexError:
            return None

    def getChildren(self, pid: int) -> List[dict[str, Union[int, str, None]]]:
        """
        Method returns list of items where 'parent'=pid
        :param pid: parent id
        :return: list of children
        """
        return list(filter(lambda x: x.get('parent') == pid, self.items))

    def getAllParents(self, idx: int) -> List[
        dict[str, Union[int, str, None]]]:
        """
        The method returns a hierarchical array of parents for item.
        :param idx: item id
        :return: list of parents
        """
        if not (self.getItem(idx)):
            return []
        pid = self.getItem(idx).get('parent')
        parents = []
        while pid != 'root':
            item = self.getItem(pid)
            parents.append(item)
            pid = item.get('parent')
        return parents

