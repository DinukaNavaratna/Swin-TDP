function getdata(survey_num) {
    var settings = {
        "url": backendURL+"/Snominations",
        "method": "POST",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json"
        },
        "data": JSON.stringify({
            "survey": survey_num,
            "house": "",
            "sid": "37915"
        }),
    };

    $.ajax(settings).done(function (response) {
        di1(dijson(response.net_0_Friends));
        di2(dijson(response.net_1_Influential));
        di3(dijson(response.net_2_Feedback));
        di4(dijson(response.net_3_MoreTime));
        di5(dijson(response.net_4_Advice));
        di6(dijson(response.net_5_Disrespect));
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(errorThrown);
    });
}

function dijson(diarr) {
    var json = {
        "nodes": [],
        "links": [],
        "categories": []
    }

    for (node of diarr) {
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
    return json
}

function di1(json) {
    var chartDom = document.getElementById('di1');
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
                text: 'Friends',
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

function di2(json) {
    var chartDom = document.getElementById('di2');
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
                text: 'Influential',
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

function di3(json) {
    var chartDom = document.getElementById('di3');
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
                text: 'Feedback',
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

function di4(json) {
    var chartDom = document.getElementById('di4');
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
                text: 'More Time',
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

function di5(json) {
    var chartDom = document.getElementById('di5');
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
                text: 'Advice',
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

function di6(json) {
    var chartDom = document.getElementById('di6');
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
                text: 'Disrespect',
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
