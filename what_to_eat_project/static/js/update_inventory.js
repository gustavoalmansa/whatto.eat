$(function() {
    // using jQuery

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        type: "POST",
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    $(".input-group-btn .btn").on("click", function(){
        /*TODO: get ingredientID and quantity*/
        var ingredientId = "";
        var quantity = "";
        var passedData = {ingredient: 18, quantity: 4};
        $.ajax({
            url: "/whatToEat/update-inventory/",
            dataType: "JSON",
            data: passedData,
            done: function(data){
                console.log("My data " + data);
            }
        });
    })



});
