package coda.implementazioni;

import coda.interfaccia.CodaWrapper;
import coda.interfaccia.Coda;


public class CodaWrapperSynch extends CodaWrapper{
    public CodaWrapperSynch(Coda c){
        super(c);
    }

    public void inserisci(int val){
        synchronized(coda){
            try{
                while(full()){
                    coda.wait();
                }
            }catch (InterruptedException e){
                e.printStackTrace();
            }
            
            // int x = (int)(Math.random()*100);
            coda.inserisci(val);
            System.out.println(Thread.currentThread().getName()+" inserito nella coda il valore: "+val);

            coda.notifyAll();
        }
    }

    public int preleva(){
        int res;
        synchronized(coda){
            try{
                while(empty()){
                    coda.wait();
                }
            }catch (InterruptedException e){
                e.printStackTrace();
            }
            
            res = coda.preleva();
            System.out.println(Thread.currentThread().getName()+" prelevato dalla coda il valore: "+res);
            coda.notifyAll();
            return res;
        }
    }

}
