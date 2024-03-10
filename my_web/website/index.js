$(".button-main").mouseover(function() {
    $(".button-icon")
      .addClass("button-icon-hover")
      .removeClass("button-icon-default");
  });
  
  $(".button-main").mouseleave(function() {
    $(".button-icon")
      .addClass("button-icon-default")
      .removeClass("button-icon-hover");
  });