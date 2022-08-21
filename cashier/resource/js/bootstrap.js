window._ = require('lodash');

try {
    //window.Popper = require('popper.js').default;
    window.$ = window.jQuery = require('jquery');
    
    //require('jquery-ui');
    require('bootstrap');
    //require('startbootstrap-sb-admin-2');
} catch (e) {}