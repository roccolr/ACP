package tests;
import implementazioni.*;
import interfacce.*;

public class Main {
    public static void main(String[] args) {
        Coda c = new CodaCircolare(5);
        CodaWrapper coda = new CodaWrapperSynchr(c);
        WorkerThread [] threads = new WorkerThread[10];
        for (int i=0; i<10; i++){
            if(i%2 == 0){
                threads[i] = new WorkerThread(coda, "prod");
            }else{
                threads[i] = new WorkerThread(coda, "cons");
            }
            threads[i].start();

        }
        
        // for (WorkerThread w : threads){
        //     System.out.println(w.getName());
        // }

        for (int i=0; i<10; i++){
            try{
                threads[i].join();
                System.out.println("THREAD FINITO");
            }catch(InterruptedException e){
                e.printStackTrace();
            }
        }
    }
}
