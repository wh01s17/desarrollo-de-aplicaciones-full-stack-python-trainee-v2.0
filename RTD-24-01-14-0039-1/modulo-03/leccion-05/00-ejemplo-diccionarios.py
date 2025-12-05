dict()

{}


{
    'rut1':{
        'nombre':'Christian',
        'apellido':'Donoso',
        'edad':37
    },
    'clave2':{

    },
    'clave3':{
        
    }
}



dicccionario = {
    'elizabeth':25,
    'tomas':17,
    'christian':37
} 

dicccionario['christian'] #37 

#dicccionario['jordy'] # error

dicccionario['jordy'] = 25


for k, v in dicccionario.items():
    print(k, v)