
$(document).ready(initPage());

function initPage() {
    "use strict"; //Help to get better code quality by applying strict rules in code execution


    //Initial select styling
    $(".selectpicker").selectpicker();


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
    $(".table tbody").on("click", ".custom-update .btn-update", updateClickHandler);
    $(".table tbody").on("click", ".btn-danger", deleteClickHandler);
    $("#btn-add-ingredient").on("click", addClickHandler);


    //Event handlers
    function updateClickHandler() {
        var inputField = $(this).closest(".custom-update").find("input");
        var selectField = $(this).closest(".custom-update").find("select");
        var quantity = inputField.val();
        var ingredientId = inputField.attr("id").split("-")[1];
        var unitId = selectField.val();
        updateIngredient(ingredientId, quantity, unitId);
    }

    function addClickHandler() {
        var ingredientList = $(this).closest("form").find("#list-ingredients");
        var inputField = $(this).parent().find("#new-ingredient-quantity");
        var unitList = $(this).closest("form").find("#list-units");
        var ingredientId = ingredientList.val();
        var quantity = inputField.val();
        var unitId = unitList.val();
        addIngredient(ingredientId, quantity, unitId);
    }


    function deleteClickHandler() {
        var inputField = $(this).closest("form").find("input[type=number]");
        var ingredientId = inputField.attr("id").split("-")[1];
        deleteFromDatabase(ingredientId);
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

    function appendNewRow(ingredientId, quantity, ingredientName, unitId) {
        var newLine = $("<tr>");
        var column1 = $("<td>");
        var column2 = $("<td>");
        var column3 = $("<td>");
        var form = $("<form>", {role: "form", class: "form-inline"});
        var div2 = $("<div>", {class: "input-group custom-update"});
        var input = $("<input>", {
            type: "number", class: "form-control",
            id: "ingredient-" + ingredientId, value: quantity,
            placeholder: "Quantity"
        });
        var inputGroupBtn = $("<div>", {class: "input-group-btn"});
        var button = $("<button>", {type: "button", class: "btn btn-default btn-primary btn-update"});
        var select = $("<select>",{class: "selectpicker", "data-width": "100px"});
        if (unitId == 1) {
            select.append("<option value='1'>ml</option>");
            select.append("<option value='2'>g</option>");
            select.append("<option value='3'> </option>");
        } else if (unitId == 2) {
            select.append("<option value='2'>g</option>");
            select.append("<option value='1'>ml</option>");
            select.append("<option value='3'> </option>");
        } else {
            select.append("<option value='3'> </option>");
            select.append("<option value='2'>g</option>");
            select.append("<option value='1'>ml</option>");
        }
        var dangerButton = $("<a>", {class: "btn btn-danger"});
        var spanIcon = $("<span>", {class: "fa fa-times"});
        dangerButton.append(spanIcon);

        button.html("update");
        inputGroupBtn.append(button);
        div2.append(select);
        div2.append(input);
        div2.append(inputGroupBtn);
        form.append(div2);
        form.append(dangerButton);
        column2.append(form);
        column1.html(ingredientName);
        column3.html("Sucessfully added");
        newLine.append(column1);
        newLine.append(column2);
        newLine.append(column3);
        $(".table tbody").append(newLine);
        $(".selectpicker").selectpicker();
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

    function updateIngredientStatus(text, ingredientId) {
        var inputField = $("#ingredient-" + ingredientId);
        inputField
            .closest("tr")
            .find("td")
            .last()
            .html(text);
    }

    function updateIngredient(ingredientId, quantity, unit) {
        var passedData = {ingredient: ingredientId, quantity: quantity, unit: unit};
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


    function addIngredient(ingredientId, quantity, unit) {
        var passedData = {ingredient: ingredientId, quantity: quantity, unit:unit};
        $.ajax({
            url: "/whatToEat/update-inventory/",
            dataType: "JSON",
            data: passedData
        })
            .done(function (data) {

                var status = data.status;
                var ingredientId = data.ingredient;
                var ingredientName = data.ingredientname;
                var quantity = data.quantity;
                var unitId = data.unit;
                console.log("OK");

                if (status == "success" && ingredientId > 0) {
                    resetAllStatus();
                    appendNewRow(ingredientId, quantity, ingredientName, unitId);
                }
            })
    }

    function deleteFromDatabase(ingredientId){
        var passedData = {ingredient: ingredientId};
        $.ajax({
            url: "/whatToEat/delete-inventory/",
            dataType: "JSON",
            data: passedData
        })
            .done(function (data) {

                var status = data.status;
                var ingredientId = data.ingredient;
                console.log("OK");
                console.log("id " + ingredientId);
                if (status == "success" && ingredientId > 0) {
                    resetAllStatus();
                    $("#ingredient-"+ingredientId).closest("tr").hide();
                }
            })
    }

}
