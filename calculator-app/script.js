$(document).ready(function () {
    $("#number_people").change(function () {
        $(".mistake").text = 'Cant be zero!'
    });
});