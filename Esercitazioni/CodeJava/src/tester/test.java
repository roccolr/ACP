package tester;

import coda.*;
import codaImpl.*;
// import codaimpl.CodaWrapperSynchr;

public class test {
    public static void main(String argv[]){
        Coda c = new CodaCircolare(5);
        CodaWrapper wrapper = new CodaWrapperSynchr(c);

        WorkerThread workers [] = new WorkerThread[20];

        for(int i=0; i<20; i++){
            if(i%2 == 0){
                workers[i] = new WorkerThread(wrapper, true);
            }
            else{
                workers[i] = new WorkerThread(wrapper, false);
            }
            workers[i].start();
        }

        for ( int i=0; i<20; i++ ){
			try{
				workers[i].join();
			}catch( InterruptedException e ){
				e.printStackTrace();
			}
		}
    }
}
