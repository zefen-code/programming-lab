
#======================
# Classe per file CSV
#======================

class CSVFile():

    def __init__(self, name):
        if not isinstance(name, str):
            raise Exception("ERRORE: name non è una stringa")
        self.name = name

    def get_data(self, start=None, end=None):
		if start>end:
			raise Exception("Errore")
		
		#self.name=self.name.readlines()
		#valori=[]
		#i=0
		#for line in range(start, end):


        # Inizializzo una lista vuota per salvare i valori
        values = []


        # Provo ad aprire il file per estrarci i dati. Se non ci riesco, prima avverto del'errore, 
        # poi devo abortire. Questo e' un errore "un-recoverable", ovvero non posso proseguire con
        # la lettura dei dati se non riesco ad aprire il file!
        try:
            my_file = open(self.name, 'r')

			numerodirigha=0
        except Exception as e:
            
            # Stampo l'errore
            print('Errore nella lettura del file: "{}"'.format(e))
            
            # Esco dalla funzione tornando "niente".
            return None
		
		def get_data(self, start=None, end=None)

        
        # Ora inizio a leggere il file linea per linea
        for line in my_file:
            
            # Faccio lo split di ogni linea sulla virgola
            elements = line.split(',')

            # Se NON sto processando l'intestazione...
            if elements[0] != 'Date':
                    
                # Setto la data ed il valore
                date  = elements[0]
                value = elements[1]
                
                # La variabile "value" al momento e' ancora una stringa, poiche' ho letto da file di testo,
                # quindi converto a valore floating point, e se nel farlo ho un errore avverto. Questo e'
                # un errore "recoverable", posso proseguire (semplicemente salto la linea).
                try:
                    value = float(value)
                except Exception as e:
                    
                    # Stampo l'errore
                    print('Errore nella conversione a float: "{}"'.format(e))
                    
                    # Vado al prossimo "giro" del ciclo, quindi NON eseguo quanto viene dopo (ovvero l'append)
                    continue
                
                # Infine aggiungo alla lista dei valori questo valore
                values.append(value)
        
        # Chiudo il file
        my_file.close()
        
        # Quando ho processato tutte le righe, ritorno i valori
        return values
    

#mio_file = CSVFile(name = 'shampoo_sales.csv')
mio_file = CSVFile(name = "2")

print('Nome del file: "{}"'.format(mio_file.name))
print('Dati contenuti nel file: "{}"'.format(mio_file.get_data()))

