const path = require('path');
var webpack = require("webpack");

module.exports = {
  entry: './cashier/resource/js/app.js',  // path to our input file
  output: {
    filename: 'index-bundle.js',  // output bundle file name
    path: path.resolve(__dirname, './cashier/static/js'),  // path to our Django static directory
  },
  externals: {
    jquery: 'jQuery',
  },
  module: {
    rules: [
        
      { parser: { amd: false } }
    ] },
   
   /*
    module: {
        rules: [
          {
            test: /\.js$/,
            use: [
              {
                loader: "imports-loader",
                options: {
                  imports: {
                    moduleName: "jquery",
                    name: "$",
                  },
                  additionalCode:
                    "var define = false; ",
                },
              },
            ],
          },
        ],
      },
  */
};