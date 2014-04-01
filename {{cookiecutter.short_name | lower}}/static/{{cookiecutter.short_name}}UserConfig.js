/**
 * Module that controls the {{cookiecutter.full_name}} user settings. Includes Knockout view-model
 * for syncing data.
 */
;(function (global, factory) {
    if (typeof define === 'function' && define.amd) {
        define(['knockout', 'jquery', 'osfutils', 'knockoutpunches'], factory);
    } else {
        global.{{cookiecutter.short_name | capitalize}}UserConfig  = factory(ko, jQuery);
    }
}(this, function(ko, $) {
    // Enable knockout punches
    ko.punches.enableAll();


    var ViewModel = function(url) {
        var self = this;
        self.userHasAuth = ko.observable(false);
        // TODO: Observables, computes, etc. here
    };

    function {{cookiecutter.short_name | capitalize}}NodeConfig(selector, url) {
        // Initialization code
        var self = this;
        self.viewModel = new ViewModel(url);
        $.osf.applyBindings(self.viewModel, selector);
    }

}));
