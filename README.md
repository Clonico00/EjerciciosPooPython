# Ejercicios poo python

1) Haz una clase llamada Persona que siga las siguientes condiciones:

    Sus atributos son: nombre, edad, DNI, sexo (H hombre, M mujer), peso y altura. No queremos que se accedan directamente a ellos. Piensa que modificador de acceso es el más adecuado, también su tipo. Si quieres añadir algún atributo puedes hacerlo.
    Por defecto, todos los atributos menos el DNI serán valores por defecto según su tipo (0 números, cadena vacía para String, etc.). Sexo sera mujer por defecto.
    Se implantaran un constructor:
        Un constructor con todos los atributos como parámetro.
    Los métodos que se implementaran son:
        calcularIMC(): calculara si la persona esta en su peso ideal (peso en kg/(altura^2  en m)), devuelve un -1 si esta por debajo de su peso ideal, un 0 si esta en su peso ideal y un 1 si tiene sobrepeso . También devuelve el IMC.
        esMayorDeEdad(): indica si es mayor de edad, devuelve un booleano.
        introducirSexo(char sexo):  introducido el sexo. Si no es correcto, sera M. No sera visible al exterior.
        toString(): devuelve toda la información del objeto.
        generaDNI(): genera un numero aleatorio de 8 cifras, genera a partir de este su número su letra correspondiente. Este método sera invocado cuando se construya el objeto.
        Métodos set de cada parámetro, excepto de DNI.

Ahora,

    Pide por teclado el nombre, la edad, sexo, peso y altura.
    Crea 3 objetos de la clase anterior, el primer objeto obtendrá las anteriores variables pedidas por teclado, el segundo objeto obtendrá todos los anteriores menos el peso y la altura y el último los datos por defecto, para este último utiliza los métodos set para darle a los atributos un valor.
    Para cada objeto, deberá comprobar si esta en su peso ideal, tiene sobrepeso o por debajo de su peso ideal con un mensaje.
    Indicar para cada objeto si es mayor de edad.
    Por último, mostrar la información de cada objeto.

 2) Crearemos una supeclase llamada Electrodoméstico con las siguientes características:

    Sus atributos son precio base, color, consumo energético (letras entre A y F) y peso. Indica que se podrán heredar.
    Por defecto, el color sera blanco, el consumo energético sera F, el precioBase es de 100 € y el peso de 5 kg. Usa constantes para ello.
    Los colores disponibles son blanco, negro, rojo, azul y gris. No importa si el nombre esta en mayúsculas o en minúsculas.
    Crearemos un constructor con todos los atributos.

    Los métodos que implementara serán:
        Métodos get de todos los atributos.
        comprobarConsumoEnergetico(char letra): comprueba que la letra es correcta, sino es correcta usara la letra por defecto. Se invocara al crear el objeto y no sera visible.
        comprobarColor(String color): comprueba que el color es correcto, sino lo es usa el color por defecto. Se invocara al crear el objeto y no sera visible.
        precioFinal(): según el consumo energético, aumentara su precio, y según su tamaño, también. Esta es la lista de precios:

			Letra	Precio
			A		100 €
			B		80 €
			C		60 €
			D		50 €
			E		30 €
			F		10 €

			Tamaño					Precio
			Entre 0 y 19 kg			10 €
			Entre 20 y 49 kg		50 €
			Entre 50 y 79 kg		80 €
			Mayor que 80 kg			100 €

	Crearemos una subclase llamada Lavadora con las siguientes características:

    Su atributo es carga, ademas de los atributos heredados.
    Por defecto, la carga es de 5 kg. Usa una constante para ello.
    El constructor que se implementará será:
        
        Un constructor con la carga y el resto de atributos heredados.

    Los métodos que se implementara serán:
        Método get de carga.
        precioFinal():, si tiene una carga mayor de 30 kg, aumentara el precio 50 €, sino es así no se incrementara el precio. Llama al método padre y añade el código necesario. Recuerda que las condiciones que hemos visto en la clase Electrodoméstico también deben afectar al precio.

	Crearemos una subclase llamada Television con las siguientes características:

    Sus atributos son resolución (en pulgadas) y fourK (booleano), ademas de los atributos heredados.
    Por defecto, la resolución sera de 20 pulgadas y el fourK sera false.
    Los constructor que se implementará será:
        Un constructor con el precio y peso. El resto por defecto.
    Los métodos que se implementara serán:
        Método get de resolución y fourK.
        precioFinal(): si tiene una resolución mayor de 40 pulgadas, se incrementara el precio un 30% y si tiene 4K, aumentara 50 €. Recuerda que las condiciones que hemos visto en la clase Electrodoméstico también deben afectar al precio.

	Ahora crea una clase ejecutable que realice lo siguiente:

    Crea una lista de Electrodomésticos de 10 elementos.
    Asigna a cada posición un objeto de las clases anteriores con los valores que desees.
    Ahora, recorre este array y ejecuta el método precioFinal().
    Deberás mostrar el precio de cada clase, es decir, el precio de todas las televisiones por un lado, el de las lavadoras por otro y la suma de los Electrodomésticos (puedes crear objetos Electrodoméstico, pero recuerda que Television y Lavadora también son electrodomésticos).

	Por ejemplo, si tenemos un Electrodoméstico con un precio final de 300, una lavadora de 200 y una televisión de 500, el resultado final sera de 1000 (300+200+500) para electrodomésticos, 200 para lavadora y 500 para televisión.

3)Crearemos una clase llamada Serie con las siguientes características:

    Sus atributos son titulo, numero de temporadas, entregado, genero y creador.
    Por defecto, el numero de temporadas es de 3 temporadas y entregado false. El resto de atributos serán valores por defecto según el tipo del atributo.
    Crearemos un constructor con todos los atributos, excepto de entregado.

    Los métodos que se implementara serán:
        Métodos get de todos los atributos, excepto de entregado.
        Métodos set de todos los atributos, excepto de entregado.
        Sobreescribe los métodos toString.

	Crearemos una clase Videojuego con las siguientes características:

    Sus atributos son titulo, horas estimadas, entregado, genero y compañía.
    Por defecto, las horas estimadas serán de 10 horas y entregado false. El resto de atributos serán valores por defecto según el tipo del atributo.
    Crearemos un constructor  con todos los atributos, excepto de entregado.

    Los métodos que se implementara serán:
        Métodos get de todos los atributos, excepto de entregado.
        Métodos set de todos los atributos, excepto de entregado.

	

	Implementa los anteriores métodos en las clases Videojuego y Serie. Ahora crea una aplicación  y realiza lo siguiente:

    Crea dos listas, uno de Series y otro de Videojuegos, de 5 posiciones cada uno.
    Crea un objeto en cada posición de la lista, con los valores que desees.
    Entrega algunos Videojuegos y Series con el método entregar().
    Cuenta cuantos Series y Videojuegos hay entregados. Al contarlos, devuélvelos.
    Por último, indica el Videojuego tiene más horas estimadas y la serie con mas temporadas.
