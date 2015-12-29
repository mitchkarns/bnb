$('.type').click(function (){
    var atLeastOneIsChecked = $('input[name="housing_type[]"]:checked').length > 0;
    if (atLeastOneIsChecked)
        $('#create').prop('disabled', false)
    else
        $('#create').prop('disabled', true)
});
