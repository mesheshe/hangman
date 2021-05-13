var express = require('express');
var app = express();

var handlebars = require('express-handlebars').create({defaultLayout:'main'});
app.engine('handlebars',handlebars.engine);
app.set('port', 9794);
app.set('view engine','handlebars');
app.set('views','./D/views');

app.get('/', function(req,res){
  res.render('home');
});

app.get('/other-page', function(req,res){
  res.render('other-page');
});

function generate(){
  var rando = {};
  rando.random = Math.random();
  return rando;
}

app.get('/generate-random-number', function(req,res){
  res.render('generate-random-number', generate())
});

app.use(function(req,res){
  res.status(404);
  res.render('404');
});

app.use(function(error,req,res,next){
  console.error(error.stack);
  res.status(500);
  res.send('500');
});

app.listen(app.get('port'), function(){
  console.log('Express started on http://localhost:' + app.get('port') + '; press Ctrl-C to terminate.');
});


