$(document).ready(function () {
    $("#on_click").click(function (event) {
        $.getJSON('/on_click', {}, function (data) { });
        return false;
    });


    $("#off_click").click(function () {
        $.ajax({
            type: "GET",
            url: "{{ url_for( 'app.on_click' ) }}",
            success: function () {
                alert("Tree Off.");
            }
        });
    });

    $("#cycle_click").click(function () {
        $.ajax({
            type: "GET",
            url: "{{ url_for( 'app.cycle_click' ) }}",
            success: function () {
                alert("Cycle on.");
            },
            fail: function () {
                alert("fail")
            }
        });
    });

    $("#one_by_one_click").click(function () {
        $.ajax({
            type: "GET",
            url: "{{ url_for( 'app.one_by_one_click' ) }}",
            success: function () {
                alert("One by one on.");
            }
        });
    });

    $("#sparkle_click").click(function () {
        $.ajax({
            type: "GET",
            url: "{{ url_for( 'app.sparkle_click' ) }}",
            success: function () {
                alert("Sparkle On.");
            }
        });
    });
});