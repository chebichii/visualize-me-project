 
//data
const url = "http://127.0.0.1:5000/api/v1.0/population";

function getStateIdByStateCode (stateArray, stateCode) {
    return Object.keys(stateArray).find(k => stateArray[k] === stateCode);
}

const dataPromise = d3.json(url);
 //    console.log("Data Promise: ", dataPromise);
 
 // State Population Info panel
// function buildInfo(stateId) {

    d3.json(url).then(function(data) {
        // console.log(data);
        var stateData = data.state;
        var populationData = data.population_est_2014;
        console.log(populationData[0]);
        var stateIdx = getStateIdByStateCode(stateData, "AL");
        // var stateIdx = getStateIdByStateCode(stateData, stateId);
        var stateCode = stateData[stateIdx];
        var statePopulation = populationData[stateIdx];
        console.log(stateData[stateIdx], populationData[stateIdx]);

        //add filter for ids
    
        var panel = (stateData[stateIdx], populationData[stateIdx]);
        //var results = panel[0];
        //Add code for dropdown menu to populate the state id info
        var info_data = d3.select("#state-data"); 
        //clear list
        info_data.html("");
        //append the Info section
        Object.entries(stateData[stateIdx], populationData[stateIdx]).forEach(([value]) => {
            //console.log(value);
            var row = info_data.append("p")
            row.text(`Population: ${value}`);
        });
        
    });

// };
//build chart function goes here

// function init() {
    //reference id in the dropdownMenu
    var selector = d3.selectAll("#selDataset");
    // //get data
    // const url = "http://127.0.0.1:5000/api/v1.0/population";

    // const dataPromise = d3.json(url);
    // console.log("Data Promise: ", dataPromise);

    d3.json(url).then(function(data) {
        var startValue = data.state;
        
        Object.entries(data.state).forEach((entry, idx) => {
            const stateId = entry[1];
            //console.log(stateId);
            console.log(entry);
            selector
            .append("option")
            .text(stateId)
            .property("value", stateId);
        });

        //initial plots
        // var sample1 = startValue[0];
        // buildInfo(sample1);
        //buildChart(sample1);      
        
    });
// }
//D3 change option event handler 
function optionChanged(newData){
    buildInfo(newData);
    //buildChart(newData);
}
// init();