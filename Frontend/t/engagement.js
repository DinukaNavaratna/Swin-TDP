var surveynum = ""
function getdata(survey_num) {
    surveynum = survey_num;
    $("#survey_num").html("Survey 0"+survey_num+" Analysis");
    var settings = {
        "url": backendURL+"/Tengagement",
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
        engagement(response.engagement);
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(errorThrown);
    });
}

function engagement(engagement) {
    var tbl = ""
    for (var student of engagement) {
        tbl += "<tr onclick=\"window.open('student.php?sid="+student[0]+"&survey="+surveynum+"', '_self')\"><td>" + student[0] + "</td><td>" + student[1] + "</td><td>" + student[2] + "</td><td>" + student[3] + "</td><td>" + student[4] + "</td></tr>";
    }
    $("#engagement_tbl").html(tbl);
}