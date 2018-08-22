class Dict:

    def __init__(self, solt_number):
        self.solt_number = solt_number
        self.solts = []
        for i in range(solt_number):
            self.solts.append([])

    def put(self, key, value):
        idx = hash(key) % self.solt_number
        self.solts[idx].append((key, value))
        # print(idx, self.solts[idx])

    def get(self, key):
        idx = hash(key) % self.solt_number
        for k, v in self.solts[idx]:
            if key == k:
                return v
            else:
                raise KeyError(key)

if __name__ == '__main__':
    d = Dict(16)
    for x in range(20):
        d.put(str(x), x)
    print(d.get('16'))
    print(d.get(16))
