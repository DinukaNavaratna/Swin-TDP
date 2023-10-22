function getdata(survey_num) {
    $("#survey_num").html("Survey 0"+survey_num+" Analysis");
    var settings = {
        "url": backendURL+"/Tmasculinity",
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
        masculinity(response.masculinity);
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(errorThrown);
    });
}

function masculinity(masculinity) {
    var tbl = ""
    for (var student of masculinity) {
        tbl += "<tr onclick=\"window.open('student.php?sid="+student[0]+"', '_self')\"><td>" + student[0] + "</td><td>" + student[1] + "</td><td>" + student[2] + "</td><td>" + student[3] + "</td><td>" + student[4] + "</td></tr>";
    }
    $("#masculinity_tbl").html(tbl);
}