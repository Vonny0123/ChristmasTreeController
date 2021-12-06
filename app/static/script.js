$(document).ready(function () {
    $("#on_click").click(function () {
        $.ajax({
            type: "POST",
            url: "/on_click",
            success: function () {
                alert("Tree On.");
            }
        });
    });

    $("#off_click").click(function () {
        $.ajax({
            type: "POST",
            url: "/off_click",
            success: function () {
                alert("Tree Off.");
            }
        });
    });

    $("#cycle_click").click(function () {
        $.ajax({
            type: "POST",
            url: "/cycle_click",
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
            type: "POST",
            url: "/one_by_one_click",
            success: function () {
                alert("One by one on.");
            }
        });
    });

    $("#sparkle_click").click(function () {
        $.ajax({
            type: "POST",
            url: "/sparkle_click",
            success: function () {
                alert("Sparkle On.");
            }
        });
    });
});