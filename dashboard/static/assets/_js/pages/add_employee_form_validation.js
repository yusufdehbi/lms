class addEmployeeFormValidation {
    static initValidation() {
        Dashmix.helpers('jq-validation');
        jQuery('.js-validation').validate({
            ignore: [],
            rules: {
                'first_name': {
                    required: true,
                    minlength: 3
                },
                'last_name': {
                    required: true,
                    minlength: 3
                },
                'username': {
                    required: true,
                    minlength: 3
                },
                'email': {
                    required: true,
                    emailWithDot: true
                },
                'birthday': {
                    date: true
                },
                'gender': {
                    required: true
                },
                'employee_id': {
                    required: true,
                },
                'department': {
                    required: true
                },
                'position': {
                    required: true
                },
                'date_joined': {
                    required: true,
                    date: true
                }
            },
            messages: {
                'first_name': {
                    required: 'First name is required',
                    minlength: 'First name must be at least 3 characters long'
                },
                'last_name': {
                    required: 'Last name is required',
                    minlength: 'Last name must be at least 3 characters long'
                },
                'username': {
                    required: 'Username is required',
                    minlength: 'Username must be at least 3 characters long'
                },
                'email': {
                    required: 'Email is required',
                    emailWithDot: 'Please enter a valid email address'
                },
                'birthday': {
                    date: 'Please enter a valid date'
                },
                'gender': {
                    required: 'Please select your gender'
                },
                'employee_id': {
                    required: 'Employee ID is required'
                },
                'department': {
                    required: 'Department is required'
                },
                'position': {
                    required: 'Position is required'
                },
                'date_joined': {
                    required: 'Date joined is required',
                    date: 'Please enter a valid date'
                }
            }
        });
        // Init Validation on Select2 change
        jQuery('.js-select2').on('change', e => {
            jQuery(e.currentTarget).valid();
        });

        jQuery('.js-flatpickr').on('change', e => {
            jQuery(e.currentTarget).valid();
        })
    }

    static init() {
        this.initValidation();
    }
}

Dashmix.onLoad(() => addEmployeeFormValidation.init());
