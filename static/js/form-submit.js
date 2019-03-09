function escapeHtml(str) {
    var div = document.createElement('div');
    div.appendChild(document.createTextNode(str));
    return div.innerHTML;
};

function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\[").replace(/[\]]/, "\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results === null ? "" : decodeURIComponent(results[1].replace(/\+/g, " "));
}

/** Function that count occurrences of a substring in a string;
 * @param {String} string               The string
 * @param {String} subString            The sub string to search for
 * @param {Boolean} [allowOverlapping]  Optional. (Default:false)
 * @author Vitim.us http://stackoverflow.com/questions/4009756/how-to-count-string-occurrence-in-string/7924240#7924240
 */
function occurrences(string, subString, allowOverlapping) {

    string += "";
    subString += "";
    if (subString.length <= 0) return (string.length + 1);

    var n = 0,
        pos = 0,
        step = allowOverlapping ? 1 : subString.length;

    while (true) {
        pos = string.indexOf(subString, pos);
        if (pos >= 0) {
            ++n;
            pos += step;
        } else break;
    }
    return n;
}

function removeClassesFromDiv(formName) {
    formName = '#' + formName + ' *'
    $(formName).filter(':input').each(function(){
        $(this).parent().removeClass("attempted-submit");
        $(this).removeClass("field-error");
    });
}

function validateFields(formName) {
    removeClassesFromDiv(formName);
    var valid = true;
    formName = '#' + formName + ' *'
    $(formName).filter(':input').each(function(){
        if ((!$(this).val() && !$(this).is("button") && $(this).prop('name') !== 'csrfmiddlewaretoken' && $(this).prop('id').toLowerCase().indexOf('honey') == -1)) {
            $(this).parent().addClass("attempted-submit");
            $(this).addClass("field-error");
            valid = false;
        } else if ($(this).val() && $(this).prop('id').toLowerCase().indexOf('honey') !== -1) {
            valid = false;
        }
    });
    return valid;
}

function abortButtonLoading(tid, button, text) { 
  clearTimeout(tid);
  $(button).text(text);
}

function loadingButton(button, text, processing) {
    var count = occurrences($(button).text(), ".")
    dots = "."
    if (count != 3) {
        dots = dots.repeat(count);
        dots += "."
    }
    
    msg = processing + dots;    
    
    $(button).text(msg);
}

function generateFormDict(formName) {
    formName = '#' + formName + ' *';
    d = {};
    
    $(formName).filter(':input').each(function(){
        if (!$(this).is("button") && ($(this).prop('id')) && $(this).prop('id').toLowerCase().indexOf('honey') == -1) {
            var key = $(this).prop('id');
            var val = escapeHtml($(this).val());
            if ($(this).prop('id').toLowerCase().indexOf('v') != -1) {
                if (val.length > 140) {
                    val = val.slice(0,140);
                }
            }
            d[key] = val;
        } else if ($(this).prop('name') == 'csrfmiddlewaretoken') {
            d['csrfmiddlewaretoken'] = escapeHtml($(this).val());
        }
    });
        
    return d;
}

function failRedirect(formName) {
    formName = '#' + formName
    $(formName).fadeOut(300, function(){
        var $parent = $(formName).parent();
        $(formName).remove();
        $('#thanks').html("<h3 class='uppercase color-red mb10 mb-xs-24'>Error!</h3><h4 class='uppercase'>Please try again. Reloading page...</h4>");
    });

    $(this).delay(2000).queue(function() {
        window.location.href = '/';
        $(this).dequeue();
    });
}

function sendAjaxRequest(formName) {
  u = formName;
  d = generateFormDict(formName);
  formName = '#' + formName;
  var $submitform = $(formName);
  var airtable_write_endpoint = $SCRIPT_ROOT + "/demo";
  var final_dict = {};
  final_dict = d;
  $.ajax({
        url: airtable_write_endpoint,
        type:"POST",
        data: JSON.stringify(final_dict),
        headers: {
        "content-type":"application/json"
        },
        success: function( data ) {
            console.log(data)
            if (data != null) {
                $(formName).fadeOut(300, function(){
                    var $parent = $(formName).parent();
                    $(formName).remove();
                    $('#thanks').html("<h3 class='uppercase color-primary mb10 mb-xs-24'>Thank You!</h3><h4 class='uppercase'>Your Message has been queued.</h4>");
                });
            } else {
                console.log("in here 1");
                failRedirect(u);
            }
        },
        error: function(xhr, status, error) {
           console.log("in here 2");
           console.log(xhr)
           failRedirect(u);  
        },
        dataType : "json"
      }).done(function(data){

      });
      
}

 $('#submit-form').submit(function(event) {
        var $submitform = $('#submit-form');

        // Disable the submit button to prevent repeated clicks
        $submitform.find(':submit').prop('disabled', true);
        // set interval
     
        var processing = "Processing"
        var text = processing + "."
        $submitform.find(':submit').text(text);
        var $button = $submitform.find(':submit');
        var tid = setInterval(loadingButton, 300, $button, text, processing);     
        var isValid = validateFields('submit-form');
        if (isValid) {
            //SEND AJAX REQUEST
            sendAjaxRequest('submit-form');
        } else {
            $submitform.find(':submit').prop('disabled', false);
            abortButtonLoading(tid, $button,"SAY SOMETHING")
        }

        // Prevent the form from submitting with the default action
        return false;
});