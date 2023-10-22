function getdata(survey_num) {
    if(survey_num == "1"){
        alert("No K6 data available for Survey 01");
        return;
    }
    $("#survey_num").html("Survey 0"+survey_num+" Analysis");
    var settings = {
        "url": backendURL+"/Tk6",
        "method": "POST",
        "timeout": 0,
        "headers": {
            "Content-Type": "application/json"
        },
        "data": JSON.stringify({
            "survey": survey_num,
            "house": ""
        }),
    };

    $.ajax(settings).done(function (response) {
        abnormal(response.abnormal);
        borderline(response.borderline);
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(errorThrown);
    });
}

function abnormal(abnormal) {
    var tbl = ""
    for (var student of abnormal) {
        tbl += "<tr onclick=\"window.open('student.php?sid="+student[6]+"', '_self')\"><td>" + student[0] + "</td><td>" + student[1] + "</td><td>" + student[2] + "</td><td>" + student[3] + "</td><td>" + student[4] + "</td><td>" + student[5] + "</td></tr>";
    }
    $("#abnormal").html(tbl);
}

function borderline(borderline) {
    var tbl = ""
    for (var student of borderline) {
        tbl += "<tr onclick=\"window.open('student.php?sid="+student[6]+"', '_self')\"><td>" + student[0] + "</td><td>" + student[1] + "</td><td>" + student[2] + "</td><td>" + student[3] + "</td><td>" + student[4] + "</td><td>" + student[5] + "</td></tr>";
    }
    $("#borderline").html(tbl);
}