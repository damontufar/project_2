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
let wght = []
let hght = []

for (i = 20; i < 170; ++i) {
    wght.push(i)
}

for (i = 50; i < 230; ++i) {
    hght.push(i)
}

for (i = 1950; i < new Date().getFullYear() - 9; ++i) {
    birthYear.push(i)
}

d3.select("#selHeight")
    .selectAll("option")
    .data(hght)
    .enter()
    .append("option")
    .text(d => d)
    .attr("value", d => d)

d3.select("#selWeight")
    .selectAll("option")
    .data(wght)
    .enter()
    .append("option")
    .text(d => d)
    .attr("value", d => d)

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

let addUser = d3.select("#add-btn");

addUser.on('click', runEnter);

function runEnter() {
    d3.event.preventDefault();

    let bmiHTML = d3.select("#BMI");
    bmiHTML.selectAll("p").remove();
    bmiHTML.selectAll("ul").remove();

    let inputBYear = d3.select("#selBirthYear");
    let bYear = inputBYear.node().value;
    let tYear = new Date().getFullYear();
    
    let age = tYear - bYear;

    let h = d3.select("#selHeight").node().value;
    let w = d3.select("#selWeight").node().value;

    let st = d3.select("#selState").node().value;

    let bmi = Math.round(w/((h/100)**2),2);

    bmiHTML.append("p")
        .text(`Your body mass index is ${bmi},
        but what does this mean?`)

    if (age > 18) {
        if (bmi < 18.5) {
            bmiHTML.append("ul")
                .append("li")
                .text("According to the World Health Organization, you are in the underweighted range.")
                .append("li")
                .text("According to Singapore, you have a risk of developing problems \
                such as nutritional deficiency and osteoporosis")
        } else if (bmi < 25) {
            if (bmi < 23) {
                bmiHTML.append("ul")
                    .append("li")
                    .text("According to the World Health Organization, you are in the normal weight range.")
                    .append("li")
                    .text("According to Singapore, you are in low risk")
            } else {
                bmiHTML.append("ul")
                    .append("li")
                    .text("According to the World Health Organization, you are in the normal weight range.")
                    .append("li")
                    .text("According to Singapore, you are in moderate risk of developing heart disease, high \
                    blood pressure, stroke or diabetes.")
            }
        } else if (bmi < 30) {
            if (bmi < 27.5) {
                bmiHTML.append("ul")
                    .append("li")
                    .text("According to the World Health Organization, you are in the overweighted range.")
                    .append("li")
                    .text("According to Singapore, you are in moderate risk of developing heart disease, high \
                    blood pressure, stroke or diabetes.")
            } else {
                bmiHTML.append("ul")
                    .append("li")
                    .text("According to the World Health Organization, you are in the overweighted range.")
                    .append("li")
                    .text("According to Singapore, you are in high risk of developing heart disease, high \
                    blood pressure, stroke or diabetes.")
            }
        } else {
            bmiHTML.append("ul")
                .append("li")
                .text("According to the World Health Organization, you are in the obessity range.")
                .append("li")
                .text("According to Singapore, you are in high risk of developing heart disease, high \
                blood pressure, stroke or diabetes.")
        }
    }
    
}