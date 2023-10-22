var url_string = window.location.href; 
var url = new URL(url_string);
var sid = url.searchParams.get("sid");
if(sid != ""){
    $('#sid').val(sid);
}

var chartDom = document.getElementById('student_sna');
var myChart = echarts.init(chartDom);

function search() {
    var cat = $('#cat').find(":selected").val();
    var survey = $('#survey').find(":selected").val();
    var sid = $('#sid').val()

    if (cat == "" || survey == "" || sid == "") {
        alert("Please enter the requred details to start the analysis.");
        return;
    }
    myChart.showLoading();

    var settings = {
        "url": backendURL+"/Tstudent",
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
        if(response.network.length == 0){
            alert("No networks identified!\nPlease try a different combination.");
            myChart.hideLoading();
            return;
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
