d3.json("./static/json/states.json").then((importedData) => {
    let data = importedData;
    let states = []
    // let birthYear = []
    // let sex = ["Female","Male","Other"]
    // let smoke = ["Daily","Frequently","Occasionally","Never"]

    // for (i = 1950; i < new Date().getFullYear() - 9; ++i) {
    //     birthYear.push(i)
    // }

    for (i = 0; i < data.length; ++i) {
        states.push(data[i].name)
    }
    
    // d3.select("#selBirthYear")
    //     .selectAll("option")
    //     .data(birthYear)
    //     .enter()
    //     .append("option")
    //     .text(d => d)
    //     .attr("value", d => d)

    // d3.select("#selSex")
    //     .selectAll("option")
    //     .data(sex)
    //     .enter()
    //     .append("option")
    //     .text(d => d)
    //     .attr("value", d => d)
    
    d3.select("#selState")
        .selectAll("option")
        .data(states)
        .enter()
        .append("option")
        .text(d => d)
        .attr("value", d => d)

    // d3.select("#selSmoke")
    //     .selectAll("option")
    //     .data(smoke)
    //     .enter()
    //     .append("option")
    //     .text(d => d)
    //     .attr("value", d => d)

    // console.log(birthYear);
})

let birthYear = []
let sex = ["Female","Male","Other"]
let freq = ["Daily","Frequently","Occasionally","Never"]
let sleep = ["0 - 4 hours","4 - 6 hours","6 - 8 hours","+8 hours"]

for (i = 1950; i < new Date().getFullYear() - 9; ++i) {
    birthYear.push(i)
}

d3.select("#selBirthYear")
    .selectAll("option")
    .data(birthYear)
    .enter()
    .append("option")
    .text(d => d)
    .attr("value", d => d)

d3.select("#selSex")
    .selectAll("option")
    .data(sex)
    .enter()
    .append("option")
    .text(d => d)
    .attr("value", d => d)

d3.select("#selSmoke")
    .selectAll("option")
    .data(freq)
    .enter()
    .append("option")
    .text(d => d)
    .attr("value", d => d)

d3.select("#selDrink")
    .selectAll("option")
    .data(freq)
    .enter()
    .append("option")
    .text(d => d)
    .attr("value", d => d)

d3.select("#selWorkout")
    .selectAll("option")
    .data(freq)
    .enter()
    .append("option")
    .text(d => d)
    .attr("value", d => d)

d3.select("#selSleep")
    .selectAll("option")
    .data(sleep)
    .enter()
    .append("option")
    .text(d => d)
    .attr("value", d => d)