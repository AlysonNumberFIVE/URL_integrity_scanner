
// store form HTML markup in a JS variable
var formTemplate = $('#form-template > form').clone()[0];
$('#form-template').remove();

// prepare SweetAlert configuration
var swalConfig = {
  title: 'Demo Form',
  content: formTemplate,
  button: {
    text: 'Submit',
    closeModal: false
  }
};

// handle clicks on the "Click me" button
$('#click-me-btn').click(function () {
  swal(swalConfig);
});

// handle clicks on the "Submit" button of the modal form
$('body').on('click', '.swal-button--confirm', function() {
  simulateAjaxRequest();
});

// mock AJAX requests for this demo
var isFakeAjaxRequestSuccessfull = false;

function simulateAjaxRequest() {
  // "send" the fake AJAX request
  var fakeAjaxRequest = new Promise(function (resolve, reject) {
    setTimeout(function () {
      isFakeAjaxRequestSuccessfull ? resolve() : reject();
      isFakeAjaxRequestSuccessfull = !isFakeAjaxRequestSuccessfull;
      swal.stopLoading();
    }, 200);
  });
  
  // attach success and error handlers to the fake AJAX request
  fakeAjaxRequest.then(function () {
    // do this if the AJAX request is successfull:
    $('input.invalid').removeClass('invalid');
    $('.invalid-feedback').remove();
  }).catch(function () {
    // do this if the AJAX request fails:
    var errors = {
      username: 'Username is invalid',
      password: 'Password is invalid'
    };
    $.each(errors, function(key, value) {
      $('input[name="' + key + '"]').addClass('invalid').after('<div class="invalid-feedback">' + value + '</div>');
    });
  });
}