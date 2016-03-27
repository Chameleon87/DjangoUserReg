$(document).ready(function () {
    var basic = $('#basic-info');
    var address = $('#address');
    var user = $('#user');
    var home = $('#home');
    var contact = $('#contact');

    user.click().toggle(basic);
    home.click().toggle(address);
    
});
