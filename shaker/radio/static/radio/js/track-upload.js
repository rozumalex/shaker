$(function () {
  $(".upload-tracks").click(function () {
    $("#trackupload").click();
  });

  $("#trackupload").fileupload({
    dataType: 'json',
    done: function (e, data) {  /* 3. PROCESS THE RESPONSE FROM THE SERVER */
      if (data.result.is_valid) {
        $("#new-tracks").prepend(
          "<li>" + data.result.artist + " - " + data.result.title + " uploaded by " + data.result.user_uploaded + "</li>"
        )
        $("#new-tracks li:last-child").remove();
      }
    }
  });

});