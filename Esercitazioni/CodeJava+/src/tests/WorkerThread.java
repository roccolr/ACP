package tests;

import interfacce.Coda;

public class WorkerThread extends Thread{

    Coda coda;

    public WorkerThread(Coda coda, String name){
        super(name);
        this.coda = coda;
    }
    public void run(){
        if(Thread.currentThread().getName().equals("prod")){
            int val = (int)(Math.random()*100);
            coda.inserisci( val);
            System.out.println("[PRODUTTORE]\t prodotto"+val);

        }else{
            int result = coda.preleva();
            System.out.println("[CONSUMATORE]\t consumato "+result);
        }
    }
}
