const express = require('express');
const request = require('request');
const CircularJSON = require('circular-json');
const app = express();

app.get('/', (req, res) => {
    res.send("Web Server started...");
})

app.get('/hello', (req, res) => { //본인의 Hello
    res.send("Hello World - Lee");
})

let option = "http://192.168.1.79:8000/hello"
app.get("/rhello", function (req, res) {
    request(option, { json: true }, (err, result, body) => {
        if (err) { return console.log(err)}
        res.send(CircularJSON.stringify(body))
    })
})

const data = JSON.stringify({ todo : 'Buy the milk - Lee' })
app.get("/data", function (req, res) {
    res.send(data);
})

option = "http://192.168.1.79:8000/data"
app.get("/rdata", function (req, res) {
    request(option, { json: true }, (err, result, body) => {
        if (err) { return console.log(err)}
        res.send(CircularJSON.stringify(body))
    })
})

app.listen(8000, function () {
    console.log('8000 Port : Server Started....');
})