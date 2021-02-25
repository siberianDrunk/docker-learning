var express = require('express');
const history = require('connect-history-api-fallback')
var path = require('path');

var serveStatic = require('serve-static');
var app = express();
app.use(history({
  verbose: true
}));
app.use(serveStatic(__dirname));
var port = process.env.PORT || 5000;
app.listen(port);
console.log('server started '+ port);



