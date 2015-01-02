jQuery(document).ready(function ($) {

    $('body').on('keypress', '.form-control', function () {
        $('.has-error').hide();
    });

    $('body').on('click', 'form', function () {
        $('.has-error').hide();
    });
});
