from collections import OrderedDict

class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        super().__init__()
        self._capacity = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        print('self1=',self)
        if len(self) - containsKey == self._capacity:
            print('self2=',self)
            last = self.popitem(last=False)
            print('remove:', last)
            print('self3=',self)
        if containsKey:
            print('self4=',self)
            del self[key]
            print('set:', (key, value))
            print('self5=',self)
        else:
            print('add:', (key, value))
            print('self6=',self)
        OrderedDict.__setitem__(self, key, value)
        print('self7=',self)

mod_test = LastUpdatedOrderedDict(2)

mod_test['a'] = 1
print('=================='
      '=================================\n')

mod_test['b'] = 2
print('=================='
      '=================================\n')

mod_test['c'] = 3
print('=================='
      '=================================')
