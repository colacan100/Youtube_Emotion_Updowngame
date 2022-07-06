const express = require('express');
const port = process.env.PORT || 7070;

const app = express();


app.use(express.json()); //accept data in json format
app.use(express.urlencoded()); //decode data send through html
app.use(express.static('public'));

//API routes
app.get('/form',(req, res)=>{
    res.sendfile(__dirname+ '/public/index.html');
})

app.post('/formpost',(req, res)=>{
    console.log(req.body);
})


app.listen=(port, ()=>{
    console.log('Server started at https://localhost:${port}')
})