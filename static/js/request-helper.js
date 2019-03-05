$(function () {
    $('#btnSignUp').click(function () {

        $.ajax({
            url: '/signup',
            data: $('form').serialize(),
            type: 'POST',
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
    $('#btnSingIn').click(function () {

        $.ajax({
            url: '/login',
            data: $('form').serialize(),
            type: 'POST',
            success: function (response) {
                console.log(response);
            },
            error: function (error) {
                console.log(error);
            }
        });
    });
});
