$( document ).ready(initPage());
function initPage() {
    "use strict"; //Help to get better code quality

    //Initial Ajax setup
    var csrftoken = getCookie('csrftoken');
    $.ajaxSetup({
        type: "POST",
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    //Event registers
    $(".input-group-btn .btn").on("click", updateClickHandler);


    //Event handlers
    function updateClickHandler(){
        var inputField = $(this).closest(".input-group").find("input");
        var quantity = inputField.val();
        var ingredientId = inputField.attr("id").split("-")[1];
        createOrUpdateIngredient(ingredientId, quantity);
    }


    //Helper functions
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

    function resetAllStatus() {

        var allInventoryRows = $(".table tr");

        $.each(allInventoryRows, function () {
            $(this)
                .find("td")
                .last()
                .html("Not changed");
        });
    }

    function updateIngredientStatus(text, ingredientId){
        var inputField = $("#ingredient-" + ingredientId);
        inputField
            .closest("tr")
            .find("td")
            .last()
            .html(text);
    }

    function createOrUpdateIngredient(ingredientId, quantity) {
        var passedData = {ingredient: ingredientId, quantity: quantity};
        $.ajax({
            url: "/whatToEat/update-inventory/",
            dataType: "JSON",
            data: passedData
        })
            .done(function (data) {

                var status = data.status;
                var ingredientId = data.ingredient;

                if (status == "success" && ingredientId > 0) {
                    resetAllStatus();
                    updateIngredientStatus("Updated successfully", ingredientId);
                }

            })
    }

}
