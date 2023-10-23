var url_string = window.location.href;
var url = new URL(url_string);
var usid = url.searchParams.get("sid");
var sid = "";
if (usid != "") {
    sid = usid;
    $('#sid').val(usid);
}
var survey_num = "";
var usur = url.searchParams.get("survey");
if (usur != "") {
    survey_num = usur;
    $('#survey').val(usur);
}

var chartDom1 = document.getElementById('student_data');
var myChart1 = echarts.init(chartDom1);
if (survey_num != "" && sid != "") {
    getdata();
}


var chartDom = document.getElementById('student_sna');
var myChart = echarts.init(chartDom);

function getdata() {
    myChart1.showLoading();

    var settings = {
        "url": backendURL + "/Tdata",
        "method": "POST",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json"
        },
        "data": JSON.stringify({
            "survey": survey_num,
            "sid": sid
        }),
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
        if (response.email == "error") {
            $('#datasection').hide();
        } else {
            student_data(response.email, [response.eff1, response.eff2], [response.aca1, response.aca2], [response.attn1, response.attn2]);
        }
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(errorThrown);
    });
}

function search() {
    var cat = $('#cat').find(":selected").val();
    var survey = $('#survey').find(":selected").val();
    var sid = $('#sid').val()

    if (cat == "" || survey == "" || sid == "") {
        alert("Please enter the requred details to start the analysis.");
        return;
    }
    myChart1.showLoading();
    myChart.showLoading();

    var settings = {
        "url": backendURL + "/Tstudent",
        "method": "POST",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json"
        },
        "data": JSON.stringify({
            "survey": survey,
            "category": cat,
            "sid": sid
        }),
    };

    $.ajax(settings).done(function (response) {
        console.log(response);
        if (response.network.length == 0) {
            alert("No networks identified!\nPlease try a different combination.");
            myChart1.hideLoading();
            myChart.hideLoading();
            return;
        }
        if (response.data.email == "error") {
            $('#datasection').hide();
        } else {
            student_data(response.data.email, [response.data.eff1, response.data.eff2], [response.data.aca1, response.data.aca2], [response.data.attn1, response.data.attn2]);
        }
        student(response.network);
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(errorThrown);
    });
}

function student(network) {
    var json = {
        "nodes": [],
        "links": [],
        "categories": []
    }

    for (node of network) {
        if (json.nodes.length == 0) {
            json.nodes.push({
                "id": node[0].toString(),
                "name": node[0].toString()
            });
            json.nodes.push({
                "id": node[1].toString(),
                "name": node[1].toString()
            });
        } else {
            var new1 = true;
            var new2 = true;
            for (var i = 0; i < json.nodes.length; i++) {
                if (json.nodes[i].id === node[0].toString()) {
                    new1 = false;
                }
                if (json.nodes[i].id === node[1].toString()) {
                    new2 = false;
                }
                if ((new1 == false) && (new2 == false)) {
                    break;
                }
            }
            if (new1) {
                json.nodes.push({
                    "id": node[0].toString(),
                    "name": node[0].toString()
                });
            }
            if (new2) {
                json.nodes.push({
                    "id": node[1].toString(),
                    "name": node[1].toString()
                });
            }
        }
        json.links.push({
            "source": node[0].toString(),
            "target": node[1].toString()
        });
    }
    console.log(json);
    student_sna(json);
}

function student_sna(json) {
    var option;

    $(function () {
        myChart.hideLoading();
        json.nodes.forEach(function (node) {
            node.symbolSize = 10;
        });
        option = {
            title: {
                text: 'Network Analysis',
                subtext: 'Individual Student',
                top: 'top',
                left: 'left'
            },
            tooltip: {},
            legend: [
                {
                    // selectedMode: 'single',
                    data: json.categories.map(function (a) {
                        return a.name;
                    })
                }
            ],
            series: [
                {
                    name: 'Participant ID',
                    type: 'graph',
                    layout: 'force',
                    data: json.nodes,
                    links: json.links,
                    categories: json.categories,
                    roam: true,
                    animation: true,
                    label: {
                        position: 'right'
                    },
                    force: {
                        edgeLength: 50,
                        repulsion: 200,
                        gravity: 0.1
                    },
                }
            ]
        };
        myChart.setOption(option);
    });

    option && myChart.setOption(option);

}

function student_data(email, eff, aca, att) {
    myChart1.hideLoading();
    echarts.init(document.querySelector("#student_data")).setOption({
        title: {
            text: email
        },
        tooltip: {
            trigger: 'axis'
        },
        legend: {
            data: ['Effort', 'Academic Performance', 'Attendance']
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        toolbox: {
            feature: {
                saveAsImage: {}
            }
        },
        xAxis: {
            type: 'category',
            boundaryGap: true,
            data: ['Survey 01', 'Survey 02']
        },
        yAxis: {
            type: 'value'
        },
        series: [
            {
                name: 'Effort',
                type: 'line',
                data: eff,
                markPoint: {
                  data: [
                    { type: 'max', name: 'Max' },
                    { type: 'min', name: 'Min' }
                  ]
                },
                markLine: {
                  data: [{ type: 'average', name: 'Avg' }]
                }
            },
            {
                name: 'Academic Performance',
                type: 'line',
                data: aca,
                markPoint: {
                  data: [
                    { type: 'max', name: 'Max' },
                    { type: 'min', name: 'Min' }
                  ]
                },
                markLine: {
                  data: [{ type: 'average', name: 'Avg' }]
                }
            },
            {
                name: 'Attendance',
                type: 'line',
                data: att,
                markPoint: {
                  data: [
                    { type: 'max', name: 'Max' },
                    { type: 'min', name: 'Min' }
                  ]
                },
                markLine: {
                  data: [{ type: 'average', name: 'Avg' }]
                }
            }
        ]
    });
}