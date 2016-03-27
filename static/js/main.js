$(document).ready(function () {
    var basic = $('#basic-info'),
        address = $('#address'),
        contact1 = $('#contact1'),
        user = $('#user'),
        home = $('#home'),
        contact = $('#contact');

    basic.hide();
    address.hide();
    contact1.hide();

    user.on('click', function() {
        address.hide();
        contact1.hide();
        basic.show();
    }),
    home.on('click', function() {
        basic.hide();
        contact1.hide();
        address.show();
    }),
    contact.on('click', function() {
        basic.hide();
        address.hide();
        contact1.show();
    });
});
