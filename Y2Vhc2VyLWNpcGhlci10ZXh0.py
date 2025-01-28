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

dGV4dA =  input("RW50ZXIgdGV4dCB0byBlbmNyeXB0OiA=")
c2hpZnQ = int(input("RW50ZXIgc2hpZnQgdmFsdWU6IA=="))

ZW5jcnlwdGVkX3RleHQ = Y2Flc2FyX2NpcGhlcg(dGV4dA, c2hpZnQ)
print("RW5jcnlwdGVkIFRleHQ6", ZW5jcnlwdGVkX3RleHQ)

ZGVjcnlwdGVkX3RleHQ = Y2Flc2FyX2NpcGhlcg(dGV4dA, -(c2hpZnQ))
print("RGVjcnlwdGVkIFRleHQ6", ZGVjcnlwdGVkX3RleHQ)
