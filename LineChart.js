d3.csv("data/cdc_data_clean.csv").then(function(data){
  console.log(data.length)
  console.log(data)
  var stateid=[]
  var percentage_Male=[]
  var percentage_Female=[]
    for(var i =0; i < data.length; i++){
        stateid.push(data[i].stateid);
        console.log(data[i].stateid)
        if (data[i].gender=="Male")
      
        percentage_Male.push(data[i].percentage_obese);
        else 
        percentage_Female.push(data[i].percentage_obese);

    }
    console.log("string")
    console.log(percentage_Male)
    var trace1 = {
      x: stateid,
      y: percentage_Male,
      type: "bar"
    };
    var trace2 = {
      x: stateid,
      y: percentage_Female,
      type: "bar"
    };
    // 6. Create the data array for our plot
    var data = [trace1, trace2];
    
    // 7. Define our plot layout
    var layout = {
      title: "Obesity Percentages of Male and Female in US States",
      xaxis: { title: "State" },
      yaxis: { title: "Percentage Rate of Obesity"}
    };
    
    var config = {responsive: true}
    // 8. Plot the chart to a div tag with id "plot"
    Plotly.newPlot("plot", data, layout, config);
});
