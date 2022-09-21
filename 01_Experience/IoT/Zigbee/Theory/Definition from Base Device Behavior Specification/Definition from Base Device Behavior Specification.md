# Definition
## Application cluster:
- An application cluster is *a cluster that generates persistent functional transactions*, e.g., a temperature measurement server cluster that reports to a client or an on/off server cluster that receives commands from a client

## Application transaction:
- An application (or functional) transaction is *a cluster command*, and possible *response*, that is generated *to perform the device’s persistent function*, such as attribute reporting (e.g. reporting a sensor’s measured value) or actuation commands (e.g. On, Off, Toggle, etc.). An application transaction is not a ZDO transaction, one249 time transaction, or commissioning transaction.

- The cluster that *generates* the *application transaction* is the *initiator*. A corresponding cluster that *receives* the initial message of the transaction is the *target*. The same cluster on multiple endpoints/nodes could be the target of an application transaction, because of multiple source bindings or bindings with a group or broadcast destination.

## Binding (noun):
- A binding is a ZigBee source binding table entry on a node which *indicates where data is sent to* from a cluster on an endpoint

## Centralized security network:
- A centralized security network is a ZigBee network formed by a *ZigBee coordinator with the functionality of a Trust Center*. *Each node* that joins such a network *is authenticated with the Trust Center* before it can operate on the network.

## Device:
- An application implementation corresponding to a ZigBee defined device type *with a unique device identifier and part of a node*. *A device is resident on a single endpoint, called a device endpoint*. *A single node can have one or more devices*

## Distributed security network:
- A distributed security network is a ZigBee network *formed by a ZigBee router* and which *does not have a Trust Center*. *Each node* that joins such a network *is authenticated by its parent* before it can operate on the network.


## Dynamic device:
- A dynamic device is an application implementation of an *endpoint* that has *no specific set of application clusters*

## EZ-Mode:
- EZ-Mode is a *commissioning method that defines network steering and device reset on the node as well as finding & binding for endpoints with target or initiator clusters*. The method requires that a product supports interactive mechanisms to invoke the method. These mechanisms are accessible to the installer of the product. These mechanisms are implementation dependent and can be overloaded and/or automatic.
- Invoking EZ-Mode on a device endpoint puts the node and device in EZ-Mode for 3 a minute window. Each time EZ-Mode is invoked on a device, it extends the window for another 3 minutes. During the window, nodes perform EZ-Mode Network Steering and devices perform EZ-Mode Finding & Binding to other devices in EZ-Mode. Target devices use the Identify cluster to identify during the window. Initiator devices actively discover targets during the window and then bind to corresponding target clusters.

## EZ-Mode finding & binding:
- EZ-Mode finding & binding is the process of *automatically establishing application connections*, by using the identify cluster, *between matching application clusters on two or more devices*. Note that hereafter “EZ-Mode finding & binding” is referred to as “finding & binding”.

## EZ-Mode network steering:
- *For a node* that is *not* already *joined* to a network, EZ-Mode network steering is the action of *searching for and joining an open network*. For a node that *has joined a network*, EZ-Mode network steering is the action of *opening the network to allow new nodes to join*. Note that hereafter “EZ-Mode network steering” is referred to as “network steering”.

## Initiator cluster:
- An initiator cluster is an application cluster that *initiates cluster transactions*

## Joined:
- *A node* is said to be joined to a network if it has *successfully executed the network joining process or has formed a network*. Note that if the node formed the network it is possible that it does not yet have any peer nodes with which to communicate. Similarly, if a node has joined a network it is possible that it does not yet have any bound endpoints

## Node:
- A node defines *a single instance of the ZigBee-PRO stack with a single IEEE address on a single network*. A node is *made up of one or more logical device instances each represented on an endpoint* and *a node can have a node endpoint which is an instance for the entire node*, e.g., the ZDO on endpoint 0

## Simple device:
- A simple device is an application implementation of an application specific *endpoint* that *has mandatory application clusters*

## Target cluster:
- A target cluster is an application cluster that *receives the initiated messages from an initiator cluster* and could potentially respond to the initiator

## Touchlink commissioning:
- Touchlink commissioning is an optional commissioning mechanism where nodes are commissioned on a network using commands sent using inter-PAN communication in close physical proximity

## Utility cluster:
A utility cluster is a cluster *whose function is not part of the persistent functional operation of the product*. Function examples: commissioning, configuration, discovery, etc.

## ZigBee coordinator:
- A ZigBee coordinator is a ZigBee logical device type that includes the *functionality of a Trust Center* and is *responsible for starting a centralized security network* and *managing node joining and key distribution* for the network. A ZigBee coordinator has the logical type field of the *node descriptor* set to *0b000*.

## ZigBee end device:
- A ZigBee end device is a ZigBee logical device type that *can only join an existing network*. A ZigBee end device has the logical type field of the *node descriptor* set to *0b010*.

## ZigBee router:
- A ZigBee router is a ZigBee logical device type that is *responsible for managing node joining*. A ZigBee router *cannot start* a *centralized* security network but it *can start* a *distributed* security network. A ZigBee router has the logical type field of the *node descriptor* set to *0b001*.











# 

---
- Status: #done

- Tags: #zigbee 

- References:
	- [Book: Base Device Behavior Specification]

- Related:
	- 
