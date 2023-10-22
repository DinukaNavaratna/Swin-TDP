function getdata(survey_num, type) {
    $("#survey_num").html("Survey 0"+survey_num+" Analysis");
    var settings = {
        "url": backendURL+"/Oacademic/"+type,
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
        academic_attendance(response.academic_attendance);
        languge(response.language);
        academic_language(response.academic_language);
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(errorThrown);
    });
}

function academic_attendance(academic_attendance) {
    var year = [];
    var attendance = [];
    var results = [];
    var tbl = ""
    for (var key in academic_attendance) {
        var res = Math.round((academic_attendance[key].results) * 100) / 100;
        var att = Math.round((academic_attendance[key].attendance) * 100) / 100;
        tbl += "<tr><td>" + key + "</td><td>" + res + " %</td><td>" + att + " %</td></tr>";
        year.push(key);
        attendance.push(att);
        results.push(res);
    }
    $("#academic_attendance_tbl").html(tbl);

    echarts.init(document.querySelector("#academic_attendance")).setOption({
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
            name: 'Percentage',
            nameLocation: 'middle',
            nameGap: 50,
            type: 'value',
            boundaryGap: [0, 0.01],
            axisLabel: {
                formatter: "{value} %"
            },
            max: 100
        },
        xAxis: {
            name: 'Years completed',
            nameLocation: 'middle',
            nameGap: 50,
            type: 'category',
            data: year
        },
        series: [{
            name: 'Attendance',
            type: 'bar',
            data: attendance
        },
        {
            name: 'Results',
            type: 'bar',
            data: results
        }
        ]
    });
}

function languge(language) {
    var year = [];
    var english = [];
    var non_english = [];
    var tbl = ""
    for (var key in language) {
        var non = Math.round((language[key].non_english) * 100) / 1;
        var eng = Math.round((language[key].english) * 100) / 1;
        tbl += "<tr><td>" + key + "</td><td>" + eng + " %</td><td>" + non + " %</td></tr>";
        year.push(key);
        non_english.push(non);
        english.push(eng);
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
            name: 'Percentage',
            nameLocation: 'middle',
            nameGap: 50,
            type: 'value',
            boundaryGap: [0, 0.01],
            axisLabel: {
                formatter: "{value} %"
            },
            max: 100
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
            stack: 'total',
            data: english
        },
        {
            name: 'Non-English',
            type: 'bar',
            stack: 'total',
            data: non_english
        }
        ]
    });
}

function academic_language(academic_language) {
    var year = [];
    var english = [];
    var non_english = [];
    var tbl = ""
    for (var key in academic_language) {
        var eng = Math.round((academic_language[key].english) * 100) / 100;
        var non = Math.round((academic_language[key].non_english) * 100) / 100;
        tbl += "<tr><td>" + key + "</td><td>" + eng + " %</td><td>" + non + " %</td></tr>";
        year.push(key);
        english.push(eng);
        non_english.push(non);
    }
    $("#academic_language_tbl").html(tbl);

    echarts.init(document.querySelector("#academic_language")).setOption({
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
            name: 'Results Percentage',
            nameLocation: 'middle',
            nameGap: 50,
            type: 'value',
            boundaryGap: [0, 0.01],
            axisLabel: {
                formatter: "{value} %"
            },
            max: 100
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