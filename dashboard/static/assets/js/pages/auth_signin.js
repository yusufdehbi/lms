!(function () {
    class e {
        static initValidation() {
            Dashmix.helpers("jq-validation"),
                jQuery(".js-validation-signin").validate({
                    rules: {
                        "login-username": {required: true, minlength: 3},
                        "login-password": {required: true, minlength: 5},
                    },
                    messages: {
                        "login-username": {
                            required: "Please enter a username",
                            minlength: "Your username must consist of at least 3 characters",
                        },
                        "login-password": {
                            required: "Please provide a password",
                            minlength: "Your password must be at least 5 characters long",
                        },
                    },
                })
        }

        static init() {
            this.initValidation()
        }
    }
    Dashmix.onLoad(() => e.init())
})();