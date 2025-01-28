import sys

def Y2Flc2FyX2NpcGhlcg(dGV4dA, c2hpZnQ):
    cmVzdWx0 = ""
    dW5jaGFuZ2VkX2NoYXJz = [' ', '.', ',', "'", '\n']

    for Y2hhcg in dGV4dA:
        if Y2hhcg.isalpha():
            if Y2hhcg.isupper():
                c3RhcnQ = 65  
            else: 
                c3RhcnQ = 97
            cmVzdWx0 += chr((ord(Y2hhcg) - c3RhcnQ + c2hpZnQ) % 26 + c3RhcnQ)
        elif Y2hhcg in dW5jaGFuZ2VkX2NoYXJz:
            cmVzdWx0 += Y2hhcg
        else:
            cmVzdWx0 += Y2hhcg
    return cmVzdWx0

def bWFpbg():
    if len(sys.argv) != 4:
        print("VXNhZ2U6 cHl0aG9u Y2Vhc2VyLWNpcGhlci10ZXh0LWZpbGUucHk= <aW5wdXRfZmlsZQ==> <b3V0cHV0X2ZpbGU=> <c2hpZnRfdmFsdWU=>")

    aW5wdXRfZmlsZQ = sys.argv[1]
    b3V0cHV0X2ZpbGU = sys.argv[2]
    c2hpZnRfdmFsdWU = int(sys.argv[3])

    try:
        dGV4dA = ""
        with open(aW5wdXRfZmlsZQ, 'r') as aW5maWxl:
            dGV4dA = aW5maWxl.read()

        ZW5jcnlwdGVkX3RleHQ = Y2Flc2FyX2NpcGhlcg(dGV4dA, c2hpZnRfdmFsdWU)


        with open(b3V0cHV0X2ZpbGU, 'w') as b3V0ZmlsZQ:
            b3V0ZmlsZQ.write(ZW5jcnlwdGVkX3RleHQ)
        
        print(f"RW5jcnlwdGVk dGV4dA= d3JpdHRlbg== dG8= {b3V0cHV0X2ZpbGU}")

    except FileNotFoundError:
        print(f"RXJyb3I=: VGhl ZmlsZQ== {aW5wdXRfZmlsZQ} d2Fz bm90 Zm91bmQu")
    except Exception as ZQ:
        print(f"QW4= ZXJyb3I= b2NjdXJyZWQ6 {ZQ}")

if __name__ == "__main__":
    bWFpbg()