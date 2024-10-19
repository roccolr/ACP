package implementazioni;
import interfacce.*;

public class CodaWrapperSynchr extends CodaWrapper {
    public CodaWrapperSynchr(Coda c){
        super(c);
    }

    public void inserisci(int i){
        //implementiamo la logica di sincornizzazione
        synchronized(coda){
            try{
                while(coda.full()){
                    coda.wait();
                }
            }catch (InterruptedException e){
                e.printStackTrace();
            }

            coda.inserisci(i);
            coda.notifyAll();
        //c'è una sola coda: dobbiamo notificare tutti quelli che aspettano, sia produttori che consumatori
        }
    }

    public int preleva(){
        int result = -1;
        synchronized(coda){
            try{
                while(coda.empty()){
                    coda.wait();
                }
            }catch(InterruptedException e){
                e.printStackTrace();
            }

            result = coda.preleva();
            coda.notifyAll();
        }
        return result;
    }
}   
