# Is MQTT secure?
- As a protocol, MQTT is secure
- However, the way MQTT is implemented and configured can cause issues

# Security implementation
- There are 3 pillars of security:
	- Confidentially
	- Integrity
	- Availability
- Security implementation for MQTT:
	- Authentication with Username and password in Connect packet
		- On application layer
	- Authorization with TLS/SSL implementation
		- On transport layer
		- Apply encryption on the full MQTT packet
	- Payload encryption
		- On application layer
		- Encrypt MQTT payload in
			- Publish message
			- LWT in Connect message

## Authentication
- You can send a username without a password but not a password without username 
	- In MQTT v5, you can send password without username
	- Username and password are send in plain text

## TLS
- TLS increase overhead in both broker and client
- In some case, TLS cannot be used due to resource constraint
	- -> There are 2 other options:
		- Use payload encryption
		- Encrypt Password in Connect message
- Different methods to encrypt the message using TLS
	- Root authority certificate
	- Root CA certificate, Client certificate and key
	- Using pre-shared key PSK

## Payload encryption
- Payload encryption is useful when you cannot use TSL due to computation and communication overhead
- Disadvantages:
	- Cannot be implemented in device with very low resources
	- Attacker can still modify message if an unsecure channel is used

### Encryption mechanism
- Type of encryption mechanism
	- Asymmetric encryption
	- Symmetric encryption

#### Asymmetric encryption
- Asymmetric encryption requires 2 keys
	- Public key to encrypt the data
	- Private key to decrypt the data
- Data encrypt by public key cannot be decrypt using the same public key
- Encrypted data can only be decrypted using private key
- In MQTT, asymmetric encryption is the best choice when your system has
	- Few trusted subscribers
	- Many untrusted publishers
![[01_Experience/IoT/MQTT/MQTT Master class/Section 10_Security/Asymmetric encryption.png]]

#### Symmetric encryption
- In symmetric encryption, messages can be encrypted and decrypted using the same key
- If your MQTT system is very trusted, symmetric encryption can work very well
- Symmetric encryption vs Asymmetric encryption
	- Symmetric encryption is easier and faster to implement
	- The most important disadvantages of symmetric encryption are the key distribution problem and the key management problem

![[01_Experience/IoT/MQTT/MQTT Master class/Section 10_Security/Symmetric encryption.png]]

### MQTT encryption scenarios
- End-to-end encryption
- Client-to-broker encryption

#### End-to-end encryption
- The data is encrypted all the time
	- The payload is encrypted and the broker cannot read it
- The broker uses unencrypted packet metadata for routing and QoS handling
![[01_Experience/IoT/MQTT/MQTT Master class/Section 10_Security/End-to-end encryption.png]]

#### Client-to-broker encryption
- The payload is encrypted during the communication between the client and the broker
- The broker can decrypt the message before distributing it
- Client-to-broker encryption is a good replacement for TLS
![[01_Experience/IoT/MQTT/MQTT Master class/Section 10_Security/Client-to-broker encryption.png]]

# Integrity
- Integrity checks ensure that an attacker does not modify the MQTT message.
![[01_Experience/IoT/MQTT/MQTT Master class/Section 10_Security/Integrity.png]]

## Digital signature
- A digital signature is a digital code generated and authenticated by public key encryption
- Digital signature can be used to verify its contents and the sender's identity
![[01_Experience/IoT/MQTT/MQTT Master class/Section 10_Security/Digital signature.png]]

## Checksum
- It checksum is created by converting the payload data into a fixed string called a hash value
- In MQTT, checksum is add at the beginning of payload data
- The receiver will recalculate the checksum to validate the integrity of the message

## Message authentication code
![[01_Experience/IoT/MQTT/MQTT Master class/Section 10_Security/Message Authentication Code.png]]
- A message authentication code is used to verify that the message came from a trusted client and not being tinkered during transit.
- A Message Authentication Code is created based on both a secret key and an MQTT message payload
- Message Authentication Code is sent in the MQTT message

#
---
- Status: #done
- Tags: #mqtt
- References:
	- [Source]()
- Related:
