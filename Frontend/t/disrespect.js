var surveynum = ""
function getdata(survey_num) {
    surveynum = survey_num;
    $("#survey_num").html("Survey 0" + survey_num + " Analysis");
    var settings = {
        "url": backendURL+"/Tdisrespect",
        "method": "POST",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json"
        },
        "data": JSON.stringify({
            "survey": survey_num,
            "house": "Vanguard"
        }),
    };

    $.ajax(settings).done(function (response) {
        disrespect(response.disrespect, "Vanguard");
        disrespectee_tbl(response.disrespect.sort());
        disrespecter_tbl(response.disrespect.sort());
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(errorThrown);
    });
}

function disrespect(disrespect, house) {
    var json = {
        "nodes": [],
        "links": [],
        "categories": []
    }

    for (node of disrespect) {
        if (json.nodes.length == 0) {
            json.nodes.push({
                "id": node[0].toString(),
                "name": node[1] + " " + node[2],
            });
        } else {
            var new1 = true;
            var new2 = true;
            for (var i = 0; i < json.nodes.length; i++) {
                if (json.nodes[i].id === node[0].toString()) {
                    new1 = false;
                }
                if (json.nodes[i].id === node[3].toString()) {
                    new2 = false;
                }
                if ((new1 == false) && (new2 == false)) {
                    break;
                }
            }
            if (new1) {
                json.nodes.push({
                    "id": node[0].toString(),
                    "name": node[1] + " " + node[2]
                });
            }
            if (new2) {
                json.nodes.push({
                    "id": node[3].toString(),
                    "name": node[4] + " " + node[5]
                });
            }
        }
        json.links.push({
            "source": node[0].toString(),
            "target": node[3].toString()
        });
    }
    console.log(json);
    disrespect_sna(json, house);
}

function disrespect_sna(json, house) {
    var chartDom = document.getElementById('disrespect_sna');
    var myChart = echarts.init(chartDom);
    var option;

    myChart.showLoading();
    $(function () {
        myChart.hideLoading();
        json.nodes.forEach(function (node) {
            node.symbolSize = 10;
        });
        option = {
            title: {
                text: 'Disrespect Matrix',
                subtext: 'For ' + house + " House",
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
                    name: 'Student Name',
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

function disrespectee_tbl(disrespect) {
    disrespectee = {};
    for (var row of disrespect) {
        if (disrespectee.hasOwnProperty(row[0])) {
            disrespectee[row[0]]['count'] = disrespectee[row[0]]['count'] + 1;
        } else {
            disrespectee[row[0]] = { 'fname': row[1], 'lname': row[2], 'count': 1 };
        }
    }

    var tbl = ""
    for (var row in disrespectee) {
        tbl += "<tr onclick=\"window.open('student.php?sid="+row+"&survey="+surveynum+"', '_self')\"><td>" + row + "</td><td>" + disrespectee[row]['fname'] + "</td><td>" + disrespectee[row]['lname'] + "</td><td>" + disrespectee[row]['count'] + "</td></tr>";
    }
    $("#disrespectee_tbl").html(tbl);
}

function disrespecter_tbl(disrespect) {
    disrespecter = {};
    for (var row of disrespect) {
        if (disrespecter.hasOwnProperty(row[3])) {
            disrespecter[row[3]]['count'] = disrespecter[row[3]]['count'] + 1;
        } else {
            disrespecter[row[3]] = { 'fname': row[4], 'lname': row[5], 'count': 1 };
        }
    }
    var tbl = ""
    for (var row in disrespecter) {
        tbl += "<tr onclick=\"window.open('student.php?sid="+row+"&survey="+surveynum+"', '_self')\"><td>" + row + "</td><td>" + disrespecter[row]['fname'] + "</td><td>" + disrespecter[row]['lname'] + "</td><td>" + disrespecter[row]['count'] + "</td></tr>";
    }
    $("#disrespecter_tbl").html(tbl);
}