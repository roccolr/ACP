package implementazioni;

import interfacce.Coda;
import interfacce.CodaWrapper;
import java.util.concurrent.locks.*;

public class CodaWrapperLock extends CodaWrapper{
    private Lock lock;
    private Condition cv_produttori;
    private Condition cv_consumatori;

    public CodaWrapperLock(Coda coda){
        super(coda);
        this.lock = new ReentrantLock();
        this.cv_consumatori = lock.newCondition();
        this.cv_produttori = lock.newCondition();
    }

    public void inserisci(int elem){
        lock.lock(); //entro nel monitor

        while(coda.full()){
            try{
                cv_produttori.await();
            }catch (InterruptedException e){
                e.printStackTrace();
            }
        }
        coda.inserisci(elem);
        cv_consumatori.signal();
        lock.unlock();
    }

    public int preleva(){
        lock.lock();

        while(coda.empty()){
            try{
                cv_consumatori.await();
            }catch (InterruptedException e){
                e.printStackTrace();
            }
        }
        int res = coda.preleva();
        cv_produttori.signal();
        lock.unlock();
        return res;
    }
}
