from hashling import hashling


class Block:
    def __init__(self, last_block_hash, data):

        self.last_block_hash = last_block_hash
        self.data = data

        self.block_data = "-".join(data) + "-" + last_block_hash
        self.block_hash = hashling(self.block_data, hash_char_len=64)

    def __repr__(self):
        return f"Block({self.last_block_hash}, {self.data})\n"


class BlockHead:
    def __init__(self):
        self.blocks = []

    def add_block(self, data):

        if len(self.blocks) == 0:
            last_block_hash = hashling("initialize genesis block", hash_char_len=64)
        else:
            last_block_hash = self.blocks[-1].block_hash

        block = Block(last_block_hash, data)
        self.blocks.append(block)

    def validate(self):
        for i in range(len(self.blocks)):
            if i == 0:
                continue

            block = self.blocks[i]
            last_block = self.blocks[i - 1]

            if block.last_block_hash != last_block.block_hash:
                return False

        return True

    def get_block_size(self):
        return len(self.blocks)

    def get_block(self, index):
        return self.blocks[index]

    def get_block_hash(self, index):
        return self.blocks[index].block_hash

    def get_block_data(self, index):
        return self.blocks[index].data

