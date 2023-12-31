from block import Block

class Blockchain:
    """
    Blockchain: a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions
    """
    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data):
        self.chain.append(Block.mine_block(self.chain[-1], data))

    def __repr__(self):
        return f'Blockchain: {self.chain}'

def main():
    myBlockchain = Blockchain()
    myBlockchain.add_block('Sara owes Rana 10$')
    myBlockchain.add_block('Rana give sara 5$')

    print(myBlockchain)
    print(f'blockchain.py __name__: {__name__}')

if __name__ == '__main__':
    main()