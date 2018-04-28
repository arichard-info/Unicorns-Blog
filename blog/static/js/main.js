$(function() {
    $("#search-field").on("focus", function(event){
    	$(event.currentTarget).parent().addClass("active");
    })

     $(document).click(function(event) { 
	    if(!$(event.target).closest('#search-form').length) {
	      
	            $('#search-form').removeClass("active");
	    }        
	});
});