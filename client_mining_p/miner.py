import hashlib
import requests

import sys


# TODO: Implement functionality to search for a proof 
def proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm
        - Find a number p' such that hash(pp') contains 4 leading
        zeroes, where p is the previous p'
        - p is the previous proof, and p' is the new proof
        """

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

def valid_proof(last_proof, proof):
    # encode
    guess = f"{last_proof}{proof}".encode()
    guess_hash = hashlib.sha256(guess).hexdigest()

    # return True if the last 4 digit of the has zero
    return guess_hash[:4] == "0000"

if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    coins_mined = 0
    # Run forever until interrupted
    while True:

        # TODO: Get the last proof from the server and look for a new one
        r = requests.get(url=node + "/last_proof")
        data = r.json()
        new_proof = proof_of_work(data.get('proof'))
        
        # TODO: When found, POST it to the server {"proof": new_proof}
        post_data = {"proof": new_proof}

        if data.get('message') == 'New Block Forged':
            coins_mined += 1
            print("Total coins mined: " + str(coins_mined))
        else:
            print(data.get('message'))

      

