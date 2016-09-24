path = require('path');
const webpack = require('webpack');

module.exports = {
    devtool: 'eval',
    entry:  [
        'webpack-dev-server/client?http://0.0.0.0:3333', 
        './client/assets/js/index.jsx',
    ],
    output: {
        path: path.join(__dirname, 'static/js/'),
        filename: 'bundle.js',
        publicPath: 'static/js/',
    },
    module: {
        loaders: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                loaders: ['react-hot','babel-loader?presets[]=react,presets[]=es2015'],
                presets : ['es2015', 'react']
            },
            {
              test: /\.scss$/,
              loaders: ["style", "css", "sass"]

            }
        ]
    }
}
