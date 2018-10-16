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

    $('#wordColorNext').click(function() {
        var color = $('#wordSelector').css("color");
        var newColor = rgb2hex(color);
        console.log(newColor);
        newColor = newColor.split("#")[1]
        window.location.assign("/final?color=" + newColor);
    });

    function rgb2hex(rgb) {
    rgb = rgb.match(/^rgb\((\d+),\s*(\d+),\s*(\d+)\)$/);
    function hex(x) {
        return ("0" + parseInt(x).toString(16)).slice(-2);
    }
    return "#" + hex(rgb[1]) + hex(rgb[2]) + hex(rgb[3]);
}

function getUrlParams( prop ) {
    var params = {};
    var search = decodeURIComponent( window.location.href.slice( window.location.href.indexOf( '?' ) + 1 ) );
    var definitions = search.split( '&' );

    definitions.forEach( function( val, key ) {
        var parts = val.split( '=', 2 );
        params[ parts[ 0 ] ] = parts[ 1 ];
    } );

    return ( prop && prop in params ) ? params[ prop ] : params;
}

    var x = getUrlParams('color');
    console.log(x);
    $('#colorFinal').css("color", "#" + x);

    $('#fogToggle').click(function() {
        $('#fog').css('display','block');
        var color = $('#wordSelector').css('color');
        var newColor = rgb2hex(color);
        console.log("color" + newColor)
        $('body').css('background-color', newColor);

    });

    $('#fog').click(function() {
        $('#fog').css('display','none');

    });



    if($('#fog').css('display') == 'none') {


    }

    while( $('.fit_in p').width() < ($('.fit_in').width() - 90)) {
        $('.fit_in p').css('font-size', (parseInt($('.fit_in p').css('font-size')) + 1) + "px" );
    }

    $('.lightbox').click(function() {
        console.log("clidfksjdlf");
        while( $('.lightbox-target p').width() < ($('.lightbox-target').width() / 2)) {
            $('.lightbox-target p').css('font-size', (parseInt($('.lightbox-target p').css('font-size')) + 1) + "px" );
        }
    });

    $('.subG').click(function() {
        var color = x;
        window.location.assign("/submit?color=" + color);
    });




});