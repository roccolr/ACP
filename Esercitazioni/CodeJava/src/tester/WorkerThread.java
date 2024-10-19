package tester;
import coda.*;


public class WorkerThread extends Thread{

    private Coda coda;
    private boolean flag; 

    public WorkerThread(Coda c, boolean flag){
        coda = c;
        this.flag = flag;
    }
    public void run(){
        if(flag){
            coda.inserisci((int)(1+Math.random()*100));
        }
        else{
            coda.preleva();
        }
    }
}
