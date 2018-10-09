$(function() {
    console.log("hello");
    $('#submitBtn').click(function() {
        var val1 = $('#1Box').children().text().split("#")[1];
        var val2 = $('#2Box').children().text().split("#")[1];
        var val3 = $('#3Box').children().text().split("#")[1];
        var val4 = $('#4Box').children().text().split("#")[1];
        var val5 = $('#5Box').children().text().split("#")[1];

        var args = "?val1=" + val1 + "&val2=" + val2 +
            "&val3=" + val3 + "&val4=" + val4 + "&val5=" + val5;

        console.log(args);
        window.location.assign("/wordcolor" + args)
    });

    $('.box').click(function() {
        $('#wordSelector').css('color', $(this).children().text());
    });

    $('#nextPhoto').click(function() {
        var name = $('#selectPhoto').val();
        window.location.assign("/colorpicker?name=" + name);
    });
});