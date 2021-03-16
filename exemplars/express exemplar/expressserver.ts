import express from 'express'
import bodyparser from 'body-parser'
//probably require more libraries like axios, database(sqlite), 
// if you have a routes folder with controller setup add:
//  require('.routes/{routesfile here} )(app);


//Port number for server is 3000
const app = express();
const port = 3000;

//request body will be in the form of json
app.use(bodyparser.json())

//using function instead of '=>' is clearer if you're not using routes+controller
app.get('/', function(req, res) {})


/* In routes file
module.exports = function(app) { 
    var users = require('../{controller file})
    app.get/post/put/delete functions go below such with format below
}*/
//in the routes file, functions would look like 
app.get('/', users.get);

/* in controller file the functions are then expressed like:
    users.get = function(req, res) {
        code body here
    };
*/

app.listen(port, (){
    return console.log("listening at http://localhost:%s", port)
})