package implementazioni;

import java.util.concurrent.Semaphore;

import interfacce.Coda;
import interfacce.CodaWrapper;

public class CodaWrapperSem extends CodaWrapper{
    Semaphore spaziDisponibili;
    Semaphore messaggiDisponibili;

    public CodaWrapperSem(Coda coda){
        super(coda);
        spaziDisponibili = new Semaphore(this.coda.getSize());
        messaggiDisponibili = new Semaphore(0);
    }

    public void inserisci(int elem){
        try{
            spaziDisponibili.acquire();
        
            synchronized(coda){
                coda.inserisci(elem);
            }

            messaggiDisponibili.release();
            
        }catch (InterruptedException e){
            e.printStackTrace();
        }

    }

    public int preleva(){
        int res = -1;
        try{
            messaggiDisponibili.acquire();
            synchronized(coda){
                res = coda.preleva();
            }

            spaziDisponibili.release();
            
        }catch (InterruptedException e){
            e.printStackTrace();
        }
        return res;
    }
}
