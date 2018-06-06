$(function() {
    $("#search-field").on("focus", function(event){
    	$(event.currentTarget).parent().addClass("active");
    })

     $(document).on("click", function(event) { 
	    if(!$(event.target).closest('#search-form').length) {
	      
	            $('#search-form').removeClass("active");
	    }        
	})

     $("#extend-results-button").on("click", function(event){
     	$('.result-item').each(function(){
		  $(this).removeClass('hidden')
		});
		$(this).addClass("hidden");
     })

     $("iframe").wrap("<div class='iframe-wrapper'/>");


     $('#cookiebox button').on('click', function(event){
     	$('#cookiebox').addClass("hidden");
     })
});