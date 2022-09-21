# Helpful tools
![[01_Experience/Code/JavaScript/JavaScript/JavaScript project setup/Helpful tools.png]]

# Setup

![[01_Experience/Code/JavaScript/JavaScript/JavaScript project setup/setup.png]]


# init
```
npm init
npm i -D eslint
eslint init
npm i -D webpack@4 --save-exact // webpack@4
npm i -D webpack-cli
npm i -D webpack-dev-server
npm i -D clean-webpack-plugin
npm i -D babel-loader @babel/core @babel/preset-env
```

```json
// package.json
	"scripts": {
        "test": "echo \"Error: no test specified\" && exit 1",
        "build": "webpack",
        "build:dev": "webpack-dev-server",
        "build:prod": "webpack --config webpack.config.prod.js"
    },
```

```js
// create webpack.config.js file
const path = require('path');
const CleanPlugin = require('clean-webpack-plugin');

module.exports = {
    mode: 'development',
    entry: './modules-09-executing-code-in-modules/src/app.js',
    output: {
        filename: 'app.js',
        path: path.resolve(
            __dirname,
            'modules-09-executing-code-in-modules',
            'assets',
            'scripts'
        ),
        publicPath: 'assets/scripts/',
    },
    devtool: 'eval-cheap-module-source-map',
    devServer: {
        static: './modules-09-executing-code-in-modules/',
    },
    plugins: [new CleanPlugin.CleanWebpackPlugin()], // bug with `devServer: static` path
};
```

```js
// create webpack.config.prod.js file
const path = require('path');
const CleanPlugin = require('clean-webpack-plugin');

module.exports = {
    mode: 'production',
    entry: './modules-09-executing-code-in-modules/src/app.js',
    output: {
        filename: '[contenthash].js',
        path: path.resolve(
            __dirname,
            'modules-09-executing-code-in-modules',
            'assets',
            'scripts'
        ),
        publicPath: 'assets/scripts/',
    },
    devtool: 'cheap-source-map',
    devServer: {
        static: './modules-09-executing-code-in-modules/',
    },
    plugins: [new CleanPlugin.CleanWebpackPlugin()],
};

```



# 

---
- Status: #writing

- Tags: 

- References:
	- 

- Related:
	- 
