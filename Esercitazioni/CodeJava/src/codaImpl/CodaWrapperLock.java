package codaImpl;
import coda.*;
import java.util.concurrent.locks.*;

public class CodaWrapperLock extends CodaWrapper {
    private Lock lock;
    private Condition empty;
    private Condition full;

    public CodaWrapperLock(Coda c){
        super(c);
        lock = new ReentrantLock();
        empty = lock.newCondition();
        full = lock.newCondition();
    }

    public void inserisci(int i){
        lock.lock();

        try{
            while(coda.full()){
                try{
                    full.await();
                }catch (InterruptedException e){
                    e.printStackTrace();
                }
            }

            coda.inserisci(i);
            empty.signal();
        }
        finally{
            lock.unlock();
        }
    }

    public int preleva(){
        int res = -1;
        lock.lock();
        try{
            while(coda.empty()){
                try{
                    empty.await();
                }catch (InterruptedException e){
                    e.printStackTrace();
                }
            }

            res = coda.preleva();
            full.signal();
        }
        finally{
            lock.unlock();
        }
        return res;
    }
}
