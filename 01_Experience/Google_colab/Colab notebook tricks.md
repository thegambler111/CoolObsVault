# Tesla P100 GPU notebook

[Tesla P100 GPU notebook](https://colab.research.google.com/drive/1D6krVG0PPJR2Je9g5eN_2h6JP73_NUXz)


# Prevent notebook disconnection from inactivity

- Paste the following code into the console of notebook tab (right mouse click -> inspect -> Console tab and insert code):

```js
function ConnectButton(){
    console.log("Connect pushed"); 
    document.querySelector("#top-toolbar > colab-connect-button").shadowRoot.querySelector("#connect").click() 
}

setInterval(ConnectButton,60000);
```

- Use Colab Auto Reconnect extension


# 

---
Status: #done

Tags: #google_colab #trick #notebook

References:
- [Source](https://twitter.com/amitness/status/1372465387242065921?s=1001)

Related:
