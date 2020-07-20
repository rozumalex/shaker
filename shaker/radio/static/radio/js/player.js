( function( d ){
    'use strict';
    var timeout = 5; // интервал обновления информации в секундах
        function getStats(){
            $.ajax({
                url:"https://shakethe.rocks:8443/status-json.xsl",
                success: function(response){
                    $( '#song-title' ).text(response.icestats.source.title),
                    $( '#listeners' ).text(response.icestats.source.listeners),
                    $( '#location' ).text(response.icestats.location)
                }
            });
        }
        getStats();
        setInterval(getStats,timeout * 1000);

    var test = true,
        but = d.querySelector( '#control-button' ),
        aud = d.querySelector( '#player' ),
        stream = "https://shakethe.rocks:8443/stream";
    aud.src = "";
    aud.classList.add( 'remove' );
    d.querySelector( '#control-button-wrapper' ).classList.remove( 'hidden' );

    but.addEventListener('click',
        function() {
            if ( test === true ) {
              but.classList.add( 'pause' );
              test = false;
              aud.src = stream;
              aud.play();
         }
         else {
              changeSVG();
              aud.pause();
              aud.src = "";
         }
      }, false );

   aud.addEventListener( 'ended',
      function() {
         changeSVG();
         aud.load();
       }, false );

   function changeSVG() {
      but.classList.remove( 'pause' );
      test = true;
    }
 }( document ));
