var express = require('express');
var app = express();

app.set('port', 9794);
app.set('views','./Web-Development/week8/D/views');
app.get('/', function(req,res){
  res.type('text/plain');
  res.send('Welcome to the main page!');
});

app.get('/other-page', function(req,res){
  res.type('text/plain');
  res.send('Welcome to the other page!');
});

app.get('/generate-random-number', function(req,res){
  res.type('text/plain');
  res.send(`Your random number is ${Math.random()}`);
});

app.use(function(req,res){
  res.type('text/plain');
  res.send('404 - Not Found');
});

app.use(function(error,req,res,next){
  console.error(err.stack);
  res.type('text/plain');
  res.send('500 - Server Error');
});

app.listen(app.get('port'), function(){
  console.log('Express started on http://localhost:' + app.get('port') + '; press Ctrl-C to terminate.');
});

