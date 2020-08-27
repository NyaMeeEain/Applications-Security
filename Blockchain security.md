# Blockchain security and the underlying concept
Blockchain technology relies heavily on P2P networks. there would be no current development of blockchain. The blockchain has a decentralized application theory, so it has strict security requirements for the P2P process.

# What is P2P?
```
P2P ( peer-to-peer ) network is also called peer-to-peer network, or peer-to-peer network. This is an Internet system where there is no central server and information is exchanged entirely by user groups. Each user of the P2P network is a client and also has the function of a server. Before P2P technology, all our network applications were implemented using C/S or B/S architecture. However, in the previous C/S architecture applications, the client software sent a request to the server, and the server then made a request to the client. Respond. In this case, if there are more clients, the pressure on the server will increase. However, each computer implemented by P2P technology is both a client and a server, and their functions are equal. For computers installed with P2P software (such as Thunder, QQ, etc.) to join a common P2P network, data transmission and communication can be directly carried out between nodes in the network.
```

# Distributed storage of network resources
```
 all clients download all data resources directly from the server, which will inevitably increase the burden on the server, while P2P changes the server-centric state so that each node can download from the server first Part of it, and then download the rest from each other or other nodes. In this way, when a large number of clients download at the same time, there will be no network congestion
```
# P2P Network in the blockchain Technology
Having explained so much content, then we will now take out the P2P technology in the blockchain separately and analyze the truth behind it
**From a technical perspective, blockchain technology is-P2P + consensus mechanism + cryptography** Specifically, the blockchain is the P2P network architecture, which uses cryptography to ensure data security, and uses consensus algorithms to ensure data consistency. For other architectures, failures are inevitable. But for the distributed P2P network of the blockchain, there is basically no single point of failure. Even the frequent advances and retreats of nodes will not affect the entire system.
And we know that there are many blockchain projects, but we can roughly divide these contents into three categories-public chain, private chain, and consortium chain. The public chain is completely open, so it determines that it will not use P2P encryption in the network. As for the other two (especially the alliance chain), the fact that the nodes cooperate with each other without complete trust makes the P2P network particularly important.

# blockchain terminology 
**There are several terminology in blockchaing you have to familar with each terminology**
### 1  Decentralization
```
The resources and services of the blockchain are distributed on all participating nodes, and the consistency of the blockchain network is maintained through the consensus mechanism, without the existence of a central system.
```

### 2 Robustness

```
The blockchain network has no central node, so there is no target of attack. Participating nodes are distributed in the network, and the destruction of some nodes has no impact on the blockchain system.

```
### 3 Scalability
```
Blockchain nodes can join and exit freely, and the network system can expand freely according to the nodes.


```

### 4 Privacy protection
```
The block information uses a broadcast mechanism, which cannot locate the initial node of the broadcast, prevents user communications from being monitored, and protects user privacy
```

### 5 Load balancing
```
Blockchain avoids resource load and network congestion by limiting the number of node connections and other configurations
```
