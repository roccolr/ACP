package codaImpl;

import java.util.concurrent.Semaphore;

import coda.*;

public class CodaWrapperSem extends CodaWrapper{
    private Semaphore postoDisp;
    private Semaphore elemDisp;

    public CodaWrapperSem(Coda c){
        super(c);
        postoDisp = new Semaphore(coda.getSize());
        elemDisp = new Semaphore(0);
    }

    public void inserisci(int i){
        try{
            postoDisp.acquire();

            try{
                synchronized(coda){
                    coda.inserisci(i);
                }
            }
            finally{
                elemDisp.release();
            }
        }catch(InterruptedException e){
            e.printStackTrace();
        }
    }

    public int preleva(){
        int result = -1;
        try{
            elemDisp.acquire();

            try{
                synchronized(coda){
                    result = coda.preleva();
                }
            }finally{
                postoDisp.release();
            }
        }catch (InterruptedException e){
            e.printStackTrace();
        }
        return result;
    }
}
