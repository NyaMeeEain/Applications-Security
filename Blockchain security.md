# Blockchain Technology From a CyberSecurity perspective
Blockchain technology relies heavily on P2P networks. there would be no current development of blockchain. The blockchain has a decentralized application theory, so it has strict security requirements for the P2P process.T his A comprehensive Document come out as a result of forcing My Global Manager.

# What is P2P?
P2P ( peer-to-peer ) network is also called peer-to-peer network, or peer-to-peer network. This is an Internet system where there is no central server and information is exchanged entirely by user groups. Each user of the P2P network is a client and also has the function of a server. Before P2P technology, all our network applications were implemented using C/S or B/S architecture. However, in the previous C/S architecture applications, the client software sent a request to the server, and the server then made a request to the client. Respond. In this case, if there are more clients, the pressure on the server will increase. However, each computer implemented by P2P technology is both a client and a server, and their functions are equal. For computers installed with P2P software (such as Thunder, QQ, etc.) to join a common P2P network, data transmission and communication can be directly carried out between nodes in the network.


# Distributed storage of network resources

all clients download all data resources directly from the server, which will inevitably increase the burden on the server, while P2P changes the server-centric state so that each node can download from the server first Part of it, and then download the rest from each other or other nodes. In this way, when a large number of clients download at the same time, there will be no network congestion

# P2P Network in the blockchain Technology
Having explained so much content, then we will now take out the P2P technology in the blockchain separately and analyze the truth behind it
**From a technical perspective, blockchain technology is-P2P + consensus mechanism + cryptography** Specifically, the blockchain is the P2P network architecture, which uses cryptography to ensure data security, and uses consensus algorithms to ensure data consistency. For other architectures, failures are inevitable. But for the distributed P2P network of the blockchain, there is basically no single point of failure. Even the frequent advances and retreats of nodes will not affect the entire system.
And we know that there are many blockchain projects, but we can roughly divide these contents into three categories-public chain, private chain, and consortium chain. The public chain is completely open, so it determines that it will not use P2P encryption in the network. As for the other two (especially the alliance chain), the fact that the nodes cooperate with each other without complete trust makes the P2P network particularly important.

# blockchain terminology 
**There are several terminology in blockchaing you have to familar with each terminology**
### 1  Decentralization

The resources and services of the blockchain are distributed on all participating nodes, and the consistency of the blockchain network is maintained through the consensus mechanism, without the existence of a central system.


### 2 Robustness

The blockchain network has no central node, so there is no target of attack. Participating nodes are distributed in the network, and the destruction of some nodes has no impact on the blockchain system.


### 3 Scalability

Blockchain nodes can join and exit freely, and the network system can expand freely according to the nodes.


### 4 Privacy protection

The block information uses a broadcast mechanism, which cannot locate the initial node of the broadcast, prevents user communications from being monitored, and protects user privacy


### 5 Load balancing

Blockchain avoids resource load and network congestion by limiting the number of node connections and other configurations


# Centralized P2P network
There is a " central server " in the centralized network , and its role is to save the address information of the access node. If two peers want to communicate, they can request each other's address through the central server. For example:
the music file is associated with the node where the file is saved. When the user searches for a certain piece of music, the central server informs the storage node address, and the user connects point-to-point to obtain the music. It can be seen that the central server is used to provide address index (central servers of other architectures provide all services). If it fails, the entire system is paralyzed.


# 2. Fully distributed unstructured P2P network
Because it does not have a central index server, each machine is truly peer-to-peer in the network, acting as both a client and a server.

Fully distributed P2P nodes can join and exit freely, and there is no central node. There is no structured unified standard for the node address. The entire network structure is a random graph structure without a fixed network structure graph. However, complete freedom means that new nodes cannot know the P2P network node information, and thus cannot join the network. The more liberalization of the fully distributed P2P network also brings about the problem of node management. Frequent joining and exiting of nodes makes the entire network structure unable to be stable. A large number of broadcast messages not only cause waste of resources, but even block the network.

Bitcoin uses this P2P network structure. Fully distributed allows anyone and any node to participate. Unstructured allows nodes to synchronize block data through the blockchain P2P protocol while maintaining anonymity and privacy protection

# 3. Fully distributed structured P2P network
The biggest problem with full distributed is the node address management. There are no fixed rules between nodes, and node information cannot be accurately located. It can only be searched through flooding query, which consumes a lot of network. The structured network uses a distributed hash table (DHT) to standardize different node addresses into standard length data through encrypted hash functions such as the Hash function


# The application of P2P in the blockchain

public chains like Bitcoin and Ethereum require nodes to enter and exit freely, so there is no possibility of using P2P encryption.
For the problem of dealing with the privacy of the blockchain, the most promising solution is the Lightning Network + Sphinx protocol.
The essence of the Lightning Network is to establish a two-way flow of micro-payment channels outside the Bitcoin main chain, and coins can be transferred across nodes. Put a large number of small amounts on the Lightning Network to reduce the load on the main chain and increase the speed of small transactions.
The Lightning Network implements an onion routing protocol based on a scheme called Sphinx.
This routing protocol ensures that payment senders can construct and communicate paths through the Lightning Network, enabling:

* The intermediate node can verify and decrypt part of its routing information and find the next hop.

* Except for the previous hop and next hop, they cannot understand any other nodes that are part of the path.

* They cannot identify the length of the payment path, or their own position in the path.


# References
* [8btc](https://www.8btc.com/article/113116)

* [Peer-to-Peer overview](http://www.intsci.ac.cn/users/luojw/P2P/ch02.html)

* [The Truth About Blockchain](https://hbr.org/2017/01/the-truth-about-blockchain)

* [Blockchain and digital asset terminology](https://rsmus.com/what-we-do/services/blockchain-consulting/blockchain-and-digital-asset-terminology.html)

* [Blockchain beyond the hype](https://www.mckinsey.com/business-functions/mckinsey-digital/our-insights/blockchain-beyond-the-hype-what-is-the-strategic-business-value#)

