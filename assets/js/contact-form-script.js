/*==============================================================*/
// Klev Contact Form  JS
/*==============================================================*/
(function ($) {
    "use strict"; // Start of use strict
    $("#contactForm").validator().on("submit", function (event) {
        if (event.isDefaultPrevented()) {
            // handle the invalid form...
            formError();
            submitMSG(false, "Did you fill in the form properly?");
        } else {
            // everything looks good! Let's submit via AJAX
            event.preventDefault();
            submitForm();
        }
    });

    function submitForm(){
        // Initiate Variables With Form Content
        var name = $("#name").val();
        var email = $("#email").val();
        var message = $("#message").val();

        $.ajax({
            type: "POST",
            url: "https://formsubmit.co/ajax/lokeshvanumu61@gmail.com",
            dataType: 'json',
            accepts: 'application/json',
            data: {
                name: name,
                email: email,
                message: message,
                _captcha: false,
                _subject: "New submission from Portfolio Contact Form"
            },
            success : function(data){
                if (data.success == "true" || data.success === true){
                    formSuccess();
                } else {
                    formError();
                    submitMSG(false, "Oops! Something went wrong.");
                }
            },
            error: function() {
                formError();
                submitMSG(false, "Oops! Something went wrong.");
            }
        });
    }

    function formSuccess(){
        $("#contactForm")[0].reset();
        submitMSG(true, "Message Submitted successfully!")
    }

    function formError(){
        $("#contactForm").removeClass().addClass('shake animated').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function(){
            $(this).removeClass();
        });
    }

    function submitMSG(valid, msg){
        var msgClasses;
        if(valid){
            msgClasses = "h4 text-left tada animated text-success mt-3";
        } else {
            msgClasses = "h4 text-left text-danger mt-3";
        }
        $("#msgSubmit").removeClass().addClass(msgClasses).text(msg);
    }
}(jQuery)); // End of use strict