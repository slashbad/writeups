from gmpy2 import mpz
from tqdm.auto import tqdm

def gen_otp(seed, n):
    from qiskit import QuantumCircuit, QuantumRegister, Aer, ClassicalRegister
    
    qr = QuantumRegister(1)
    cr = ClassicalRegister(n)
    qc = QuantumCircuit(qr, cr)
    for i in range(n):
        qc.h(0)
        qc.measure(0, i)

    sv_sim = Aer.get_backend('qasm_simulator')
    job = sv_sim.run(qc, seed_simulator=seed, shots=1)
    job_result = job.result()
    otp = list(job_result.get_counts().keys())[0]

    return otp

def gaussian_elimination(mat, vec):
    mat = dict(mat)
    vec = dict(vec)

    n = len(vec)
    assert len(mat) == n

    def xor_using(a, b):
        mat[b] ^= mat[a]
        vec[b] ^= vec[a]

    # upper triangle
    for i in tqdm(reversed(range(n)), total=n):
        assert mat[i] < mpz(0).bit_set(i+1)

        ii = i-1
        while not mat[i].bit_test(i) and ii >= 0:
            xor_using(ii, i)
            ii = ii-1
        assert mat[i].bit_test(i)
        
        for j in range(i):
            if mat[j].bit_test(i):
                xor_using(i, j)

    # lower triangle
    for i in tqdm(range(n)):
        assert mat[i] == mpz(0).bit_set(i)
        
        for j in range(i + 1, n):
            if mat[j].bit_test(i):
                xor_using(i, j)
    
    return vec

class Symlfsr:
    n = 19937
    taps = [
        0, 311, 467, 623, 779, 935, 1091, 1244, 1247, 1403, 1559, 1715, 1866, 1868,
        1871, 2027, 2177, 2178, 2183, 2333, 2339, 2488, 2492, 2495, 2651, 2799, 2807, 
        2955, 2963, 3111, 3114, 3116, 3119, 3267, 3275, 3423, 3425, 3426, 3431, 3579, 
        3581, 3587, 3732, 3735, 3736, 3740, 3743, 3891, 3899, 4043, 4055, 4199, 4211, 
        4355, 4356, 4362, 4364, 4367, 4511, 4523, 4673, 4674, 4679, 4829, 4835, 4984, 
        4988, 4991, 5147, 5295, 5303, 5451, 5459, 5598, 5607, 5610, 5612, 5615, 5763, 
        5771, 5909, 5910, 5919, 5921, 5922, 5927, 6065, 6075, 6077, 6083, 6222, 6228, 
        6231, 6232, 6236, 6239, 6387, 6395, 6533, 6534, 6539, 6551, 6689, 6695, 6707, 
        6842, 6846, 6851, 6852, 6858, 6860, 6863, 7007, 7019, 7153, 7154, 7157, 7158, 
        7169, 7170, 7175, 7309, 7313, 7325, 7331, 7470, 7480, 7484, 7487, 7643, 7775, 
        7781, 7782, 7791, 7799, 7931, 7937, 7947, 7955, 8087, 8090, 8103, 8106, 8108, 
        8111, 8243, 8259, 8267, 8399, 8401, 8402, 8415, 8417, 8418, 8423, 8555, 8557, 
        8571, 8573, 8579, 8708, 8711, 8724, 8727, 8728, 8732, 8735, 8867, 8883, 8891, 
        9035, 9047, 9191, 9203, 9330, 9332, 9347, 9348, 9354, 9356, 9359, 9503, 9515, 
        9642, 9665, 9666, 9671, 9821, 9827, 9953, 9976, 9980, 9983, 9984, 10139, 10287, 
        10443, 10577, 10590, 10599, 10602, 10604, 10755, 10889, 10901, 10902, 10911, 
        10913, 10914, 11057, 11067, 11069, 11214, 11220, 11223, 11224, 11379, 11525, 
        11526, 11531, 11669, 11681, 11687, 11825, 11834, 11838, 11843, 11844, 11981, 
        11999, 12145, 12146, 12149, 12150, 12293, 12301, 12305, 12462, 12761, 12767, 
        12773, 12774, 12923, 12929, 13073, 13079, 13082, 13235, 13385, 13391, 13393, 
        13394, 13541, 13547, 13549, 13697, 13700, 13703, 13853, 13859, 14321, 14322, 
        14324, 14477, 14634, 14945, 15257, 15569, 15881, 16037, 16349, 16505, 16661, 
        16817, 17129, 17285, 17441, 17909, 18065, 18221, 18689, 18845, 19469, 19625
    ]

    def __init__(self, state):
        self.pos = 0
        self.state = state

    def next(self):
        new_state = mpz(0)
        for tap in self.taps:
            new_state ^= self.state[tap]
        res, self.state = self.state[0], self.state[1:] + [new_state]
        self.pos += 1
        return res
    
    @classmethod
    def init_sym(cls):
        return cls([
            mpz(0).bit_set(i)
            for i in range(cls.n)
        ])
    
    @classmethod
    def init_with_state(cls, initial_state):
        return cls([
            initial_state[i]
            for i in range(cls.n)
        ])

def eval_bit(initial_state, lfsr_out):
    res = 0
    for i in range(Symlfsr.n):
        if lfsr_out.bit_test(i):
            res ^= initial_state[i]
    return res

if __name__ == "__main__":
    # Run as script for testing
    print("Generating testcase...")
    otp = gen_otp(1116, Symlfsr.n * 3)

    initial_state = {
        i: int(otp[i])
        for i in range(Symlfsr.n)
    }

    print("Verifying lfsr")
    lfsr = Symlfsr.init_with_state(initial_state)
    for i in tqdm(range(Symlfsr.n * 3)):
        lfsr_out = lfsr.next()
        assert lfsr_out == int(otp[i])

    print("Verifying symbolic lfsr")
    lfsr = Symlfsr.init_sym()
    for i in tqdm(range(Symlfsr.n * 3)):
        lfsr_out = lfsr.next()
        assert eval_bit(initial_state, lfsr_out) == int(otp[i])