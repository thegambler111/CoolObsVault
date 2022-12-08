# Example code
```js
private async nodeDescriptorInternal(networkAddress: number): Promise<NodeDescriptor> {
        const response = this.znp.waitFor(Type.AREQ, Subsystem.ZDO, 'nodeDescRsp', {nwkaddr: networkAddress});
        const payload = {dstaddr: networkAddress, nwkaddrofinterest: networkAddress};
        await this.znp.request(Subsystem.ZDO, 'nodeDescReq', payload, response.ID);
        const descriptor = await response.start().promise;
```

- The code above is creating and executing a NodeDescriptor command
- `this.znp.waitFor` create a waiter to track result of a NodeDescriptor command
- `payload` is the NodeDescriptor command's payload
- `await this.znp.request` create the actual NodeDescriptor command then execute it
- `await response.start().promise` collect the result of the NodeDescriptor command
- => Waiter is used to collect results of executed commands

#
---
- Status: #done
- Tags: #z2m
- References:
- Related:
