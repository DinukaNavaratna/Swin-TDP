function getdata(survey_num) {
    $("#survey_num").html("Survey 0"+survey_num+" Analysis");
    var settings = {
        "url": backendURL+"/Tgrowthmindset",
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
        growthmindset(response.growthmindset);
    }).fail(function (jqXHR, textStatus, errorThrown) {
        console.log(errorThrown);
    });
}

function growthmindset(growthmindset) {
    var tbl = ""
    for (var student of growthmindset) {
        tbl += "<tr onclick=\"window.open('student.php?sid="+student[0]+"', '_self')\"><td>" + student[0] + "</td><td>" + student[1] + "</td><td>" + student[2] + "</td><td>" + student[3] + "</td><td>" + student[4] + "</td></tr>";
    }
    $("#growthmindset_tbl").html(tbl);
}