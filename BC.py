#Including Libraries
import datetime
import hashlib
import json
import DES
import pprint

def LoadBlockChain_():
    Chain_ = []
    chain_to_load = {}
    with open('BlockChainData.txt', 'r') as infile:
        chain_to_load = json.load(infile)

    for v in chain_to_load.values():
        Chain_.append(v)
    #print(chain_to_load)
    #print(Chain_)
    return Chain_ 
#The BlockChain class  
class Blockchain:
    
    #Constructor for the blockchain -> Loads the saved block Chain_
    def __init__(self):
        self.Chain_ = []
       # self.createBlock(proof=1, previousHash='0',data="Genesis Block")
        self.Chain_ = LoadBlockChain_()
    

    #Created a new block with give details and adds it to the blockchain
    def createBlock(self, proof, previousHash,data):
        block = {'index': len(self.Chain_) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'data' : data,
                 'previousHash': previousHash}
        self.Chain_.append(block)
        return block

    #Calculates Hash_ value for a given block -> SHA followed by DES
    def Hash_(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        sha =  hashlib.sha256(encoded_block).hexdigest()
        sha = sha.upper()
        return DES.E(sha[0:16]) +DES.E(sha[16:32]) +DES.E(sha[32:48]) +DES.E(sha[48:64]) 
    # Returns the previous block for a given block
    def get_previous_block(self):
        return self.Chain_[-1]
        
    #This functions calculates the proof of work for a given previous proof
    def get_proof_of_work(self, PreviousProof):
        new_proof_value = 1
        check_proof = False
        return 1
          
        while check_proof is False:
            print("Calculating POW for " + str(new_proof_value))
            SHA_hash = hashlib.sha256(
                str(new_proof_value**2 - PreviousProof**2).encode()).hexdigest()
            if SHA_hash[:4] == '00000':
                check_proof = True
            else:
                new_proof_value += 1
                  
        return new_proof_value
    #This functions verifies the proof of work for a given proof &  previous proof
    def verify_proof_of_work(self, PreviousProof,proof):
        
        check_proof = False
        SHA_hash = hashlib.sha256(str(proof**2 - PreviousProof**2).encode()).hexdigest()
        if SHA_hash[:4] == '00000':
            return True
        else :
            return False
   
    
    

    
    #This functions calculates the simple proof of work for a given previous proof
    def get_POW(self,PreviousProof):
        i = 0
        while True:
            if (PreviousProof*3 + i)%25 == 7:
                return i
            i = i+ 1
    #This functions verifies the simple proof of work for a given proof &  previous proof
    def verify_POW(self,PreviousProof,proof):
        if (3*PreviousProof + proof)%25 == 7:
            return True
        return False

    
    #This function verifies if the blockchain is valid or modified
    def is_create_block(self, Chain_):
        PreviousBlock = Chain_[0]
        block_index = 1
          
        while block_index < len(Chain_):
            block = Chain_[block_index]
            if block['previousHash'] != self.Hash_(PreviousBlock):
                return False
                
            PreviousProof = PreviousBlock['proof']
            proof = block['proof']
            '''SHA_hash = hashlib.sha256(
                str(proof**2 - PreviousProof**2).encode()).hexdigest()
              
            if SHA_hash[:4] != '00000':
                return False'''
            if( not self.verify_POW(PreviousProof,proof)):
                return False
            PreviousBlock = block
            block_index += 1
          
        return True
    #This function verifies the blockchain,creates a block,mines the block & adds it to blockchain
    def mine_block(self,data):
        if(not self.valid()):
            return False
        PreviousBlock = self.get_previous_block()
        PreviousProof = PreviousBlock['proof']
        proof = self.get_POW(PreviousProof)
        previousHash = self.Hash_(PreviousBlock)
        block = self.createBlock(proof, previousHash,data)
        
        print("Block mined to blockchain")
        message = {'message': 'A block is MINED',
                    'index': block['index'],
                    'timestamp': block['timestamp'],
                    'data' : data,
                    'proof': block['proof'],
                    'previousHash': block['previousHash']}
        #print(message)
        self.SaveBlockChain()
        return True
        
        #print(message)
       # return jsonify(message)

    #This function displays the block Chain_
    def print_chain(self):
        message = {'Chain_': self.Chain_,
                    'length': len(self.Chain_)}
        print(message)
        
    
    #This function prints if the blockchain is valid or modified
    def valid(self):
        valid = self.is_create_block(self.Chain_)
        
        if valid:
            print("The blockchain is secure")
            return True
        else:
            print("The blockchain was modified !")
            return False
        
    def Print_Block_Chain(self):
        pp = pprint.PrettyPrinter(indent=4)
        i =1
        for b in self.Chain_:
            print("BLOCK : " + str(i))
            i = i+1
            pp.pprint(b)

            print()
        print()


    #This function saves the blockchain to a text file
    def SaveBlockChain(self):
        chain_to_save = {}
        
        for b in self.Chain_:
            chain_to_save[b['index']] = b

        ''' json_data = ""
        json_data = json.dumps(chain_to_save)
        print(json_data)'''

        with open('BlockChainData.txt', 'w') as outfile:
            json.dump(chain_to_save,outfile)

    #This function loads the blockchain to a text file
    def LoadBlockChain(self):
        chain_to_load = {}
        with open('BlockChainData.txt', 'r') as infile:
            chain_to_load = json.load(infile)

        for v in chain_to_load.values():
            self.Chain_.append(v)
        #print(chain_to_load)
        print(self.Chain_)

            




#b = Blockchain()

# b.mine_block('data 1')
# b.SaveBlockChain()
# '''
# b.LoadBlockChain()
# '''