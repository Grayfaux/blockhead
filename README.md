# blockhead
blockhead is a simple blockchain that can be used to check the validity of a chain of chosen data

Blockhead uses my hashing algorithm hashling also found on my GitHub at https://github.com/Grayfaux/hashling.git
Once hashling is added to your project folder initialize a blockhead instance (bc = BlockHead).

Add new blocks as a list of data you would like to block (bc.add_block(data)).

get the size of the blockchain with bc.get_block_size()
get a block by it's index with bc.get_block(index)
get the hash of a block with bc.get_block_hash(index)
get block data of a block with bc.get_block_data(index)
get individual data item from a block with bc.get_block_data(index)[item index here]

You can validate the hash between blocks with blockchain with bc.validate()

