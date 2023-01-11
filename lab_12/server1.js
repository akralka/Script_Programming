const express = require('express');
const logger = require('morgan');
const bodyParser = require('body-parser');
const app = express();

// Configuring the application
app.set('views', __dirname + '/views');
app.set('view engine', 'pug');
app.locals.pretty = app.get('env') === 'development';

// Determining the contents of the middleware stack
app.use(logger('dev'));

// Parse urlencoded form into json
app.use(bodyParser.urlencoded({ extended: true }));

// app.use(express.static(__dirname + '/public'));

// *** Route definitions ***

// The first route
app.get('/', function (req, res) {
    res.render('index');

    // let name = req.query.name;
    // res.send(`<html> <body> <h1> ${name} </h1> </body> </html>`)
    // http://localhost:3000/?name=imie
});

// The second route
app.get('/submit', function (req, res) {

    var name = (typeof req.query.imie != "undefined") ? req.query.imie : "World";

    // Return the greeting in the format preferred by the WWW client
    switch (req.accepts(['html', 'text', 'json', 'xml'])) {
        case 'json':
            // Send the JSON greeting
            res.type('application/json');
            res.json({ welcome: `Hello ${name}` });  // res.json({ welcome: "Hello World" });
            console.log("The server sent a JSON document to the browser");
            break;

        case 'xml':
            // Send the XML greeting
            res.type('application/xml');
            res.send(`<welcome>Hello ${name}</welcome>`);   
            console.log("The server sent an XML document to the browser");
            break;

        default:
            // Send the text plain greeting
            res.type('text/plain');
            res.send(`Hello ${name}`);       
            console.log("The server sent a plain text to the browser");
    }
});

app.post("/submit", function (req, res) {

    var name = (typeof req.body.imie != "undefined") ? req.body.imie : "World";


    switch (req.accepts(['html', 'text', 'json', 'xml'])) {
        case 'json':
            // Send the JSON greeting
            res.type('application/json');
            res.json({ welcome: `Hello ${name}` });  // res.json({ welcome: "Hello World" });
            console.log("The server sent a JSON document to the browser");
            break;

        case 'xml':
            // Send the XML greeting
            res.type('application/xml');
            res.send(`<welcome>Hello ${name}</welcome>`);   
            console.log("The server sent an XML document to the browser");
            break;

        default:
            // Send the text plain greeting
            res.type('text/plain');
            res.send(`Hello ${name}`);       
            console.log("The server sent a plain text to the browser");
    }
})



// The application is to listen on port number 3000
app.listen(3000, function () {
    console.log('The application is available on port 3000');
});