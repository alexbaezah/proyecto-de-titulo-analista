/* PROGRAMACION WEB / JS - PLANTAS DEL BOSQUE 											by Constanza Painevilo y Francisco Salazar*/

/* JAVASCRIPT: HOME Y PRODUCTOS - JS*/
$(document).ready(function(){

  var filtrador = $('.filtro-container .list-group .categorias'),
      filtroColor = $('.filtro-colores .form-check-input'),
      listaAFiltrar = $('.productos');

  filtrador.click(function(){
      $('.categorias').removeClass('active');
      $(this).addClass('active');
      var categoria = $(this).data('categoria');

      listaAFiltrar.find('.producto').hide().removeClass('producto-activo');

      $('.productos').find(`[data-categoria='${categoria}']`).show().addClass('producto-activo');
      console.log(categoria)

  });
  //LIMPIAR FILTRO
  $('.ver-todo').click(function(){
      filtrador.removeClass('active')
      listaAFiltrar.find('.producto').show()
  });

  //FILTRO POR COLOR 
  filtroColor.each(function(){
      $(this).change(function(){
          if($(this).hasClass('color-activo')){
              $(this).removeClass('color-activo');
          }else{
              $(this).addClass('color-activo');
              var colorActivo = $(this).data('color'),
                  productosActivos = listaAFiltrar.find('.producto.activo'),
                  productosConColorActivo = listaAFiltrar.find(`[data-color='${colorActivo}']`);
              productosActivos.find(`[data-color='${colorActivo}']`).show()
          }
      })
  });

  filtroColor.change(function(){
  })



    //API CLIMA 

    window.addEventListener('load', ()=> {
        let lon
        let lat
      
        let temperaturaValor = document.getElementById('temperatura-valor')  
        let temperaturaDescripcion = document.getElementById('temperatura-descripcion')  
        
        let ubicacion = document.getElementById('ubicacion')  
        let iconoAnimado = document.getElementById('icono-animado') 
      
        let vientoVelocidad = document.getElementById('viento-velocidad') 
      
      
        if(navigator.geolocation){
           navigator.geolocation.getCurrentPosition( posicion => {
               //console.log(posicion.coords.latitude)
               lon = posicion.coords.longitude
               lat = posicion.coords.latitude
                //ubicación actual    
               //const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${AQUI_VIENE_TU_API_KEY}`
      
               //ubicación por ciudad
               const url = `https://api.openweathermap.org/data/2.5/weather?q=Santiago&lang=es&units=metric&appid=4784ba3eb5c4c8982e49c1c054989e2a`
      
               //console.log(url)
      
               fetch(url)
                .then( response => { return response.json()})
                .then( data => {
                    //console.log(data)
                    
                    let temp = Math.round(data.main.temp)
                    //console.log(temp)
                    temperaturaValor.textContent = `${temp} ° C`
      
                    //console.log(data.weather[0].description)
                    let desc = data.weather[0].description
                    temperaturaDescripcion.textContent = desc.toUpperCase()
                    ubicacion.textContent = data.name
                    
                    vientoVelocidad.textContent = `${data.wind.speed} m/s`
                    
                    //para iconos estáticos
                    //const urlIcon = `http://openweathermap.org/img/wn/${iconCode}.png`                     
                    //icono.src = urlIcon
                    //console.log(data.weather[0].icon)
      
                    //para iconos dinámicos
                    console.log(data.weather[0].main)
                    switch (data.weather[0].main) {
                        case 'Thunderstorm':
                          iconoAnimado.src='animated/thunder.svg'
                          console.log('TORMENTA');  
                          break;
                        case 'Drizzle':
                          iconoAnimado.src='animated/rainy-2.svg'
                          console.log('LLOVIZNA');
                          break;
                        case 'Rain':
                          iconoAnimado.src='animated/rainy-7.svg'
                          console.log('LLUVIA');
                          break;
                        case 'Snow':
                          iconoAnimado.src='animated/snowy-6.svg'
                            console.log('NIEVE');
                          break;                        
                        case 'Clear':
                            iconoAnimado.src='animated/day.svg'
                            console.log('LIMPIO');
                          break;
                        case 'Atmosphere':
                          iconoAnimado.src='animated/weather.svg'
                            console.log('ATMOSFERA');
                            break;  
                        case 'Clouds':
                            iconoAnimado.src='animated/cloudy-day-1.svg'
                            console.log('NUBES');
                            break;  
                        default:
                          iconoAnimado.src='animated/cloudy-day-1.svg'
                          console.log('por defecto');
                      }
      
                })
                .catch( error => {
                    console.log(error)
                })
           })
              
        }
      })


});