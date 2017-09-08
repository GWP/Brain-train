const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');

// const HtmlWebpackPluginConfig = new HtmlWebpackPlugin({
//   template: './app/templates/hello.html',
//   filename: 'hello.html',
//   inject: 'body'
// })

module.exports = {
  entry: ['./app/static/jsx/driver.js', './app/static/jsx/problem-page.js', './app/static/jsx/counter.js', './app/static/jsx/main-page.js', './app/static/jsx/problem-generator.js', './app/static/jsx/stats-page.js'],
  output: {
    path: path.resolve('./app/static/scripts/js/'),
    filename: '[name].js'
  },

  module: {
    loaders: [
      { test: /\.js$/, loader: 'babel-loader', exclude: /node_modules/ },
      { test: /\.jsx$/, loader: 'babel-loader', exclude: /node_modules/ }
    ]
  },

//   plugins: [HtmlWebpackPluginConfig]
}
