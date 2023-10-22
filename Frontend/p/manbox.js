function getdata(survey_num, type) {
    $("#survey_num").html("Survey 0"+survey_num+" Analysis");
    var settings = {
        "url": backendURL+"/manbox/"+type,
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
        manbox(response.manbox.year, response.manbox.manbox);
        languge(response.language.year, response.language.english, response.language.nonenglish);
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(errorThrown);
    });
}

function manbox(year, manbox) {
    manbox = manbox.map(function(each_element){
        return Number(each_element.toFixed(2));
    });
    echarts.init(document.querySelector("#manbox")).setOption({
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
            name: 'Manbox Score',
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
            data: manbox
        }
        ]
    });
}

function languge(year, english, non_english) {
    english = english.map(function(each_element){
        return Number(each_element.toFixed(2));
    });
    non_english = non_english.map(function(each_element){
        return Number(each_element.toFixed(2));
    });
    var c = 0;
    tbl = "";
    for (var yr in year) {
        tbl += "<tr><td>" + yr + "</td><td>" + english[c] + "</td><td>" + non_english[c] + "</td></tr>";
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
            left: '5%',
            right: '1%',
            containLabel: true
        },
        yAxis: {
            name: 'Manbox Score',
            nameLocation: 'middle',
            nameGap: 25,
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
            data: english
        },
        {
            name: 'Non-English',
            type: 'bar',
            data: non_english
        }
        ]
    });
}
