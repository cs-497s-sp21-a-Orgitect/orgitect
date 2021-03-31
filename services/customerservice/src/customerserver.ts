import express from 'express'
import sqlite3 from 'sqlite3'
import bodyParser from 'body-parser'
import path from 'path';

const app = express();
const port = 3000;


var db = new sqlite3.Database(':memory:');
db.serialize(function () {
    db.run("CREATE TABLE customers (uid INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT UNIQUE, phone TEXT, customer_number TEXT, street_address TEXT, zip TEXT, state TEXT, processID INTEGER)")
    /* 
        uid Int
        name text
        email text
        phone text
        customernum text
        street_add text
        zipcode text
        state text
        processID Int
    */
}); 

app.use(express.json());
app.use(express.urlencoded({
  extended: true
}));

// list out all the customers and their info
app.get('/',(req,res) =>{
    db.all("SELECT rowid AS id, name FROM customers", function(err,rows){
        res.json(rows)
    })

});
app.get('/api/:uid',(req,res) =>{
    db.serialize(function ()  {
        db.get("SELECT * FROM customers where uid = (\"" + req.params.uid + "\")", function(err,row){
            if (err) {
                res.status(400).json({"error":err.message});
                return;
            }
            res.json(row)
        })
    })
});

app.post('/api/', (req,res)=>{
    console.log('post')
    //console.log(req.body)
    var data = {
        name: req.body.name,
        email: req.body.email,
        phone: req.body.phone
    }
    var sql= "INSERT INTO customers (name,email,phone) VALUES (?,?,?)"
    var params =[data.name, data.email, data.phone]
    db.serialize(function () {
        
        db.run(sql,params, function (err: { message: any; }, result: any) {
            if (err){
                res.status(400).json({"error": err.message})
                return;
            }
            res.json({
                "message": "customer added!",
                "data": data,
            })
        })
        /* db.all("SELECT rowid AS id, info FROM sampleTable", function(err,rows){
            res.json(rows)
        }) */
    })
})
app.put('/api/:name', (req,res)=>{
    console.log('put')
    db.serialize(function () {
        db.run("UPDATE customers SET processID = (\""+ req.body.processID + "\")"+ " WHERE name = (\"" + req.params.name + "\")", function (err: { message: any; }, result: any) {
            if (err){
                res.status(400).json({"error": err.message})
                return;
            }
            res.json({
                "message": "customer stage for " +req.params.name+ " updated!",
                "data": req.body,
            })
        })
        /* db.all("SELECT rowid AS id, info FROM sampleTable", function(err,rows){
            res.json(rows)
        }) */
    })
})

app.delete('/api/:name', (req,res)=>{
    console.log('delete')
    db.serialize( function () {
        db.run("DELETE FROM customers WHERE name =(\"" + req.params.name + "\")", function (err: { message: any; }, result: any) {
            if (err){
                res.status(400).json({"error": err.message})
                return;
            }
            res.json({
                "message": "customer " +req.params.name+" deleted!",
                "data": req.params.name,
            })
        })
        /* db.all("SELECT rowid AS id, info FROM sampleTable", function(err,rows){
            res.json(rows)
        }) */
    })
})

app.listen(port, () =>{
   return console.log('listening on port 3000')
});
