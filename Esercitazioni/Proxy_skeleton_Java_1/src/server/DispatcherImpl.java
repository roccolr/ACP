package server;
import coda.interfaccia.*;

public class DispatcherImpl extends DispatcherSkeleton{
    Coda c;

    public DispatcherImpl(int port, Coda c){
        super(port);
        this.c = c;
    }

    public void sendCommand(int cmd){
        c.inserisci(cmd);
        System.out.println(Thread.currentThread().getName()+" inserito comando "+cmd);
    }
    public int getCommand(){
        int res = c.preleva();
        System.out.println(Thread.currentThread().getName()+" prelevato comando "+res);

        return res;
    }
}
