/* Fomrulario de usuario */
const     mascotaIput =  document.querySelector('#mascota');
const propietarioIput =  document.querySelector('#propietario');
const    telefonoIput =  document.querySelector('#telefono');
const       fechaIput =  document.querySelector('#fecha');
const        horaIput =  document.querySelector('#hora');
const    sintomasIput =  document.querySelector('#sintomas');

/* UI */
const   fomularioCita =  document.querySelector('#nueva-cita');
const contenedorCitas =  document.querySelector('#citas');

/* Clases */
class Citas{
    constructor(){
        this.citas=[];
    }
}

class UI{
    imprimirAlerta(mensaje,tipo){

        /* Crear el DIV */
        const divMensaje = document.createElement('div');
        divMensaje.classList.add('text-center', 'alert', 'd-block', 'col-12');

        /* Agregar clase  en base  al tipo de error */
        if(tipo=='error'){
            divMensaje.classList.add('alert-danger');
        }else{
            divMensaje.classList.add('alert-success');
        }

        /*Mensaje de error  */
        divMensaje.textContent = mensaje;

        /* Agregar el Dom */
        document.querySelector('#contenido').insertBefore(divMensaje,document.querySelector('.agregar-cita'));

        /* Quitar alerta despues de 5 segundos */

        setTimeout(() => {
            divMensaje.remove();
        }, 5000)
    }

}
/* Instancias de la cita class*/
const ui = new UI();
const administrarCita = new Citas();

/* Registrar Eventos */
evenListeners();
function evenListeners(){
    mascotaIput.addEventListener('input', datosCitas);
    propietarioIput.addEventListener('input', datosCitas);
    telefonoIput.addEventListener('input', datosCitas);
    fechaIput.addEventListener('input', datosCitas);
    horaIput.addEventListener('input', datosCitas);
    sintomasIput.addEventListener('input', datosCitas);
    fomularioCita.addEventListener('submit',nuevaCita);
}

/* Objeto principal con la informacion de la cita */
const citaObj = {
    mascota:'',
    propietario:'',
    telefono: ' ',
    fecha: '',
    hora: '',
    sintomas: ''
}

/* Agraga datos al objeto a la cita */
function datosCitas(e){
    citaObj[e.target.name] = e.target.value;
    console.log(citaObj);
}

/* Valida y agrega una nueva cita en la clase de Citas */
function nuevaCita(e){
    e.preventDefaul();

    /* Extraer la informacion del objeto citaObj */
    const {mascota,propietario,telefono,fecha,hora,sintomas} = citaObj;

    /* Validar */
    if(mascota === '' || propietario === '' || telefono === '', fecha === '' || hora === '' || sintomas === ''){
        ui.imprimirAlerta('Todo los campos son  obligatorios','error');
        // console.log('Todo los campos son obligatorios')
        return;
    }
}