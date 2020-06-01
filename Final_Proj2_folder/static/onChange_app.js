 
//data
//const pop_url = "http://127.0.0.1:5000/api/v1.0/population";


//const dataPromise = d3.json(pop_url);
function returndata6(id){ 
    d3.json(pop_url).then(function(data) {
        console.log(data)
       // pop_data =data
        })
        //return pop_data
};
console.log("in gridel's js")
    //console.log(pop_data)