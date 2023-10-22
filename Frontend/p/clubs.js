var chartDom = document.getElementById('clubs_sna');
var myChart = echarts.init(chartDom);

function search() {
    var cat = $('#cat').find(":selected").val();

    if (cat == "") {
        alert("Please select a category to start the analysis.");
        return;
    }
    myChart.showLoading();

    var settings = {
        "url": backendURL+"/clubs",
        "method": "POST",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json"
        },
        "data": JSON.stringify({
            "cat": cat,
            "club": "Photography Club"
        }),
    };

    $.ajax(settings).done(function (response) {
        var src = response.source;
        var trg = response.target;
        var clb = response.club;
        tojson(src, trg, clb);
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(errorThrown);
    });
}

function tojson(source, target, club) {
    var json = {
        "nodes": [],
        "links": [],
        "categories": []
    }

    var c = 0;
    for (src of source) {
        if (json.nodes.length == 0) {
            json.nodes.push({
                "id": source[c].toString(),
                "name": source[c].toString(),
                "category": club[c].toString()
            });
            json.nodes.push({
                "id": target[c].toString(),
                "name": target[c].toString(),
                "category": club[c].toString()
            });
        } else {
            var new1 = true;
            var new2 = true;
            for (var i = 0; i < json.nodes.length; i++) {
                if (json.nodes[i].id === source[c].toString()) {
                    new1 = false;
                }
                if (json.nodes[i].id === target[c].toString()) {
                    new2 = false;
                }
                if ((new1 == false) && (new2 == false)) {
                    break;
                }
            }
            if (new1) {
                json.nodes.push({
                    "id": source[c].toString(),
                    "name": source[c].toString(),
                    "category": club[c].toString()
                });
            }
            if (new2) {
                json.nodes.push({
                    "id": target[c].toString(),
                    "name": target[c].toString(),
                    "category": club[c].toString()
                });
            }
        }

        json.links.push({
            "source": source[c].toString(),
            "target": target[c].toString()
        });

        if (json.categories.length == 0) {
            json.categories.push({
                "name": club[c].toString()
            });
        } else {
            var newclub = true;
            for (var i = 0; i < json.categories.length; i++) {
                if (json.categories[i].name === club[c].toString()) {
                    newclub = false;
                    break;
                }
            }
            if (newclub) {
                json.categories.push({
                    "name": club[c].toString()
                });
            }
        }
        c++;
    }

    console.log(json);
    club_sna(json);
}

function club_sna(json) {
    var option;

    $(function () {
        myChart.hideLoading();
        json.nodes.forEach(function (node) {
            node.symbolSize = 10;
        });
        option = {
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
                    draggable: true,
                    data: json.nodes,
                    links: json.links,
                    categories: json.categories,
                    roam: true,
                    animation: true,
                    label: {
                        position: 'right'
                    },
                    force: {
                        edgeLength: 100,
                        repulsion: 500,
                        gravity: 0.1
                    },
                }
            ]
        };
        myChart.setOption(option);
    });

    option && myChart.setOption(option);

}
