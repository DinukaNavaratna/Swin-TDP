getdata("1");

function getdata(survey_num) {
  $("#survey_num").html("Survey 0" + survey_num + " Analysis");
  var settings = {
    "url": backendURL+"/Odashboard",
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
    console.log(response);
    $('.total').each(function () {
      $(this).html("Total: " + (response.total));
    });
    $("#completed").html(response.completed);
    $("#in_progress").html(response.in_progress);
    $("#invited").html(response.invited);
    Student_Participation_Chart(response.completed, response.in_progress, response.invited);
    byYears(response.participation_by_year.year, response.participation_by_year.count);
    byHouses(response.participation_by_house.house, response.participation_by_house.count);
  });
  getFeedback(survey_num, 1);
}


function Student_Participation_Chart(completed, in_progress, invited) {
  echarts.init(document.querySelector("#trafficChart")).setOption({
    tooltip: {
      trigger: 'item'
    },
    legend: {
      top: '5%',
      left: 'center'
    },
    series: [{
      name: 'Student Participation',
      type: 'pie',
      radius: ['40%', '70%'],
      avoidLabelOverlap: false,
      label: {
        show: false,
        position: 'center'
      },
      emphasis: {
        label: {
          show: true,
          fontSize: '18',
          fontWeight: 'bold'
        }
      },
      labelLine: {
        show: false
      },
      data: [{
        value: parseInt(completed),
        name: 'Completed'
      },
      {
        value: parseInt(in_progress),
        name: 'In Progress'
      },
      {
        value: parseInt(invited),
        name: 'Pending'
      }
      ]
    }]
  });
}

function byYears(years, count) {
  echarts.init(document.querySelector("#byyears")).setOption({
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'shadow'
      }
    },
    xAxis: {
      name: 'Years completed in the school',
      nameLocation: 'middle',
      nameGap: 50,
      type: 'category',
      data: years
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
    "url": backendURL+"/Ofeedback",
    "method": "POST",
    "timeout": 0,
    "headers": {
      "Content-Type": "application/json"
    },
    "data": JSON.stringify({
      "survey": survey_num,
      "count": count
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
