// Define SVG area dimensions
let svgWidth = 550;
let svgHeight = 350;

// Define the chart's margins as an object
let chartMargin = {
  top: 30,
  right: 30,
  bottom: 50,
  left: 100
};

// Define dimensions of the chart area
let chartWidth = svgWidth - chartMargin.left - chartMargin.right;
let chartHeight = svgHeight - chartMargin.top - chartMargin.bottom;

// Select body, append SVG area to it, and set the dimensions
let svg = d3
  .select("#deathsChart")
  .append("svg")
  .attr("height", svgHeight)
  .attr("width", svgWidth);

// Append a group to the SVG area and shift ('translate') it to the right and down to adhere
// to the margins set in the "chartMargin" object.
let chartGroup = svg.append("g")
  .attr("transform", `translate(${chartMargin.left}, ${chartMargin.top})`);

// Load data from deaths_risk_factor.csv
d3.csv("deaths_risk_factor.csv").then(deathsData => {

  deathsData.forEach(data => {
    data.alcoholUse = +data.alcoholUse;
  });

  // Configure a band scale for the horizontal axis with a padding of 0.1 (10%)
  let xBandScale = d3.scaleBand()
  .domain(deathsData.map(d => d.countryName))
  .range([0, chartWidth])
  .padding(0.1);

  // Create a linear scale for the vertical axis.
  let yLinearScale = d3.scaleLinear()
  .domain([0, d3.max(deathsData, d => d.alcoholUse)])
  .range([chartHeight, 0]);

  // Create two new functions passing our scales in as arguments
  // These will be used to create the chart's axes
  let bottomAxis = d3.axisBottom(xBandScale);
  let leftAxis = d3.axisLeft(yLinearScale).ticks(10);

  // Append two SVG group elements to the chartGroup area,
  // and create the bottom and left axes inside of them
  chartGroup.append("g")
  .call(leftAxis);

  chartGroup.append("g")
  .attr("transform", `translate(0, ${chartHeight})`)
  .call(bottomAxis);

  // Create one SVG rectangle per piece of deathsData
  // Use the linear and band scales to position each rectangle within the chart
  chartGroup.selectAll(".bar")
  .data(deathsData)
  .enter()
  .append("rect")
  .attr("class", "bar")
  .attr("x", d => xBandScale(d.countryName))
  .attr("y", d => yLinearScale(d.alcoholUse))
  .attr("width", xBandScale.bandwidth())
  .attr("height", d => chartHeight - yLinearScale(d.alcoholUse));

  // Create axes labels
  chartGroup.append("text")
  .attr("transform", "rotate(-90)")
  .attr("y", 0 - chartMargin.left +25)
  .attr("x", 0 - (svgHeight / 2) - 90)
  .attr("dy", "1em")
  .attr("class", "axisText")
  .text("Number of Deaths by Alcohol Use (2017)");

  chartGroup.append("text")
      .attr("transform", `translate(${svgWidth / 2 - 150}, ${svgHeight + chartMargin.top - 75})`)
      .attr("class", "axisText")
      .text("Country Name");

}).catch(function(error) {
console.log(error);
});


