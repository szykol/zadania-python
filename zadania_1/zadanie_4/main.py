from smartphone import Smartphone, smartphones
import pickle

if __name__ == "__main__":
    pickle.dump(smartphones, open('zadanie_4/phones.dat', 'wb'))
    smartphones_b = pickle.load(open('zadanie_4/phones.dat', 'rb'))

    for sp in smartphones_b:
        print(sp)

    # samsung, ip, op = smartphones
    # with open('phones.dat', 'wb') as f:
    #     pickle.dump(samsung, f)
    #     pickle.dump(ip, f)
    #     pickle.dump(op, f)

    # with open('phones.dat', 'rb') as f:
    #     samsung_b = pickle.load(f)
    #     ip_b = pickle.load(f)
    #     op_b = pickle.load(f)

    # print(samsung_b, op_b, ip_b)