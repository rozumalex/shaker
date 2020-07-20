$(function () {
  $(".upload-tracks").click(function () {
    $("#trackupload").click();
  });

  $("#trackupload").fileupload({

    dataType: 'json',
    sequentialUploads: true,
    start: function (e) {
      $("#progress-info").show();
    },
    stop: function (e) {
      $("#progress-info").hide();
    },
    progressall: function (e, data) {
      var progress = parseInt(data.loaded / data.total * 100, 10);
      var strProgress = progress + "%";
      $(".progress").text(strProgress);
    },

    done: function (e, data) {
      if (data.result.is_valid) {
        $("#new-tracks").prepend(
          "<li>" + data.result.artist + " - " + data.result.title + " uploaded by " + data.result.user_uploaded + "</li>"
        )
        $("#new-tracks li:last-child").remove();
      }
    }
  });

});