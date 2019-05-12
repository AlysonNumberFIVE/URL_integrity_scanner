$(document).ready(restart());

function restart(){
  $('.text').css({'top': '40px'}),
  $('.text').css({'display': 'none'}),
  $('.text').animate({'top': 0}, {"duration":2000,"queue":false});
  $('.text').fadeIn(2000);
}