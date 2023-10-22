function getdata(survey_num, type) {
    if(survey_num == "1"){
        alert("No K6 data available for Survey 01");
        return;
    }
    $("#survey_num").html("Survey 0"+survey_num+" Analysis");
    var settings = {
        "url": backendURL+"/k6/"+type,
        "method": "POST",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json"
        },
        "data": JSON.stringify({
            "survey": survey_num
        }),
    };

    $.ajax(settings).done(function (response) {
        k6(response.k6.year, response.k6.k6);
        k6_problem(response.k6_problem.year, response.k6_problem.k6_problem);
        k6_language(response.k6_language.year, response.k6_language.k6_english, response.k6_language.k6_nonenglish);
        k6_problem_list(response.k6_problem_list);
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(errorThrown);
    });
}

function k6(year, k6) {
    echarts.init(document.querySelector("#k6_score")).setOption({
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {},
        grid: {
            top: '12%',
            left: '6%',
            right: '2%',
            containLabel: true
        },
        yAxis: {
            name: 'K6 Score',
            nameLocation: 'middle',
            nameGap: 50,
            type: 'value',
            boundaryGap: [0, 0.01]
        },
        xAxis: {
            name: 'Years completed',
            nameLocation: 'middle',
            nameGap: 50,
            type: 'category',
            data: year
        },
        series: [{
            type: 'bar',
            data: k6
        }
        ]
    });
}

function k6_problem(year, k6_problem) {
    echarts.init(document.querySelector("#k6_problem")).setOption({
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {},
        grid: {
            top: '12%',
            left: '6%',
            right: '2%',
            containLabel: true
        },
        yAxis: {
            name: 'No of Students',
            nameLocation: 'middle',
            nameGap: 50,
            type: 'value',
            boundaryGap: [0, 0.01]
        },
        xAxis: {
            name: 'Years completed',
            nameLocation: 'middle',
            nameGap: 50,
            type: 'category',
            data: year
        },
        series: [{
            type: 'bar',
            stack: 'total',
            data: k6_problem
        }
        ]
    });
}

function k6_language(year, k6_english, k6_nonenglish) {
    k6_english = k6_english.map(function(each_element){
        return Number(each_element.toFixed(2));
    });
    k6_nonenglish = k6_nonenglish.map(function(each_element){
        return Number(each_element.toFixed(2));
    });
    var tbl = ""
    var c = 0;
    for (var yr in year) {
        tbl += "<tr><td>" + yr + "</td><td>" + k6_english[c] + "</td><td>" + k6_nonenglish[c] + "</td></tr>";
        c++;
    }
    $("#language_tbl").html(tbl);

    echarts.init(document.querySelector("#language")).setOption({
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {},
        grid: {
            top: '12%',
            left: '3%',
            right: '2%',
            containLabel: true
        },
        yAxis: {
            name: 'K6 Score',
            nameLocation: 'middle',
            nameGap: 50,
            type: 'value',
            boundaryGap: [0, 0.01]
        },
        xAxis: {
            name: 'Years completed',
            nameLocation: 'middle',
            nameGap: 50,
            type: 'category',
            data: year
        },
        series: [{
            name: 'English',
            type: 'bar',
            data: k6_english
        },
        {
            name: 'Non-English',
            type: 'bar',
            data: k6_nonenglish
        }
        ]
    });
}

function k6_problem_list(k6_problem_list) {
    var tbl = ""
    for (var student of k6_problem_list) {
        tbl += "<tr><td>" + student[0] + "</td><td>" + student[1] + "</td><td>" + student[2] + "</td><td>" + student[3] + "</td><td>" + student[4] + "</td></tr>";
    }
    $("#k6_problem_list_tbl").html(tbl);
}