// Application using the 'Pug' template system
const express = require('express'),
    logger = require('morgan'),
	fs = require('fs'),
	mongoose = require('mongoose'),
	bodyParser = require('body-parser');
const app = express();
const x = 1;
const y = 2;

const { Schema } = mongoose;
mongoose.connect('mongodb://127.0.0.1:27017/skryptowe', { useNewUrlParser: true, useUnifiedTopology: true }).then(() => {
const daySchema = new Schema({
    data: String,
    date: String
})
const day = mongoose.model('biblio', daySchema);

app.use(bodyParser.urlencoded({ extended: true }));
app.set('views', __dirname + '/views-lab');
app.set('view engine', 'pug');
app.use(logger('dev'));

app.get('/', function (req, res) {
	res.render('index');
});

app.post('/', async function (req, res) {
	if (req.body === undefined) {
		res.render('index', {error: "Missing POST data"});
		return;
	}
	
	if (req.body['title'] == '')
	{
		res.render('index', {error: "Missing book title"});
		return;
	}
	
	if (req.body['date'] == '')
	{
		res.render('index', {error: "Missing date title"});
		return;
	}
	
	let d = await day.find({date: req.body['date']});
	d = d[0];
	console.log(d);
	if (d.date === undefined)
	{
		await (new day({date: req.body['date'], data: JSON.stringify([ [req.body['title'], req.body['user']] ])})).save();
	}
	else
	{
		let dt = JSON.parse(d.data);
		let done = false;
		
		dt.forEach((d, it) => {
			if (done || d[0] == req.body['title']) {
				dt[it][1] = req.body['user'];
				done = true;
			}
		});
		
		if (!done) {
			dt.push([req.body['title'], req.body['user']]);
		}
		
		d.data = JSON.stringify(dt);
		await d.save();
	}
	
	res.render('index', {result: "Zapisano"});
});

app.get('/results', async function (req, res) {
    let d = await day.find().sort({date: 1});
	
	d.forEach(x => {
		console.log(x)
	});

    res.render('index', {result: "Ok"});
});

app.listen(3000, function () {
    console.log('The application is available on port 3000');
});
});
