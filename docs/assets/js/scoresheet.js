(function($) {

	$(function() {
	        var _player_id_lookup = {
                'B':'1',
                'D': '2',
                'G': '3',
                'S': '4',
                'Vk':'5',
		        'V':'6'
		    };
		 //ADD
			var $add = $('a[href="#add"]');
			$add
				.on('click', function(event) {
				       var $player = $(this).text()
				       $('a[href="#remove"]').each(function(){
				           if($(this).text() == 'N/A'){
				                $(this).text($player);
				                return false;
				           }
				       })
                       return true;
				})
	    // Remove.
			var $remove = $('a[href="#remove"]');
			$remove
				.on('click', function(event) {
					  $(this).text('N/A');
                       return true;
				})
        // Save.
			var $save = $('a[href="#save"]');
			$save
				.on('click', function(event) {
				      var $game = '';
				      $('a[href="#remove"]').each(function(){
				           if($(this).text() != 'N/A'){
				                if($game == ''){
				                    $game = _player_id_lookup[$(this).text()];
				                }else{
				                    $game = $game+','+ _player_id_lookup[$(this).text()];
				                }

				           }
				       })
				      var $_all_games = localStorage.getItem('_all_games')
				      if($_all_games == null){
				        $_all_games = $game;
				      }else{
				        $_all_games = $_all_games + '\n' + $game;
				      }
				      localStorage.setItem('_all_games', $_all_games);
				      $(this).addClass("disabled")
                      return true;
				})
		// Reset.
			var $reset = $('a[href="#reset"]');
			$reset
				.on('click', function(event) {
				       var $player = $(this).text()
				       $('a[href="#remove"]').each(function(){
				           if($(this).text() != 'N/A'){
				                $(this).text('N/A');
				           }
				       })
				       $('a[href="#save"]').removeClass("disabled")
                       return true;
				})
		// Raw.
			var $raw = $('a[href="#raw"]');
			$raw
				.on('click', function(event) {
				    var $_all_games = localStorage.getItem('_all_games')
				    if($_all_games != null){
				      $('#csvData').text(localStorage.getItem('_all_games'));
				    }
			        $('#formatCSV').toggle()
                    return true;
				})
        // Clear.
			var $clear = $('a[href="#clear"]');
			$clear
				.on('click', function(event) {
				    $('#csvData').text('');
		            localStorage.clear();
		            $('#formatCSV').hide();
                    return true;
				})
	});

})(jQuery);