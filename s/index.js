getdata("2");

function getdata(survey_num) {
  $("#survey_num").html("Survey 0" + survey_num + " - Status Pending");
  var settings = {
    "url": backendURL+"/Sdashboard",
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
    console.log(response);
    var qanda = "";
    var c = 0;
    for(question of response.questions){
      qanda += "<tr><td>"+question+"</td><td>"+response.answers[c]+"</td></tr>";
      c++;
    }
    $("#survey_num").html("Survey 0" + survey_num + " - "+response.status);
    $("#answers").html(qanda);
  });
  getFeedback(survey_num, 1);
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
      "house": ""
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
