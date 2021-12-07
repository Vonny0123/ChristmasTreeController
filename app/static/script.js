const Http = new XMLHttpRequest();
var brightness_slider = document.getElementById("brightness_slider");
var on_button = document.getElementById("on_button");
var off_button = document.getElementById("off_button");
var cycle_button = document.getElementById("cycle_button");
var one_by_one_button = document.getElementById("one_by_one_button");
var sparkle_button = document.getElementById("sparkle_button");

var current;

brightness_slider.oninput = function () {
    current = this.value;

    // I've added this call to the server, which send 'current' value
    Http.open('POST', '/brightness_slider')
    Http.send(current)
}

on_button.onclick = function () {
    current = this.value;

    // I've added this call to the server, which send 'current' value
    Http.open('POST', '/on_button')
    Http.send(current)
}

off_button.onclick = function () {
    current = this.value;

    // I've added this call to the server, which send 'current' value
    Http.open('POST', '/off_button')
    Http.send(current)
}

cycle_button.onclick = function () {
    current = this.value;

    // I've added this call to the server, which send 'current' value
    Http.open('POST', '/cycle_button')
    Http.send(current)
}

one_by_one_button.onclick = function () {
    current = this.value;

    // I've added this call to the server, which send 'current' value
    Http.open('POST', '/one_by_one_button')
    Http.send(current)
}

sparkle_button.onclick = function () {
    current = this.value;

    // I've added this call to the server, which send 'current' value
    Http.open('POST', '/sparkle_button')
    Http.send(current)
}