getdata("1");

function getdata(survey_num) {
  $("#survey_num").html("Survey 0" + survey_num + " Analysis");
  var settings = {
    "url": backendURL+"/Tdashboard",
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
    console.log(response);
    $('.total').each(function () {
      $(this).html("Total: " + (response.total));
    });
    $("#completed").html(response.completed);
    $("#incomplete").html((response.in_progress)+(response.invited));
    $("#total").html(response.total);
    $("#hcompleted").html(response.hcompleted+" from House");
    $("#hincomplete").html((response.hin_progress)+(response.hinvited)+" from House");
    $("#htotal").html(response.htotal+" from House");
    var incompletelist = "";
    for(stu of response.hincomplete_list){
      incompletelist += "<tr><td>"+stu[0]+"</td><td>"+stu[1]+"</td><td>"+stu[2]+"</td><td>"+stu[3]+"</td></tr>";
    }
    $("#incompletelist").html(incompletelist);
    stuparticipation(response.completed, response.in_progress, response.invited, response.hcompleted, response.hin_progress, response.hinvited);
    byHouses(response.participation_by_house.house, response.participation_by_house.count);
  });
  getFeedback(survey_num, 1);
}


function stuparticipation(completed, in_progress, invited, hcompleted, hin_progress, hinvited) {
  echarts.init(document.querySelector("#stuparticipation")).setOption({
    legend: {
      data: ['Total Students', 'Students from House']
    },
    radar: {
      indicator: [{
          name: 'In Progress',
          max: 20
        },
        {
          name: 'Completed',
          max: 200
        },
        {
          name: 'Invited',
          max: 20
        }
      ]
    },
    series: [{
      type: 'radar',
      data: [{
          value: [in_progress, completed, invited],
          name: 'Total Students'
        },
        {
          value: [hin_progress, hcompleted, hinvited],
          name: 'Students from House'
        }
      ]
    }]
  });
}

function byHouses(houses, count) {
  echarts.init(document.querySelector("#byhouses")).setOption({
    xAxis: {
      name: 'House',
      nameLocation: 'middle',
      nameGap: 50,
      type: 'category',
      data: houses
    },
    yAxis: {
      name: 'No. of students',
      nameLocation: 'middle',
      nameGap: 50,
      type: 'value'
    },
    series: [{
      data: count,
      type: 'bar'
    }]
  });
}

function getFeedback(survey_num, count) {
  var settings = {
    "url": backendURL+"/Tfeedback",
    "method": "POST",
    "timeout": 0,
    "headers": {
      "Content-Type": "application/json"
    },
    "data": JSON.stringify({
      "survey": survey_num,
      "count": count,
      "house": "Vanguard"
    }),
  };

  $.ajax(settings).done(function (response) {
    console.log(typeof (response));
    var feedback = "";
    Object.keys(response.comments).forEach(function (key) {
      feedback += '<div class="post-item clearfix"><h4 style="margin-left: 0px;"><a href="#">' + key + '</a></h4><p style="margin-left: 0px;">' + response.comments[key] + '</p></div>';
    });
    $("#feedback").html(feedback)
    start = (count * 10);
    console.log(response.count);
    if (start > response.count) {
      start = response.count;
    }
    $("#comm_count").html("(" + start + "/" + (response.count) + ")");
    if (start < response.count) {
      $("#comm_n").html(">>");
      $("#comm_n").attr("onclick", "getFeedback('" + survey_num + "', " + (count + 1) + ")");
    } else {
      $("#comm_n").html("");
    }
    if (count > 1) {
      $("#comm_b").html("<<");
      $("#comm_b").attr("onclick", "getFeedback('" + survey_num + "', " + (count - 1) + ")");
    } else {
      $("#comm_b").html("");
    }
  });
}
